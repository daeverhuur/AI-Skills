# Licensing & Governance Reference

## License Types Overview

Power Platform licensing uses a combination of per-user plans, per-app plans, and capacity-based pricing. License requirements depend on which features, connectors, and services an app or flow uses.

### License Type Matrix

| License Type | Scope | Includes | Use Case |
|-------------|-------|----------|----------|
| Power Apps per user | Unlimited apps per user | All premium connectors, Dataverse, custom connectors, on-prem gateway | Power users running many apps |
| Power Apps per app | 1 app per user | Same premium features as per-user but scoped to one app | Broad deployment of a single app |
| Power Automate per user | Unlimited flows per user | Premium connectors, Dataverse, custom connectors, 40K Power Platform requests/day | Users building multiple flows |
| Power Automate per flow | 1 flow, unlimited users | Same premium features, 250K Power Platform requests/day | High-throughput shared process flows |
| Pay-as-you-go | Per meter usage | Same features as standalone plans; billed monthly on Azure | Variable/unpredictable usage; testing |
| Developer plan | Single user | Full premium features in developer environment | Learning, prototyping, individual development |
| Trial | 30 days | Full premium features | Evaluation before purchase |
| M365 included | Per M365 license | Standard connectors only, no Dataverse, limited customization | Simple apps within M365 ecosystem |

### Microsoft 365 Included Capabilities

Users with M365 E1/E3/E5/F1/F3 licenses can use Power Apps and Power Automate with limitations:

| Feature | M365 Included | Standalone Plan Required |
|---------|---------------|------------------------|
| Standard connectors | Yes | Yes |
| Premium connectors | No | Yes |
| Custom connectors | No | Yes |
| On-premises data gateway | No | Yes |
| Dataverse (full) | No (limited Dataverse for Teams) | Yes |
| Custom tables in Dataverse | No (Dataverse for Teams only) | Yes |
| AI Builder | No | Yes (credits included with some plans) |
| Power Pages | No | Separate Power Pages license |
| HTTP connector | No | Yes |
| Environment creation | Default + Teams environments only | Yes |

### Dataverse for Teams vs Full Dataverse

| Aspect | Dataverse for Teams | Full Dataverse |
|--------|-------------------|----------------|
| License required | M365 (included) | Power Apps standalone or per-app |
| Storage | 2 GB per environment, 1M rows | Based on tenant capacity allocation |
| Environments | Linked to Teams team | Standalone environments |
| Tables | Up to 500 custom tables | Unlimited |
| Business logic | Basic rules | Full plugins, workflows, business rules |
| Security | Teams-based (Owner, Member, Guest) | Full Dataverse security model |
| ALM | Limited | Full solution lifecycle |

## Premium vs Standard Features

### Connector Tiers

| Tier | Examples | License Required |
|------|----------|-----------------|
| Standard | SharePoint, Outlook, Excel, OneDrive, Teams, Planner, Approvals | M365 or standalone |
| Premium | Dataverse, SQL Server, Azure SQL, Salesforce, ServiceNow, SAP, Adobe | Standalone Power Apps/Automate plan |
| Custom | Any connector you build via OpenAPI | Standalone plan |
| On-premises | Any connector via data gateway | Standalone plan |

### Features Requiring Premium License

- **Dataverse**: Full Dataverse database (not Dataverse for Teams)
- **Custom connectors**: Any custom-built connector
- **On-premises data gateway**: Connecting to on-prem SQL, file shares, etc.
- **HTTP connector**: Direct HTTP requests to any API
- **AI Builder**: Document processing, prediction, text recognition
- **Premium connectors**: SQL Server, Azure services, SAP, Salesforce, etc.
- **Power Automate process mining**: Task mining and process mining
- **Power Automate desktop flows (attended/unattended)**: Requires per-user plan with attended RPA or unattended RPA add-on
- **Custom pages**: In model-driven apps (requires Dataverse = premium)

### Seeded App Rights

Some Dynamics 365 and M365 licenses include "seeded" Power Apps and Power Automate rights:

