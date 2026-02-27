# Microsoft Power Platform

---
description: Build Power Apps (canvas + model-driven), Power Automate flows, Dataverse schemas, Power Pages portals, Copilot Studio agents, PCF components, and AI Builder solutions. Covers Power Fx formulas, delegation, ALM, connectors, security, and administration.
triggers:
  - power platform
  - power apps
  - power app
  - canvas app
  - model-driven app
  - model driven app
  - dataverse
  - power automate
  - power fx
  - power pages
  - copilot studio
  - power virtual agents
  - pcf component
  - ai builder
  - power platform connector
  - sharepoint form
  - dynamics 365
  - business process flow
  - approval flow
  - cloud flow
  - desktop flow
  - dataverse table
  - dataverse column
  - dataverse relationship
  - solution aware
  - environment variable
  - connection reference
  - delegation
  - collect filter lookup
  - patch submit form
  - gallery form screen
  - navigate set updatecontext
  - low-code
  - citizen developer
  - power platform alm
  - power platform governance
---

## 1. Decision Tree: Choose the Right Tool

```
What are you building?
|
+-- Data entry/management app for INTERNAL users?
|   |
|   +-- Complex data model with relationships, security roles, BPFs?
|   |   --> MODEL-DRIVEN APP (Workflow 2)
|   |
|   +-- Custom UX, pixel-perfect design, specific layout?
|       --> CANVAS APP (Workflow 1)
|
+-- Data entry/management for EXTERNAL users (customers, partners)?
|   --> POWER PAGES portal (Workflow 6)
|
+-- Automate a business process?
|   |
|   +-- Triggered by events (email, SharePoint, Dataverse)?
|   |   --> AUTOMATED CLOUD FLOW (Workflow 4)
|   |
|   +-- Triggered on schedule?
|   |   --> SCHEDULED CLOUD FLOW (Workflow 4)
|   |
|   +-- Triggered manually / from app?
|   |   --> INSTANT CLOUD FLOW (Workflow 4)
|   |
|   +-- Automate legacy desktop/web app (RPA)?
|       --> DESKTOP FLOW (Workflow 4)
|
+-- Build a chatbot / conversational agent?
|   --> COPILOT STUDIO (Workflow 7)
|
+-- Add AI capabilities (text analysis, document processing)?
|   --> AI BUILDER (Workflow 5)
|
+-- Custom UI component for existing app?
    --> PCF COMPONENT (ref: pcf-component-framework.md)
```

### Data Source Selection

| Scenario | Data Source | Notes |
|----------|-----------|-------|
| Enterprise data, relationships, security | **Dataverse** | Default choice for Power Platform |
| Already in SharePoint | **SharePoint** | Delegation limits apply; 5K threshold |
| Already in SQL Server | **SQL Server** | Full delegation support |
| Simple lists, small data | **Excel Online** | Max ~2K rows practical |
| External REST API | **Custom Connector** | OpenAPI 2.0 definition required |
| SAP, Salesforce, etc. | **Premium Connector** | Check connector catalog |

## 2. Workflow 1: Canvas App

> Load reference: [references/canvas-apps-complete.md](references/canvas-apps-complete.md)
> Load reference: [references/canvas-controls-reference.md](references/canvas-controls-reference.md)

### Step 1: Create the App
- **From data**: Start with a Dataverse table or SharePoint list (auto-generates browse/detail/edit screens)
- **From blank**: Tablet (1366x768) or Phone (640x1136) layout
- **From Copilot**: Describe app in natural language; AI generates initial screens

### Step 2: Connect Data Sources
- Add connections in Data panel (left sidebar)
- Dataverse tables, SharePoint lists, SQL, Excel, connectors
- For Dataverse: tables appear directly; use `LookUp`, `Filter`, `Search` to query

### Step 3: Build Screens
Common screen pattern (3+ screens):
1. **Browse Screen**: Gallery control bound to data source with search
2. **Detail Screen**: Display form showing selected record
3. **Edit Screen**: Edit form for create/update

