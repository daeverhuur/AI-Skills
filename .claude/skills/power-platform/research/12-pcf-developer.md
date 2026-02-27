# PCF & Power Platform Developer APIs Reference

> Research compiled from Microsoft Learn documentation (25 pages).
> Sources: learn.microsoft.com/en-us/power-apps/developer/

---

## 1. PCF (Power Apps Component Framework)

### Overview

PCF enables professional developers to create **code components** for model-driven and canvas apps. Unlike HTML web resources, code components render as part of the same context and load simultaneously with other components, providing a seamless UX.

**Component types:**

| Type | `control-type` | Interface | DOM Container |
|------|---------------|-----------|---------------|
| Standard | `standard` | `StandardControl<IInputs, IOutputs>` | Receives empty `div` in `init()` |
| React/Virtual | `virtual` | `ReactControl<IInputs, IOutputs>` | No `div`; returns `ReactElement` from `updateView()` |

**Property binding types:**

| Usage | Description |
|-------|-------------|
| `bound` | Bound to a column value |
| `input` | Bound to a column or allows a static value |

### Component Lifecycle

```
init() --> updateView() --> [user interaction] --> getOutputs() --> updateView() --> ... --> destroy()
```

| Method | Purpose |
|--------|---------|
| `init(context, notifyOutputChanged, state, container)` | One-time initialization. Set up DOM, event listeners, store references. |
| `updateView(context)` | Called when any property bag value changes (field values, datasets, container resize, metadata). |
| `getOutputs()` | Called by framework to retrieve output values. Return object matching `IOutputs` interface. |
| `destroy()` | Cleanup: remove event listeners, cancel remote calls. |

**StandardControl lifecycle (TypeScript):**

```typescript
export class MyControl implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  private _value: number;
  private _notifyOutputChanged: () => void;
  private _container: HTMLDivElement;
  private _context: ComponentFramework.Context<IInputs>;

  constructor() {}

  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ): void {
    this._context = context;
    this._notifyOutputChanged = notifyOutputChanged;
    // Create DOM elements, attach to container
  }

  public updateView(context: ComponentFramework.Context<IInputs>): void {
    this._value = context.parameters.myProperty.raw!;
  }

  public getOutputs(): IOutputs {
    return { myProperty: this._value };
  }

  public destroy(): void {
    // Remove event listeners
  }
}
```

**ReactControl lifecycle:**

```typescript
export class MyReactControl implements ComponentFramework.ReactControl<IInputs, IOutputs> {
  public init(context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void, state: ComponentFramework.Dictionary): void { }

  public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
    return React.createElement(MyComponent, { value: context.parameters.myProp.raw });
  }

  public getOutputs(): IOutputs { return {}; }
  public destroy(): void { }
}
```

### React Controls and Platform Libraries

React controls use the platform's shared React and Fluent UI libraries instead of bundling their own. Benefits include reduced bundle size, optimized packaging, faster runtime rendering, and theme alignment with Power Apps Fluent design system. Create with `pac pcf init -fw react`. The `control-type` in the manifest is `virtual`. Platform libraries (React 16.14.0, Fluent 8/9) are declared in `<platform-library>` elements within `<resources>`.

**Supported platform library versions:**

| Name | npm Package | Version Loaded |
|------|-------------|---------------|
| React | react | 17.0.2 (Model) / 16.14.0 (Canvas) |
| Fluent 8 | @fluentui/react | 8.29.0 or 8.121.1 |
| Fluent 9 | @fluentui/react-components | 9.68.0 |

React controls cannot be used in Power Pages. Fluent 8 and 9 cannot both be in the same manifest.

### Manifest Schema (ControlManifest.Input.xml)

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace"
    constructor="MyControl"
    version="1.0.0"
    display-name-key="MyControl_Display"
    description-key="MyControl_Desc"
    control-type="standard">

    <type-group name="numbers">
      <type>Whole.None</type>
      <type>Currency</type>
      <type>FP</type>
      <type>Decimal</type>
    </type-group>

    <property name="controlValue"
      display-name-key="Value"
      description-key="The bound value"
      of-type-group="numbers"
      usage="bound"
      required="true" />

    <data-set name="dataSet" display-name-key="DataSet" />

    <resources>
      <code path="index.ts" order="1" />
      <css path="css/styles.css" order="1" />
      <platform-library name="React" version="16.14.0" />
      <platform-library name="Fluent" version="9.46.2" />
    </resources>

    <feature-usage>
      <uses-feature name="Device.captureImage" required="true" />
    </feature-usage>

    <external-service-usage enabled="true">
      <domain>www.example.com</domain>
    </external-service-usage>
  </control>
