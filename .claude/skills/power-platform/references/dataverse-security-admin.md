# Dataverse Security & Administration Reference

## Security Model Overview

Authentication flow:
1. Users authenticated by Microsoft Entra ID
2. Licensing acts as first control gate
3. Security roles control app/flow creation permissions
4. App visibility: canvas apps = sharing, model-driven apps = security roles
5. Environments = top-level security boundaries
6. Flows and canvas apps use connector credentials of the connection owner
7. Dataverse environments support granular row/column-level security

---

## Role-Based Security

**Core principle: all privilege grants are accumulative. Greatest access always prevails.**
You cannot revoke access for specific records once broader access is granted through any role.

### Privilege Types
| Category | Privileges |
|---|---|
| Table | Create, Read, Write, Delete, Append, Append To, Assign, Share |
| Miscellaneous | Task-based operations not tied to records |
| Privacy-related | Data export and integration |

### Access Levels (from broadest to narrowest)
| Level | Scope |
|---|---|
| Organization | All records in all BUs |
| Parent:Child BU | Own BU + all subordinate BUs |
| Business Unit | Own BU only |
| User | Own records + explicitly shared records |
| None | No access |

### Quick Permission Presets
| Preset | Read | Write |
|---|---|---|
| Full Access | All | All |
| Collaborate | All | Own only |
| Private | Own only | Own only |
| Reference | All | None |

---

## Predefined Security Roles

### Without Dataverse
| Role | Purpose |
|---|---|
| Environment Admin | Full admin rights, DLP policies |
| Environment Maker | Create apps/connections/flows, no data access |

### With Dataverse
| Role | Purpose |
|---|---|
| App Opener | Minimum privileges; use as template for custom roles |
| Basic User | Run apps, common tasks on owned records |
| Environment Maker | Create resources, no data access |
| System Administrator | Full permission to customize and administer |
| System Customizer | Full customization; own core records only |
| Delegate | Allows code to run as (impersonate) another user |
| Service Reader/Writer/Deleted | Service-to-service only roles |

**Design decision**: Start with App Opener as base, add only needed privileges. Never grant System Administrator broadly.

---

## Business Units

- Define security boundaries within a Dataverse environment
- Every database has one root BU (cannot be deleted)
- Each user belongs to exactly one BU
- BU hierarchy determines access level scoping (BU, Parent:Child)
- **Matrix Data Access**: Enable "Record ownership across business units" to let users own records in BUs they do not belong to

### When to Use BUs
- Departments or divisions with distinct data access needs
- Geographic separation requiring data isolation
- Regulatory requirements for data compartmentalization

---

## Table/Record Ownership

| Ownership Type | Access Model |
|---|---|
| Organization-owned | Binary: can or cannot access all records |
| User/Team-owned | Tiered: Organization, BU, BU+Child, User only |

**Design decision**: Use Organization-owned for reference data (countries, currencies). Use User/Team-owned when row-level access control is needed.

---

## Teams

### Owning Teams
- Can own records directly
- Members inherit the team's security roles
- Use for: shared mailboxes, department-owned data, records not belonging to one person

### Access Teams
- Cannot own records or have security roles
- Share individual records with team members
- Use for: ad-hoc collaboration on specific records

**Design decision**: Prefer Owning Teams for structural access patterns. Use Access Teams only for exception-based sharing on individual records.

---

## Record Sharing

- Share individual records with specific users or teams
- Grants access beyond what security roles provide
- **Performance impact**: sharing is less performant than role-based access
- Use as an exception, not a primary access strategy

---

## Hierarchy Security

### Two Models
| Model | Based On | Direct Reports | Up the Chain |
|---|---|---|---|
| Manager Hierarchy | Manager field on user record | Read, Write, Append, Append To | Read only |
| Position Hierarchy | Admin-defined position records | Read, Write, Append, Append To | Read only |

### Setup
Settings > Users + Permissions > Hierarchy security. Enable one model, select applicable tables, set depth limit.

**Performance guideline**: Keep effective hierarchy to 50 or fewer users under any manager/position.

**Design decision**: Use Manager Hierarchy for simple org charts. Use Position Hierarchy when access should follow job titles rather than reporting lines.

---

## Column-Level Security

Controls per-column access independent of record-level security. Managed via Column Security Profiles.

### Permissions Per Profile
| Permission | Options |
|---|---|
| Read | Allowed / Not Allowed |
| Read unmasked | All Records / One record / Not Allowed |
| Update | Allowed / Not Allowed |
| Create | Allowed / Not Allowed |

### Cannot Be Secured
Virtual table columns, Lookup columns, Formula columns, Primary name columns, System columns (createdon, modifiedon, statecode, statuscode)

