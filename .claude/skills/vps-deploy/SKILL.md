---
name: vps-deploy
description: Deploy websites to Strato Windows VPS with Plesk, IIS reverse proxy, PM2, Cloudflare DNS, and GitHub Actions CI/CD. Use when the user wants to deploy a site, set up hosting, configure CI/CD for VPS, or mentions "deploy to VPS", "Strato", "Plesk hosting", or "production deployment".
version: 1.0.0
---

# VPS Deployment Skill

Deploy Next.js (or any Node.js) websites to the user's Strato Windows Server 2022 VPS with automated CI/CD.

## Infrastructure Overview

```
User → Cloudflare (SSL/CDN) → VPS:443 (Plesk/IIS) → localhost:{PORT} (PM2)

GitHub push to main
  ├─► GitHub Actions: lint + typecheck + build
  │     ├─► Deploy backend (Convex/other)
  │     └─► SSH into VPS → git pull → npm ci → build → pm2 restart
  └─► semantic-release: tag + GitHub Release
```

## VPS Details

| Component | Details |
|-----------|---------|
| **OS** | Windows Server 2022 |
| **IP** | 212.132.117.205 |
| **Panel** | Plesk (manages IIS) |
| **Process manager** | PM2 (registered as Windows Service via pm2-windows-service) |
| **SSH** | OpenSSH Server (built-in, port 22) |
| **Apps directory** | `C:\apps\` |
| **Auth keys** | `C:\ProgramData\ssh\administrators_authorized_keys` |

## Deployment Checklist for a New Site

### 1. Prepare the VPS

```powershell
# Create app directory
mkdir C:\apps\{site-name}
cd C:\apps\{site-name}

# Clone the repo (use GitHub PAT for private repos)
git clone https://{PAT}@github.com/{owner}/{repo}.git .

# Install dependencies
npm ci

# Create production env file
notepad .env.production.local
# Add all production env vars (NEVER commit this file)

# Build
npm run build
```

### 2. Start with PM2

Create `ecosystem.config.js` in the project root:

```js
module.exports = {
  apps: [{
    name: '{site-name}',
    script: 'node_modules/next/dist/bin/next',
    args: 'start -p {PORT}',
    cwd: 'C:\\apps\\{site-name}',
    env: {
      NODE_ENV: 'production'
    }
  }]
};
```

```powershell
pm2 start ecosystem.config.js
pm2 save
```

**Port allocation** — check existing ports before choosing:
```powershell
netstat -ano | findstr "LISTENING" | findstr "30"
pm2 list
```

Currently allocated:
- Port 3010: do-it-website (doitdigital.nl)

### 3. Configure Plesk + IIS Reverse Proxy

**Prerequisites** (one-time, already done):
- IIS URL Rewrite module installed
- IIS Application Request Routing (ARR) installed and proxy enabled

**Per site:**

1. In Plesk (`https://212.132.117.205:8443`):
   - **Websites & Domains** → **Add Domain**
   - Enter domain name
   - Let Plesk create the site

2. Edit the web.config at the document root (e.g., `C:\Inetpub\vhosts\{domain}\httpdocs\web.config`):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <system.webServer>
    <rewrite>
      <rules>
        <rule name="ReverseProxy" stopProcessing="true">
          <match url="(.*)" />
          <action type="Rewrite" url="http://localhost:{PORT}/{R:1}" />
        </rule>
      </rules>
    </rewrite>
  </system.webServer>
</configuration>
```

**IMPORTANT**: If the web.config already has content (Plesk error pages, etc.), merge the `<rewrite>` block into the existing `<system.webServer>` section. Do NOT replace existing content.

### 4. Configure Cloudflare DNS

In Cloudflare Dashboard → domain → DNS:

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | @ | 212.132.117.205 | Proxied (orange cloud) |
| CNAME | www | {domain} | Proxied (orange cloud) |

In SSL/TLS settings: set mode to **Full** (not Full Strict).

No SSL certificate needed on the VPS — Cloudflare terminates SSL.

### 5. Set Up SSH Key for GitHub Actions

If not already done (one-time setup):

```powershell
# On local PC
ssh-keygen -t ed25519 -C "github-actions-deploy" -f C:\Users\DAerts\.ssh\{keyname}

# Copy public key to VPS
# Add contents of {keyname}.pub to:
# C:\ProgramData\ssh\administrators_authorized_keys (must be a FILE, not a folder)

