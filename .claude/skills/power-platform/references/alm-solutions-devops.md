# ALM, Solutions & DevOps Reference

## ALM Overview

Application Lifecycle Management covers governance, development, and maintenance of Power Platform workloads. Core building blocks:

- **Solutions** -- transport mechanism for moving components across environments
- **Dataverse** -- stores all artifacts including solutions and pipeline configuration
- **Source control** -- single source of truth for all components
- **CI/CD** -- Azure DevOps or GitHub Actions automate build, test, and deploy

All environments participating in ALM require a Dataverse database.

## Solutions: Managed vs Unmanaged

| Aspect | Unmanaged | Managed |
|--------|-----------|---------|
| Purpose | Development | Non-dev environments (test, UAT, prod) |
| Editable | Yes | No (cannot edit components directly) |
| Delete behavior | Removes container only; customizations stay in default solution | Removes all customizations and data in custom tables |
| Source | Author and export from dev | Generate as build artifact on build server |
| Source control | Check in unmanaged solution | Do not check in; build from source |

### Solution Lifecycle Actions

| Action | Description |
|--------|-------------|
| Create | Author and export unmanaged solutions |
| Update | Deploy changes to parent managed solution; cannot remove components |
| Upgrade | Full replacement; removes unused components; merges patches into new base |
| Patch | Incremental changes layered on top of parent (not recommended by Microsoft) |

### Solution Publisher

- Every solution has a publisher with a prefix (e.g., `contoso_`) to prevent naming collisions
- Cannot change publisher after components exist in a managed solution
- Best practice: use a single publisher across all solutions for flexible layering

### Solution Components

- Includes: tables, columns, apps, flows, agents, charts, plug-ins, custom connectors
- Maximum solution size: 95 MB
- System tracks dependencies between solutions for install/uninstall ordering
- Segmented solutions allow including only changed table components (columns, forms, views)

## Solution Layers

Two distinct layers at the component level:

| Layer | Description |
|-------|-------------|
| Unmanaged | All imported unmanaged solutions and ad-hoc customizations share a single layer |
| Managed | All imported managed solutions stacked in install order; system solution at base |

**Merge behavior:**
- Model-driven apps, forms, site maps: **merge** logic
- All other components: **top wins** (highest layer determines runtime)

**Within a managed solution:**
- Base layer (bottom) with publisher and managed properties
- Patches stacked above base (most recent on top)
- Pending upgrade sits on top; applying flattens all layers into new base

## Environment Strategy

| Type | Purpose | Users |
|------|---------|-------|
| Development (Sandbox) | Build and test; supports reset/delete/copy | Makers, developers |
| Test | End-to-end validation including deployment testing | Admins, testers |
| UAT/SIT | User acceptance and integration testing | Admins, selected users |
| Production | Live environment for end users | Admins, app users |
| Developer | Single-user free environment for learning | Individual developer |
| Default | Auto-created per tenant; shared by all | All users (restrict access) |

**Best practices:**
- Minimum: separate dev + test + production environments
- Developers need at least Environment Maker security role
- Dev environments should be in the same or earlier update station as production
- Solutions can import into newer environments but not reliably into older ones

## CI/CD with Azure DevOps

Power Platform Build Tools v2.0 (CLI-based) automate build and deployment tasks.

### Task Categories

| Category | Examples |
|----------|---------|
| Helper | Tool installer, environment setup |
| Quality Check | Power Apps Checker (static analysis, SARIF output) |
| Solution | Export, import, unpack, pack, clone, publish customizations |
| Environment | Create, copy, reset, backup, restore, delete |

### Pipeline Pattern

1. **Initiate** -- set up and configure tools
2. **Export from Dev** -- export unmanaged solution
3. **Build** -- generate managed solution artifact
4. **Release** -- deploy to downstream environments

### Service Connections

| Type | Description |
|------|-------------|
| Workload Identity Federation (recommended) | Service principal via federated credentials; supports MFA |
| Service principal + client secret | App registration with secret |
| Username/password | Generic; does not support MFA |

### Setup

1. Install Build Tools from Azure Marketplace
2. Create app registration in Microsoft Entra ID
3. Run `pac admin create-service-principal --environment <id>`
4. Configure Application User with System Administrator role
5. Create service connection in Azure DevOps

## CI/CD with GitHub Actions

Same CLI-based tasks as Build Tools but for GitHub workflows.

### Setup

1. Create three Dataverse environments (dev, build, prod) -- minimum 3 GB capacity
2. Register app in Microsoft Entra ID with API permissions (Dynamics CRM, PowerApps Runtime, PowerApps-Advisor)
3. Create client secret; store as GitHub Secret
4. Create Application User in each environment with System Administrator role

### Available Actions

Export/import/unpack/pack solution, solution checker, publish customizations, create/delete/backup/restore environments, deploy via `pac pipeline` commands.

## Power Platform Pipelines (In-Product)

Built-in ALM automation -- no external tools required.

### Architecture

| Component | Role |
|-----------|------|
| Host environment | Production environment storing pipeline config and artifacts |
| Development environment | Where makers build and initiate deployments |
| Target environments | QA, production, or other downstream stages |

### Key Behaviors

- Solutions exported at deployment request; same artifact flows through all stages
- Cannot skip stages (e.g., QA cannot be bypassed)
- Default import: Upgrade without overwrite customizations
- Only managed solutions deployed; automatic backups stored in host
- Supports approval-based delegated deployments and cross-region deployment

### Licensing

Host, dev, and QA environments: no license. Production targets require Managed Environment + premium license.

## ALM Tool Comparison

| Feature | Pipelines (In-Product) | Azure DevOps | GitHub Actions |
|---------|----------------------|--------------|----------------|
| Setup complexity | Low (minutes) | Medium (hours) | Medium (hours) |
| Target user | Makers, admins | Developers, DevOps | Developers, DevOps |
| External tool | No | Yes | Yes |
| Cross-tenant | No | Yes | Yes |
| Extensibility | Via Power Automate | Full pipeline customization | Full workflow customization |
| Approvals | Built-in delegation | Azure DevOps approvals | GitHub environment protections |
| Source control | Optional extension | Native | Native |

## Source Control and Branching

### Integration Options

1. Power Platform Git Integration (built-in)
2. Custom pipelines using Build Tool tasks or YAML
3. PAC CLI for export, unpack, and commit workflows

### Branching Strategies

- **Trunk-based** -- single main branch with short-lived feature branches
- **Release branching** -- separate branches per release
- **Feature branching** -- isolated branches per feature

### Team Development

- Avoid multiple people editing complex components simultaneously (forms, flows, canvas apps)
- Break solutions into logical segments to reduce contention
- Use source control as the single source of truth
