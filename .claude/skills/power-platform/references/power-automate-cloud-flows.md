# Power Automate Cloud Flows Reference

## Flow Types

| Flow Type | Trigger | Use Case |
|-----------|---------|----------|
| Automated cloud flow | Event-driven (connector event) | React to email, SharePoint item, Dataverse row change |
| Instant cloud flow | Manual button tap or app invoke | On-demand tasks: send reminder, run report |
| Scheduled cloud flow | Time-based recurrence | Daily upload, weekly report, hourly sync |
| Business process flow | User-driven stages in model-driven apps | Lead qualification, case management |

Limit: up to 600 flows per account.

## Triggers

Every flow has exactly one trigger. Categories: Automated (event in connected service), Instant/Manual (user button tap), Scheduled (recurring time schedule).

### Trigger Configuration

- **Split On**: debatch arrays so each item triggers a separate run
- **Concurrency Control**: limit parallel runs (1-50) to prevent race conditions
- **Trigger Conditions**: expressions that must evaluate to true for the trigger to fire
- **Polling Interval**: frequency for polling-based triggers

### Common Connector Triggers

- **SharePoint**: When an item is created, When an item is created or modified, For a selected item
- **Outlook 365**: When a new email arrives (V3), When an event is created (V3)
- **Dataverse**: When a row is added/modified/deleted, When an action is performed
- **Teams**: When a new channel message is added
- **HTTP**: When an HTTP request is received (webhook)

## Actions and Control Flow

| Action | Purpose |
|--------|---------|
| Condition | If/then/else branching based on value comparison |
| Switch | Multi-branch routing based on a single value |
| Apply to each | Loop through an array of items |
| Do until | Loop until a condition is met or count/timeout reached |
| Scope | Group related actions into a logical block |
| Terminate | End the flow with Succeeded, Failed, or Cancelled status |
| Compose | Create or transform data inline |
| Filter array | Filter an array based on a condition |
| Select | Map/transform array items to a new shape |
| Parse JSON | Parse a JSON string into typed dynamic content |

### Conditions

Branch into **If yes** and **If no** paths. Operators: is equal to, is not equal to, contains, does not contain, starts with, ends with, is greater than, is less than. Add rows (AND logic) and groups (OR logic).

### Loops

- **Apply to each**: iterate over an array. Enable concurrency (max 50) for parallel iterations. Use `item()` for current iteration.
- **Do until**: loop until condition met or count/timeout reached. Useful for polling patterns.

### Parallel Branches

Add parallel branches to run actions concurrently. Actions after all branches wait for every branch to complete.

## Error Handling

### Scope-Based Try-Catch-Finally

```
[Trigger]
  -> [Try Scope] -- main business logic
  -> [Catch Scope] -- run after Try "has failed"
  -> [Finally Scope] -- run after Catch "is successful" OR "has failed" OR "is skipped"
```

### Configure Run After

| Setting | When Action Runs |
|---------|-----------------|
| is successful | Previous action succeeded (default) |
| has failed | Previous action failed |
| is skipped | Previous action was skipped |
| has timed out | Previous action timed out |

Multiple options can be selected. This is the foundation for error handling.

### Retry Policies

| Policy | Behavior |
|--------|----------|
| Default | Up to 4 retries at exponentially increasing intervals |
| None | No retries |
| Fixed interval | Retry at a fixed interval |
| Exponential interval | Retry with increasing delays (preferred for transient failures) |

### Error Information

- `result('ScopeName')` -- array of action results within a scope
- `actions('actionName')?['status']` -- check status of a specific action
- `workflow()` -- metadata about current flow run
- Use Filter array on `result()` to find failed actions
- **Terminate**: stop the flow with Succeeded, Failed (with error code/message), or Cancelled

## Scopes

Group actions into a collapsible block. Benefits: organization, error management (try/catch), status monitoring. Status values: Succeeded, Failed, Skipped, Cancelled, TimedOut. Max 8 nested levels.

