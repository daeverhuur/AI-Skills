---
name: vps-deploy
description: Deploy websites to Strato Windows VPS with Docker Compose, Plesk/IIS reverse proxy, Cloudflare DNS, and GitHub Actions CI/CD. Use when the user wants to deploy a site, set up hosting, configure CI/CD for VPS, or mentions "deploy to VPS", "Strato", "Plesk hosting", or "production deployment".
version: 2.0.0
---

# VPS Deployment Skill

Deploy Next.js (or any Node.js) websites to the user's Strato Windows Server 2022 VPS using Docker Compose with automated CI/CD.

## Infrastructure Overview

```
User -> Cloudflare (SSL/CDN) -> VPS:443 (Plesk/IIS) -> localhost:{PORT} (Docker)

GitHub push to main
  |-> GitHub Actions: lint + typecheck
  |     |-> Deploy backend (Convex/other) if applicable
  |     |-> SSH into VPS -> git pull -> write .env -> docker compose build -> docker compose up -d
  |-> Tag release: deploy-YYYYMMDD-HHMMSS
```

## VPS Details

| Component | Details |
|-----------|---------|
| **OS** | Windows Server 2022 |
| **IP** | 212.132.117.205 |
| **Panel** | Plesk (manages IIS reverse proxy) |
| **Container runtime** | Docker Desktop for Windows |
| **SSH** | OpenSSH Server (built-in, port 22) |
| **Apps directory** | `C:\apps\` |
| **Auth keys** | `C:\ProgramData\ssh\administrators_authorized_keys` |
| **Node version** | 22 (inside Docker containers) |

## Deployment Checklist for a New Site

### 1. Prepare the VPS

```powershell
# Create app directory
mkdir C:\apps\{site-name}
cd C:\apps\{site-name}

# Clone the repo (use GITHUB_TOKEN for private repos)
git clone https://x-access-token:{PAT}@github.com/{owner}/{repo}.git .

# Create .env for server-side secrets (NOT NEXT_PUBLIC_ vars)
notepad .env
# Add: RESEND_API_KEY, CONTACT_EMAIL, etc.
```

### 2. Create Dockerfile (Multi-Stage Build)

Create a `Dockerfile` in the project root:

```dockerfile
# Stage 1: deps
FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Stage 2: builder
FROM node:22-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Build args for NEXT_PUBLIC_* env vars (baked into client bundle at build time)
ARG NEXT_PUBLIC_CONVEX_URL
# Add more NEXT_PUBLIC_* ARGs as needed

ENV NEXT_PUBLIC_CONVEX_URL=$NEXT_PUBLIC_CONVEX_URL
# Mirror each ARG as ENV for the build step

RUN npm run build

# Stage 3: runner
FROM node:22-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

# Copy standalone output (requires output: 'standalone' in next.config)
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/api/health || exit 1

CMD ["node", "server.js"]
```

**IMPORTANT**: Requires `output: 'standalone'` in `next.config.ts`.

### 3. Create docker-compose.yml

```yaml
services:
  web:
    build:
      context: .
      args:
        NEXT_PUBLIC_CONVEX_URL: ${NEXT_PUBLIC_CONVEX_URL}
        # Add more NEXT_PUBLIC_* build args as needed
    image: ghcr.io/{owner}/{repo}:latest
    ports:
      - "{PORT}:3000"
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

**Port allocation** - check existing ports before choosing:
```powershell
netstat -ano | findstr "LISTENING" | findstr "30"
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

Currently allocated:
- Port 3010: do-it-website (doitdigital.nl)

### 4. Create Health Check Endpoint

Create `app/api/health/route.ts`:

```ts
export async function GET() {
  return Response.json({ status: 'ok' });
}
```

### 5. Configure Plesk + IIS Reverse Proxy

**Prerequisites** (one-time, already done):
- IIS URL Rewrite module installed
- IIS Application Request Routing (ARR) installed and proxy enabled

**Per site:**

1. In Plesk (`https://212.132.117.205:8443`):
   - **Websites & Domains** -> **Add Domain**
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

### 6. Configure Cloudflare DNS

In Cloudflare Dashboard -> domain -> DNS:

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | @ | 212.132.117.205 | Proxied (orange cloud) |
| CNAME | www | {domain} | Proxied (orange cloud) |

In SSL/TLS settings: set mode to **Full** (not Full Strict).

No SSL certificate needed on the VPS - Cloudflare terminates SSL.

### 7. Set Up SSH Key for GitHub Actions

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

### 8. GitHub Actions CI/CD

**Secrets** (repo -> Settings -> Secrets -> Actions):

| Secret | Value | Purpose |
|--------|-------|---------|
| VPS_HOST | 212.132.117.205 | VPS IP or hostname |
| VPS_USERNAME | Administrator | SSH username |
| VPS_SSH_KEY | Private key contents | Ed25519 private key |
| RESEND_API_KEY | re_xxx... | Email service key (or other server-side secrets) |
| CONTACT_EMAIL | info@domain.nl | Contact form recipient |
| CONVEX_DEPLOY_KEY | (if using Convex) | Convex production deploy key |