- **Dynamics 365 licenses**: Can use Power Apps/Automate within the context of the Dynamics 365 app (e.g., extending a Sales app)
- **Power BI Pro**: Can embed Power Apps visuals in Power BI reports
- **M365**: Standard connector apps and flows only
- Seeded rights do not extend to standalone apps outside the seeded context

## Pay-As-You-Go

Pay-as-you-go links a Power Platform environment to an Azure subscription, billing based on actual usage rather than pre-purchased licenses.

### How It Works

1. Create or identify an Azure subscription
2. Link the Azure subscription to a Power Platform environment in the admin center
3. Users in that environment can use premium features without individual licenses
4. Usage is metered and billed monthly to the Azure subscription
5. Multiple environments can link to the same Azure subscription

### Meters

| Meter | Unit | What It Measures |
|-------|------|-----------------|
| Power Apps per app | Per user per app per month | Each unique user who launches a premium app |
| Power Automate per flow | Per flow per month | Each flow that uses premium features and runs at least once |
| Dataverse | Per GB per month | Database, file, and log storage consumed |
| Power Platform requests | Per request over included amount | API calls exceeding the included allocation |

### When to Use Pay-As-You-Go

- **Unpredictable user counts**: Apps where monthly active users vary significantly
- **Seasonal workloads**: Apps used only during specific periods
- **Testing and development**: Environments used intermittently
- **Gradual rollout**: Starting with a few users before committing to per-user plans
- **Cost management**: Pay only for what is used; no upfront commitment

### Configuration Steps

1. Navigate to **Power Platform admin center** > **Environments**
2. Select the target environment > **Edit**
3. Under **Pay-as-you-go**, select **Link Azure subscription**
4. Choose the Azure subscription and resource group
5. Review and confirm; billing starts when premium features are used
6. Monitor costs in Azure Cost Management

## DLP Policies (Data Loss Prevention)

DLP policies control which connectors can be used together within an app or flow, preventing unauthorized data sharing between services.

### Connector Classification Groups

| Group | Purpose | Example |
|-------|---------|---------|
| Business | Trusted connectors that can share data with each other | SharePoint, Dataverse, Outlook |
| Non-Business | Connectors that cannot share data with Business group | Twitter, personal Gmail |
| Blocked | Connectors that cannot be used at all in the policy scope | Unapproved third-party services |

**Rule**: Connectors within the same group (Business or Non-Business) can be used together in a single app or flow. Connectors from different groups cannot.

### Creating a DLP Policy

1. Navigate to **Power Platform admin center** > **Policies** > **Data policies**
2. Select **New Policy**
3. Name the policy and optionally add a description
4. **Assign connectors**: Move connectors between Business, Non-Business, and Blocked groups
5. **Define scope**: Apply to all environments, specific environments, or exclude specific environments
6. Save the policy

### Connector-Level Controls

Beyond group classification, DLP policies support granular controls:

| Control | Description |
|---------|-------------|
| Connector action control | Allow or block specific actions within a connector (e.g., allow "Get items" but block "Delete item" in SharePoint) |
| Endpoint filtering | Restrict HTTP connector to specific URL patterns |
| Custom connector patterns | Allow/block custom connectors matching URL patterns |

### HTTP Connector Policies

The HTTP connector is powerful and potentially risky. DLP configuration options:

- **Block entirely**: Prevent any direct HTTP calls (recommended default)
- **Allow with endpoint filtering**: Specify allowed URL patterns

```
// Example: Allow only internal APIs
Allowed patterns:
  https://api.contoso.com/*
  https://internal.contoso.com/api/*

Blocked patterns:
  * (everything else)
```

### Custom Connector Policies

Control custom connectors by URL pattern:

| Pattern | Effect |
|---------|--------|
| `https://api.contoso.com/*` | Allow custom connectors to this domain |
| `*` in Blocked group | Block all custom connectors not explicitly allowed |
| No pattern configured | Custom connectors follow default group assignment |

### Policy Layering and Precedence

