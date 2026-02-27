# Power Platform 2025-2026 New Features Reference

> Major features and enhancements across 2025 Release Wave 1 (Apr-Sep 2025) and 2025 Release Wave 2 (Oct 2025-Mar 2026).

---

## 1. Copilot Studio: MCP (Model Context Protocol) Servers

MCP is an open standard that lets Copilot Studio agents connect to external tools and data sources through a unified protocol. Instead of building custom connectors for each service, agents use MCP servers as standardized bridges.

### What MCP Servers Do

| Capability | Description |
|-----------|-------------|
| **Tool exposure** | MCP server exposes functions (tools) that agents can call |
| **Resource access** | Provide structured data (files, DB records, API responses) |
| **Prompt templates** | Supply reusable prompt patterns for common tasks |
| **Bi-directional** | Agent sends requests, server returns structured results |

### Connecting an MCP Server in Copilot Studio

1. Navigate to **Settings > Tools > Add an MCP server**
2. Provide the server URL (SSE endpoint or streamable HTTP endpoint)
3. Configure authentication (API key, OAuth 2.0, or none for internal servers)
4. The agent auto-discovers available tools from the server manifest
5. Tools appear in the agent's tool catalog and can be used in topics

### MCP Server Configuration Example

```json
{
  "mcpServers": {
    "custom-erp": {
      "url": "https://erp.contoso.com/mcp/sse",
      "transport": "sse",
      "authentication": {
        "type": "oauth2",
        "clientId": "{{env.ERP_CLIENT_ID}}",
        "scope": "api://erp/.default"
      }
    },
    "local-tools": {
      "command": "npx",
      "args": ["-y", "@contoso/mcp-tools"],
      "transport": "stdio"
    }
  }
}
```

### Key Points

- MCP servers run externally (your infrastructure or third-party hosted)
- Copilot Studio supports SSE (Server-Sent Events) and streamable HTTP transports
- Each MCP tool gets its own input/output schema visible in the agent designer
- Tools discovered via MCP can be used alongside native Power Platform connectors
- Authentication flows are managed per-server, supporting API keys and OAuth 2.0

---

## 2. Autonomous Agents

Copilot Studio now supports building autonomous agents that run independently, triggered by events rather than user conversation.

### Agent Builder

The unified agent builder in Copilot Studio provides:

| Feature | Description |
|---------|-------------|
| **Declarative agents** | Define behavior through instructions, knowledge, and tools |
| **Custom engine agents** | Full orchestration control using custom code |
| **Prebuilt agents** | Start from templates (IT helpdesk, HR FAQ, sales coach) |
| **Agent library** | Central catalog of all agents in the organization |

### Triggers for Autonomous Agents

| Trigger Type | Example |
|-------------|---------|
| **Schedule** | Run daily at 8 AM to process overnight orders |
| **Event-based** | Dataverse row created/modified, email received |
| **Conversation** | User message in Teams or web chat |
| **Power Automate** | Flow calls agent as an action step |
| **HTTP** | External system sends webhook to agent endpoint |

### Long-Running Tasks

Autonomous agents can handle tasks that span hours or days:

- Agent initiates a workflow and parks it while waiting for approval
- Checkpointing saves progress so the agent can resume after interruption
- Timeout policies define maximum wait periods
- Status tracking via the Automation Center dashboard

### Multi-Agent Orchestration

Multiple agents can collaborate on complex tasks:

```
Orchestrator Agent
  ├── Research Agent (gathers data from MCP sources)
  ├── Analysis Agent (processes and summarizes findings)
  └── Action Agent (creates records, sends notifications)
```

- A primary agent delegates sub-tasks to specialized agents
- Each agent has its own knowledge, tools, and instructions
- Results pass back through the orchestrator for final assembly
- Built-in guardrails prevent infinite loops and runaway costs

---

## 3. Power Apps: Code-First Apps

A new app type that lets professional developers build full-page experiences using code components (PCF).

### Code-First App Capabilities

| Feature | Description |
|---------|-------------|
| **Full-page PCF** | A single code component occupies the entire app surface |
| **React + Fluent UI** | Build with modern web frameworks, not just canvas controls |
| **Dataverse integration** | Direct Web API access from the component |
| **ALM support** | Package in solutions, deploy through pipelines |
| **Managed hosting** | Runs inside Power Apps infrastructure (auth, licensing handled) |