</manifest>
```

**Key manifest elements:**

| Element | Purpose |
|---------|---------|
| `control` | Root: defines namespace, constructor, version, control-type |
| `property` | Defines a bindable property (`of-type` or `of-type-group`) |
| `type-group` | Groups multiple data types a property can accept |
| `data-set` | Declares a dataset-bound component (grids/views) |
| `resources` | Lists code, CSS, RESX, and platform-library references |
| `platform-library` | Shares React/Fluent from the platform (virtual controls only) |
| `feature-usage` | Declares device capabilities needed (camera, geolocation) |
| `external-service-usage` | Marks component as premium if connecting to external services |

**Control element attributes:**

| Attribute | Description |
|-----------|-------------|
| `namespace` | Namespace of the code component |
| `constructor` | Constructor class name |
| `version` | Semantic version; bump on every change |
| `display-name-key` | Display name on UI |
| `description-key` | Description on UI |
| `control-type` | `standard` or `virtual` |

### PCF Tooling Commands

```bash
# Create new component project
pac pcf init --namespace MyNS --name MyControl --template field --run-npm-install

# Create React component
pac pcf init -n ReactSample -ns MyNS -t field -fw react -npm

# Build
npm run build

# Production build
npm run build -- --buildMode production

# Debug with test harness (http://localhost:8181)
npm start watch

# Refresh generated types after manifest changes
npm run refreshTypes

# Create solution wrapper
mkdir Solutions && cd Solutions
pac solution init --publisher-name MyPub --publisher-prefix mypub
pac solution add-reference --path ../../

# Build solution zip
dotnet build
# or: msbuild /t:restore && msbuild
```

**Template options for `--template`:** `field` (single value) or `dataset` (grid/view data).

### PCF API Reference (Key Interfaces)

| Interface | Description | Available For |
|-----------|-------------|---------------|
| `Context` | All properties/methods available to the component | Both |
| `StandardControl` | Standard control lifecycle (init, updateView, getOutputs, destroy) | Both |
| `ReactControl` | React control lifecycle (no DOM div, returns ReactElement) | Both |
| `WebApi` | CRUD operations on Dataverse data | Model-driven |
| `Navigation` | Navigation methods (openForm, openUrl, openAlertDialog) | Both |
| `Device` | Native device capabilities (camera, location, microphone) | Both |
| `Formatting` | Date, number, currency formatting | Both |
| `Mode` | Component state info (fullscreen, isVisible, isControlDisabled) | Both |
| `DataSet` | Properties/methods for grid/view data | Both |
| `Utility` | Utility methods (lookupObjects, getEntityMetadata) | Model-driven |
| `Resources` | Access to manifest-defined resource files | Both |
| `Factory` / `PopupService` | Popup management | Both |
| `UserSettings` | Current user info (language, security roles) | Both |
| `Client` | Client detection (web, mobile, Outlook) | Both |
| `Column` | Column metadata in a dataset | Both |
| `EntityRecord` | Base interface for dataset record results | Both |
| `Paging` | Pagination for datasets | Both |
| `Filtering` | Filter operations for datasets | Both |
| `Linking` | Table relationship info | Model-driven |
| `SortStatus` | Sort status of dataset columns | Model-driven |

### Adding Components to Model-Driven Apps

**Field-level:** Form Editor > double-click field > Controls tab > Add Control > select component > configure for Web/Phone/Tablet. Set Min, Max, Step properties. Choose Hide Default Control if desired.

**Entity-level (dataset):** Settings > Customizations > Entity > Controls tab > Add Control > select dataset component (e.g., Simple Table). Choose client display targets.

Always bump the `version` in the manifest when updating components. Publish customizations after import if using unmanaged solutions.

---

## 2. Dataverse Web API

### Endpoint and Protocol

- **Protocol:** OData v4.0 (RESTful)
- **Base URL:** `https://<org>.api.crm.dynamics.com/api/data/v9.2/`
- **Authentication:** OAuth 2.0 via Microsoft Entra ID
- **Default row limit:** 5,000 (standard tables), 500 (elastic tables)
- **Max URL length:** 32 KB (GET), 64 KB (within $batch POST)

