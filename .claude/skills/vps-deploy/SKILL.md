---
name: vps-deploy
description: Deploy websites to Strato Windows VPS with Docker, Plesk/IIS reverse proxy, Cloudflare DNS, and GitHub Actions CI/CD. Use when the user wants to deploy a site, set up hosting, configure CI/CD for VPS, or mentions "deploy to VPS", "Strato", "Plesk hosting", or "production deployment".
version: 2.0.0
---

# VPS Deployment Skill

Deploy Next.js (or any Node.js) websites to the user's Strato Windows Server 2022 VPS with automated CI/CD.

## Infrastructure Overview

```
User → Cloudflare (SSL/CDN) → VPS:443 (Plesk/IIS) → localhost:{PORT} (Docker)

GitHub push to main
  ├─► GitHub Actions: lint + typecheck
  │     ├─► Build Docker image → push to ghcr.io
  │     ├─► Deploy backend (Convex/other)
  │     └─► SSH into VPS → git pull → docker pull → docker compose up
  └─► Tag release
```

## Deployment Methods

| Method | Use Case | Status |
|--------|----------|--------|
| **Docker** (recommended) | All new deployments | Primary |
| **PM2** (legacy) | Existing sites not yet migrated | Legacy |

Docker advantages: consistent builds, no Node.js version management on VPS, instant rollback via image tags, builds happen in CI not on VPS.

## VPS Details

| Component | Details |
|-----------|---------|
| **OS** | Windows Server 2022 |
| **IP** | 212.132.117.205 |
| **Panel** | Plesk (manages IIS) |
| **Container runtime** | Docker Desktop for Windows |
| **Legacy process manager** | PM2 (registered as Windows Service via pm2-windows-service) |
| **SSH** | OpenSSH Server (built-in, port 22) |
| **Apps directory** | `C:\apps\` |
| **Auth keys** | `C:\ProgramData\ssh\administrators_authorized_keys` |

## Docker Deployment Checklist for a New Site

### 1. Project Setup (in repo)

#### Dockerfile (multi-stage, node:22-alpine)

```dockerfile
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM node:22-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Add all NEXT_PUBLIC_* vars as build args — they get baked into the client bundle
ARG NEXT_PUBLIC_CONVEX_URL
ARG NEXT_PUBLIC_GA_ID
# ... add more as needed per project

ENV NEXT_PUBLIC_CONVEX_URL=$NEXT_PUBLIC_CONVEX_URL
ENV NEXT_PUBLIC_GA_ID=$NEXT_PUBLIC_GA_ID

RUN npm run build

FROM node:22-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs
EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/api/health || exit 1

CMD ["node", "server.js"]
```

#### next.config.ts — add standalone output

```ts
output: "standalone"  // Required for minimal Docker images
```

#### .dockerignore

```
node_modules
.next
.git
.github
.env*
.claude
.ca
*.log
nul
```

#### Health check endpoint (e.g., `app/api/health/route.ts`)

```ts
import { NextResponse } from "next/server";

export const dynamic = "force-dynamic";

export function GET() {
  return NextResponse.json({
    status: "ok",
    timestamp: new Date().toISOString(),
  });
}
```

#### docker-compose.yml

```yaml
services:
  web:
    image: ghcr.io/{owner}/{repo}:latest
    ports:
      - "{HOST_PORT}:3000"
    env_file:
      - .env
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:3000/api/health"]
      interval: 30s
      timeout: 3s
      start_period: 10s
      retries: 3
```

**IMPORTANT**: The `image` field must use the lowercase version of the GitHub repo path. ghcr.io normalizes all names to lowercase. For example, repo `MyOrg/My-Repo` becomes `ghcr.io/myorg/my-repo`.

#### .nvmrc

```
22
```

### 2. GitHub Actions CI/CD

**Secrets** (repo → Settings → Secrets → Actions):

| Secret | Type | Value |
|--------|------|-------|
| `VPS_HOST` | SSH | 212.132.117.205 |
| `VPS_USERNAME` | SSH | Administrator |
| `VPS_SSH_KEY` | SSH | Private key contents |
| `NEXT_PUBLIC_*` | Build-time | Baked into Docker image at build |
| `RESEND_API_KEY` etc. | Runtime | Written to .env on VPS during deploy |

**CI workflow** (`.github/workflows/ci.yml`) — PR quality gate:

```yaml
name: CI
on:
  pull_request:
    branches: [main]
concurrency:
  group: ci-${{ github.head_ref }}
  cancel-in-progress: true
jobs:
  quality:
    name: Lint & Typecheck
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: ".nvmrc"
          cache: npm
      - run: npm ci
      - run: npx tsc --noEmit
      - run: npm run lint
```

**Deploy workflow** (`.github/workflows/deploy.yml`) — production:

```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
concurrency:
  group: deploy-${{ github.ref }}
  cancel-in-progress: true

jobs:
  quality:
    name: Code Quality
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: ".nvmrc"
          cache: npm
      - run: npm ci
      - run: npx tsc --noEmit
      - run: npm run lint

  build-and-push:
    name: Build & Push Docker Image
    needs: quality
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - name: Docker meta
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=raw,value=latest
            type=sha,prefix=
      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          build-args: |
            NEXT_PUBLIC_CONVEX_URL=${{ secrets.NEXT_PUBLIC_CONVEX_URL }}
            NEXT_PUBLIC_GA_ID=${{ secrets.NEXT_PUBLIC_GA_ID }}

  deploy-vps:
    name: Deploy to VPS
    needs: [build-and-push]
    runs-on: ubuntu-latest
    steps:
      - name: Deploy via SSH
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USERNAME }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd {VPS_APP_PATH}
            git pull
            echo RESEND_API_KEY=${{ secrets.RESEND_API_KEY }}> .env
            echo CONTACT_EMAIL=${{ secrets.CONTACT_EMAIL }}>> .env
            docker pull ghcr.io/${{ github.repository }}:latest
            docker compose up -d --force-recreate
            docker image prune -f

  release:
    name: Create Release Tag
    needs: deploy-vps
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - name: Tag release
        run: |
          TAG="deploy-$(date +'%Y%m%d-%H%M%S')"
          git tag $TAG
          git push origin $TAG
