# Dataverse Business Logic, Security & Administration Research
## Sources: 21/22 successfully fetched (1 page returned 404)

---

## 1. Business Rules in Dataverse

### Capabilities
- Set/clear column values, set requirement levels, show/hide columns (MDA only), enable/disable columns (MDA only), validate data with error messages, create recommendations (MDA only)

### Canvas vs Model-Driven
Not available in canvas: show/hide columns, enable/disable columns, business recommendations

### Scope Options
| Scope | Applies To |
|---|---|
| Entity | Model-driven forms + server |
| All Forms | All model-driven forms |
| Specific form | One model-driven form |

Canvas apps must use "Entity" scope.

### Unsupported Column Types
Choices (multi-select), File, Language

### Key Limitations
- Must deactivate before modifying
- Max 150 business rules per table
- Referenced fields must exist on form
- Execute on client (form open, field change), not inside Dataverse
- Execute before onLoad scripts
- CAN unlock fields on read-only form

---

## 2. Low-Code Plug-ins

### Types
| Type | Trigger | Parameters | Scope |
|---|---|---|---|
| Instant | Manual | Yes (Boolean, String, Float, Decimal, DateTime, Integer) | Global/Table |
| Automated | Dataverse event | No | Table |

### Automated Events
- Create, Update, Delete
- Stages: Pre-operation (before save) or Post-operation (after save)

### Key Points
- Server-side execution (security, performance, consistency)
- Use Power Fx expression language
- Can use Power Platform connectors for external data
- Use `ThisRecord` for current row in automated plug-ins
- Require System Administrator or System Customizer role
- Created via Dataverse Accelerator app

### Integration
- **Canvas apps**: Environment data source + code snippet
- **Power Automate**: "Perform an unbound/bound action" from Dataverse connector
- **Web API**: Custom API invocation endpoints

### Limitations
- Intellisense requires `[@TableName]` notation in automated plug-ins
- Can only call first-party Microsoft actions
- Some Collect scenarios require Patch workaround

---

## 3. Low-Code Plug-ins Power Fx Support

### Unsupported Formulas
Clear, ClearCollect, Update, UpdateIf, SortByColumns, Concurrent, DropColumns, AddColumns, IsEmpty, SetFocus, IsType, JSON, Download, PlainText, RemoveIf, GroupBy, SetProperty, RenameColumns, Search, ShowColumns, UTCNow, UTCToday, Validate, Weekday, As, Calendar, Choices, Clock, Select, Notify, Errors, HashTags, Form-related, Device sensor formulas

---

## 4. Real-Time Workflows

Two types: Background (async) and Real-time (synchronous). Microsoft recommends Power Automate flows instead.

---

## 5. Custom Process Actions

Define custom messages matching business operations (Escalate, Convert, Schedule, Route, Approve). Can be global (not table-specific). Custom API is newer alternative for developers.

---

## 6. Security Model Overview

1. Users authenticated by Microsoft Entra ID
2. Licensing = first control-gate
3. Security roles control app/flow creation
4. App visibility: canvas = sharing, model-driven = security roles
5. Environments = security boundaries
6. Flows/canvas apps use connector credentials
7. Dataverse environments support advanced security

---

## 7. Security Concepts in Dataverse

### Role-Based Security
All privilege grants are **accumulative** — greatest access prevails. Cannot revoke for specific records once broad access granted.

### Business Units
- Define security boundaries
- Every DB has one root BU
- Users belong to one BU
- **Matrix Data Access**: Enable "Record ownership across business units" for cross-BU access

### Table/Record Ownership
- **Organization-owned**: Binary can/cannot
- **User/Team-owned**: Tiered access (Org, BU, BU+Child, User only)

### Teams
- **Owning Teams**: Own records, give members direct access
- **Access Teams**: Record sharing only, no security roles

### Record Sharing
Individual records shared with users/teams. Less performant — use as exception.

### Column-Level Security
Per-column access via Column Security Profiles. Independent of record-level security.

---

## 8. Security Roles and Privileges

### Privilege Types
1. **Tables**: Create, Read, Write, Delete, Append, Append To, Assign, Share
2. **Miscellaneous**: Task-based non-record operations
3. **Privacy-related**: Data export/integration

### Access Levels
| Level | Description |
|---|---|
| Organization | All records |
| Parent:Child BU | Own BU + subordinate BUs |
| Business Unit | Own BU only |
| User | Own records + shared records |
| None | No access |

### Quick Permission Settings
| Setting | Effect |
|---|---|
| Full Access | View and edit all |
| Collaborate | View all, edit own |
| Private | View and edit own only |
| Reference | View only |

---

## 9. Predefined Security Roles

### Without Dataverse
- **Environment Admin**: Full admin, DLP policies
- **Environment Maker**: Create apps/connections/flows, no data access

### With Dataverse
| Role | Description |
|---|---|
| App Opener | Minimum privileges; template for custom roles |
| Basic User | Run apps, common tasks on owned records |
| Environment Maker | Create resources, no data access |
| System Administrator | Full permission to customize and administer |
| System Customizer | Full customization; own core records only |
| Delegate | Code impersonation |
| Service Reader/Writer/Deleted | Service-only roles |

---

## 10. Hierarchy Security