Navigation pattern:
```
// Browse -> Detail (on gallery item select)
Navigate(DetailScreen, ScreenTransition.None, {SelectedItem: ThisItem})

// Detail -> Edit
Navigate(EditScreen, ScreenTransition.None, {EditRecord: varSelectedItem})

// Edit -> Browse (after save)
SubmitForm(EditForm1); Back()
```

### Step 4: Key Formulas
```
// App.OnStart - initialize
Set(varCurrentUser, User());
ClearCollect(colDepartments, Departments);

// Gallery.Items with search
SortByColumns(
    Filter(Accounts,
        StartsWith(Name, TextSearchBox.Text)
    ),
    "Name", SortOrder.Ascending
)

// Form submission
SubmitForm(EditForm1);
// In Form.OnSuccess:
Notify("Saved successfully", NotificationType.Success);
Navigate(BrowseScreen, ScreenTransition.None);
```

### Step 5: Delegation Rules

> Load reference: [references/power-fx-language.md](references/power-fx-language.md)

**CRITICAL**: Non-delegable operations only process first 500 (default) or 2000 (max) rows.

| Delegable to Dataverse | NOT Delegable |
|----------------------|---------------|
| `Filter` with =, <>, <, >, <=, >= | `Search` (use `Filter` + `StartsWith` instead) |
| `Sort`, `SortByColumns` | `First`, `Last` on filtered results |
| `Lookup` | `CountRows` on large tables |
| `StartsWith` | `in` operator |
| `Sum`, `Min`, `Max`, `Avg` | `Distinct`, `GroupBy` |
| Dataverse, SQL Server | SharePoint (limited), Excel (none) |

Blue underline warning in formula bar = delegation issue.

### Step 6: Variables

| Type | Set With | Scope | Use Case |
|------|---------|-------|----------|
| Global | `Set(varName, value)` | Entire app | User info, current record |
| Context | `UpdateContext({var: value})` | Current screen | Form state, UI toggles |
| Collection | `ClearCollect(colName, source)` | Entire app | Cached data, temp tables |

### Step 7: Components
Create reusable components with custom input/output properties:
- Component library for cross-app sharing
- Define custom properties (Input/Output/Function/Action/Event)
- Use `Self.PropertyName` to reference inside component

### Step 8: Responsive Design
Use containers for responsive layouts:
- **Horizontal Container**: `LayoutDirection.Horizontal`, child `LayoutMinWidth`
- **Vertical Container**: `LayoutDirection.Vertical`, child `LayoutMinHeight`
- Set `Fill portions` for flexible sizing (like CSS flexbox)
- Use `LayoutOverflowY: Scroll` for scrollable content

### Step 9: Publish & Share
1. Save (Ctrl+S) -> Publish -> Share
2. Assign security roles or share with specific users
3. Set co-owners for management access

## 3. Workflow 2: Model-Driven App

> Load reference: [references/model-driven-apps-complete.md](references/model-driven-apps-complete.md)

### Step 1: Design Data Model First
Model-driven apps are data-first. Design your Dataverse tables, columns, and relationships before building the app (see Workflow 3).

### Step 2: Create App in App Designer
1. Go to make.powerapps.com > Solutions > your solution
2. New > App > Model-driven app
3. Add **Tables** (each gets auto-generated forms/views)
4. Add **Pages**: table-based, custom (canvas), dashboard, or Copilot

### Step 3: Configure Forms
Main form layout sections:
- **Header**: Key fields visible at all times
- **Tabs**: Organize related fields (General, Details, Related)
- **Sections**: Group fields within tabs (1-4 columns)
- **Sub-grids**: Show related records inline
- **Quick View**: Display lookup record details
- **Timeline**: Activities and notes

Form types: Main, Quick Create (modal), Quick View (read-only embed), Card.