### CRUD Operations

**Create (POST):**

```http
POST [base]/accounts
Content-Type: application/json

{
  "name": "Contoso Ltd",
  "revenue": 5000000,
  "primarycontactid@odata.bind": "/contacts(00000000-0000-0000-0000-000000000001)"
}
```

Response: `204 No Content` with `OData-EntityId` header. Use `Prefer: return=representation` for `201 Created` with data.

**Deep insert** (create related records in one atomic operation):

```http
POST [base]/accounts
{
  "name": "Parent",
  "primarycontactid": { "firstname": "John", "lastname": "Doe" },
  "opportunity_customer_accounts": [
    { "name": "Opp1", "Opportunity_Tasks": [{ "subject": "Task1" }] }
  ]
}
```

**Read / Query (GET):**

```http
GET [base]/accounts?$select=name,revenue&$filter=revenue gt 1000000
  &$orderby=name asc&$top=10&$expand=primarycontactid($select=fullname)
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

**OData query options:**

| Option | Purpose |
|--------|---------|
| `$select` | Choose columns to return |
| `$filter` | Filter rows (eq, ne, gt, lt, ge, le, contains, startswith, endswith) |
| `$orderby` | Sort results (asc/desc) |
| `$top` | Limit number of rows |
| `$expand` | Join related tables via navigation properties |
| `$count` | Include total row count |
| `$apply` | Aggregate and group data |

**Unsupported:** `$skip`, `$search`, `$format`.

Parameter aliases allow reuse: `&$filter=@p1 ne null&@p1=revenue`.

**Update (PATCH):**

```http
PATCH [base]/accounts(00000000-0000-0000-0000-000000000001)
Content-Type: application/json
If-Match: *

{ "name": "Updated Name", "revenue": 6000000 }
```

Only include changed properties to avoid triggering unnecessary business logic and audit entries. Use `Prefer: return=representation` for response data.

**Update single property (PUT):**

```http
PUT [base]/accounts(<id>)/name
Content-Type: application/json
{ "value": "New Name" }
```

**Delete (DELETE):**

```http
DELETE [base]/accounts(00000000-0000-0000-0000-000000000001)
```

**Delete single property value:**

```http
DELETE [base]/accounts(<id>)/description
```

**Upsert:** Same as PATCH with a URI referencing a primary key or alternate key. Creates if not found, updates if found. Use `If-Match: *` to prevent create, `If-None-Match: *` to prevent update.

**Bulk operations:** `CreateMultiple`, `UpdateMultiple`, `DeleteMultiple` actions for high-throughput batch processing.

**Duplicate detection:** Include `MSCRM.SuppressDuplicateDetection: false` header on create/update.

### FetchXML

FetchXML is Dataverse's proprietary XML query language, usable via SDK and Web API.

```xml
<fetch top="5" distinct="false">
  <entity name="account">
    <attribute name="name" />
    <attribute name="revenue" />
    <filter type="and">
      <condition attribute="statecode" operator="eq" value="0" />
      <condition attribute="revenue" operator="gt" value="1000000" />
    </filter>
    <order attribute="name" />
    <link-entity name="contact" from="contactid" to="primarycontactid" link-type="inner">
      <attribute name="fullname" />
    </link-entity>
  </entity>
