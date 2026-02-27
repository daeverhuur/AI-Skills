# Power Automate Cloud Flows

> Source: Microsoft Learn -- learn.microsoft.com/en-us/power-automate/

## 1. Overview and Flow Types

Power Automate provides three main flow types for automation:

| Flow Type | Trigger | Use Case | Example |
|-----------|---------|----------|---------|
| **Automated cloud flow** | Event-driven | React to events in connected services | Email arrival, SharePoint item created, Dataverse row updated |
| **Instant cloud flow** | Manual / button tap | On-demand tasks triggered by user | Send reminder, request approval, run report |
| **Scheduled cloud flow** | Time-based recurrence | Periodic batch processing | Daily data upload, weekly report, hourly sync |
| **Desktop flow** | Called from cloud flow or manual | RPA for legacy/desktop apps | Automate Win32 app, web scraping |
| **Business process flow** | User-driven stages | Guide users through multi-stage processes | Lead-to-opportunity, case management |

Limits: up to 600 flows per account. Flows created via Copilot or from scratch using the designer.

## 2. Triggers

A trigger is the event that starts a cloud flow. Every flow must have exactly one trigger.

### Trigger Categories

| Category | How It Fires | Examples |
|----------|-------------|----------|
| **Automated** | When an event occurs in a connected service | `When a new email arrives (V3)`, `When an item is created` (SharePoint) |
| **Instant / Manual** | User taps a button or invokes from an app | `Manually trigger a flow`, `For a selected item` |
| **Scheduled** | On a recurring time schedule | `Recurrence` trigger -- configure frequency (minute/hour/day/week/month) |

### Trigger Configuration Options

- **Split On**: Debatch arrays so each item triggers a separate flow run
- **Concurrency Control**: Limit parallel runs (1-50) to prevent race conditions
- **Trigger Conditions**: Add expressions that must evaluate to true for the trigger to fire (avoids unnecessary runs)
- **Polling interval**: For polling-based triggers, set how frequently the service checks for new data

### Common Connector Triggers

- **SharePoint**: When an item is created, When an item is created or modified, For a selected item
- **Outlook 365**: When a new email arrives (V3), When an event is created (V3)
- **Dataverse**: When a row is added/modified/deleted, When an action is performed
- **Teams**: When a new channel message is added, When someone is mentioned
- **HTTP**: When an HTTP request is received (webhook trigger)

## 3. Actions and Control Flow

### Core Control Actions

| Action | Purpose |
|--------|---------|
| **Condition** | If/then/else branching based on value comparison |
| **Switch** | Multi-branch routing based on a single value |
| **Apply to each** | Loop through an array of items |
| **Do until** | Loop until a condition is met or count/timeout reached |
| **Scope** | Group related actions into a logical block |
| **Terminate** | End the flow with a status (Succeeded, Failed, Cancelled) |
| **Compose** | Create or transform data inline |
| **Filter array** | Filter an array based on a condition |
| **Select** | Map/transform array items to a new shape |
| **Parse JSON** | Parse a JSON string into typed dynamic content |

### Conditions

Add a Condition action to branch the flow into **If yes** (true) and **If no** (false) paths. You can:

- Compare a dynamic value against a static value
- Use operators: is equal to, is not equal to, contains, does not contain, starts with, ends with, is greater than, is less than
- Add rows (AND logic within a group) and groups (OR logic between groups)
- Switch to advanced mode to use expressions directly

### Parallel Branches

Create parallel branches to run actions concurrently. Use the plus sign between steps and select "Add a parallel branch." Actions after all parallel branches wait for all branches to complete before executing.

Use case: Send approval requests to multiple approvers simultaneously.

## 4. Expressions

Expressions use the Workflow Definition Language (shared with Azure Logic Apps). Access via the `fx` button in the designer.

### Logical Expressions