### Step 4: Configure Views
- **Active Records**: Default view showing current records
- **All Records**: Include inactive
- **Quick Find**: Search-optimized view (configure searchable columns)
- **Lookup Views**: Used when selecting related records
- Filter criteria, column selection, sort order all configurable

### Step 5: Business Rules
No-code conditional logic on forms:
- Show/hide fields, set required/optional, set default values
- Lock/unlock fields based on conditions
- Show error messages
- Scope: Form (client-side) or Table (server-side, applies to all)

### Step 6: Commanding (Ribbon)
- Modern commanding: Power Fx-based command bar buttons
- Visibility rules, enabled rules, actions
- `OnSelect` uses Power Fx (e.g., `Patch`, `Navigate`)

### Step 7: Embed Canvas App
Embed canvas apps within model-driven forms for custom UI:
- Pass `ModelDrivenFormIntegration.Item` to canvas app
- Access parent record fields in canvas app
- Return data via output properties

## 4. Workflow 3: Dataverse Schema Design

> Load reference: [references/dataverse-data-modeling.md](references/dataverse-data-modeling.md)
> Load reference: [references/dataverse-business-logic.md](references/dataverse-business-logic.md)
> Load reference: [references/dataverse-security-admin.md](references/dataverse-security-admin.md)

### Step 1: Plan Tables

| Table Type | Use Case |
|-----------|----------|
| **Standard** | Custom business entities (Projects, Products, Orders) |
| **Activity** | Entities with timeline support (Tasks, Appointments) |
| **Virtual** | Read-only from external source (no Dataverse storage) |
| **Elastic** | High-volume IoT/log data (Azure Cosmos DB backend) |

Naming: Use publisher prefix (e.g., `cr123_Project`). Avoid changing after creation.

### Step 2: Define Columns

| Power Apps Type | API Type | Use For |
|----------------|---------|---------|
| Single line text | String (max 4000) | Names, titles, codes |
| Multiple lines | Memo (max 1M) | Descriptions, notes |
| Whole Number | Integer | Counts, quantities |
| Decimal | Decimal (0-10 precision) | Precise calculations |
| Currency | Money | Financial values (auto-creates exchange fields) |
| Date/Time | DateTime | Dates (User Local, Date Only, or Time Zone Independent) |
| Choice | Picklist | Single selection from options |
| Choices | MultiSelectPicklist | Multiple selections |
| Yes/No | Boolean | Toggle flags |
| Lookup | Lookup | Foreign key to another table |
| File | File (max 10GB) | Document attachments |
| Image | Image | Photos, thumbnails |
| Formula | Uses Power Fx | Calculated at read time (no delegation) |
| Calculated | Calculated | Server-computed on save |
| Rollup | Rollup | Aggregates child records (refreshed every 12h or on-demand) |

### Step 3: Create Relationships

| Type | Example | Key Property |
|------|---------|-------------|
| **One-to-Many (1:N)** | Account -> Contacts | Lookup column on child |
| **Many-to-Many (N:N)** | Students <-> Courses | Intersect table auto-created |

Cascade behaviors (on parent action): Cascade All, Cascade Active, Cascade User-Owned, Cascade None, Remove Link, Restrict.

### Step 4: Security Model
1. **Security Roles**: Assign CRUD permissions per table at org/BU/user levels
2. **Column-Level Security**: Restrict sensitive fields via field security profiles
3. **Hierarchy Security**: Manager can see direct reports' records
4. **Row-Level Security**: Owner-based or team-based access

### Step 5: Business Logic Options