### Creating a Code-First App

```bash
# Initialize a code-first app project
pac pcf init --namespace Contoso --name FullPageApp --template field --framework react

# Project structure
FullPageApp/
  ├── FullPageApp/
  │   ├── index.ts          # Component lifecycle
  │   ├── App.tsx            # React root component
  │   ├── ControlManifest.Input.xml
  │   └── components/
  ├── package.json
  └── tsconfig.json
```

### Key Patterns

```typescript
// index.ts - Full-page component entry
export class FullPageApp implements ComponentFramework.StandardControl<IInputs, IOutputs> {
    private container: HTMLDivElement;
    private context: ComponentFramework.Context<IInputs>;

    public init(context: ComponentFramework.Context<IInputs>,
                notifyOutputChanged: () => void,
                state: ComponentFramework.Dictionary,
                container: HTMLDivElement): void {
        this.container = container;
        this.context = context;
        // Full viewport available
        container.style.width = "100%";
        container.style.height = "100vh";
        this.renderApp();
    }

    private renderApp(): void {
        ReactDOM.render(
            React.createElement(App, {
                webAPI: this.context.webAPI,
                navigation: this.context.navigation,
                userSettings: this.context.userSettings
            }),
            this.container
        );
    }
}
```

### Pro-Dev Tool Improvements

- **pac CLI v1.33+**: `pac app create` command for code-first apps
- **Power Platform Tools VS Code extension**: Integrated debugging, hot reload
- **GitHub Codespaces**: Develop Power Platform code components in the cloud
- **Managed Identity for pac CLI**: Authenticate in CI/CD without service principal secrets

---

## 4. Python SDK for Dataverse

A new Python client library for interacting with Dataverse, targeting data engineers, data scientists, and backend developers.

### Installation and Setup

```bash
pip install microsoft-dataverse
```

### Authentication Patterns

```python
from dataverse import DataverseClient
from azure.identity import DefaultAzureCredential, ClientSecretCredential

# Interactive login (development)
client = DataverseClient(
    url="https://contoso.crm.dynamics.com",
    credential=DefaultAzureCredential()
)

# Service principal (production/CI)
credential = ClientSecretCredential(
    tenant_id="your-tenant-id",
    client_id="your-client-id",
    client_secret="your-secret"
)
client = DataverseClient(
    url="https://contoso.crm.dynamics.com",
    credential=credential
)
```

### Common Operations

```python
# Query records with OData filters
accounts = client.entities("accounts").select(
    "name", "revenue", "address1_city"
).filter(
    "revenue gt 1000000"
).top(50).execute()

for account in accounts:
    print(f"{account['name']}: ${account['revenue']:,.0f}")

# Create a record
new_contact = client.entities("contacts").create({
    "firstname": "Jane",
    "lastname": "Smith",
    "emailaddress1": "jane@contoso.com"
})

# Update a record
client.entities("contacts").update(new_contact["contactid"], {
    "jobtitle": "Senior Developer"
})

# Batch operations (up to 1000 per batch)
with client.batch() as batch:
    for record in large_dataset:
        batch.create("accounts", record)
    # Auto-commits in chunks of 1000
```

### Integration with Data Science Libraries

```python
import pandas as pd

# Query directly to DataFrame
df = client.entities("opportunities").select(
    "name", "estimatedvalue", "closeprobability", "estimatedclosedate"
).filter(
    "statecode eq 0"
).to_dataframe()

# Analyze with pandas
summary = df.groupby(df['estimatedclosedate'].dt.quarter).agg({
    'estimatedvalue': ['sum', 'mean', 'count']
})
```

---

## 5. Power Pages: SPA Mode

Power Pages introduces a Single-Page Application (SPA) framework for building modern, fast-loading portal experiences.

### SPA Mode Features

| Feature | Description |
|---------|-------------|
| **Client-side routing** | Navigate between pages without full reload |
| **Partial page updates** | Only changed content re-renders |
| **Preloading** | Linked pages prefetch in the background |
| **History management** | Browser back/forward works correctly |
| **Transition animations** | Smooth page-to-page transitions |

