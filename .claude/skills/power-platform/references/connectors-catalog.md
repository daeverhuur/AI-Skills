# Connectors Reference

> Distilled from Microsoft Learn connector reference documentation

---

## Overview

Connectors enable Power Apps, Power Automate, Copilot Studio, and Logic Apps to communicate with external services. All connectors expose **actions** (e.g., create a file) and **triggers** (e.g., when a new item is added). There are 1,000+ prebuilt connectors available. Connectors created in Power Automate are available in Power Apps and Copilot Studio (and vice versa). Logic Apps connectors must be recreated.

---

## Connector Types

| Type | Description | Licensing |
|------|-------------|-----------|
| **Standard** | Included with most Power Platform licenses | No additional cost |
| **Premium** | Higher-tier connectors for enterprise services | Requires Premium license per user |
| **Custom** | User-built connectors wrapping REST/SOAP APIs | Treated as Premium |
| **MCP Server** | Connectors exposing Model Context Protocol endpoints | Varies by connector |

---

## Top 50 Connectors by Category

### Microsoft 365 and Productivity

| Connector | Tier | Key Actions | Key Triggers |
|-----------|------|-------------|--------------|
| **SharePoint** | Standard | Create/update/delete items, get files, create folder, copy file | When item created, when item modified, when file created |
| **Office 365 Outlook** | Standard | Send email, create event, get contacts, send email with options | When new email arrives, when event is upcoming |
| **Microsoft Teams** | Standard | Post message, create channel, list members, post adaptive card | When a message is posted, when I am mentioned |
| **OneDrive for Business** | Standard | Create file, get file content, list folder, copy file | When a file is created, when a file is modified |
| **Excel Online (Business)** | Standard | Add row, get row, update row, list rows, run script | When a row is added/modified (poll) |
| **OneNote** | Standard | Create page, get pages, get notebooks | None (actions only) |
| **Planner** | Standard | Create task, update task, list tasks, list buckets | None (actions only) |
| **Microsoft Forms** | Standard | Get response details, list responses | When a new response is submitted |
| **Approvals** | Standard | Start and wait, create approval, wait for approval | None (used within flows) |
| **Microsoft To Do** | Standard | Create task, list tasks, update task | None (actions only) |

### Data and Databases

| Connector | Tier | Key Actions | Key Triggers |
|-----------|------|-------------|--------------|
| **Dataverse** | Standard* | List rows, get row, add row, update row, delete row, relate/unrelate | When a row is added/modified/deleted |
| **SQL Server** | Premium | Execute query, get rows, insert row, update row, delete row | When an item is created, when an item is modified |
| **Azure SQL Data Warehouse** | Premium | Execute query, get rows, insert row | None |
| **MySQL** | Premium | Get rows, insert row, update row, delete row | None |
| **PostgreSQL** | Premium | Get rows, insert row, execute query | None |
| **Oracle Database** | Premium | Get rows, insert row, update row, execute procedure | None |
| **Azure Cosmos DB** | Premium | Create/read document, query documents, execute procedure | None |
| **Azure Table Storage** | Standard | Insert entity, get entity, get entities, delete entity | None |

*Dataverse is Standard when used within the same environment; Premium for cross-environment.

### Cloud Services and AI

| Connector | Tier | Key Actions | Key Triggers |
|-----------|------|-------------|--------------|
| **HTTP** | Standard | Send HTTP request (any method, URL, headers, body) | None |
| **HTTP with Microsoft Entra ID** | Standard | Invoke HTTP request with Azure AD auth | None |
| **Azure Functions** | Standard | Call Azure Function | None |
| **Azure Blob Storage** | Standard | Create blob, get blob content, list blobs, delete blob | When a blob is added/modified |
| **Azure Key Vault** | Premium | Get secret, list secrets | None |
| **Azure DevOps** | Standard | Create work item, update work item, queue build | When a work item is created/updated |
| **AI Builder** | Premium | Extract text from documents, classify text, detect objects | None |
| **Azure OpenAI** | Premium | Create completion, create chat completion, create embedding | None |
| **Cognitive Services** | Premium | Analyze sentiment, detect language, extract key phrases | None |