# Set permissions on VPS (Admin PowerShell)
icacls "C:\ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant "SYSTEM:F" /grant "Administrators:R"
Restart-Service sshd
```

### 6. GitHub Actions CI/CD

**Secrets** (repo → Settings → Secrets → Actions):

| Secret | Value |
|--------|-------|
| VPS_HOST | 212.132.117.205 |
| VPS_USERNAME | Administrator |
| VPS_SSH_KEY | Private key contents |

**CI workflow** (`.github/workflows/ci.yml`) — PR quality gate:

```yaml
name: CI
on:
  pull_request:
    branches: [main]
concurrency:
  group: ci-${{ github.head_ref }}
  cancel-in-progress: true
env:
  NODE_VERSION: "20"
jobs:
  quality:
    name: Lint & Typecheck
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
      - run: npm ci
      - run: npx tsc --noEmit
      - run: npm run lint
  build:
    name: Build Test
    runs-on: ubuntu-latest
    needs: quality
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
      - run: npm ci
      - run: npm run build
```

**Deploy workflow** (`.github/workflows/deploy.yml`) — production:

```yaml
name: Deploy
on:
  push:
    branches: [main]
concurrency:
  group: deploy-${{ github.ref }}
  cancel-in-progress: true
env:
  NODE_VERSION: "20"
jobs:
  quality:
    name: Lint & Typecheck
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
      - run: npm ci
      - run: npx tsc --noEmit
      - run: npm run lint
  build:
    name: Build
    runs-on: ubuntu-latest
    needs: quality
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
      - run: npm ci
      - run: npm run build
  deploy-vps:
    name: Deploy to VPS
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy via SSH
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USERNAME }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script_stop: true
          script: |
            cd C:\apps\{site-name}
            git pull origin main
            npm ci
            npm run build
            pm2 restart {site-name}
  release:
    name: Release
    runs-on: ubuntu-latest
    needs: deploy-vps
    permissions:
      contents: write
      issues: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
      - run: npm ci
      - name: Semantic Release
        run: npx semantic-release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 7. Semantic Release Setup

```bash
npm install -D semantic-release @semantic-release/changelog @semantic-release/git
```

`.releaserc.json`:
```json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    ["@semantic-release/npm", { "npmPublish": false }],
    "@semantic-release/github",
    ["@semantic-release/git", {
      "assets": ["package.json", "package-lock.json", "CHANGELOG.md"],
      "message": "chore(release): ${nextRelease.version} [skip ci]"
    }]
  ]
}
```

## Known Issues & Gotchas

### Windows-Specific
- `pm2 startup` does NOT work on Windows. Use `pm2-windows-service` instead (`npm install -g pm2-windows-service && pm2-service-install`)
- `ssh-keygen -f ~/.ssh/key` fails on Windows PowerShell. Use full path: `ssh-keygen -f C:\Users\DAerts\.ssh\key`
- `administrators_authorized_keys` must be a FILE, not a folder. If you copy a .pub file to that path, Windows creates a folder. Use `Set-Content` or `Copy-Item` instead.
- Multi-line PowerShell commands don't paste well in terminal. Use `notepad` to create files, then reference them.

### Plesk + IIS
- Plesk manages IIS. Do NOT create IIS sites manually — they conflict with Plesk. Always add domains through Plesk first.
- If "another website may be using the same port" error: a manually created IIS site is conflicting. Delete it in IIS Manager, then retry in Plesk.
- Plesk's Node.js hosting feature has limited configurability. Use the reverse proxy approach (web.config rewrite rule) instead.

### Cloudflare
- DNS checker may show old IP — Cloudflare-proxied domains show Cloudflare IPs, not the VPS IP. This is normal.
- SSL mode must be "Full" (not "Full Strict") since the VPS doesn't have its own SSL cert.
- Cloudflare provides free SSL for the domain and all subdomains automatically.

### GitHub Actions
- `appleboy/ssh-action` works with Windows Server OpenSSH.
- The SSH script runs in cmd.exe by default. Windows-style paths (`C:\apps\...`) work fine.
- Private repos: the VPS needs a GitHub PAT stored in the git remote URL, or use a deploy key.

## Environment Separation Pattern

| | Development (laptop) | Production (VPS) |
|---|---|---|
| Config file | `.env.local` | `.env.production.local` |
| Database | Dev instance | Production instance |
| API keys | Test/sandbox keys | Real keys |
| Analytics | Disabled or dev property | Real GA4 ID |
| Git ignored | Yes | Yes (never in repo) |

Templates: `.env.example` and `.env.local.example` committed to repo.

## Quick Reference Commands (VPS)

```powershell
# Check running sites
pm2 list

# View site logs
pm2 logs {site-name} --lines 20

# Restart a site
pm2 restart {site-name}

# Check ports in use
netstat -ano | findstr "LISTENING" | findstr "30"

# Restart IIS
iisreset

# Restart SSH
Restart-Service sshd

# Check SSH service
Get-Service sshd
```