```

### 3. Prepare the VPS (one-time per site)

```powershell
# Create app directory and clone repo
mkdir C:\apps\{site-name}
cd C:\apps\{site-name}
git clone https://{PAT}@github.com/{owner}/{repo}.git {repo-folder}
cd {repo-folder}

# Authenticate Docker with ghcr.io (one-time per GitHub account)
docker login ghcr.io -u {github-username} -p {PAT-with-read:packages}
```

### 4. Configure Plesk + IIS Reverse Proxy

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

### 5. Configure Cloudflare DNS

In Cloudflare Dashboard → domain → DNS:

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | @ | 212.132.117.205 | Proxied (orange cloud) |
| CNAME | www | {domain} | Proxied (orange cloud) |

In SSL/TLS settings: set mode to **Full** (not Full Strict).

No SSL certificate needed on the VPS — Cloudflare terminates SSL.

### 6. Set Up SSH Key for GitHub Actions

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

## Rollback Strategy

Every CI build produces a SHA-tagged image (e.g., `ghcr.io/owner/repo:abc1234`). To roll back:

```powershell
cd {VPS_APP_PATH}
docker pull ghcr.io/{owner}/{repo}:{previous-sha}
docker compose down && docker compose up -d
```

## Port Allocation

Check existing ports before choosing:
```powershell
netstat -ano | findstr "LISTENING" | findstr "30"
docker ps
```

Currently allocated:
- Port 3010: do-it-website (doitdigital.nl) — Docker

## Known Issues & Gotchas

### Docker on Windows
- Docker Desktop must be running (set to start with Windows)
- ghcr.io **lowercases all image names**. Repo `MyOrg/My-Repo` becomes `ghcr.io/myorg/my-repo`. The `docker-compose.yml` image field and manual `docker pull` commands must use the lowercase version.
- `docker compose` (v2) works on Windows. Do NOT use `docker-compose` (v1 with hyphen).

### appleboy/ssh-action + Windows
- The SSH script runs in **cmd.exe** by default on Windows
- **Do NOT use the `envs` parameter** — it generates `export VAR=value` (Linux bash syntax) which fails on Windows CMD with "'export' is not recognized"
- Instead, inline secrets directly in the script: `echo KEY=${{ secrets.KEY }}> .env`. GitHub Actions resolves `${{ secrets.* }}` before sending the script over SSH.
- Windows-style paths (`C:\apps\...`) work fine in the script

### Windows-Specific
- `ssh-keygen -f ~/.ssh/key` fails on Windows PowerShell. Use full path: `ssh-keygen -f C:\Users\DAerts\.ssh\key`
- `administrators_authorized_keys` must be a FILE, not a folder. If you copy a .pub file to that path, Windows creates a folder. Use `Set-Content` or `Copy-Item` instead.

### Plesk + IIS
- Plesk manages IIS. Do NOT create IIS sites manually — they conflict with Plesk. Always add domains through Plesk first.
- If "another website may be using the same port" error: a manually created IIS site is conflicting. Delete it in IIS Manager, then retry in Plesk.
- Plesk's Node.js hosting feature has limited configurability. Use the reverse proxy approach (web.config rewrite rule) instead.

### Cloudflare
- DNS checker may show old IP — Cloudflare-proxied domains show Cloudflare IPs, not the VPS IP. This is normal.
- SSL mode must be "Full" (not "Full Strict") since the VPS doesn't have its own SSL cert.
- Cloudflare provides free SSL for the domain and all subdomains automatically.

## Environment Variable Strategy

| Variable Type | Where Defined | When Resolved | Example |
|---------------|---------------|---------------|---------|
| `NEXT_PUBLIC_*` | GitHub Secrets → Docker build args | Build time (baked into JS bundle) | `NEXT_PUBLIC_GA_ID` |
| Server-only secrets | GitHub Secrets → written to `.env` on VPS via SSH | Runtime (read by container) | `RESEND_API_KEY` |

**IMPORTANT**: `NEXT_PUBLIC_*` variables MUST be passed as Docker build args because Next.js inlines them at build time. They cannot be injected at runtime via `.env`.

## Quick Reference Commands (VPS)

```powershell
# Docker
docker ps                              # Running containers
docker logs {container-name} --tail 50 # Container logs
docker compose up -d --force-recreate  # Restart with new image
docker compose down                    # Stop container
docker image prune -f                  # Clean old images

# Legacy PM2
pm2 list
pm2 logs {site-name} --lines 20
pm2 restart {site-name}

# Network & IIS
netstat -ano | findstr "LISTENING" | findstr "30"
iisreset
Restart-Service sshd
Get-Service sshd
```

---

## Legacy: PM2 Deployment (for existing sites not yet migrated)

For sites still using PM2, the deploy workflow SSHes in and runs:
```
git pull → npm ci → npm run build → pm2 restart
```

To migrate a PM2 site to Docker:
1. Add Dockerfile, .dockerignore, docker-compose.yml, health endpoint to the repo
2. Add `output: "standalone"` to next.config
3. Update deploy.yml to use the Docker pipeline (see above)
4. On VPS: `pm2 stop {site-name} && pm2 delete {site-name}`
5. Run `docker compose up -d` to start the containerized version