### Enabling SPA Mode

1. Open Power Pages design studio
2. Navigate to **Site settings**
3. Set `EnableSPA` to `true`
4. Configure `SPAPreloadStrategy` (eager, lazy, or viewport)

| Setting | Value | Behavior |
|---------|-------|----------|
| `EnableSPA` | true/false | Toggles SPA mode for the entire site |
| `SPAPreloadStrategy` | eager | Preloads all linked pages immediately |
| `SPAPreloadStrategy` | lazy | Preloads on hover/focus |
| `SPAPreloadStrategy` | viewport | Preloads links visible in the viewport |
| `SPATransition` | fade/slide/none | Page transition animation style |

### Web API Enhancements for SPA

Power Pages expands its client-side Web API:

```javascript
// Fetch Dataverse records client-side (no page reload)
const response = await fetch("/_api/contacts?$select=fullname,emailaddress1&$top=10", {
    headers: { "Accept": "application/json" }
});
const data = await response.json();
```

### Liquid + SPA Integration

SPA mode works alongside Liquid templates. Initial page render uses server-side Liquid, subsequent navigations fetch only the page content fragment and swap it into the shell.

---

## 6. AI-First Features

### Copilot Improvements Across Power Platform

| Product | Enhancement |
|---------|-------------|
| **Power Apps Copilot** | Generate entire multi-screen apps from natural language; edit existing apps via chat |
| **Power Automate Copilot** | Describe a flow in plain English to generate it; Copilot suggests next actions |
| **Copilot Studio** | Generative orchestration replaces rigid topic routing; agent reasons over tools |
| **Dataverse Copilot** | Create tables, columns, and relationships from natural language descriptions |
| **Power Pages Copilot** | Generate site layouts, forms, and styling from prompts |

### AI Builder Enhancements

| Feature | Status (2025) |
|---------|---------------|
| **Custom prompts** | GA -- build reusable GPT prompts with structured inputs/outputs |
| **Document automation** | GA -- extract fields from invoices, receipts, contracts |
| **Text generation** | GA -- generate summaries, emails, responses in flows |
| **Custom models with GPT** | GA -- fine-tune with your data for domain-specific tasks |
| **Prompt chaining** | GA -- pipe output of one prompt into another |

### AI Builder Prompt Example in Power Automate

```json
{
  "type": "AI Builder",
  "action": "Create text with GPT",
  "inputs": {
    "prompt": "Summarize this customer complaint and suggest a resolution:\n\n{{triggerBody()?['description']}}",
    "parameters": {
      "temperature": 0.3,
      "maxTokens": 500,
      "deploymentId": "gpt-4o"
    }
  }
}
```

### Generative Orchestration in Copilot Studio

Agents no longer rely solely on topic trigger phrases. With generative orchestration:

- The agent uses an LLM to understand intent and select the right topic/tool
- Multiple topics can be active in a single conversation turn
- Fallback behavior uses generative answers from knowledge sources
- No need to define exhaustive trigger phrases per topic

---

## 7. Dataverse Enhancements

### Elastic Tables (GA)

Elastic tables use Azure Cosmos DB as the backend for massive-scale, flexible-schema data.

| Aspect | Standard Tables | Elastic Tables |
|--------|----------------|----------------|
| **Scale** | Millions of rows | Billions of rows |
| **Schema** | Fixed columns | Flexible JSON columns |
| **Partitioning** | Automatic | Custom partition key required |
| **Transactions** | Full ACID | Within same partition |
| **Query** | Full OData | Partition-scoped queries preferred |
| **Use case** | Transactional CRM data | IoT, telemetry, logs, high-volume events |

### Creating an Elastic Table

```
make.powerapps.com > Tables > New table > Type: Elastic
Set partition key column (e.g., DeviceId, TenantId)
```

### Low-Code Plug-ins Improvements

| Improvement | Description |
|------------|-------------|
| **Dataverse Accelerator app** | Visual IDE for writing Power Fx plug-ins directly in browser |
| **Pre-operation support** | Plug-ins can now run before create/update commits |
| **Async plug-ins** | Fire-and-forget for non-critical post-processing |
| **Error handling** | Return custom error messages to calling apps |
| **Performance** | Sub-100ms execution for simple validations |