### Third-Party Services

| Connector | Tier | Key Actions | Key Triggers |
|-----------|------|-------------|--------------|
| **Salesforce** | Premium | Create/update/delete record, get record, execute SOQL query | When a record is created/modified |
| **ServiceNow** | Premium | Create/update record, list records, get record | When a record is created/modified |
| **SAP ERP** | Premium | Call RFC, call BAPI, read table, send IDoc | None |
| **Jira** | Premium | Create issue, update issue, add comment, transition issue | When an issue is created/updated |
| **Slack** | Standard | Post message, list channels, upload file | When a new message is posted |
| **Google Sheets** | Premium | Get rows, insert row, update row, delete row | None |
| **Dropbox** | Standard | Create file, get file, list folder, copy file | When a file is created/modified |
| **Twitter** | Standard | Post tweet, search tweets, get followers | When a new tweet is posted |
| **Mailchimp** | Standard | Add member to list, send campaign, get lists | None |
| **DocuSign** | Premium | Send envelope, get envelope status, download document | When envelope status changes |
| **Adobe Sign** | Premium | Create agreement, get agreement status | When agreement completed/signed |

### Notifications and Communication

| Connector | Tier | Key Actions | Key Triggers |
|-----------|------|-------------|--------------|
| **Outlook.com** | Standard | Send email, create event, get contacts | When new email arrives |
| **Gmail** | Premium | Send email, get email, list labels | When new email arrives |
| **Twilio** | Premium | Send SMS, make call, get message | None |
| **SendGrid** | Premium | Send email (v4) | None |
| **Push Notifications** | Standard | Send push notification to Power Automate mobile app | None |

---

## Standard vs Premium Tier Details

| Aspect | Standard | Premium |
|--------|----------|---------|
| **License required** | Power Apps/Automate per user, Microsoft 365, Dynamics 365 | Power Apps/Automate Premium per user, or per-app/per-flow plan |
| **Per-user cost impact** | Included | Requires upgrade to Premium license (~$20/user/month for Power Automate) |
| **Custom connectors** | N/A | All custom connectors are treated as Premium |
| **DLP classification** | Default: Business or Non-Business | Default: Business or Non-Business |
| **Example connectors** | SharePoint, Outlook, Teams, OneDrive, HTTP | SQL Server, Salesforce, SAP, Azure OpenAI, ServiceNow |
| **Pay-as-you-go** | Supported | Supported (metered per request) |

### License Implications in Flows

- A flow using **any** Premium connector requires **all users** who benefit from the flow to have Premium licenses
- Exception: Service principal connections and per-flow plans cover all users
- Flows with only Standard connectors can be shared freely
- Child flows inherit the licensing requirement of the parent

---

## Throttling and Request Limits

### Power Platform Request Limits (per 24 hours)

| License Type | Requests per User per Day |
|-------------|--------------------------|
| Power Apps/Automate Premium, Dynamics 365 (most) | 40,000 |
| Power Apps per app, Microsoft 365, Dynamics 365 Team Member | 6,000 |
| Power Automate per flow plan | 250,000 (per flow) |
| Non-licensed users (via app pass) | 6,000 |

### Per-Connector Throttling

Many connectors have their own throttling limits independent of Power Platform limits:

| Connector | Throttle Limit | Notes |
|-----------|---------------|-------|
| **SharePoint** | 600 requests/min per connection | Applies to all operations |
| **Office 365 Outlook** | 300 requests/min per mailbox | Includes send/read/update |
| **Microsoft Teams** | 60 messages/min per flow | Posting messages |
| **Dataverse** | 6,000 requests/5 min per user | Applies to CRUD operations |
| **SQL Server** | No connector-level limit | Subject to SQL Server limits |
| **HTTP** | 3,000 requests/min per connection | General HTTP calls |
| **Salesforce** | Based on Salesforce API limits | Varies by Salesforce edition |
| **Excel Online** | 100 requests/min per connection | Read/write operations |

