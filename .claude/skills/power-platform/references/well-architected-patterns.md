# Power Platform Well-Architected Framework and Patterns

> Reference for designing reliable, secure, performant, and user-friendly Power Platform workloads.

---

## 1. Framework Overview

Power Platform Well-Architected provides best practices and architecture guidance for designing modern application workloads. It is organized into five pillars, each with design review checklists, recommendation guides, and tradeoff analysis.

| Pillar | Focus |
|--------|-------|
| **Reliability** | Uptime targets, recovery, redundancy, resiliency at scale |
| **Security** | Attack protection, confidentiality, data integrity |
| **Operational Excellence** | Reduce production issues, observability, automated systems |
| **Performance Efficiency** | Handle demand changes, horizontal scaling, test before deploy |
| **Experience Optimization** | Meaningful user experiences ensuring business outcomes |

**Assessment tool**: `https://aka.ms/powa/assessment`

---

## 2. Reliability Pillar

Goal: Ensure workloads meet uptime commitments and recover gracefully from failures.

### Fault Tolerance Strategies

| Strategy | Implementation |
|----------|---------------|
| **Retry logic** | Power Automate: configure retry policies (default 4x exponential, fixed interval, or none) |
| **Scope-based error handling** | Try/Catch/Finally pattern using Scope actions with "Run after" configuration |
| **Graceful degradation** | Check `Connection.Connected` in canvas apps; fall back to cached data |
| **Idempotent operations** | Design flows so re-running produces same result; use unique keys for upserts |

### Error Handling Patterns

**Canvas Apps (Power Fx):**
```powerfx
// Chain with IfError -- stops on first failure
IfError(
    Patch(DataSource1, record1), Notify("First save failed"),
    Patch(DataSource2, record2), Notify("Second save failed")
)
```

```powerfx
// Global error handler
App.OnError:
    Trace($"Error {FirstError.Message} in {FirstError.Source}");
    Error(FirstError)  // Rethrow to show default banner
```

**Power Automate (Cloud Flows):**
- Use Scope actions as Try/Catch/Finally blocks
- Configure Catch scope to "Run after" Try scope "has failed"
- Configure Finally scope to run after Catch "is successful" OR "has failed" OR "is skipped"
- Apply retry policies: Default (4x exponential), Fixed interval, Exponential interval, None

**Power Automate Desktop:**
- Per-action error handling via "On error" settings (retry, continue, label jump, new rule)
- Block-level error handling via "On block error" (wraps groups of actions)
- Individual action error handling takes precedence over block error handling

### Data Resilience

| Technique | Details |
|-----------|---------|
| **Offline data caching** | `SaveData`/`LoadData` in canvas apps (mobile only, 30-70 MB) |
| **Solution backups** | Pipelines automatically store solution backups in host environment |
| **Environment backups** | System backups (daily) + manual backups; restore via admin center |
| **Dataverse auditing** | Enable change tracking on tables for data recovery scenarios |

---

## 3. Security Pillar

Goal: Protect workloads from attacks and ensure confidentiality and data integrity.

### Authentication

| Method | Context | Notes |
|--------|---------|-------|
| **Microsoft Entra ID** | Most secure; recommended for all connectors | No extra sign-in required |
| **OAuth 2.0** | Custom connectors, external APIs | Standard authorization code flow |
| **Service principal** | CI/CD pipelines, automated processes | Required when MFA enabled |
| **Workload Identity Federation** | Azure DevOps service connections | Recommended; supports MFA |
| **API Key** | Simple external APIs | Least secure; use only when necessary |

### Authorization (Dataverse Security Model)

**Layered defense:**
1. **Security roles** -- privilege-based (Create, Read, Write, Delete, Append, Assign, Share)
2. **Business units** -- organizational security boundaries
3. **Teams** -- Owning teams (direct access) and Access teams (record sharing)
4. **Hierarchy security** -- Manager or Position-based cascading access
5. **Column-level security** -- Per-column read/update/create via Security Profiles
6. **Record sharing** -- Individual record exceptions (use sparingly; impacts performance)

**Key principle**: All privilege grants are accumulative -- greatest access prevails. Cannot revoke for specific records once broad access granted.

### Access Levels

| Level | Scope |
|-------|-------|
| Organization | All records in all BUs |
| Parent:Child BU | Own BU + subordinate BUs |
| Business Unit | Own BU records only |
| User | Own records + shared records |
| None | No access |