### Low-Code Plug-in Example

```powerfx
// Pre-validation plug-in on Account table (before create/update)
If(
    IsBlank(NewRecord.emailaddress1),
    Error("Email address is required for all accounts")
);

// Auto-calculate field
If(
    NewRecord.revenue > 1000000,
    Set(NewRecord.accountcategorycode, 1),  // Preferred Customer
    Set(NewRecord.accountcategorycode, 2)   // Standard
);
```

---

## 8. Power Automate Updates

### Process Mining (GA)

Process mining analyzes actual business processes by ingesting event logs from systems of record.

| Feature | Description |
|---------|-------------|
| **Ingestion** | Import CSV/event logs, connect to Dataverse, ERP, or custom sources |
| **Process map** | Auto-generated visual of actual process flow with variants |
| **Bottleneck detection** | Identifies steps with highest wait times |
| **Conformance checking** | Compares actual vs. ideal process model |
| **Recommendations** | Suggests automation opportunities |
| **KPIs** | Throughput, cycle time, rework rate dashboards |

### Automation Center

A centralized dashboard for managing all automation across the organization:

- View all cloud flows, desktop flows, and agents in one place
- Monitor execution health, failure rates, and SLA compliance
- Capacity management: see API request consumption per environment
- Alerts and notifications for flow failures or quota limits
- Role-based access for CoE admins and business process owners

### Agent Flows

A new flow type that bridges Power Automate and Copilot Studio:

```
Copilot Studio Agent
  └── Agent Flow (Power Automate)
        ├── Receive input from agent conversation
        ├── Execute business logic (connectors, data operations)
        ├── Return structured result to agent
        └── Agent presents result to user
```

- Agent flows appear as callable tools inside Copilot Studio
- Support both synchronous (wait for result) and asynchronous (fire-and-forget) patterns
- Full connector ecosystem available within agent flows
- Input/output schemas defined in the flow trigger

### Work Queues

Work queues provide a managed queue infrastructure for processing items:

| Feature | Description |
|---------|-------------|
| **Queue types** | Standard (FIFO), Priority, Deadline-based |
| **Processing** | Desktop flows, cloud flows, or agents dequeue and process items |
| **Retry** | Automatic retry with configurable backoff |
| **Monitoring** | Built-in dashboards for queue depth, processing rate, error rate |
| **Orchestration** | Load balance across multiple processors |

---

## 9. Governance and Administration Updates

### Managed Environments Enhancements

| Feature | Description |
|---------|-------------|
| **Sharing limits** | Restrict how many users an app can be shared with |
| **Solution checker enforcement** | Block deployments that fail solution checker rules |
| **Maker welcome content** | Custom onboarding message when makers enter the environment |
| **Usage insights** | Per-app and per-flow usage analytics |
| **Data policies** | Environment-level DLP in addition to tenant-level |
| **IP firewall** | Restrict Dataverse access to specific IP ranges |
| **Customer-managed keys** | Encrypt Dataverse data with your own encryption keys |

### Tenant Isolation

| Setting | Effect |
|---------|--------|
| **Inbound isolation** | Block external tenants from connecting to your Dataverse |
| **Outbound isolation** | Block your users from connecting to external Dataverse environments |
| **Allowlist** | Exempt specific partner tenants from isolation rules |
| **Cross-tenant connector blocking** | DLP policies can block connectors that reach external tenants |

### Power Platform Advisor

A built-in tool in the admin center that scans environments and provides actionable recommendations:

- Security posture assessment
- Licensing optimization suggestions
- Performance improvement opportunities
- Compliance gap identification
- Best practice adoption tracking

---

## 10. Developer Experience Improvements

### pac CLI Updates

| Command | Description |
|---------|-------------|
| `pac app create` | Scaffold a new code-first Power App |
| `pac agent init` | Initialize a Copilot Studio agent project locally |
| `pac solution sync` | Two-way sync between local files and Dataverse solution |
| `pac pipeline deploy` | Deploy solution through Power Platform pipelines |
| `pac admin backup` | Create environment backup from CLI |
| `pac auth create --managed-identity` | Authenticate with managed identity in CI/CD |
| `pac pcf push` | Hot-push PCF component changes during development |