</fetch>
```

**Key FetchXML elements:**

| Element | Purpose |
|---------|---------|
| `fetch` | Root: `top`, `distinct`, `aggregate`, `returntotalrecordcount` |
| `entity` | Primary table (`name` = logical name) |
| `attribute` | Column to select |
| `filter` | Filter group (`type`: and/or) |
| `condition` | Filter condition (`attribute`, `operator`, `value`) |
| `order` | Sort order (`attribute`, `descending`) |
| `link-entity` | Join to related table (`from`, `to`, `link-type`) |

**FetchXML advantages over OData:** supports joins without relationships, cross-table column comparisons, late materialize optimization, and more flexible aggregation.

**Community tool:** XrmToolBox FetchXML Builder for visual query construction.

---

## 3. Dataverse SDK for .NET (Organization Service)

### IOrganizationService Interface

The SDK for .NET provides `IOrganizationService` with two implementations: `CrmServiceClient` (legacy, ADAL) and `ServiceClient` (recommended, MSAL). Core methods:

```csharp
Guid id = svc.Create(entity);
Entity e = svc.Retrieve("account", id, new ColumnSet("name"));
EntityCollection results = svc.RetrieveMultiple(query);
svc.Update(entity);
svc.Delete("account", id);
OrganizationResponse resp = svc.Execute(request);
```

Operations use message request/response pattern: `CreateRequest`/`CreateResponse`, `RetrieveRequest`/`RetrieveResponse`, etc. Available in `Microsoft.Xrm.Sdk.Messages` and `Microsoft.Crm.Sdk.Messages` namespaces.

**NuGet packages:**
- `Microsoft.PowerPlatform.Dataverse.Client` (.NET Framework + .NET Core, recommended)
- `Microsoft.CrmSdk.CoreAssemblies` (.NET Framework only)

**Connection string patterns:**

```
AuthType=ClientSecret;url=https://org.crm.dynamics.com;ClientId=<appId>;Secret=<secret>
AuthType=Certificate;url=https://org.crm.dynamics.com;ClientId=<appId>;thumbprint=<thumbprint>
AuthType=OAuth;url=https://org.crm.dynamics.com;Username=<user>;Password=<pass>;ClientId=<appId>
```

---

## 4. Plug-in Development

### Event Pipeline Stages

| Stage | Value | Timing | Transaction |
|-------|-------|--------|-------------|
| PreValidation | 10 | Before main operation | Outside DB transaction (initial call); inside for cascaded |
| PreOperation | 20 | Before main operation | Inside transaction |
| MainOperation | 30 | Core operation | Inside transaction (internal use / Custom API only) |
| PostOperation | 40 | After main operation | Inside transaction (sync) or outside (async) |

### Writing a Plug-in

Plug-in classes implement `IPlugin` interface (or derive from generated `PluginBase`). Must target .NET Framework 4.6.2. Classes must be **stateless** (no instance-level data between invocations).

```csharp
public class MyPlugin : IPlugin
{
  public void Execute(IServiceProvider serviceProvider)
  {
    // 1. Get execution context
    var context = (IPluginExecutionContext)
      serviceProvider.GetService(typeof(IPluginExecutionContext));

    // 2. Get organization service
    var factory = (IOrganizationServiceFactory)
      serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    var orgService = factory.CreateOrganizationService(context.UserId);

    // 3. Get tracing service
    var tracing = (ITracingService)
      serviceProvider.GetService(typeof(ITracingService));

    try {
      if (context.InputParameters.Contains("Target")
          && context.InputParameters["Target"] is Entity entity)
      {
        tracing.Trace("Processing: {0}", entity.LogicalName);
        // Business logic here
      }
    }
    catch (FaultException<OrganizationServiceFault> ex) {
      throw new InvalidPluginExecutionException("Error in MyPlugin", ex);
    }
    catch (Exception ex) {
      tracing.Trace("MyPlugin: error: {0}", ex.ToString());
      throw;
    }
  }
}
```

**Key context properties:**

| Property | Description |
|----------|-------------|
| `InputParameters` | Message request parameters (e.g., `Target` entity) |
| `OutputParameters` | Message response parameters |
| `PreEntityImages` | Snapshots of record before operation |
| `PostEntityImages` | Snapshots of record after operation |
| `PrimaryEntityName` | Logical name of the primary entity |
| `MessageName` | Operation name (Create, Update, Delete, etc.) |
| `Stage` | Pipeline stage (10, 20, 30, 40) |
| `Depth` | Execution depth (detects recursion) |
| `UserId` | Impersonated user |
| `InitiatingUserId` | Actual calling user |

**Constructor signatures** for configuration data:

```csharp
public MyPlugin() {}
public MyPlugin(string unsecure) {}
public MyPlugin(string unsecure, string secure) {}
```

### Registering Plug-ins

Use **Plug-in Registration Tool (PRT)** or **Power Platform Tools for Visual Studio**.

**Step configuration fields:**

| Field | Description |
|-------|-------------|
| Message | The operation (Create, Update, Delete, Retrieve, etc.) |
| Primary Entity | Table to filter on |
| Filtering Attributes | Columns that trigger execution (Update only); do not include primary key |
| Event Handler | Assembly and class name |
| Execution Mode | Synchronous or Asynchronous (async only for PostOperation) |
| Execution Order | Numeric order for multiple plug-ins on same stage |
| Run in User's Context | Impersonation user (default: Calling User) |
| Deployment | Server or Offline |
| Unsecure/Secure Config | String configuration data passed to constructor |

**Entity image availability:**

| Stage | Pre Image | Post Image |
|-------|-----------|------------|
| PreValidation | Yes (Update/Delete) | No |
| PreOperation | Yes (Update/Delete) | No |
| PostOperation | Yes (Update/Delete) | Yes (Create/Update) |

Images must specify only the columns needed (never use default "all columns" for performance).

**Assembly versioning:** Build/revision changes = in-place upgrade. Major/minor changes = treated as different assembly; steps must be manually re-pointed.

---

## 5. Client Scripting (Model-Driven Apps)

### Form Events

| Event | Trigger |
|-------|---------|
| `OnLoad` | Form loads |
| `OnSave` | Form saves |
| `OnChange` | Field value changes |
| `TabStateChange` | Tab expand/collapse |
| `OnPreSearch` | Before lookup search |
| `OnRecordSelect` | Grid record selected |

Attach JavaScript via **Script web resource** (type 3, .js file). Business rules should be preferred for simple logic; use client scripting when business rules are insufficient.

### Client API Object Model

```
Xrm
 +-- App                    // App-level APIs
 +-- Copilot                // Copilot-related APIs
 +-- Device                 // Camera, barcode, geolocation
 +-- Encoding               // HTML/XML encoding
 +-- Navigation             // openForm, openUrl, openAlertDialog, openWebResource
 +-- Panel                  // Side panel control
 +-- Utility                // getGlobalContext, getEntityMetadata, lookupObjects
 +-- WebApi                 // createRecord, retrieveRecord, updateRecord, deleteRecord