### Data Loss Prevention (DLP)

**Connector classification groups:**

| Group | Purpose |
|-------|---------|
| **Business** | Sensitive data connectors; isolated from non-business |
| **Non-Business** | Non-sensitive connectors (default group) |
| **Blocked** | Cannot be used in any app or flow |

**Enforcement behavior:**
- Design-time: cannot save apps/flows with blocked connectors
- Runtime: existing blocked connections fail and are set to "disabled"
- Full enforcement propagation: up to 24 hours
- Connectors in the same group can share data; different groups are denied
- Environment admins cannot override tenant admin policies

### Data Protection Best Practices

- Use connection references and environment variables for cross-environment portability (never hardcode credentials)
- Store secrets as GitHub Secrets or Azure DevOps Secure Variables
- Apply column-level security for sensitive fields (SSN, salary, etc.)
- Enable Managed Environments for IP Firewall, CMK, conditional access per app, and VNet support
- Limit connector count (max 10 per canvas app, 20 connection references)

---

## 4. Operational Excellence Pillar

Goal: Reduce production issues through observability, ALM discipline, and automated systems.

### Monitoring and Observability

| Capability | How |
|------------|-----|
| **Tenant analytics** | Enable in admin center > Tenant settings; reports in 24-48 hours |
| **Power Automate run history** | Built-in action-level logs with inputs/outputs |
| **Trace function** | `Trace()` in Power Fx for custom telemetry |
| **App.OnError** | Global error handler for centralized logging |
| **CoE Starter Kit dashboards** | Power BI dashboards for inventory, adoption, compliance |
| **Weekly insights** | Managed Environments provide automated admin digests |

### ALM Best Practices

| Practice | Guidance |
|----------|----------|
| **Environment separation** | Minimum: dev + test + production |
| **Source control** | Single source of truth; unpack solutions to repo |
| **Managed solutions** | Deploy only managed solutions to non-dev environments |
| **Solution publisher** | Define a single publisher with consistent prefix |
| **Segmented solutions** | Include only changed components to avoid unnecessary layers |
| **Build automation** | Generate managed solutions via build server (Azure DevOps or GitHub Actions) |
| **Pipeline stages** | Cannot skip stages (e.g., QA must precede production) |

### DevOps Pipeline Pattern

```
1. Initiate -- set up and configure tools
2. Export from Dev -- export unmanaged solution
3. Build -- generate managed solution artifact
4. Quality Check -- run Solution Checker (static analysis, SARIF output)
5. Release -- deploy to downstream environments (test > UAT > production)
```

### Branching Strategies

| Strategy | When to Use |
|----------|-------------|
| **Trunk-based** | Small teams; single main branch with short-lived feature branches |
| **Release branching** | Versioned releases; separate branches per release |
| **Feature branching** | Isolated development per feature; merge when complete |

### Team Development

- Avoid multiple people editing complex components (forms, flows, canvas apps) simultaneously
- Break solutions into logical segments to reduce merge contention
- Orchestrate changes to minimize conflicts
- Use Power CAT Toolkit for automated code reviews against coding guidelines

---

## 5. Performance Efficiency Pillar

Goal: Handle demand changes through proper query patterns, caching, and async processing.

### Delegation (Critical)

Delegation means Power Apps translates queries to run server-side. Non-delegable queries retrieve only the first 500 records (max 2,000) and process locally.

**Delegable data sources**: Dataverse, SharePoint, SQL Server, Salesforce

**Delegable functions**: Filter, Search, First, LookUp, Sort (single column), SortByColumns, Sum, Average, Min, Max, CountRows, Count

**Delegable operators within Filter/LookUp**: And (&&), Or (||), Not (!), In, =, <>, >=, <=, >, <, +, -, TrimEnds, IsBlank, StartsWith, EndsWith

**NOT delegable**: If, *, /, Mod, Text, Value, Concatenate, Lower, Upper, Left, Mid, Len, FirstN, Last, LastN, GroupBy, Ungroup

**Query limits**: Max 2 lookup levels, max 20 entity joins, entity property must be on LEFT side of equality

**Detection**: Yellow triangle / blue underline warnings. Set data row limit to 1 during development to catch issues early.

### Caching Patterns