### GitHub Integration

| Feature | Description |
|---------|-------------|
| **GitHub Actions for Power Platform** | Official actions for build, deploy, solution checker |
| **Source control sync** | Automatic export of solutions to Git repo on change |
| **PR validation** | Solution checker runs on pull requests |
| **Environment provisioning** | Create/delete environments as part of GitHub workflows |
| **Copilot Studio in Git** | Agent definitions stored as YAML in source control |

### GitHub Actions Workflow Example

```yaml
name: Deploy Power Platform Solution
on:
  push:
    branches: [main]
    paths: ['solutions/**']

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Power Platform CLI
        uses: microsoft/powerplatform-actions/install-pac@v1

      - name: Authenticate
        uses: microsoft/powerplatform-actions/who-am-i@v1
        with:
          environment-url: ${{ secrets.ENV_URL }}
          app-id: ${{ secrets.CLIENT_ID }}
          client-secret: ${{ secrets.CLIENT_SECRET }}
          tenant-id: ${{ secrets.TENANT_ID }}

      - name: Pack solution
        uses: microsoft/powerplatform-actions/pack-solution@v1
        with:
          solution-folder: solutions/ContosoApp
          solution-file: out/ContosoApp.zip
          solution-type: Managed

      - name: Deploy solution
        uses: microsoft/powerplatform-actions/import-solution@v1
        with:
          environment-url: ${{ secrets.PROD_ENV_URL }}
          app-id: ${{ secrets.CLIENT_ID }}
          client-secret: ${{ secrets.CLIENT_SECRET }}
          tenant-id: ${{ secrets.TENANT_ID }}
          solution-file: out/ContosoApp.zip
          force-overwrite: true
```

---

## 11. Additional Notable Features

### Power Apps

| Feature | Description |
|---------|-------------|
| **Named formulas (GA)** | `App.Formulas` for declarative, auto-recalculating values |
| **User-defined functions** | Reusable Power Fx functions within an app |
| **ParseJSON improvements** | Strongly-typed JSON parsing with Untyped Object enhancements |
| **Modern controls GA** | Fluent UI-based controls replace classic controls |
| **Responsive containers** | Auto-layout containers for all screen sizes |
| **Offline enhancements** | LoadData/SaveData improvements, conflict resolution UI |
| **Card-based controls** | New card layout components for galleries and lists |

### Power Automate

| Feature | Description |
|---------|-------------|
| **Hosted RPA (GA)** | Microsoft-hosted machines for desktop flows, no VM management |
| **AI Recorder** | Record desktop actions with AI-assisted element identification |
| **Flow error analytics** | Aggregated error patterns and suggested fixes |
| **Reusable flow components** | Child flows with typed inputs/outputs |
| **Natural language to flow** | Copilot generates complete flows from descriptions |

### Dataverse

| Feature | Description |
|---------|-------------|
| **Long-term data retention** | Archive old records to reduce active DB size and cost |
| **Dataverse file storage** | Managed file/image columns with up to 10 GB per record |
| **Virtual tables enhancements** | Better support for SQL Server, Cosmos DB, and custom providers |
| **Business events** | Publish Dataverse events to Azure Event Grid or Service Bus |
| **Calculated/rollup perf** | Improved recalculation engine, near real-time rollups |

### Copilot Studio

| Feature | Description |
|---------|-------------|
| **Knowledge management** | Unified knowledge sources across SharePoint, web, Dataverse, and files |
| **Generative actions** | Agent dynamically selects and invokes connector actions |
| **Agent analytics** | Conversation quality, resolution rate, and escalation metrics |
| **Multi-language GA** | Single agent serves conversations in 50+ languages |
| **Voice channel** | Agents can handle voice calls via Dynamics 365 Contact Center |

---

## Version and Timeline Summary

| Wave | Period | Key Theme |
|------|--------|-----------|
| **2025 Wave 1** | Apr-Sep 2025 | AI-first development, MCP integration, code-first apps |
| **2025 Wave 2** | Oct 2025-Mar 2026 | Autonomous agents, Python SDK, SPA pages, process mining GA |

> Features tagged GA are generally available. Features tagged Preview require opt-in via admin center. Check release plans for current status of each feature.