formContext
 +-- data
 |    +-- entity            // getId, getEntityName, save, addOnSave
 |    +-- process           // BPF methods (getActiveProcess, setActiveStage)
 +-- ui
 |    +-- tabs / sections   // setVisible, setFocus, setLabel
 |    +-- controls          // getAttribute, setDisabled, setVisible
 +-- getAttribute()         // Access column values (getValue, setValue, addOnChange)
 +-- getControl()           // Access controls on the form

gridContext                  // Grid/subgrid interaction (getGrid, getSelectedRows)
executionContext             // Event context (getFormContext, getEventSource, getDepth)
```

**Key Xrm.WebApi methods:**

```javascript
// CRUD via client-side Web API wrapper
Xrm.WebApi.createRecord(entityLogicalName, data).then(successCallback, errorCallback);
Xrm.WebApi.retrieveRecord(entityLogicalName, id, options).then(...);
Xrm.WebApi.retrieveMultipleRecords(entityLogicalName, options, maxPageSize).then(...);
Xrm.WebApi.updateRecord(entityLogicalName, id, data).then(...);
Xrm.WebApi.deleteRecord(entityLogicalName, id).then(...);
```

### Web Resources

Virtual files stored in Dataverse database, accessible via unique URLs.

| Type | Extension | Type Value |
|------|-----------|------------|
| Webpage (HTML) | .htm, .html | 1 |
| CSS | .css | 2 |
| JavaScript | .js | 3 |
| XML | .xml | 4 |
| PNG | .png | 5 |
| JPG | .jpg | 6 |
| GIF | .gif | 7 |
| XAP (Silverlight) | .xap | 8 |
| XSL/XSLT | .xsl, .xslt | 9 |
| ICO | .ico | 10 |
| SVG | .svg | 11 |
| RESX (strings) | .resx | 12 |

**Reference methods:**
- `$webresource:` directive (creates solution dependencies, used in SiteMap/ribbon)
- `Xrm.Navigation.openWebResource()` (opens in new window with caching token)
- Relative URLs between web resources (use consistent naming with publisher prefix)
- Full URL: `https://<org>.crm.dynamics.com/WebResources/<name>`

**Limitations:** No server-side code execution (no .aspx); static files only. Max file size governed by `Organization.MaxUploadFileSize` (default 5 MB).

---

## 6. OAuth Authentication with Dataverse

### App Registration (Microsoft Entra ID)

1. Register app in Azure Portal > Microsoft Entra ID > App registrations
2. Set redirect URI (native: `app://<guid>`, web: `https://localhost`)
3. Grant API permission: **Dynamics CRM > user_impersonation** (delegated) for interactive users
4. For S2S: create client secret or upload certificate; create application user in Dataverse with custom security role