When multiple DLP policies apply to an environment:

- **Most restrictive wins**: If Policy A allows a connector and Policy B blocks it, the connector is blocked
- **Cross-policy groups**: If Connector X is in Business in Policy A but Non-Business in Policy B, the connector is effectively isolated (cannot combine with any other connector)
- **Evaluation order**: All applicable policies are evaluated simultaneously; there is no priority ranking
- **Best practice**: Start with a restrictive tenant-wide policy, then create environment-specific policies for exceptions

### DLP Policy Strategy Recommendations

1. **Tenant-wide baseline**: Block HTTP and custom connectors; classify common connectors
2. **Environment overrides**: Enable HTTP for specific dev/production environments that need it
3. **Regular review**: Audit connector usage quarterly; reclassify as needed
4. **Communication**: Inform makers before policy changes to avoid breaking existing apps
5. **Testing**: Test policy changes in sandbox environments first
6. **Documentation**: Maintain a registry of which connectors are allowed and why

## Managed Environments

Managed environments provide administrators with enhanced governance controls for Power Platform environments.

### Features

| Feature | Description |
|---------|-------------|
| Sharing limits | Restrict how many users an app can be shared with (e.g., max 20 users, or security groups only) |
| Solution checker enforcement | Require apps to pass Solution Checker before import (warn or block mode) |
| Usage insights | Weekly digest email to admins with app/flow adoption data |
| Maker welcome content | Custom welcome message shown to makers when they enter the environment |
| Data policies | Enhanced DLP management specific to the environment |
| Pipelines | Deployment pipelines for ALM (managed environments required at target) |
| IP firewall | Restrict Dataverse access to specific IP ranges (additional feature) |
| Customer-managed key | Encrypt Dataverse data with your own key (additional feature) |
| Extended backup | 28-day backup retention (vs 7 days for non-managed) |

### Sharing Limits Configuration

Control how canvas apps and cloud flows are shared:

| Setting | Options |
|---------|---------|
| Exclude sharing with security groups | Prevent sharing with broad security groups |
| Limit sharing to specific number | Set a maximum number of users (e.g., 20) |
| No limits | Same as non-managed environment |

This prevents makers from accidentally sharing an app with the entire organization before it is properly reviewed.

### Solution Checker Enforcement

| Mode | Behavior |
|------|----------|
| None | No enforcement; Solution Checker is optional |
| Warn | Show checker results on solution import; admin can proceed |
| Block | Prevent solution import if critical/high severity issues found |

Configuration:
1. Navigate to **Power Platform admin center** > **Environments**
2. Select environment > **Edit** > enable **Managed environment**
3. Under **Solution checker**, select enforcement level
4. Save changes

### Setup and Requirements

- Requires Power Apps or Power Automate per-user/per-app licenses (or Dynamics 365 license)
- Enabling managed environment is a one-way operation per environment (can be disabled by admin)
- Enabling does not affect existing apps or flows immediately
- New sharing limits apply only to future sharing actions
- Available for production, sandbox, developer, and teams environment types

### Limitations

- Cannot be enabled on the default environment (in some configurations)
- IP firewall and customer-managed key require additional licensing
- Some features are rolling out gradually and may not be available in all regions
- Maker welcome content has a character limit (plain text and links only)

## CoE Starter Kit (Center of Excellence)

The CoE Starter Kit is a collection of Power Platform components that help organizations adopt, govern, and nurture their Power Platform investments.

### Components Overview

| Component | Purpose | Key Artifacts |
|-----------|---------|---------------|
| Core | Inventory and environment data collection | Dataverse tables, cloud flows for sync |
| Admin | Governance and compliance tools | Admin app, inactive app/flow cleanup, capacity alerts |
| Audit | Compliance and audit logging | Audit log sync, DLP violation tracking, compliance dashboards |
| Nurture | Maker community building | Maker assessment app, training module, app catalog |
| Innovation Backlog | Idea management and prioritization | Idea submission app, voting mechanism, backlog management |
| Theming | Branded UI components | Theme editor, branded canvas app templates |