### Key Rules
- Does NOT apply to System Administrators (they see everything)
- Independent of record-level security: a user with record Read can still be blocked from reading a secured column
- Use for: salary fields, SSN, confidential notes, API keys

---

## User Types and Access Modes

### User Types
| Type | Description |
|---|---|
| Regular | Synced from Entra ID, standard interactive user |
| Application | Identified by ApplicationId, no user limit |
| Non-interactive | SDK/API only, max 7 per environment |
| Support/Delegated | Microsoft support or partner placeholders |

### Access Modes
| Mode | Description | License Required |
|---|---|---|
| Read-Write | Full interactive access (default) | Yes |
| Administrative | Settings and admin only | No |
| Non-interactive | Programmatic only, max 7 | Yes |

### User Requirements
1. Enabled in Entra ID
2. Valid license assigned (with exceptions for Administrative mode)
3. Member of environment's security group (if configured)

---

## Environments

### Types and When to Use
| Type | Purpose | Key Detail |
|---|---|---|
| Production | Live workloads | Requires 1 GB database capacity |
| Default | Auto-created per tenant | For experimentation, shared by all users |
| Sandbox | Dev/test | Supports copy and reset operations |
| Trial | Evaluation | 30-day auto-cleanup, one per user |
| Developer | Personal dev | Single-user, free Developer Plan |
| Dataverse for Teams | Team apps | Auto-created inside Teams |

### License Requirements for Creating Environments
| License | Can Create |
|---|---|
| Dynamics 365 / Power Apps / Power Automate plans | Production and Sandbox |
| Trial licenses | Trial only |
| M365 / Developer Plan | Cannot create environments |

### Critical: "Enable Dynamics 365 apps" cannot be changed after environment creation.

---

## DLP (Data Loss Prevention)

### Connector Groups
| Group | Purpose |
|---|---|
| Business | Sensitive data connectors, isolated from Non-business |
| Non-business (Default) | Non-sensitive connectors, isolated from Business |
| Blocked | Connectors that cannot be used at all |

**Rule**: Connectors in the same group can share data. Connectors in different groups cannot.

### Enforcement Timeline
- Design-time: Cannot save apps/flows using blocked connector combinations
- Runtime: Existing connections using blocked combinations are disabled
- Full enforcement: up to 24 hours after policy change

### DLP Policy Creation Steps
1. Name the policy
2. Classify connectors into Business / Non-Business / Blocked
3. Set default group for newly added connectors
4. Configure custom connector rules
5. Define scope (which environments to include/exclude)
6. Review and create

### Governance Rules
- Environment admins cannot edit or delete tenant admin policies
- Environment-level policies cannot override tenant-wide policies
- Multiple policies can apply; most restrictive combination wins

---

## Managed Environments

Premium admin capabilities for managing at scale. Included with standalone Power Apps, Power Automate, Copilot Studio, Power Pages, and Dynamics 365 licenses.

Features: environment groups, sharing limits, weekly usage insights, enhanced data policies, deployment pipelines, solution checker enforcement, IP Firewall, Customer Managed Keys, extended backup retention, virtual network support, conditional access per app.

---

## Capacity and Storage

### Storage Types
| Type | Contains |
|---|---|
| Database | All Dataverse tables except file and log |
| File | Attachments (PDFs, images) |
| Log | Audit records, trace logs |

Default allocation: 3 GB database, 3 GB file, 1 GB log per default environment.

**Overage restrictions**: Cannot create environments, copy environments, restore backups, or convert trials when over capacity.

---

## Licensing Summary

| License Type | Dataverse Access |
|---|---|
| Premium (per-user Power Apps/Automate) | Full Dataverse |
| M365 Seeded | Standard connectors, default environment only |
| Dynamics 365 Seeded | Within Dynamics 365 context |
| Developer Plan | Free, isolated environment |
| Pay-as-you-go | Azure subscription billing, no commitment |
| Trials | Power Apps 30-day, Power Automate 90-day |

---

## Security Design Checklist

1. Map organizational structure to BUs (or keep flat if simple)
2. Choose table ownership type based on access needs (Org-owned vs User/Team-owned)
3. Start with App Opener role, layer on minimum needed privileges
4. Use Owning Teams for structural patterns, Access Teams for exceptions
5. Apply column-level security for sensitive fields (salary, PII)
6. Enable hierarchy security only if manager/position-based access is required
7. Create DLP policies before users build apps (prevent bad connector combinations)
8. Use Managed Environments for production governance at scale
9. Plan capacity before provisioning (1 GB database minimum per production environment)
10. Set environment security groups to control who can access each environment