**CI workflow** (`.github/workflows/ci.yml`) - PR quality gate:

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
  build:
    name: Build Test
    runs-on: ubuntu-latest
    needs: quality
    env:
      # Placeholder values so NEXT_PUBLIC_* vars don't fail the build
      NEXT_PUBLIC_CONVEX_URL: https://ci-placeholder.convex.cloud
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: ".nvmrc"
          cache: npm
      - run: npm ci
      - run: npm run build
```

**Deploy workflow** (`.github/workflows/deploy.yml`) - production:

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

  deploy-convex:
    name: Deploy Convex
    needs: quality
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: ".nvmrc"
          cache: npm
      - run: npm ci
      - run: npx convex deploy
        env:
          CONVEX_DEPLOY_KEY: ${{ secrets.CONVEX_DEPLOY_KEY }}

  deploy-vps:
    name: Deploy to VPS
    needs: [quality, deploy-convex]
    runs-on: ubuntu-latest
    steps:
      - name: Setup SSH key
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.VPS_SSH_KEY }}" > ~/.ssh/deploy_key
          chmod 600 ~/.ssh/deploy_key
          ssh-keyscan -H ${{ secrets.VPS_HOST }} >> ~/.ssh/known_hosts 2>/dev/null

      - name: Deploy via SSH
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          RESEND_API_KEY: ${{ secrets.RESEND_API_KEY }}
          CONTACT_EMAIL: ${{ secrets.CONTACT_EMAIL }}
          NEXT_PUBLIC_CONVEX_URL: ${{ secrets.NEXT_PUBLIC_CONVEX_URL }}
          NEXT_PUBLIC_GA_ID: ${{ secrets.NEXT_PUBLIC_GA_ID }}
          NEXT_PUBLIC_PHONE_DISPLAY: ${{ secrets.NEXT_PUBLIC_PHONE_DISPLAY }}
          NEXT_PUBLIC_PHONE_HREF: ${{ secrets.NEXT_PUBLIC_PHONE_HREF }}
          NEXT_PUBLIC_WHATSAPP_NUMBER: ${{ secrets.NEXT_PUBLIC_WHATSAPP_NUMBER }}
          GH_REPO: ${{ github.repository }}
        run: |
          SSH_CMD="ssh -i ~/.ssh/deploy_key -o StrictHostKeyChecking=no -o ServerAliveInterval=30 -o ServerAliveCountMax=20 ${{ secrets.VPS_USERNAME }}@${{ secrets.VPS_HOST }}"

          echo "=== Pulling latest code ==="
          $SSH_CMD "cd C:\apps\{site-name} && git remote set-url origin https://x-access-token:${GITHUB_TOKEN}@github.com/${GH_REPO}.git && git pull && git remote set-url origin https://github.com/${GH_REPO}.git"

          echo "=== Writing environment file ==="
          $SSH_CMD "cd C:\apps\{site-name} && (echo RESEND_API_KEY=${RESEND_API_KEY})> .env && (echo CONTACT_EMAIL=${CONTACT_EMAIL})>> .env && (echo NEXT_PUBLIC_CONVEX_URL=${NEXT_PUBLIC_CONVEX_URL})>> .env && (echo NEXT_PUBLIC_GA_ID=${NEXT_PUBLIC_GA_ID})>> .env && (echo NEXT_PUBLIC_PHONE_DISPLAY=${NEXT_PUBLIC_PHONE_DISPLAY})>> .env && (echo NEXT_PUBLIC_PHONE_HREF=${NEXT_PUBLIC_PHONE_HREF})>> .env && (echo NEXT_PUBLIC_WHATSAPP_NUMBER=${NEXT_PUBLIC_WHATSAPP_NUMBER})>> .env"

          echo "=== Building and starting container ==="
          $SSH_CMD "cd C:\apps\{site-name} && docker compose build --no-cache && docker compose up -d --force-recreate"

          echo "=== Waiting for container to start ==="
          sleep 10

          echo "=== Checking container status ==="
          $SSH_CMD "cd C:\apps\{site-name} && docker compose ps"

          echo "=== Checking health endpoint ==="
          $SSH_CMD "curl -sf http://localhost:{PORT}/api/health" || (echo "FAILED: Health check failed" && exit 1)

          echo "=== Cleaning up old images ==="
          $SSH_CMD "docker image prune -f"

          echo "=== Deployment successful ==="

      - name: Cleanup SSH key
        if: always()
        run: rm -f ~/.ssh/deploy_key

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

**Key deployment steps:**
1. SSH into VPS using raw SSH (not appleboy/ssh-action)
2. Git pull latest code (using GITHUB_TOKEN for private repos)
3. Write `.env` with server-side secrets only
4. `docker compose build --no-cache` - rebuild the image
5. `docker compose up -d --force-recreate` - replace the running container
6. Health check via `curl -sf http://localhost:{PORT}/api/health`
7. Prune old Docker images to save disk space