### Handling Throttling

- **429 Too Many Requests**: Flow automatically retries with exponential backoff (default)
- **Retry-After header**: Respected by the runtime; flow pauses for the specified duration
- **Concurrency control**: Set action concurrency (1-50) to limit parallel executions
- **Pagination**: Use `$top` and `$skip` or `nextLink` for large datasets
- **Batch operations**: Use batch endpoints where available (e.g., SharePoint batch, Graph batch)

---

## On-Premises Data Gateway

### Overview

The on-premises data gateway acts as a bridge for secure data transfer between on-premises data sources and cloud services (Power BI, Power Apps, Power Automate, Azure Analysis Services, Logic Apps).

### Gateway Types

| Type | Users | Sharing | Use Case |
|------|-------|---------|----------|
| **Standard (Enterprise)** | Multiple | Shared across users | Team/org scenarios, multiple data sources |
| **Personal Mode** | Single user | Not shareable | Individual Power BI reports only |

### Supported On-Premises Connectors

| Connector | Gateway Required |
|-----------|-----------------|
| SQL Server (on-prem) | Yes |
| Oracle Database | Yes |
| MySQL (on-prem) | Yes |
| PostgreSQL (on-prem) | Yes |
| File System | Yes |
| SAP ERP (on-prem) | Yes |
| SharePoint (on-prem) | Yes |
| IBM DB2 | Yes |
| Informix | Yes |
| BizTalk Server | Yes |

### Gateway Architecture

```
[Cloud Service] --> [Azure Service Bus Relay] --> [Gateway Service on-prem] --> [Data Source]
```

- All communication is **outbound** from the gateway (no inbound firewall rules needed)
- Data encrypted in transit via TLS 1.2+
- Gateway authenticates using Azure Service Bus relay
- No data is stored in the cloud; the gateway is a pass-through

### Gateway Setup Steps

1. Download and install the gateway on an on-premises Windows server
2. Sign in with your organizational account
3. Register the gateway in Power Platform admin center
4. Configure data source connections in the admin center
5. Assign gateway admins and users
6. Use the gateway in flows/apps by selecting it during connection creation

### Gateway Requirements

| Requirement | Details |
|-------------|---------|
| OS | Windows Server 2019+, Windows 10/11 (64-bit) |
| .NET | .NET Framework 4.8+ |
| CPU | 8-core recommended |
| Memory | 8 GB minimum |
| Network | Outbound HTTPS to Azure Service Bus |
| Always-on | Server must remain running for flows to execute |

### Gateway Clustering

- Install multiple gateways in the same cluster for high availability
- Load balancing distributes requests across cluster members
- If one gateway goes offline, requests route to other members
- All cluster members must be on the same version

---

## Connection References

Connection references are solution-aware components that point to a specific connection. They allow solutions to be transported across environments without embedding credentials.

### How They Work

1. Developer creates a connection reference in a solution
2. Apps/flows reference connections through the connection reference (not directly)
3. On solution import, the admin maps connection references to actual connections
4. Connections can be swapped without modifying the app/flow

### Configuration at Import

```
Solution Import Wizard:
  Connection Reference: "SharePoint Connection"
  → Map to: [Select existing connection or create new]

  Connection Reference: "SQL Server Connection"
  → Map to: [Select existing connection or create new]
```

---

## Environment Variables

Environment variables store configuration values that differ across environments. Set during solution import so apps/flows avoid hardcoded values.

### Variable Types

| Type | Description | Example |
|------|-------------|---------|
| String | Plain text value | API base URL |
| Number | Numeric value | Timeout duration |
| JSON | JSON object/array | Complex configuration |
| Data source | Connection to a data source | SharePoint site URL |
| Secret | Azure Key Vault reference | API key, client secret |

### Key Vault Integration

- References Azure Key Vault secrets for sensitive values
- Cached for 5 minutes (reduces Key Vault API calls)
- Requires **Key Vault Secrets User** role assignment on the app identity
- Supports `AllowedEnvironments` and `AllowedAgents` tags for scoping

---