### Authentication Patterns

**Interactive (public client) with MSAL:**

```csharp
var authBuilder = PublicClientApplicationBuilder.Create(clientId)
    .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
    .WithRedirectUri("http://localhost")
    .Build();
var token = authBuilder.AcquireTokenInteractive(
    new[] { "https://org.crm.dynamics.com/user_impersonation" }).ExecuteAsync().Result;

// Use token in HTTP header
headers.Authorization = new AuthenticationHeaderValue("Bearer", token.AccessToken);
```

**Client credentials (confidential client, S2S):** Use scope `<environment-url>/.default` with client secret or certificate.

**ServiceClient connection strings:**

```
AuthType=ClientSecret;SkipDiscovery=true;url=https://org.crm.dynamics.com;
  Secret=<secret>;ClientId=<appId>;RequireNewInstance=true

AuthType=Certificate;SkipDiscovery=true;url=https://org.crm.dynamics.com;
  thumbprint=<thumbprint>;ClientId=<appId>;RequireNewInstance=true
```

**Best practice:** Use `DelegatingHandler` to auto-refresh tokens on each HTTP request rather than acquiring once.

---

## 7. Custom Connectors

### Overview

Custom connectors extend Power Automate, Power Apps, Logic Apps, and Copilot Studio to connect to any REST API. Defined using **OpenAPI 2.0** (Swagger) format. OpenAPI 3.0 is not supported.

### Creating a Custom Connector

1. **Define OpenAPI 2.0 spec** (must be < 1 MB):

```json
{
  "swagger": "2.0",
  "info": { "title": "MyAPI", "version": "1.0.0", "description": "..." },
  "host": "api.example.com",
  "basePath": "/v1",
  "schemes": ["https"],
  "securityDefinitions": {
    "api_key": { "type": "apiKey", "in": "header", "name": "X-API-Key" }
  },
  "paths": {
    "/items": {
      "get": {
        "operationId": "GetItems",
        "summary": "List all items",
        "responses": { "200": { "description": "Success" } }
      }
    }
  }
}
```

2. **Import:** Power Apps/Automate > Data > Custom connectors > New > Import OpenAPI file
3. **Configure:** Review General (host, base URL), Security (auth type), Definition (actions/triggers/parameters), and Validation pages
4. **Test:** Create connection with credentials, invoke test operation
5. **Deploy:** Package in solution for ALM; share within org or certify for public use

### Authentication Types

| Type | Use Case |
|------|----------|
| No auth | Public APIs |
| API Key | Header or query parameter key |
| Basic Auth | Username/password |
| OAuth 2.0 | Azure AD, generic OAuth providers |
| Windows Auth | On-premises via data gateway |

### Key OpenAPI Extensions for Power Platform

| Extension | Purpose |
|-----------|---------|
| `x-ms-summary` | Friendly display name for parameters/properties |
| `x-ms-visibility` | Control visibility: `none`, `advanced`, `internal`, `important` |
| `x-ms-trigger` | Marks operation as a trigger (for flows) |
| `x-ms-dynamic-values` | Dynamic dropdown values from another operation |
| `x-ms-dynamic-schema` | Dynamic schema from another operation |

### Connector Wizard Pages

| Page | Purpose |
|------|---------|
| General | API host, base URL, description, scheme (HTTPS) |
| Security | Authentication type and parameters |
| Definition | Actions, triggers, request/response schemas, parameter editing |
| Code (preview) | Custom C# code for request/response transformation |
| Test | Connection testing and operation invocation |

---

## 8. Quick Reference: Development Tools

| Tool | Purpose |
|------|---------|
| `pac pcf init` | Scaffold PCF component project |
| `pac solution init` | Create solution project |
| `pac plugin init` | Scaffold plug-in project |
| `pac tool prt` | Launch Plug-in Registration Tool |
| `pac auth create` | Authenticate to Dataverse environment |
| `npm start watch` | PCF debug harness with hot reload |
| `npm run build` | Build PCF component |
| `dotnet build` / `msbuild` | Build solution packages |
| Power Platform Tools for VS | Integrated plug-in dev, deploy, debug, profiling |
| XrmToolBox | Community tools (FetchXML Builder, REST Builder, WebResources Manager) |
| Insomnia / Postman / Bruno | HTTP client tools for Web API testing |
| Power Platform CLI (`pac`) | Unified CLI for all Power Platform development tasks |