### 9. Node Version Pinning

Create `.nvmrc` in project root:
```
22
```

Both CI and deploy workflows read this via `node-version-file: ".nvmrc"`.

## Known Issues & Gotchas

### Docker on Windows
- Docker Desktop must be running on the VPS for `docker compose` commands to work.
- Windows containers vs Linux containers: ensure Docker Desktop is set to **Linux containers** mode for Node.js Alpine images.
- `docker compose build --no-cache` can be slow on first build due to downloading base images. Subsequent builds are faster.
- Use `docker image prune -f` after deployments to reclaim disk space from dangling images.

### SSH in GitHub Actions
- Direct SSH (`ssh -i key user@host "commands"`) is used instead of `appleboy/ssh-action` for more control over the deployment sequence.
- The SSH script runs commands in the VPS shell. Windows-style paths (`C:\apps\...`) work fine.
- `GITHUB_TOKEN` is used temporarily for `git pull` on private repos, then the remote URL is reset to the public URL.
- Always clean up the SSH key in an `if: always()` step.
- **SSH keep-alive is required.** Docker builds on the VPS can take 5-10 minutes. Without `-o ServerAliveInterval=30 -o ServerAliveCountMax=20`, the SSH connection will drop with "Broken pipe" during `npm ci` or `npm run build`. Always add keep-alive options to the SSH command.

### Windows-Specific
- `ssh-keygen -f ~/.ssh/key` fails on Windows PowerShell. Use full path: `ssh-keygen -f C:\Users\DAerts\.ssh\key`
- `administrators_authorized_keys` must be a FILE, not a folder. If you copy a .pub file to that path, Windows creates a folder. Use `Set-Content` or `Copy-Item` instead.

### Plesk + IIS
- Plesk manages IIS. Do NOT create IIS sites manually - they conflict with Plesk. Always add domains through Plesk first.
- If "another website may be using the same port" error: a manually created IIS site is conflicting. Delete it in IIS Manager, then retry in Plesk.
- The IIS reverse proxy forwards traffic from port 443/80 to the Docker container's mapped port.

### Cloudflare
- DNS checker may show old IP - Cloudflare-proxied domains show Cloudflare IPs, not the VPS IP. This is normal.
- SSL mode must be "Full" (not "Full Strict") since the VPS doesn't have its own SSL cert.
- Cloudflare provides free SSL for the domain and all subdomains automatically.

### NEXT_PUBLIC_* Environment Variables
- `NEXT_PUBLIC_*` vars are baked into the client bundle at **build time** (not runtime).
- They must be available as Docker build args or in the build environment.
- Server-side secrets (e.g., `RESEND_API_KEY`) go in `.env` and are passed at runtime via `env_file` in docker-compose.yml.
- **The CI/CD `.env` write step must include ALL vars.** If the workflow overwrites `.env` with only server-side secrets, the `NEXT_PUBLIC_*` vars are lost. Docker Compose reads build args from `.env` via `${VAR}` interpolation, so ALL needed vars must be present before `docker compose build`.
- **docker-compose.yml must have a `build:` directive.** Without `build: { context: . }`, `docker compose build --no-cache` has nothing to build and silently does nothing. The container will keep running the old image. Always include both `build:` and `image:` in docker-compose.yml.

### Convex
- If the project uses Convex, the `deploy-convex` job runs `npx convex deploy` with the `CONVEX_DEPLOY_KEY` secret.
- If the project does NOT use Convex, remove the `deploy-convex` job and its dependency from `deploy-vps.needs`.

## Environment Separation Pattern

| | Development (laptop) | Production (VPS) |
|---|---|---|
| Config file | `.env.local` | `.env` (written by CI) |
| Container | None (bare `npm run dev`) | Docker Compose |
| Database | Dev instance (e.g., Convex dev) | Production instance |
| API keys | Test/sandbox keys | Real keys (injected by CI) |
| Analytics | Disabled or dev property | Real GA4 ID |
| Git ignored | `.env.local` - yes | `.env` - yes |

## Quick Reference Commands (VPS)

```powershell
# Check running containers
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# View container logs
docker compose -f C:\apps\{site-name}\docker-compose.yml logs --tail 50

# Restart a site
docker compose -f C:\apps\{site-name}\docker-compose.yml restart

# Rebuild and restart (after manual changes)
cd C:\apps\{site-name}
docker compose build --no-cache && docker compose up -d --force-recreate

# Check health
curl -sf http://localhost:{PORT}/api/health

# Check ports in use
netstat -ano | findstr "LISTENING" | findstr "30"

# Clean up old Docker images
docker image prune -f

# Check disk usage by Docker
docker system df

# Restart IIS (if reverse proxy issues)
iisreset

# Restart SSH
Restart-Service sshd

# Check SSH service
Get-Service sshd
```