## DLP Policies (Data Loss Prevention)

### Connector Groups

| Group | Description |
|-------|-------------|
| **Business** | Connectors that handle business-sensitive data |
| **Non-Business** | Connectors for general or personal use |
| **Blocked** | Connectors prohibited from use entirely |

### Key Rules

- Connectors in **different groups cannot** be used together in the same app or flow
- Policies can be scoped to specific environments or applied **tenant-wide**
- Multiple DLP policies can apply; **most restrictive policy wins**
- Custom connectors can be classified into any group
- HTTP connector and custom connector DLP policies available for finer control

### Connector-Level DLP Controls

| Control | Description |
|---------|-------------|
| Connector classification | Assign to Business, Non-Business, or Blocked |
| Action-level control | Block specific actions within a connector |
| Endpoint filtering | Allow/block specific URL patterns for HTTP connectors |
| Custom connector patterns | Classify custom connectors by URL pattern |

### Administration

- Managed from **Power Platform admin center** > Policies > Data policies
- Requires **Tenant Admin** or **Environment Admin** role
- Best practice: start with a tenant-wide baseline policy, then layer environment-specific policies
- Use PowerShell cmdlets (`Get-DlpPolicy`, `Set-DlpPolicy`) for bulk management

---

## Common Connector Patterns

### Pattern 1: SharePoint List Automation

```
Trigger: SharePoint - When an item is created
Action: Office 365 Outlook - Send email
Action: Microsoft Teams - Post message
Action: Planner - Create task
```

### Pattern 2: Approval Workflow

```
Trigger: Microsoft Forms - When a response is submitted
Action: Approvals - Start and wait for approval
Condition: If approved
  Action: SharePoint - Create item
  Action: Office 365 Outlook - Send approval notification
Else:
  Action: Office 365 Outlook - Send rejection notification
```

### Pattern 3: Data Synchronization

```
Trigger: Recurrence (scheduled)
Action: SQL Server - Get rows (source)
Apply to each:
  Action: Dataverse - Get row (check exists)
  Condition: If not exists
    Action: Dataverse - Add row
  Else:
    Action: Dataverse - Update row
```

### Pattern 4: Multi-System Integration

```
Trigger: Dataverse - When a row is added
Action: HTTP - Call external API
Parse JSON response
Action: Salesforce - Create record
Action: SharePoint - Create file (store response)
Action: Teams - Post adaptive card (notify team)
```

### Pattern 5: Error Handling with Scope

```
Scope: Try
  Action: SQL Server - Execute query
  Action: SharePoint - Create item
Scope: Catch (runs on failure of Try)
  Action: Office 365 Outlook - Send error email
  Action: Dataverse - Add row (error log)
```

---

## Connector Health and Monitoring

### Monitoring Tools

| Tool | Purpose |
|------|---------|
| **Power Automate Analytics** | Flow run success/failure rates, action performance |
| **Power Platform Admin Center** | Environment-level usage, capacity, DLP violations |
| **Application Insights** | Custom telemetry from flows (via Log Analytics connector) |
| **Microsoft 365 Service Health** | Connector service status and incidents |
| **CoE Starter Kit** | Governance dashboards for connector usage across the org |

### Key Metrics to Track

- **Flow run success rate**: Target > 95%
- **Action failure rate per connector**: Identify unreliable connections
- **Throttling events (429s)**: Indicates need for flow optimization
- **Connection expiration**: OAuth tokens needing re-authentication
- **Gateway health**: For on-premises connections, monitor gateway uptime

### Troubleshooting Connection Issues

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| "Connection not configured" | Connection reference unmapped | Map connection reference in solution settings |
| "Unauthorized (401)" | Token expired | Re-authenticate the connection |
| "Forbidden (403)" | Insufficient permissions | Check API permissions and user roles |
| "Gateway offline" | On-prem gateway server down | Restart gateway service, check server status |
| "DLP violation" | Connectors in conflicting groups | Review DLP policy, move connector to correct group |
| "Request timeout" | Slow API or large payload | Increase timeout, paginate results, optimize query |