| Expression | Description | Example |
|------------|-------------|---------|
| `and(expr1, expr2)` | True if both are true | `and(greater(1,0), equals(0,0))` |
| `or(expr1, expr2)` | True if either is true | `or(greater(1,10), equals(0,0))` |
| `equals(val1, val2)` | True if values are equal | `equals(parameters('status'), 'Active')` |
| `less(val1, val2)` | True if first < second | `less(10, 100)` |
| `lessOrEquals(val1, val2)` | True if first <= second | `lessOrEquals(10, 10)` |
| `greater(val1, val2)` | True if first > second | `greater(100, 10)` |
| `greaterOrEquals(val1, val2)` | True if first >= second | `greaterOrEquals(10, 10)` |
| `empty(value)` | True if empty string/array/object | `empty('')` |
| `not(expr)` | Returns opposite boolean | `not(contains('200 Success','Fail'))` |
| `if(expr, trueVal, falseVal)` | Conditional return | `if(equals(1,1), 'yes', 'no')` |

### Common Expression Patterns

```
// Check item field value
@equals(item()?['Status'], 'Active')

// Combine conditions
@and(equals(item()?['Status'], 'blocked'), equals(item()?['Assigned'], 'John'))

// Check for empty values
@and(empty(item()?['Status']), empty(item()?['Assigned']))

// Date comparison
@less(item()?['DueDate'], addDays(utcNow(), 1))

// Combine greater and less with and
@and(greater(item()?['Due'], item()?['Paid']), less(item()?['dueDate'], addDays(utcNow(),1)))
```

Full function reference: Workflow Definition Language Functions Reference (shared with Azure Logic Apps).

## 5. Apply to Each (Loops)

The **Apply to each** action iterates over an array. Each iteration processes one item.

- **Input**: Select an output array from a previous step (e.g., `value` from List rows)
- **Concurrency control**: Enable in Settings to run iterations in parallel (default: sequential, max 50 concurrent)
- **Nested loops**: Supported but impacts performance; use `item()` to access current iteration data
- **Performance tip**: Enable concurrency for independent iterations; keep loop body minimal

Pattern: Scheduled flow (every 15 min) -> Get emails (V3) -> Apply to each over emails -> Condition on subject -> Send notification.

## 6. Error Handling

### Scope-Based Try-Catch-Finally

Use Scope actions to implement structured error handling:

```
[Trigger]
  |
[Try Scope] -- contains main business logic actions
  |
[Catch Scope] -- configured to run after Try Scope "has failed"
  |
[Finally Scope] -- configured to run after Catch Scope "is successful" OR "has failed" OR "is skipped"
```

### Configure Run After

Every action has "Run after" settings that control when it executes relative to the preceding action:

| Setting | When Action Runs |
|---------|-----------------|
| **is successful** | Previous action succeeded (default) |
| **has failed** | Previous action failed |
| **is skipped** | Previous action was skipped |
| **has timed out** | Previous action timed out |

You can select multiple options. This is the foundation of error handling -- configure the Catch scope to run after the Try scope "has failed."

### Retry Policies

Configure in action Settings:

| Policy | Behavior |
|--------|----------|
| **Default** | Up to 4 retries at exponentially increasing intervals |
| **None** | No retries |
| **Fixed interval** | Retry at a fixed interval (e.g., every 30 seconds) |
| **Exponential interval** | Retry with increasing delays (preferred for transient failures) |

### Error Information Functions

- `result('ScopeName')` -- returns an array of action results within a scope; use Filter array to find failed actions
- `workflow()` -- returns metadata about current flow run (ID, name, environment)
- `actions('actionName')?['status']` -- check status of a specific action

### Terminate Action

Use **Terminate** to stop the flow with a status:
- **Succeeded**: Mark flow as successful
- **Failed**: Mark flow as failed with error code and message
- **Cancelled**: Mark flow as cancelled

## 7. Scopes

Scopes group related actions into a single collapsible block.

**Benefits**: Organization, error management (try/catch), bulk collapse/expand, status monitoring.

**Scope status values**: Succeeded, Failed, Skipped, Cancelled, TimedOut.

**Limitation**: Maximum 8 nested levels of actions (scopes, conditions, switches, apply-to-each combined). Triggers and response actions must remain outside scopes.

## 8. Child Flows

Child flows allow reusable flow logic called from a parent flow.

