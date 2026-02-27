# Dataverse Business Logic Reference

## Decision Guide: Which Logic Option to Use

| Scenario | Use | Why |
|---|---|---|
| Simple field validation on forms | Business Rules | No code, declarative, runs on form |
| Set/clear values when field changes | Business Rules | Built-in actions, easy to configure |
| Server-side validation before save | Low-Code Plug-ins (Pre-operation) | Runs in Dataverse, not bypassable |
| Cascade updates after record save | Low-Code Plug-ins (Post-operation) | Guaranteed execution after commit |
| Trigger from canvas app or API | Instant Low-Code Plug-in | Callable from any client |
| Named business operation (Escalate, Approve) | Custom Process Action | Semantic API endpoint |
| Long-running async processing | Power Automate cloud flow | Background, retries, complex orchestration |

---

## Business Rules

### What They Do
- Set or clear column values
- Set requirement levels (required/optional)
- Show/hide columns (model-driven only)
- Enable/disable columns (model-driven only)
- Validate data and show error messages
- Create recommendations (model-driven only)

### Scope Options
| Scope | Behavior |
|---|---|
| Entity | All model-driven forms + server-side for canvas |
| All Forms | Every model-driven form |
| Specific Form | One model-driven form only |

Canvas apps: must use Entity scope. Only set/clear values and validation work.

### Key Constraints
- Execute client-side (on form open, field change), not inside Dataverse
- Execute before onLoad scripts
- Must deactivate before editing
- Max 150 per table
- Referenced fields must exist on the form
- Can unlock fields on read-only forms
- Unsupported column types: Choices (multi-select), File, Language

---

## Low-Code Plug-ins

### When to Use
Use when logic must run server-side for security, consistency, or performance.
Created via the Dataverse Accelerator app. Written in Power Fx.

### Two Types

**Automated Plug-ins** (event-driven)
- Triggers: Create, Update, Delete
- Stages: Pre-operation (before save) or Post-operation (after save)
- Use `ThisRecord` to reference the current row
- No custom parameters

**Instant Plug-ins** (on-demand)
- Triggered manually from apps, flows, or API
- Accept parameters: Boolean, String, Float, Decimal, DateTime, Integer
- Can be global or table-bound

### How to Call Instant Plug-ins
| From | Method |
|---|---|
| Canvas apps | Environment data source + code snippet |
| Power Automate | "Perform an unbound/bound action" (Dataverse connector) |
| Web API | Custom API invocation endpoint |

### Limitations
- Require System Administrator or System Customizer role to create
- Use `[@TableName]` notation for Intellisense in automated plug-ins
- Can only call first-party Microsoft actions
- Some Collect scenarios require Patch workaround
- Many Power Fx formulas unsupported (Clear, ClearCollect, Update, UpdateIf, SortByColumns, Concurrent, JSON, IsEmpty, Search, UTCNow, UTCToday, and others)

---

## Real-Time Workflows

Two types exist: Background (async) and Real-time (synchronous).
Microsoft recommends Power Automate flows as the replacement. Use only for legacy maintenance.

---

## Custom Process Actions

### When to Use
Define custom messages that map to business operations: Escalate, Convert, Schedule, Route, Approve.

### Key Points
- Can be global (not tied to a specific table)
- Create semantic API endpoints for business operations
- Custom API is the newer developer-focused alternative
- Useful when you want a named, reusable operation callable from multiple clients

---

## Logic Execution Summary

| Option | Runs Where | Triggered By | Code Language |
|---|---|---|---|
| Business Rules | Client (form) | Form open, field change | Declarative (no code) |
| Low-Code Plug-ins | Server (Dataverse) | Data events or manual call | Power Fx |
| Real-Time Workflows | Server (Dataverse) | Data events | Declarative (legacy) |
| Custom Process Actions | Server (Dataverse) | API/flow call | Declarative config |
| Power Automate | Cloud | Triggers + connectors | Low-code flow designer |

### Critical Distinction
- Business Rules: client-side, can be bypassed by API/import operations
- Low-Code Plug-ins: server-side, always enforced regardless of client