| Pattern | Implementation |
|---------|---------------|
| **Collections** | `ClearCollect()` reference data on startup; use collection throughout app |
| **Named Formulas** | Define in `App.Formulas` for lazy-evaluated, always-available cached values |
| **SaveData/LoadData** | Persist collections to device storage (mobile only) |
| **sessionStorage** | Model-driven apps: cache data in sessionStorage with stale-while-revalidate pattern |

### Async Patterns

| Context | Approach |
|---------|----------|
| **Power Automate triggers** | Use async patterns for long-running operations |
| **AI Builder actions** | Always leave Asynchronous Pattern setting to "On" in cloud flows |
| **Model-driven JS** | Use async network requests; return Promises from OnLoad/OnSave |
| **Plug-ins** | Register PostOperation steps as async when real-time response not required |
| **Dataverse rollup columns** | Aggregate values computed asynchronously by system jobs |

### Query Optimization

1. **Do data mashups on the server**, not in the app
2. **Minimize startup actions** -- delay/eliminate OnStart operations
3. **Keep data payloads small** -- retrieve only needed columns and rows
4. **Use delegable patterns** -- rewrite non-delegable queries to use supported functions
5. **Limit connectors** -- max 10 per canvas app; each connection adds overhead
6. **Load code only when needed** -- deferred tab loading in model-driven apps

---

## 6. Experience Optimization Pillar

Goal: Create meaningful user experiences that ensure business outcomes.

### Responsive Design

**Setup**: Settings > Display > turn off "Scale to fit"

**Screen dimensions:**
```powerfx
Width = Max(App.Width, App.DesignWidth)
Height = Max(App.Height, App.DesignHeight)
```

**Breakpoints:**

| Constant | Value | Device |
|----------|-------|--------|
| ScreenSize.Small | 1 | Phone |
| ScreenSize.Medium | 2 | Tablet (vertical) |
| ScreenSize.Large | 3 | Tablet (horizontal) |
| ScreenSize.ExtraLarge | 4 | Desktop |

**Common layout formulas:**
```powerfx
// Fill width with margin
X = N; Width = Parent.Width - (N * 2)

// Conditional visibility by device
Visible = Parent.Size >= ScreenSize.Medium

// Dynamic column width
Width = Parent.Width * Switch(Parent.Size,
    ScreenSize.Small, 1,
    ScreenSize.Medium, 0.5,
    0.33)
```

### Accessibility

- Use Accessibility Checker in canvas apps (errors, warnings, tips)
- Set accessible labels on all interactive controls
- Ensure FocusBorderThickness > 0 for keyboard navigation
- Provide closed captions for media controls
- Use descriptive screen and control names
- Use Container controls for proper accessibility hierarchy

### Progressive Disclosure

| Technique | Implementation |
|-----------|---------------|
| **Deferred loading** | Load detail data only when user navigates to detail screen |
| **Conditional sections** | Show/hide form sections based on user role or selection |
| **Tab-based layout** | Default tab management in model-driven apps; load non-visible tabs on demand |
| **Expandable groups** | Use container visibility to collapse/expand sections |
| **Wizard pattern** | Guide users through steps; validate each step before advancing |

---

## 7. Common Architectural Patterns

### Master-Detail

Browse screen with gallery listing records; tap/click navigates to detail screen with full record view; edit screen for modifications.

```powerfx
// Gallery OnSelect
Navigate(DetailScreen, ScreenTransition.None);

// Detail screen Item
BrowseGallery.Selected
```

Generated automatically when creating an app from SharePoint or Dataverse (3-screen app: Browse, Details, Edit).

### Wizard / Multi-Step Form

Guide users through sequential steps with validation at each stage.

```powerfx
// Track current step
UpdateContext({ currentStep: 1 });

// Navigate steps
UpdateContext({ currentStep: currentStep + 1 });

// Show/hide step containers
Visible = currentStep = 1   // Step 1 container
Visible = currentStep = 2   // Step 2 container
```

### Offline-First

```powerfx
// App.OnStart
If(Connection.Connected,
    ClearCollect(LocalData, DataSource.GetItems());
    SaveData(LocalData, "LocalData"),
    LoadData(LocalData, "LocalData", true)
);

// Sync button
If(Connection.Connected,
    ForAll(LocalData, Patch(DataSource, ThisRecord));
    ClearCollect(LocalData, DataSource.GetItems());
    SaveData(LocalData, "LocalData")
)
```

