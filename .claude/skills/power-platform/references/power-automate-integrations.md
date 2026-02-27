# Power Automate Integrations Reference

## Dataverse Connector Patterns

### Triggers

When a row is added/modified/deleted, When a row is selected (model-driven app), When an action is performed (custom actions).

### Actions

| Action | Description |
|--------|-------------|
| Create a new row | Insert into a Dataverse table |
| Update / Delete a row | Modify or remove by ID |
| Get a row by ID | Retrieve single row |
| List rows | Query with OData filter, select, expand, order by |
| Search rows | Full-text relevance search across tables |
| Relate / Unrelate rows | Manage many-to-many or lookup relationships |
| Execute a changeset request | Batch operations in a single transaction |
| Perform bound / unbound action | Execute custom Dataverse actions |

### Best Practices

- Use `$select` to retrieve only needed columns; use `$filter` to limit rows
- Use changeset requests for transactional batch operations
- Avoid infinite loops: workflows updating a column that triggers the same workflow (limit: 16 iterations)
- Use environment variables for configuration across environments

## SharePoint Integration

### Triggers

When an item is created, When an item is created or modified, For a selected item (manual trigger from list).

### Actions

Create/Update/Delete/Get item, Get items, Create file, Get file content, Update file properties, Copy/Move file, Send HTTP request to SharePoint (advanced REST API calls).

### Patterns

**Document approval**: file created -> Start approval -> If approved -> Move to approved folder, update metadata -> Notify requester.

**List processing**: item created -> Validate data -> Create Dataverse row -> Update SharePoint status -> Send confirmation.

**Scheduled report**: Recurrence -> Get items with filter -> Create CSV/HTML table -> Send email.

## Teams Integration

### Triggers

When a new channel message is added, When someone is mentioned, When keywords are mentioned.

### Actions

Post message in chat or channel, Post adaptive card and wait for response, Create channel, Get team members, Reply to message, Post as Flow bot.

### Patterns

**Adaptive card approval**: event trigger -> Post adaptive card -> Wait for response -> Process outcome -> Update source system.

**Notification bot**: system event -> Compose notification -> Post as Flow bot to user or channel.

## Email Flows (Outlook 365)

### Triggers

When a new email arrives (V3) -- filter by folder, subject, from, importance, attachments. When an event is created (V3).

### Actions

Send email (V2): to, cc, bcc, subject, body (HTML), attachments. Reply, Forward, Move, Flag email. Get emails, Export email. Create/Update/Delete calendar events.

### Patterns

**Auto-reply with processing**: email arrives (subject filter) -> Get attachment -> Save to SharePoint -> Send confirmation reply.

**Email-to-ticket**: email arrives -> Parse body -> Create Dataverse row -> Send acknowledgment with ticket number.

**Scheduled digest**: Recurrence -> Get items needing attention -> Create HTML table -> Send summary email.

## HTTP Connector

| Action | Use Case |
|--------|----------|
| HTTP | Send any REST request (GET, POST, PUT, PATCH, DELETE) |
| HTTP + Swagger | Call APIs with OpenAPI definition for typed inputs/outputs |
| HTTP Webhook | Subscribe to webhook callbacks; flow waits for callback |

**HTTP Trigger**: "When an HTTP request is received" creates a webhook endpoint. Define JSON schema for typed dynamic content. Respond with Response action.

Authentication types: None, Basic, Client Certificate, Active Directory OAuth, Raw.

## Common Integration Patterns

### Event-Driven Processing

```
Dataverse row created -> Validate data -> HTTP call to external API
  -> Update Dataverse with response -> Notify via Teams
```

### Scheduled Sync Between Systems

```
Recurrence -> List rows (Dataverse) with filter
  -> Apply to each -> HTTP POST to external system
  -> [Catch] -> Log errors to SharePoint -> Send failure email
```

### Multi-Channel Notification

```
Event trigger -> Compose message
  -> [Branch 1] Send email  [Branch 2] Post to Teams  [Branch 3] Push notification
```

### Document Lifecycle

```
SharePoint file created -> Approval (manager)
  -> Approved: update metadata, move to published library
  -> Rejected: notify author via Teams, update status
```

### Form-to-Record Pipeline

```
Forms response submitted -> Get response details -> Create Dataverse row
  -> Create SharePoint folder -> Upload attachments -> Send confirmation
```