### Inventory (Core Module)

The inventory syncs data about all Power Platform resources:

- **Apps**: Canvas apps, model-driven apps, custom pages (name, owner, environment, last modified, connector usage)
- **Flows**: Cloud flows and desktop flows (name, owner, state, trigger type, connector usage)
- **Makers**: Users who have created apps or flows (name, department, last active)
- **Environments**: All tenant environments (type, region, Dataverse status, admin)
- **Connectors**: Connector usage across all apps and flows
- **Chatbots**: Copilot Studio agents (name, owner, environment)

Data is synced via scheduled cloud flows running daily or weekly.

### Admin Module Features

- **App and flow management**: View all apps/flows, identify orphaned resources, contact owners
- **Compliance dashboard**: DLP violations, apps using blocked connectors, audit trail
- **Cleanup workflows**: Automated notifications to owners of inactive apps/flows
- **Capacity monitoring**: Track Dataverse storage usage, API request consumption
- **Environment management**: Request and approval workflow for new environments

### Nurture Module Features

- **Maker assessment**: Self-service quiz for makers to assess their skill level
- **Training resources**: Curated learning paths and links to Microsoft Learn
- **App catalog**: Showcase of approved/featured apps for inspiration
- **Community engagement**: Templates for internal events, hackathons, newsletters

### Setup Process

1. **Prerequisites**: Dedicated environment with Dataverse, Power BI Pro license for dashboards
2. **Install Core module** first as a managed solution
3. **Configure inventory flows**: Set up connections, configure sync schedule
4. **Install additional modules** (Admin, Audit, Nurture, Innovation Backlog) as needed
5. **Configure Power BI reports**: Connect to Dataverse, publish to workspace
6. **Set up notifications**: Configure email templates and notification flows
7. **Assign security roles**: Grant CoE admins and viewers appropriate access

### Governance Patterns with CoE Kit

| Pattern | How |
|---------|-----|
| Identify shadow IT | Inventory reveals all apps/flows including those outside managed solutions |
| Enforce naming standards | Audit flows flag apps not matching naming conventions |
| License optimization | Usage data shows which users need premium vs standard licenses |
| Risk assessment | Connector usage data identifies apps accessing sensitive data sources |
| Maker onboarding | Welcome email with training resources triggered on first app creation |
| App lifecycle | Automated reminders for owners of apps not updated in 60+ days |

## Capacity and Storage

Dataverse storage is allocated per tenant based on licenses purchased and comes in three categories.

### Storage Types

| Type | What Counts | Default Allocation |
|------|-------------|-------------------|
| Database | Table rows, metadata, indexes, audit logs (if stored in Dataverse) | 10 GB base + 50 MB per premium user license |
| File | Attachments, notes, images stored in Dataverse tables | 20 GB base + 2 GB per premium user license |
| Log | Audit logs, plugin trace logs, activity logs | 2 GB base + additional from certain licenses |

### Capacity Allocation Rules

- **Tenant-level pool**: All storage is pooled at the tenant level, not per environment
- **Base capacity**: Included with the first Power Apps or Dynamics 365 license
- **Additional capacity**: Purchased as add-on packs (1 GB increments)
- **Overage**: When capacity is exceeded, admins receive warnings; new environment creation may be blocked

### Monitoring Capacity

**From Power Platform admin center:**
1. Navigate to **Resources** > **Capacity**
2. View summary: total available vs used for each storage type
3. Drill into **Per environment** tab to see consumption by environment
4. View **Top tables** to identify which tables consume the most storage

### Capacity Optimization Strategies

| Strategy | Impact |
|----------|--------|
| Archive old records | Move inactive data to Azure Data Lake or archive tables |
| Clean up audit logs | Reduce log retention period; move old logs to external storage |
| Optimize attachments | Store large files in SharePoint/Azure Blob instead of Dataverse |
| Delete unused environments | Remove sandbox/dev environments no longer needed |
| Remove duplicate data | Merge or deduplicate records in tables |
| Bulk delete jobs | Schedule recurring bulk delete for temporary or expired records |
| Reduce indexes | Remove unused custom indexes from tables |
| Trim note attachments | Clean old note attachments that are no longer referenced |