**Limitations**: SaveData/LoadData work ONLY in Power Apps Mobile (not Studio or web browser). Teams apps limited to 1 MB. No automatic merge conflict resolution.

### Event-Driven (Power Automate)

Trigger flows from events rather than polling:

| Trigger Type | Examples |
|-------------|----------|
| **Automated** | When a record is created/updated, when a file is added, when an email arrives |
| **Scheduled** | Recurrence-based for batch processing and data sync |
| **Instant** | Button-triggered from apps or manual runs |
| **Business event** | Dataverse business events for cross-system integration |

### Scope-Based Error Handling (Power Automate)

```
[Trigger]
  |
[Try Scope] -- main business logic
  |
[Catch Scope] -- Run after: "has failed"
  |
[Finally Scope] -- Run after: "is successful" OR "has failed" OR "is skipped"
```

### Solution Segmentation

Include only changed components in solutions to avoid unnecessary layers:

| Option | When to Use |
|--------|-------------|
| No objects selected | Minimal reference only |
| Edit objects | Select specific changed columns, forms, views |
| Include table metadata | Table properties only (auditing, change tracking) |
| Include all objects | New tables only; never for existing tables |

---

## 8. Anti-Patterns to Avoid

### Performance Anti-Patterns

| Anti-Pattern | Why It's Bad | Do This Instead |
|-------------|-------------|-----------------|
| Loading all data at startup | Slow app launch, memory pressure | Defer data loading; use Named Formulas for lazy evaluation |
| Turning everything into collections | Memory overhead; stale data | Use direct data source references with delegable queries |
| Overloading OnStart | Blocks app display until complete | Move to App.Formulas (lazy) or Screen.OnVisible (deferred) |
| Non-delegable queries on large datasets | Only processes first 500-2000 records silently | Rewrite to use delegable functions; move logic server-side |
| Too many connectors | Each connection adds latency | Consolidate; max 10 per canvas app |

### Security Anti-Patterns

| Anti-Pattern | Why It's Bad | Do This Instead |
|-------------|-------------|-----------------|
| Hardcoding credentials | Exposed in source; not portable | Use connection references + environment variables |
| Broad security roles | Violates least privilege | Create custom roles from App Opener template |
| Relying on record sharing at scale | Poor query performance | Use security roles and business units instead |
| Skipping DLP policies | Uncontrolled data flow between connectors | Classify all connectors; set default group for new ones |
| Windows Authentication for connectors | Insecure credential handling | Use Entra ID or OAuth 2.0 |

### ALM Anti-Patterns

| Anti-Pattern | Why It's Bad | Do This Instead |
|-------------|-------------|-----------------|
| Editing in production | No rollback; no audit trail | Always develop in sandbox; deploy managed solutions |
| Using patches | Complex layering; Microsoft discourages | Use full solution upgrades |
| Including all objects for existing tables | Creates unnecessary layers; can deactivate customizations | Segment solutions; include only changed components |
| Multiple publishers | Cannot move components between solutions later | Single publisher across all solutions |
| Skipping test environments | Deployment failures hit production | Minimum: dev + test + production pipeline |

### Architecture Anti-Patterns

| Anti-Pattern | Why It's Bad | Do This Instead |
|-------------|-------------|-----------------|
| Multiple people editing same form/flow | Merge conflicts; lost work | Orchestrate; one maker per complex component |
| Client-side business rules for security | Bypassable; rules run on forms only | Use server-side plug-ins or Dataverse security |
| Synchronous plug-ins for non-critical logic | Blocks user; increases form save time | Register as async PostOperation |
| Ignoring delegation warnings | Silent data truncation in production | Fix every yellow triangle; test with row limit = 1 |
| `console.log` in production JS | Performance overhead; information leak | Remove debug logging; use Trace() for telemetry |

---

## Quick Reference: Pillar Checklist

Use before deploying any workload:

- [ ] **Reliability**: Error handling in all flows (Try/Catch), offline fallback if mobile, retry policies configured
- [ ] **Security**: DLP policies applied, security roles follow least privilege, no hardcoded credentials, column security on sensitive fields
- [ ] **Operational Excellence**: Solutions in source control, managed deployments only, monitoring/analytics enabled, CoE dashboards active
- [ ] **Performance**: All delegation warnings resolved, startup optimized, data payloads minimized, async where possible
- [ ] **Experience**: Responsive layout tested across devices, accessibility checker clean, progressive disclosure for complex forms