### Requirements

- Both parent and child flows must be in the **same solution**
- Child flow must use the **Manually trigger a flow** trigger
- Child flow uses **Respond to a Power App or flow** (or HTTP Response) to return data
- Call via the **Run a Child Flow** action (Flows connector, Built-in tab)

### Parameter Passing

- **Inputs**: Define on the manual trigger card (text, number, boolean, file, email, etc.)
- **Outputs**: Define on the Respond action card; available as dynamic content in parent flow

### Connection Handling

Child flows must use **embedded connections** (not "Provided by run-only user"). Configure in the child flow's Properties > Run only users > set each connection to "Use this connection."

### Lifetime

Parent flow waits for child flow completion:
- **Built-in/Dataverse connections**: up to 1 year
- **All other connections**: up to 30 days

### Known Issues

- Cannot pass connections from parent to child flow
- Create both flows directly in the same solution (importing may cause issues)

## 9. Approvals

Power Automate provides built-in approval actions.

### Approval Types

| Type | Behavior |
|------|----------|
| **Approve/Reject - First to respond** | First approver's response decides |
| **Approve/Reject - Everyone must approve** | All assigned approvers must approve |
| **Custom Responses - Wait for one response** | Custom options, first response decides |
| **Custom Responses - Wait for all responses** | Custom options, all must respond |

### Sequential Approvals

Chain multiple **Start and wait for an approval** actions in sequence. Each subsequent approval only fires after the previous one completes. Pattern: Pre-approver -> check response -> Final approver -> check response -> notify requester.

### Parallel Approvals

Use parallel branches, each containing a separate **Start and wait for an approval** action. All branches run simultaneously. After all branches complete, add actions to summarize decisions.

### Approval Attachments

- Use **Attachments Name** and **Attachments Content** fields in the approval action
- File content must be binary encoded
- Approvers can view attachments in email and the Approvals center
- Supports Markdown formatting in the **Details** field

### Approval Center

Approvers can respond from: email, Power Automate Approvals center, Power Automate mobile app, or Teams (with Approvals app).

## 10. Dataverse Connector

### Triggers

| Trigger | Description |
|---------|-------------|
| **When a row is added, modified, or deleted** | Fires on Dataverse table row changes |
| **When a row is selected** | Fires when user selects a row in a model-driven app |
| **When an action is performed** | Fires on custom Dataverse actions/messages |

### Actions

| Action | Description |
|--------|-------------|
| **Create a new row** | Insert a row into a Dataverse table |
| **Update a row** | Update an existing row by ID |
| **Delete a row** | Delete a row by ID |
| **Get a row by ID** | Retrieve a single row |
| **List rows** | Query rows with OData filter, select, expand, order by |
| **Search rows (Relevance Search)** | Full-text search across Dataverse tables |
| **Relate / Unrelate rows** | Manage many-to-many or lookup relationships |
| **Execute a changeset request** | Batch multiple operations in a single transaction |
| **Upload / Download file or image** | Handle file/image columns |
| **Perform bound / unbound action** | Execute custom Dataverse actions |

## 11. Solution-Aware Flows

Solution-aware flows live inside Dataverse solutions for ALM (Application Lifecycle Management).

### Benefits

- Transportable between environments via solution export/import
- Connection references for environment-specific connections
- Environment variables for configuration values
- Managed/unmanaged solution layering
- Parent-child flow linking preserved across environments

### Creating

1. Navigate to Solutions in Power Automate
2. Select or create a solution
3. New > Automation > Cloud flow > choose type
4. Build and save the flow

### Adding Existing Flows

Use **Add existing > Automation > Cloud flow** in the solution explorer. Non-solution flows appear in the "Outside Dataverse" tab.

### Connection References

When adding flows to solutions, connections are abstracted as connection references. During import to a new environment, map connection references to local connections.

## 12. Business Process Flows

Business process flows (BPFs) guide users through multi-stage business processes within model-driven apps.

### Key Concepts