### Bulk Delete Jobs

Create recurring cleanup jobs in Dataverse:

1. Navigate to **Settings** > **Data Management** > **Bulk Record Deletion**
2. Define criteria (e.g., "Activity records older than 1 year with status = Completed")
3. Set recurrence schedule (weekly, monthly)
4. Review estimated record count before confirming
5. Monitor job execution in system jobs

## Tenant-Level Analytics

Power Platform admin center provides analytics dashboards for monitoring adoption and usage across the tenant.

### Available Reports

| Report | Scope | Key Metrics |
|--------|-------|-------------|
| Power Apps analytics | Tenant or environment | Active users, app launches, app count, device types |
| Power Automate analytics | Tenant or environment | Flow runs, success/failure rates, connector usage |
| Dataverse analytics | Tenant | Storage consumption, API usage, active tables |
| Copilot Studio analytics | Tenant or environment | Session count, resolution rate, escalation rate |
| Capacity | Tenant | Storage breakdown by type and environment |
| API usage | Tenant | Power Platform request consumption vs entitlement |

### Power Apps Analytics Details

| Metric | Description |
|--------|-------------|
| Unique users | Count of distinct users who launched an app in the period |
| App opens | Total number of app launches |
| Device breakdown | Web, iOS, Android, Windows usage percentages |
| Location | Geographic distribution of app usage |
| Service performance | Average app load time and API call duration |

### Adoption Metrics to Track

| Metric | Healthy Indicator | Action if Low |
|--------|-------------------|---------------|
| Monthly active users | Growing month-over-month | Increase awareness; review onboarding |
| App creation rate | Steady new app creation | Nurture makers; provide training |
| Flow success rate | >95% success rate | Investigate failures; improve error handling |
| Premium feature adoption | Increasing usage of Dataverse, AI Builder | Ensure licenses are allocated to active makers |
| Maker-to-user ratio | More consumers than makers | Healthy; focus on quality apps |
| Inactive app percentage | <20% of all apps | Clean up; contact owners; archive |

### Exporting Analytics Data

- **Power BI**: Connect Power BI to the CoE Starter Kit Dataverse tables for custom dashboards
- **Data Export Service**: Export Dataverse analytics data to Azure SQL or Data Lake
- **Admin center export**: Download CSV of current view from analytics pages
- **API**: Use Power Platform admin API to programmatically retrieve usage data

## Environment Management

### Environment Types and Lifecycle

| Type | Creation | Lifecycle | Backup | Reset |
|------|----------|-----------|--------|-------|
| Production | Admin or approved request | Permanent until deleted | Automatic daily (7-28 days) | Not supported (copy from sandbox) |
| Sandbox | Admin or approved request | Permanent; can be reset | Automatic daily (7-28 days) | Full reset to blank state |
| Developer | Self-service (1 per user) | Permanent; no inactivity deletion | Manual only | Full reset |
| Trial | Self-service | 30 days; can extend or convert | Not automatic | Not supported |
| Default | Auto-created per tenant | Cannot be deleted | Automatic daily | Not supported |
| Dataverse for Teams | Auto-created per Team | Linked to Teams team lifecycle | Limited | Not supported |

### Environment Lifecycle Operations

| Operation | Description | Considerations |
|-----------|-------------|----------------|
| Create | Provision new environment with or without Dataverse | Requires capacity; choose region carefully |
| Copy | Clone environment (full or minimal) to another | Target must be sandbox; useful for refreshing test data |
| Backup | Manual or automatic point-in-time backup | Production: system backups every ~8 hours; manual on demand |
| Restore | Restore to a point in time from backup | Overwrites target environment completely |
| Reset | Wipe all data and customizations | Sandbox only; irreversible |
| Delete | Remove environment permanently | 7-day recovery window; then permanent |
| Recover | Restore a recently deleted environment | Within 7 days of deletion |
| Convert | Change trial to production | Requires available production environment capacity |