## Child Flows

- Both parent and child must be in the same solution
- Child uses "Manually trigger a flow" trigger and "Respond to a Power App or flow" to return data
- Call via "Run a Child Flow" action (Flows connector)
- Inputs: define on manual trigger card (text, number, boolean, file, email)
- Outputs: define on Respond action card; available as dynamic content in parent
- Child flows must use embedded connections ("Use this connection" in Properties)
- Lifetime: Built-in/Dataverse connections up to 1 year; others up to 30 days

## Approvals

| Type | Behavior |
|------|----------|
| Approve/Reject - First to respond | First approver's response decides |
| Approve/Reject - Everyone must approve | All assigned approvers must approve |
| Custom Responses - Wait for one response | Custom options, first response decides |
| Custom Responses - Wait for all responses | Custom options, all must respond |

- **Sequential**: chain multiple approval actions; each fires after the previous completes
- **Parallel**: use parallel branches with separate approval actions
- **Attachments**: binary encoded via Attachments Name/Content fields
- **Response channels**: email, Approvals center, mobile app, Teams

## Business Process Flows

Guide users through multi-stage processes in model-driven apps.

- **Stages**: visual steps as a process bar (max 30 per process)
- **Steps**: data entry fields within each stage (max 30 per stage)
- **Stage-gating**: require fields before advancing
- **Branching**: conditions route users to different stages
- **Workflows**: trigger on stage entry/exit or process completion

Limits: max 10 active BPFs per table, max 5 tables per multi-table BPF. Must be created inside a solution.

## Dataverse Connector

### Triggers

When a row is added/modified/deleted, When a row is selected (model-driven app), When an action is performed (custom actions).

### Actions

| Action | Description |
|--------|-------------|
| Create a new row | Insert into a Dataverse table |
| Update / Delete a row | Update or delete by ID |
| Get a row by ID | Retrieve single row |
| List rows | Query with OData filter, select, expand, order by |
| Search rows | Full-text relevance search |
| Relate / Unrelate rows | Manage relationships |
| Execute a changeset request | Batch operations in a single transaction |
| Perform bound / unbound action | Execute custom Dataverse actions |

## Solution-Aware Flows

Flows inside Dataverse solutions for ALM. Benefits: transportable via export/import, connection references for environment-specific connections, environment variables, managed/unmanaged layering, parent-child linking preserved.

Create: Solutions > select/create solution > New > Automation > Cloud flow. Connections are abstracted as connection references; map to local connections during import.

## Key Patterns

### Scheduled Data Sync with Error Handling

```
Recurrence (daily)
  -> [Try Scope] -> List rows -> Apply to each -> Create/Update row
  -> [Catch Scope] -> Filter failed results -> Send email -> Terminate (Failed)
```

### Approval with Escalation

```
When item created -> Approval (manager) -> If Approved -> Approval (director)
  -> If Approved -> Update (Approved) / Else -> Update (Rejected)
```

### Parallel Processing with Aggregation

```
HTTP request received -> [Branch 1: API A] [Branch 2: API B] [Branch 3: API C]
  -> Compose combined results -> Respond with aggregated data
```

### Child Flow Reuse

```
Child Flow: "Process Contact" (manual trigger -> lookup/create -> respond with ID)
Parent Flow A: email arrives -> Run "Process Contact"
Parent Flow B: form submitted -> Run "Process Contact"
```

## Best Practices

- Use descriptive names for flows, actions, and variables
- Use scopes for grouping and try-catch patterns
- Use child flows for reusable logic; avoid flows with hundreds of steps
- Use solution-aware flows for ALM and environment portability
- Enable concurrency on Apply to each for independent iterations
- Use Select/Filter array instead of loops for data transformation
- Use trigger conditions to prevent unnecessary runs
- Always implement try-catch using scopes and Run After
- Use retry policies (exponential preferred) for transient failures
- Log errors to SharePoint/Dataverse and send failure notifications