### Two Models
- **Manager Hierarchy**: Based on Manager field. Direct reports: RWAA access. Chain: read-only.
- **Position Hierarchy**: Admin-defined positions. Higher positions get RWAA (direct) or read-only (chain).

### Setup
Settings > Users + Permissions > Hierarchy security. Enable model, select tables, set Depth.

### Performance
Keep effective hierarchy to 50 users or less under a manager/position.

---

## 11. Column-Level (Field-Level) Security

### Permissions per Column Security Profile
| Permission | Options |
|---|---|
| Read | Allowed / Not Allowed |
| Read unmasked | All Records / One record / Not Allowed |
| Update | Allowed / Not Allowed |
| Create | Allowed / Not Allowed |

### Cannot Be Secured
Virtual table columns, Lookup columns, Formula columns, Primary name columns, System columns (createdon, modifiedon, statecode, statuscode)

### Important
- Does NOT apply to System Administrators
- Column-level security is independent of record-level security

---

## 12. Create Users

### User Types
| Type | Description |
|---|---|
| Regular | Synced from Entra ID |
| Application | Identified by ApplicationId, no limit |
| Non-interactive | SDK/API only, max 7 per instance |
| Support/Delegated | Microsoft support/partner placeholders |

### Access Modes
- **Read-Write**: Full access (default)
- **Administrative**: Settings/admin only, no license needed
- **Non-interactive**: Programmatic only, max 7

### Requirements
1. Enabled in Entra ID
2. Valid license (with exceptions)
3. Part of environment security group

---

## 14. Environments Overview

### Environment Types
| Type | Purpose |
|---|---|
| Production | Permanent; 1 GB database capacity required |
| Default | Auto-created per tenant; experimentation |
| Sandbox | Dev/test with copy/reset features |
| Trial | 30-day auto-cleanup; one per user |
| Developer | Single-user for Developer Plan |
| Dataverse for Teams | Auto-created in Teams |

### Built-in Roles
1. **Environment Admin**: Manage users, provision DBs, DLP policies
2. **Environment Maker**: Create apps/connections/flows, share resources

---

## 15. Create Environment

### License Requirements
| License | Can Create |
|---|---|
| Dynamics 365/Power Apps/Automate plans | Production |
| Trial licenses | Trial only |
| M365/Developer Plan | Not allowed |

### Prerequisites
- Qualifying license or admin role
- 1 GB database storage capacity (production/sandbox)
- **Critical**: "Enable Dynamics 365 apps" cannot be changed after creation

---

## 16. Pricing & Licensing

### License Types
- **Premium**: Power Apps/Automate per-user, Copilot Studio, Power Pages — full Dataverse access
- **M365 Seeded**: Extend Office; standard connectors; limited Dataverse (default env only)
- **Dynamics 365 Seeded**: Power Apps/Automate within Dynamics 365
- **Trials**: Power Apps 30-day, Power Automate 90-day
- **Developer Plan**: Free, individual, isolated environments
- **Pay-as-you-go**: Azure subscription billing

---

## 17. Capacity & Storage

### Storage Types
| Type | Contains |
|---|---|
| Database | All Dataverse tables except file/log |
| File | Attachments (.pdf, images) |
| Log | Audit records, trace logs |

### Default: 3 GB database, 3 GB file, 1 GB log per default environment

### Overage Restrictions
Blocked: creating environments, copying, restoring backups, converting trials

---

## 18. DLP Concepts

### Connector Groups
| Group | Purpose |
|---|---|
| Business | Sensitive data; isolated |
| Non-business (Default) | Non-sensitive; isolated |
| Blocked | Cannot be used |

Connectors in same group can share data. Different groups = denied.

### Enforcement
- Design-time: Can't save apps/flows with blocked connectors
- Runtime: Existing blocked connections fail; set to "disabled"
- Full enforcement: up to 24 hours

---

## 19. Create DLP Policy

### Steps
1. Name the policy
2. Classify connectors (Business / Non-Business / Blocked)
3. Set default group for new connectors
4. Configure custom connectors
5. Define scope (environments to include/exclude)
6. Review and create

### Key Rules
- Environment admins cannot edit/delete tenant admin policies
- Environment-level policies cannot override tenant-wide

---

## 20. Tenant-Level Analytics

Free feature. Enable in admin center > Tenant settings > Analytics. Reports appear within 24-48 hours. Covers Power Apps and Power Automate usage across all environments.

---

## 21. Managed Environments

Premium capabilities for managing at scale: environment groups, sharing limits, weekly insights, data policies, pipelines, solution checker, IP Firewall, CMK, extended backup, virtual network support, conditional access per app.

Included with standalone Power Apps/Automate/Copilot Studio/Power Pages/Dynamics 365 licenses.

---

## 22. Pay-As-You-Go

Pay via Azure subscription. No license commitments. Link environments to Azure billing policy. Pay only when used. Supports Dataverse storage and Copilot Studio messages.

---

## Key Patterns
- Security is **accumulative** — greatest access prevails
- Business rules run client-side (forms), not server-side
- Low-code plug-ins run server-side using Power Fx
- Column-level security is independent of record-level security
- DLP policies control connector access at design-time and runtime
- Managed Environments = premium admin capabilities at scale
- Environment types serve different lifecycle purposes (prod, sandbox, trial, dev)