### Environment Routing Best Practices

| Environment | Audience | DLP Policy |
|-------------|----------|------------|
| Default | All users (restrict to minimal use) | Most restrictive tenant-wide policy |
| Development | Makers and developers | Allow premium connectors for building |
| Test/QA | Testers and admins | Mirror production DLP; enable test data |
| UAT | Business users for acceptance | Same as production DLP |
| Production | End users | Balanced: secure but functional |
| Sandbox (data refresh) | Developers needing prod-like data | Same as production; mask sensitive data after copy |

### Environment Variables

Environment variables allow configuration values to differ per environment without code changes:

| Type | Examples |
|------|----------|
| Text | API endpoints, feature flags, email addresses |
| Number | Thresholds, limits, retry counts |
| JSON | Complex configuration objects |
| Data source | Dataverse table references, SharePoint site URLs |
| Secret | Azure Key Vault references for credentials |

Usage in apps and flows:
- Canvas apps: Access via Dataverse lookup or `Environment()` function
- Cloud flows: Use environment variable action or dynamic content
- Plugins: Read from organization settings or Dataverse table

### Environment Security Layers

Multiple security layers protect each environment:

| Layer | Mechanism |
|-------|-----------|
| Tenant isolation | Cross-tenant access controls for connectors |
| DLP policies | Connector grouping and action-level controls |
| Environment access | Environment security roles (Admin, Maker) |
| Dataverse security | Business units, security roles, teams, column-level security |
| App-level | Canvas app sharing, model-driven app security roles |
| Record-level | Row-level security via business units and sharing rules |
| IP restrictions | Managed environment IP firewall (premium) |
| Conditional access | Azure AD conditional access policies applied to Power Platform |

## Licensing Decision Framework

### Choosing the Right License

```
Is the app using premium connectors, Dataverse, or custom connectors?
  No  -> M365 included license is sufficient
  Yes -> How many users will use the app?
    Few users (<50) using many apps -> Per-user plan
    Many users (>50) using one app  -> Per-app plan
    Variable/unpredictable usage    -> Pay-as-you-go
    Single developer learning       -> Developer plan
    Evaluating before purchase      -> Trial (30 days)
```

### Common Licensing Scenarios

| Scenario | Recommended License |
|----------|-------------------|
| Department app with SharePoint data, 200 users | M365 included (standard connectors only) |
| CRM app with Dataverse, 50 users using 3 apps each | Power Apps per user (most cost-effective for multi-app users) |
| Facility check-in app with Dataverse, 5000 users | Power Apps per app (cheaper per user for single app) |
| Integration flow connecting SAP to Dataverse | Power Automate per user or per flow (premium connector) |
| Seasonal reporting app used 3 months/year | Pay-as-you-go (pay only for active months) |
| AI document processing pipeline | Power Automate per user + AI Builder add-on |

### License Compliance Monitoring

- **Admin center**: View active licenses vs assigned in Microsoft 365 admin center
- **CoE Starter Kit**: Inventory shows which apps use premium features and which users need licenses
- **Power Platform requests**: Monitor API consumption in admin center to prevent throttling
- **Self-service purchase controls**: Admins can disable self-service license purchases in M365 admin center to maintain governance

### API Request Limits

| License | Daily Power Platform Requests |
|---------|------------------------------|
| Power Apps per user | 40,000 |
| Power Apps per app | 6,000 |
| Power Automate per user | 40,000 |
| Power Automate per flow | 250,000 |
| M365 (included) | 6,000 |
| Dynamics 365 Enterprise | 40,000 |
| Dynamics 365 Professional | 20,000 |
| Pay-as-you-go | Based on consumption; overage billed |

Requests are pooled at the tenant level with a 24-hour rolling window. Individual user spikes are tolerated as long as tenant total stays within limits. Sustained overage triggers 429 (throttling) responses.
