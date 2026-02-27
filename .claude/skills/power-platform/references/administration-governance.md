# Administration & Governance Reference

## Environment Types

| Type | Purpose | Notes |
|------|---------|-------|
| Production | Live workloads for end users | Requires appropriate licensing |
| Sandbox | Development and testing; supports reset/delete/copy | Low-risk experimentation |
| Developer | Single-user environment for learning/building | Free with developer plan |
| Trial | 30-day temporary environment | Can convert to production |
| Default | Auto-created per tenant; shared by all users | Restrict access; avoid for development |

All environments participating in ALM require a Dataverse database. Each environment has separate location, roles, security, and audience.

### Supported Operations

- Backup, restore, copy, reset, delete, recover
- NOT supported: move between tenants

## Admin Roles

| Role | Scope |
|------|-------|
| Global Administrator | Full tenant-level access to all Power Platform resources |
| Power Platform Administrator | Manage environments, DLP policies, analytics, billing |
| Dynamics 365 Administrator | Manage Dynamics 365 environments and Power Platform settings |
| Environment Admin | Full control within a specific environment |
| Environment Maker | Create apps, flows, and agents within an environment |
| System Administrator | Full Dataverse access within an environment |

- Developers need at least Environment Maker security role
- Production users should have only necessary privileges
- System Administrator role required for full environment management

## CoE Starter Kit (Center of Excellence)

A collection of managed solution components for adopting and governing Power Platform.

### Modules

| Module | Purpose |
|--------|---------|
| Admin | Inventory of apps, flows, makers; Power BI dashboards; adoption insights |
| Govern | Audit and compliance processes; DLP policy management; environment management |
| Nurture | Community building; maker onboarding; training resources; app showcases |

### Setup

- Install as managed solution in a dedicated environment
- Requires Dataverse, Power Automate, and Power BI
- Target audiences: CoE leads, IT admins, enterprise architects, CISOs, line-of-business leaders

## Well-Architected Framework

Five pillars of best-practice guidance for Power Platform workloads:

| Pillar | Focus |
|--------|-------|
| Reliability | Uptime and recovery targets; redundancy and resiliency at scale |
| Security | Protect workloads from attacks; confidentiality and data integrity |
| Operational Excellence | Reduce production issues; observability and automated systems |
| Performance Efficiency | Handle demand changes; horizontal scaling; test before deploy |
| Experience Optimization | Meaningful user experiences ensuring business outcomes |

### Resources

- Design review checklists per pillar
- Recommendation guides with tradeoff analysis
- Assessment tool at `https://aka.ms/powa/assessment`
- Architecture Center for Power Platform and Copilot Studio solutions

## Adoption Methodology

| Pillar | Description |
|--------|-------------|
| Strategy | Document objectives, measurable key results, key initiatives |
| Plan | Define roles, responsibilities, delivery models |
| Security | Protect workloads and data; meet compliance requirements |
| Governance | Digital guardrails for makers to create with confidence |
| Operations | ALM strategy and ongoing production support |
| Availability | Plan for failures and disaster recovery |
| Readiness | Upskill makers; envision high-value use cases |
| Community | Internal community of practice; knowledge sharing |

## Power Apps Coding Guidelines

Standards for consistent, performant, and maintainable canvas apps:

- **Naming conventions** -- objects, collections, and variables
- **Code organization** -- screens and controls
- **Performance best practices** -- formulas and data calls
- **Maintainability** -- team development standards

### Recommended Tooling

- **Power CAT Toolkit** (marketplace): automated code reviews against guidelines, flags non-compliant patterns, maintains quality standards across projects

## Governance Patterns

### DLP Policy Strategy

- Start with a tenant-wide baseline policy classifying connectors into Business / Non-Business / Blocked groups
- Layer environment-specific policies for exceptions
- Most restrictive policy wins when multiple policies apply
- Block HTTP and custom connectors by default; allow explicitly per environment

### Environment Strategy

- Minimum: separate dev + test + production environments
- Isolate development work to avoid conflicts between makers
- Restrict the default environment to prevent uncontrolled citizen development
- Dev environments should be in the same or earlier update station as production

### Monitoring and Compliance

- Use CoE Admin module for inventory and usage analytics
- Power BI dashboards for adoption metrics
- Audit logs for change tracking and compliance
- Solution checker for static analysis of apps and flows