- **Stages**: Visual steps displayed as a process bar at the top of a form (max 30 per process)
- **Steps**: Data entry fields within each stage (max 30 per stage)
- **Stage-gating**: Require fields to be completed before advancing
- **Branching**: Add conditions to route users to different stages
- **Workflows**: Trigger on-demand workflows on stage entry/exit or process completion/abandonment

### Limits

| Limit | Value |
|-------|-------|
| Max active BPFs per table | 10 |
| Max stages per process | 30 |
| Max steps per stage | 30 |
| Max tables per multi-table BPF | 5 |
| Max branch depth | 10 levels |

### Security

- Associate BPFs with security roles to control visibility
- Set process flow order to control default assignment
- System Administrator and System Customizer roles have access by default

### Creating BPFs

Must be created inside a solution (Power Apps or solution explorer). No longer supported to create from Power Automate outside solution explorer (as of August 2022). Requires Power Apps/Power Automate per-user license or Dynamics 365 license.

## 13. Best Practices

### Flow Design

- **Use descriptive names** for flows, actions, and variables
- **Add notes/comments** to actions to document purpose and changes
- **Use scopes** to group related actions and implement try-catch patterns
- **Use child flows** for reusable logic; avoid flows with hundreds of steps
- **Use solution-aware flows** for ALM and environment portability

### Performance

- **Enable concurrency** on Apply to each when iterations are independent
- **Minimize loop body** actions; batch operations where possible
- **Use Select/Filter array** actions instead of loops for data transformation
- **Limit polling triggers** frequency to reduce API consumption
- **Use trigger conditions** to prevent unnecessary flow runs

### Error Handling

- **Always implement try-catch** using scopes and Run After configuration
- **Use retry policies** (exponential preferred) for transient failures
- **Log errors** to SharePoint/Dataverse; send notification emails on failure
- **Use Terminate action** for critical failures with meaningful error messages
- **Use the `result()` function** with Filter array to extract specific error details from scope

### Workflow Process Best Practices (Dataverse)

- **Avoid infinite loops**: Workflows that update a column and trigger on that column's change create loops (limit: 16 iterations before auto-cancel)
- **Use workflow templates** for common patterns
- **Use child workflows** to avoid duplicating logic
- **Enable auto-delete** of completed workflow jobs to save disk space
- **Limit workflows per table** that update the same table to avoid resource lock issues

## 14. Key Patterns

### Pattern: Scheduled Data Sync with Error Handling

```
Recurrence (daily)
  -> [Try Scope]
       -> List rows (source)
       -> Apply to each
            -> Create/Update row (destination)
  -> [Catch Scope] (run after Try: has failed)
       -> Filter array: result('Try') where status eq 'Failed'
       -> Send email notification with error details
       -> Terminate (Failed)
```

### Pattern: Approval with Escalation

```
When item created (SharePoint)
  -> Start and wait for approval (manager)
  -> Condition: Response eq 'Approve'
       -> Yes: Start and wait for approval (director)
            -> Condition: Response eq 'Approve'
                 -> Yes: Update item (Approved)
                 -> No: Update item (Rejected by director)
       -> No: Update item (Rejected by manager)
  -> Send email to requester with decision
```

### Pattern: Parallel Processing with Aggregation

```
When HTTP request received
  -> [Branch 1]: Call API A
  -> [Branch 2]: Call API B
  -> [Branch 3]: Call API C
  -> Compose: combine results from all branches
  -> Respond to HTTP request with aggregated data
```

### Pattern: Child Flow Reuse

```
Solution contains:
  - Child Flow: "Process Contact" (Manually trigger -> lookup/create contact -> Respond with contact ID)
  - Parent Flow A: When email arrives -> Run a Child Flow "Process Contact"
  - Parent Flow B: When form submitted -> Run a Child Flow "Process Contact"
```

### Pattern: BPF with Workflow Automation

```
Business Process Flow: Lead Qualification
  Stage 1: Qualify (on exit -> trigger scoring workflow)
  Stage 2: Develop (on exit -> trigger notification workflow)
  Stage 3: Propose (on exit -> trigger approval workflow)
  Stage 4: Close
  Global Workflow: on Process Completed -> update reporting table
```