| Method | Use Case | Runs |
|--------|---------|------|
| Business Rules | Simple field-level logic on forms | Client + Server |
| Low-Code Plug-ins (Power Fx) | Server-side validation, calculated updates | Server |
| Real-time Workflows | Multi-step automation on record events | Server |
| Power Automate | Complex integrations, approvals | Async |
| Classic Plug-ins (C#) | Complex server-side logic | Server |

## 5. Workflow 4: Power Automate

> Load reference: [references/power-automate-cloud-flows.md](references/power-automate-cloud-flows.md)
> Load reference: [references/power-automate-expressions.md](references/power-automate-expressions.md)
> Load reference: [references/power-automate-desktop-flows.md](references/power-automate-desktop-flows.md)
> Load reference: [references/power-automate-integrations.md](references/power-automate-integrations.md)

### Flow Type Selection

| Type | Trigger | Example |
|------|---------|---------|
| Automated | Event occurs | "When an item is created" in SharePoint |
| Scheduled | Time-based | "Every day at 8 AM" |
| Instant | Button press | "Manually trigger a flow" |
| Desktop | From cloud flow or manual | Automate legacy Win32 app |

### Key Actions

| Action | Purpose |
|--------|---------|
| Condition | If/then/else branching |
| Apply to each | Loop over array items |
| Compose | Create/transform data inline |
| Parse JSON | Extract typed properties from JSON |
| Select | Map array to new shape |
| Filter array | Filter client-side array |
| Scope | Group actions for try/catch |
| HTTP | Call any REST API |

### Error Handling Pattern (Try-Catch)
```
[Trigger]
  |
[Try Scope] -- main business logic
  |
[Catch Scope] -- "Run after" Try: has failed
  |  -> Filter array: result('Try') where status eq 'Failed'
  |  -> Send error notification
  |  -> Terminate (Failed)
  |
[Finally Scope] -- "Run after" Catch: succeeded OR failed OR skipped
```

### Expression Cheat Sheet
```
// String
concat('Hello ', triggerBody()?['name'])
toLower(variables('email'))
substring(variables('text'), 0, 10)

// Date
utcNow()
addDays(utcNow(), 7)
formatDateTime(utcNow(), 'yyyy-MM-dd')

// Conditional
if(equals(triggerBody()?['status'], 'Active'), 'Yes', 'No')
coalesce(triggerBody()?['name'], 'Unknown')

// Array/Object
length(body('Get_items')?['value'])
first(body('Get_items')?['value'])
json(variables('jsonString'))
```

### Approval Pattern
```
Trigger -> Start and wait for an approval (Approve/Reject - First to respond)
  -> Condition: Outcome eq 'Approve'
    -> Yes: Update record (Approved), notify requester
    -> No: Update record (Rejected), notify requester
```

### Child Flows
- Must be in same solution
- Trigger: "Manually trigger a flow"
- Return data: "Respond to a Power App or flow"
- Call via: "Run a Child Flow" action
- Connections must be embedded (not run-only user)

## 6. Workflow 5: AI Integration

> Load reference: [references/ai-builder-guide.md](references/ai-builder-guide.md)
> Load reference: [references/copilot-ai-features.md](references/copilot-ai-features.md)

### AI Builder Models

| Model | Input | Output | Use Case |
|-------|-------|--------|----------|
| Document Processing | PDF/image | Extracted fields | Invoice, receipt processing |
| Object Detection | Image | Detected objects + locations | Inventory, inspection |
| Text Classification | Text | Category labels | Support ticket routing |
| Entity Extraction | Text | Named entities | Contact info extraction |
| Sentiment Analysis | Text | Positive/Negative/Neutral | Customer feedback |
| Prediction | Dataverse data | Binary/multi outcome | Churn prediction |

### AI Functions in Power Fx
```
// Sentiment analysis
AISentiment("Great product, love it!")  // Returns 1 (positive)

// Summarize text
AISummarize(TextInput.Text)

// Classify into categories
AIClassify(TextInput.Text, ["Billing", "Technical", "General"])

// Extract structured data
AIExtract(TextInput.Text, {Name: "", Email: "", Phone: ""})

// Translate
AITranslate(TextInput.Text, "fr")

// Generate reply
AIReply(EmailBody.Text, {Tone: "Professional"})
```

### Prompts (GPT Builder)
Custom AI prompts in AI Builder:
1. Create prompt with instructions and dynamic inputs
2. Use in Power Automate: "Create text with GPT" action
3. Use in Power Apps: add AI Builder model to app
4. Grounding: optionally connect to Dataverse/documents for RAG

## 7. Workflow 6: Power Pages

> Load reference: [references/power-pages-guide.md](references/power-pages-guide.md)

### Step 1: Create Site
1. Go to make.powerpages.microsoft.com
2. Select environment (avoid default)
3. Choose template or start from blank
4. Set site name and URL

### Step 2: Add Pages
- Use Design Studio Pages workspace
- Add components: Text, Form, List, Multistep Form, Button, Image
- Set page hierarchy (parent/child) for URL structure

### Step 3: Display Data with Lists
- Select Dataverse table + model-driven views
- Configure search, pagination, filtering
- Link to detail page via "Web Page for Details View"

### Step 4: Collect Data with Forms
- **Basic Form**: Single-step (Insert/Edit/ReadOnly mode)
- **Multistep Form**: Multi-step wizard with branching
- Configure success actions: display message or redirect

### Step 5: Security
- **Table Permissions**: CRUD per table, scoped by Global/Contact/Account/Self
- **Page Permissions**: Restrict Read or Grant Change per web role
- **Web Roles**: Assign to authenticated/anonymous users
- **Authentication**: Entra ID, Azure AD B2C, Google, Facebook, local

### Step 6: Liquid Templating
```liquid
{% if user %}
  Welcome, {{ user.fullname | escape }}!
{% else %}
  Please sign in.
{% endif %}

{% fetchxml query %}
<fetch><entity name="account">
  <attribute name="name"/>
</entity></fetch>
{% endfetchxml %}
{% for item in query.results.entities %}
  {{ item.name | escape }}
{% endfor %}
```

### Step 7: Web API (Client-Side CRUD)
```
Endpoint: [Site URL]/_api/<EntitySetName>
Methods: GET, POST, PATCH, DELETE
Auth: Portal session + __RequestVerificationToken (CSRF)
```

## 8. Workflow 7: Copilot Studio

> Load reference: [references/copilot-studio-guide.md](references/copilot-studio-guide.md)

### Step 1: Create Agent
1. Go to copilotstudio.microsoft.com
2. Describe what the agent should do (up to 1,024 chars)
3. Configure name (max 42 chars), instructions (up to 8,000 chars)
4. Add knowledge sources (websites, SharePoint, Dataverse, documents)

### Step 2: Choose Orchestration Mode

| Feature | Generative | Classic |
|---------|-----------|---------|
| Topic selection | By description match | By trigger phrases |
| Tool calling | Auto-selects tools | Explicit from topics |
| Knowledge | Proactive search | Fallback only |
| Multi-intent | Yes (chains tools/topics) | No (single topic) |
| Missing info | Auto-generates questions | Requires authored nodes |

### Step 3: Author Topics
Topics define conversation flows with nodes:
- **Message**: Send text/cards to user
- **Question**: Ask and store response in variable
- **Condition**: Branch on variable values
- **Tool**: Call Power Automate, connector, REST API, MCP server
- **Adaptive Card**: Interactive JSON-based UI

### Step 4: Add Knowledge Sources
- Public websites (up to 25 URLs)
- SharePoint (up to 25 URLs, Entra ID auth)
- Dataverse tables (unlimited)
- Uploaded documents (stored in Dataverse)
- Web search via Bing Grounding

### Step 5: Publish & Deploy
1. Publish from top menu bar
2. Connect channels: Teams, custom website (iframe), SharePoint, Facebook, WhatsApp
3. For Teams: install for self, share link, or submit for admin approval

## 9. Workflow 8: ALM & Deployment

> Load reference: [references/alm-solutions-devops.md](references/alm-solutions-devops.md)
> Load reference: [references/administration-governance.md](references/administration-governance.md)

### Solution Strategy
- **Unmanaged**: Development only; fully editable
- **Managed**: Production deployment; can't edit directly
- Use publisher prefix consistently (e.g., `contoso_`)

### Environment Strategy
```
DEV (unmanaged) -> TEST/QA (managed) -> PROD (managed)
```

### Export/Import Flow
1. Develop in DEV environment (unmanaged solution)
2. Export as managed solution (.zip)
3. Import to TEST environment
4. Validate and test
5. Import to PROD environment

### CI/CD with GitHub Actions
```yaml
# .github/workflows/deploy.yml
- uses: microsoft/powerplatform-actions/export-solution@v1
  with:
    solution-name: MySolution
    solution-output-file: solution.zip
- uses: microsoft/powerplatform-actions/import-solution@v1
  with:
    environment-url: https://target.crm.dynamics.com
    solution-file: solution.zip
```

### Connection References & Environment Variables
- **Connection References**: Abstract connections; map during import
- **Environment Variables**: Store config values (URLs, IDs, secrets via Key Vault)
- Both enable environment-independent solutions

## 10. Quick Reference: Power Fx Top Functions

> Full reference: [references/power-fx-functions-reference.md](references/power-fx-functions-reference.md)
> Patterns: [references/power-fx-patterns.md](references/power-fx-patterns.md)

### Data Operations
| Function | Purpose | Example |
|----------|---------|---------|
| `Filter` | Query records (delegable) | `Filter(Accounts, Status = "Active")` |
| `LookUp` | Get single record (delegable) | `LookUp(Contacts, ID = varID)` |
| `Search` | Text search (NOT delegable) | `Search(Products, SearchBox.Text, "Name")` |
| `Sort` / `SortByColumns` | Order records | `SortByColumns(Items, "Date", SortOrder.Descending)` |
| `Patch` | Create/update record | `Patch(Accounts, Defaults(Accounts), {Name: "New"})` |
| `Remove` | Delete record | `Remove(Accounts, LookUp(Accounts, ID = varID))` |
| `Collect` | Add to collection | `Collect(colCart, {Product: "Widget", Qty: 1})` |
| `ClearCollect` | Replace collection | `ClearCollect(colItems, Filter(Items, Active))` |
| `Distinct` | Unique values | `Distinct(Contacts, Department)` |
| `AddColumns` | Add computed columns | `AddColumns(Orders, "Total", Price * Qty)` |
| `GroupBy` | Group + aggregate | `GroupBy(Sales, "Region", "RegionSales")` |
| `ForAll` | Iterate + action | `ForAll(colItems, Patch(Items, ThisRecord, {Status: "Done"}))` |

### Form Operations
| Function | Purpose |
|----------|---------|
| `SubmitForm(form)` | Save form data to data source |
| `ResetForm(form)` | Reset form to default values |
| `NewForm(form)` | Switch form to Insert mode |
| `EditForm(form)` | Switch form to Edit mode |
| `ViewForm(form)` | Switch form to View mode |

### Navigation & UI
| Function | Purpose |
|----------|---------|
| `Navigate(screen, transition)` | Go to screen |
| `Back()` | Return to previous screen |
| `Set(var, value)` | Set global variable |
| `UpdateContext({var: value})` | Set context variable |
| `Notify(message, type)` | Show notification bar |
| `Launch(url)` | Open URL in browser |
| `Concurrent(fn1, fn2, ...)` | Run operations in parallel |

### Text
| Function | Example |
|----------|---------|
| `Concatenate` / `&` | `"Hello " & User().FullName` |
| `Text(value, format)` | `Text(Now(), "yyyy-mm-dd")` |
| `Value(string)` | `Value("42")` -> 42 |
| `Left` / `Mid` / `Right` | `Left("Hello", 3)` -> "Hel" |
| `Upper` / `Lower` / `Proper` | `Proper("john doe")` -> "John Doe" |
| `Substitute` | `Substitute(name, " ", "_")` |
| `Split` | `Split("a,b,c", ",")` -> table |
| `IsMatch` | `IsMatch(email, Match.Email)` |

## 11. Quick Reference: Controls

> Full reference: [references/canvas-controls-reference.md](references/canvas-controls-reference.md)

| Control | Key Properties | Common Use |
|---------|---------------|------------|
| **Gallery** | Items, TemplateFill, OnSelect | Browse lists of records |
| **Edit Form** | DataSource, Item, OnSuccess | Create/edit records |
| **Display Form** | DataSource, Item | Read-only record view |
| **Text Input** | Default, HintText, OnChange | User text entry |
| **Dropdown** | Items, Default, OnChange | Single selection |
| **ComboBox** | Items, DefaultSelectedItems, SelectMultiple | Multi-select with search |
| **Date Picker** | DefaultDate, OnChange | Date selection |
| **Button** | OnSelect, Text, DisplayMode | Trigger actions |
| **Label** | Text, Font, Color | Display text/values |
| **Image** | Image (URL/media), OnSelect | Display images |
| **Container** | Flexible height/width | Group controls |
| **Horizontal Container** | LayoutDirection, Gap, Padding | Responsive row layout |
| **Vertical Container** | LayoutDirection, Gap, Padding | Responsive column layout |
| **Data Table** | Items, columns auto-detect | Quick read-only grid |
| **Toggle** | Default, OnChange | Boolean switch |
| **Checkbox** | Default, OnCheck, OnUncheck | Multi-selection |
| **Rich Text Editor** | Default, HtmlText | Formatted text input |

## 12. Reference Files Index

### App Development
| File | Content |
|------|---------|
| [canvas-apps-complete.md](references/canvas-apps-complete.md) | Canvas app creation, data binding, variables, components, responsive, offline, performance |
| [canvas-controls-reference.md](references/canvas-controls-reference.md) | All canvas controls with properties, events, and usage patterns |
| [model-driven-apps-complete.md](references/model-driven-apps-complete.md) | Model-driven app design, forms, views, charts, dashboards, commanding |

### Data Platform
| File | Content |
|------|---------|
| [dataverse-data-modeling.md](references/dataverse-data-modeling.md) | Tables, columns, relationships, solutions, virtual/elastic tables |
| [dataverse-business-logic.md](references/dataverse-business-logic.md) | Business rules, low-code plug-ins, workflows, actions |
| [dataverse-security-admin.md](references/dataverse-security-admin.md) | Security roles, field security, hierarchy, DLP, environments |

### Power Fx
| File | Content |
|------|---------|
| [power-fx-language.md](references/power-fx-language.md) | Data types, operators, tables, delegation, named formulas, UDFs, error handling |
| [power-fx-functions-reference.md](references/power-fx-functions-reference.md) | Complete function reference A-Z with signatures and examples |
| [power-fx-patterns.md](references/power-fx-patterns.md) | Common formula patterns, cascading dropdowns, bulk operations |

### Automation
| File | Content |
|------|---------|
| [power-automate-cloud-flows.md](references/power-automate-cloud-flows.md) | Triggers, actions, conditions, approvals, child flows, BPFs |
| [power-automate-desktop-flows.md](references/power-automate-desktop-flows.md) | Desktop automation, recording, variables, web/UI/Excel actions |
| [power-automate-expressions.md](references/power-automate-expressions.md) | Workflow Definition Language functions, expression patterns |
| [power-automate-integrations.md](references/power-automate-integrations.md) | Dataverse, SharePoint, Teams, Outlook, HTTP connector patterns |

### AI & Copilot
| File | Content |
|------|---------|
| [ai-builder-guide.md](references/ai-builder-guide.md) | AI models, document processing, prompts, confidence scores, model lifecycle, Azure OpenAI integration |
| [copilot-ai-features.md](references/copilot-ai-features.md) | Copilot in Power Apps/Automate, AI Functions in Power Fx, prompt engineering, governance |

### Developer
| File | Content |
|------|---------|
| [pcf-component-framework.md](references/pcf-component-framework.md) | PCF lifecycle, manifest, React/Fluent controls, dataset components, debugging, canvas support |
| [dataverse-developer-api.md](references/dataverse-developer-api.md) | Web API (OData), FetchXML, batch ops, change tracking, elastic tables, plug-ins, file/image columns |
| [custom-connectors.md](references/custom-connectors.md) | OpenAPI definition, OAuth2 patterns, policy templates, testing, certification |
| [client-scripting-mda.md](references/client-scripting-mda.md) | formContext API, Client API reference, Xrm namespace, web resources, ribbon JS, events |

### Platform
| File | Content |
|------|---------|
| [alm-solutions-devops.md](references/alm-solutions-devops.md) | Solutions, managed/unmanaged, CI/CD, GitHub Actions, pipelines |
| [connectors-catalog.md](references/connectors-catalog.md) | Standard/premium connectors, top connectors detail, throttling, on-premises gateway |
| [administration-governance.md](references/administration-governance.md) | Environments, licensing, DLP, CoE, tenant management |
| [licensing-governance.md](references/licensing-governance.md) | License matrix, DLP policies, managed environments, CoE Starter Kit, capacity |
| [testing-monitoring.md](references/testing-monitoring.md) | Test Studio, Monitor tool, Solution Checker, automated testing, Application Insights |
| [performance-optimization.md](references/performance-optimization.md) | Delegation patterns, concurrent ops, caching, batch processing, API limits |
| [well-architected-patterns.md](references/well-architected-patterns.md) | Reliability, security, performance, operational excellence patterns |

### External Facing
| File | Content |
|------|---------|
| [power-pages-guide.md](references/power-pages-guide.md) | Portal creation, Liquid, lists, forms, table permissions, Web API |
| [copilot-studio-guide.md](references/copilot-studio-guide.md) | Agent creation, topics, triggers, generative AI, channels, auth |

### New Features & Updates
| File | Content |
|------|---------|
| [2025-2026-new-features.md](references/2025-2026-new-features.md) | MCP servers, autonomous agents, Code apps, Python SDK, SPA Power Pages, AI-first features |

## 13. 2025-2026 Feature Highlights

> Full reference: [references/2025-2026-new-features.md](references/2025-2026-new-features.md)

### Key New Capabilities

| Feature | Product | Status |
|---------|---------|--------|
| **MCP Server connectors** | Copilot Studio | GA 2025 Wave 2 |
| **Autonomous agents** | Copilot Studio | GA 2025 Wave 1 |
| **Agent builder** | Power Platform | Preview 2025 |
| **AI Functions in Power Fx** | Power Apps | GA 2025 Wave 1 |
| **Code-first components** | Power Apps | Preview 2025 |
| **Python SDK for Dataverse** | Dataverse | Preview 2025 |
| **SPA framework** | Power Pages | GA 2025 Wave 2 |
| **Elastic tables GA** | Dataverse | GA 2025 |
| **Process mining GA** | Power Automate | GA 2025 Wave 1 |
| **Managed environments v2** | Admin | GA 2025 Wave 1 |
| **Pay-as-you-go** | Platform | GA |
| **Copilot in Power Automate** | Power Automate | GA 2025 |

### Quick References for New Features

- **MCP in Copilot Studio**: Topics > Tool node > Add MCP server URL > Auto-discovers tools
- **Autonomous agents**: Copilot Studio > Agents > New > Configure triggers + actions + long-running behavior
- **AI Functions**: `AISentiment()`, `AISummarize()`, `AIClassify()`, `AIExtract()`, `AITranslate()`, `AIReply()` — call directly from Power Fx formula bar
- **Performance optimization**: Load ref [performance-optimization.md](references/performance-optimization.md) for delegation patterns, caching, API limits
- **Testing**: Load ref [testing-monitoring.md](references/testing-monitoring.md) for Test Studio, Monitor, Solution Checker
- **Licensing**: Load ref [licensing-governance.md](references/licensing-governance.md) for license matrix, DLP, managed environments
