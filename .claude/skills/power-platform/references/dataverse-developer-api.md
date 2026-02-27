# Dataverse Developer API Reference

> Distilled from research/12-pcf-developer.md and Microsoft Learn documentation

---

## Web API (OData v4)

**Endpoint:** `https://<org>.api.crm.dynamics.com/api/data/v9.2/`
**Protocol:** OData v4.0 (RESTful)
**Auth:** OAuth 2.0 via Microsoft Entra ID
**Default row limit:** 5,000 (standard tables), 500 (elastic tables)
**Max URL length:** 32 KB (GET), 64 KB (within $batch POST)

---

## CRUD Operations

### Create (POST)

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

**Deep insert** (create related records atomically):

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

### Read / Query (GET)

```http
GET [base]/accounts?$select=name,revenue&$filter=revenue gt 1000000
  &$orderby=name asc&$top=10&$expand=primarycontactid($select=fullname)
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
```

### Update (PATCH)

```http
PATCH [base]/accounts(00000000-0000-0000-0000-000000000001)
Content-Type: application/json
If-Match: *

{ "name": "Updated Name", "revenue": 6000000 }
```

Only include changed properties to avoid triggering unnecessary business logic and audit entries.

### Update Single Property (PUT)

```http
PUT [base]/accounts(<id>)/name
Content-Type: application/json
{ "value": "New Name" }
```

### Delete (DELETE)

```http
DELETE [base]/accounts(00000000-0000-0000-0000-000000000001)
```

Delete single property: `DELETE [base]/accounts(<id>)/description`

### Upsert

Same as PATCH with URI referencing primary/alternate key. Creates if not found, updates if found.
- `If-Match: *` -- prevent create (update only)
- `If-None-Match: *` -- prevent update (create only)

### Bulk Operations

`CreateMultiple`, `UpdateMultiple`, `DeleteMultiple` actions for high-throughput batch processing.

---

## Batch Operations ($batch)

The `$batch` endpoint groups multiple operations into a single HTTP request. Useful for reducing round-trips and executing atomic changesets.

**Endpoint:** `POST [base]/$batch`

### Request Structure

```http
POST [base]/$batch
Content-Type: multipart/mixed; boundary=batch_boundary

--batch_boundary
Content-Type: multipart/mixed; boundary=changeset_boundary

--changeset_boundary
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 1

POST [base]/accounts HTTP/1.1
Content-Type: application/json

{"name": "Account A"}

--changeset_boundary
Content-Type: application/http
Content-Transfer-Encoding: binary
Content-ID: 2

POST [base]/contacts HTTP/1.1
Content-Type: application/json

{"firstname": "Jane", "lastname": "Doe", "parentcustomerid_account@odata.bind": "$1"}

--changeset_boundary--
--batch_boundary
Content-Type: application/http
Content-Transfer-Encoding: binary

GET [base]/accounts?$top=3 HTTP/1.1
Accept: application/json

--batch_boundary--
```

### Key Concepts

| Concept | Detail |
|---------|--------|
| **Changeset** | Group of CUD operations that execute atomically (all-or-nothing) |
| **Content-ID** | Reference earlier operations in the same changeset via `$<Content-ID>` |
| **GET in batch** | Must be outside changesets; GETs are read-only, not transactional |
| **Max operations** | 1,000 per batch request (default); configurable per environment |
| **Execution order** | Operations within a changeset have no guaranteed order unless dependent via Content-ID |

### JSON Batch Format (Preferred)

Since v9.1, Dataverse supports a simpler JSON-based batch format:

```http
POST [base]/$batch
Content-Type: application/json

{
  "requests": [
    {
      "id": "1",
      "method": "POST",
      "url": "accounts",
      "headers": { "Content-Type": "application/json" },
      "body": { "name": "Account B" }
    },
    {
      "id": "2",
      "method": "PATCH",
      "url": "accounts(00000000-0000-0000-0000-000000000002)",
      "headers": { "Content-Type": "application/json" },
      "body": { "revenue": 9000000 }
    }
  ]
}
```

**Atomicity group:** Add `"atomicityGroup": "group1"` to each request object to form a transactional changeset.

---

## OData Query Options

| Option | Purpose |
|--------|---------|
| `$select` | Choose columns to return |
| `$filter` | Filter rows (eq, ne, gt, lt, ge, le, contains, startswith, endswith) |
| `$orderby` | Sort results (asc/desc) |
| `$top` | Limit number of rows |
| `$expand` | Join related tables via navigation properties |
| `$count` | Include total row count |
| `$apply` | Aggregate and group data |

**Not supported:** `$skip`, `$search`, `$format`.

Parameter aliases: `&$filter=@p1 ne null&@p1=revenue`

Duplicate detection header: `MSCRM.SuppressDuplicateDetection: false`

---

## Advanced Query Patterns

### Nested $expand

Expand multiple levels of relationships (up to 10 levels deep via FetchXML, limited in OData):

```http
GET [base]/accounts?$select=name
  &$expand=primarycontactid($select=fullname;
    $expand=account_primary_contact($select=name,revenue))
```

**Limitation:** Web API supports max 10 `$expand` per query. Use FetchXML for deeper or more complex joins.

### $apply Aggregation

Server-side aggregation without returning individual rows:

```http
GET [base]/opportunities?$apply=
  groupby((statecode),aggregate(estimatedvalue with sum as total_value,
    $count as opp_count))
```

Supported transformations: `aggregate`, `groupby`, `filter`, `compute`.

Aggregate functions: `sum`, `avg`, `min`, `max`, `countdistinct`, `$count`.

```http
GET [base]/accounts?$apply=
  filter(revenue gt 0)/
  groupby((address1_stateorprovince),
    aggregate(revenue with average as avg_revenue))
  &$orderby=avg_revenue desc
```

### Cross-Table Filtering

Filter parent by child conditions using lambda operators:

```http
GET [base]/accounts?$filter=contact_customer_accounts/any(c: c/statecode eq 0)
  &$select=name
```

`any()` returns parents where at least one child matches. `all()` requires every child to match.

### Pagination with Paging Cookie

First request returns `@odata.nextLink` when more pages exist. For FetchXML, the response includes a paging cookie:

```http
GET [base]/accounts?fetchXml=<fetch page="2" paging-cookie="%3Ccookie%20...%2F%3E" count="50">
  <entity name="account"><attribute name="name" /></entity></fetch>
```

For OData, follow `@odata.nextLink` directly -- it contains an opaque `$skiptoken`. Do not construct skip tokens manually.

**Ordering requirement:** Results must be deterministically ordered for stable paging. Add `$orderby` on a unique column (e.g., primary key).

---

## FetchXML

Dataverse proprietary XML query language, usable via SDK and Web API.

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

**Key elements:**

| Element | Purpose |
|---------|---------|
| `fetch` | Root: `top`, `distinct`, `aggregate`, `returntotalrecordcount` |
| `entity` | Primary table (`name` = logical name) |
| `attribute` | Column to select |
| `filter` | Filter group (`type`: and/or) |
| `condition` | Filter condition (`attribute`, `operator`, `value`) |
| `order` | Sort order (`attribute`, `descending`) |
| `link-entity` | Join to related table (`from`, `to`, `link-type`) |

**Advantages over OData:** joins without relationships, cross-table column comparisons, late materialize optimization, flexible aggregation.

### FetchXML Aggregates

Use `aggregate="true"` on the `<fetch>` element to enable aggregation mode. In this mode, every `<attribute>` must have an `aggregate` function or be used in a `groupby`.

```xml
<fetch aggregate="true">
  <entity name="opportunity">
    <attribute name="estimatedvalue" alias="total_value" aggregate="sum" />
    <attribute name="opportunityid" alias="opp_count" aggregate="countcolumn" />
    <attribute name="ownerid" alias="owner" groupby="true" />
  </entity>
</fetch>
```

**Supported aggregate functions:**

| Function | Description |
|----------|-------------|
| `sum` | Sum of numeric values |
| `avg` | Average of numeric values |
| `min` | Minimum value |
| `max` | Maximum value |
| `count` | Count of all rows (use on any attribute) |
| `countcolumn` | Count of non-null values in column |

**Distinct count:**

```xml
<attribute name="customerid" alias="unique_customers" aggregate="countcolumn" distinct="true" />
```

**Date grouping** with `dategrouping` attribute:

```xml
<fetch aggregate="true">
  <entity name="opportunity">
    <attribute name="estimatedvalue" alias="monthly_total" aggregate="sum" />
    <attribute name="actualclosedate" alias="close_month" groupby="true" dategrouping="month" />
    <attribute name="actualclosedate" alias="close_year" groupby="true" dategrouping="year" />
  </entity>
</fetch>
```

Valid `dategrouping` values: `day`, `week`, `month`, `quarter`, `year`, `fiscal-period`, `fiscal-year`.

**Having-style filter (aggregate filter):**

```xml
<fetch aggregate="true">
  <entity name="opportunity">
    <attribute name="estimatedvalue" alias="total" aggregate="sum" />
    <attribute name="ownerid" alias="owner" groupby="true" />
    <filter type="and">
      <condition attribute="statecode" operator="eq" value="1" />
    </filter>
  </entity>
</fetch>
```

Row-level filters apply before aggregation. To filter on aggregated values, use post-processing on the client side.

---

## Change Tracking

Change tracking enables efficient data synchronization by returning only records that changed since the last sync.

### Enabling Change Tracking

Enable per table in the table properties: **Track changes** = Yes. Available on standard and custom tables. Some system tables have it enabled by default.

### Web API Usage

**Initial sync** -- get all data plus a delta token:

```http
GET [base]/accounts?$select=name,revenue
Prefer: odata.track-changes
```

Response includes `@odata.deltaLink`:
```
"@odata.deltaLink": "[base]/accounts?$select=name,revenue&$deltatoken=919042%2108%2f22%2f2017..."
```

**Delta sync** -- request only changes since last token:

```http
GET [base]/accounts?$select=name,revenue&$deltatoken=919042%2108%2f22%2f2017...
Prefer: odata.track-changes
```

### Delta Response Content

| Change Type | Indicator |
|-------------|-----------|
| Created/Updated | Normal entity record in response |
| Deleted | Record with `@odata.context` containing `$deletedEntity` and only the ID |

### SDK Usage (RetrieveEntityChangesRequest)

```csharp
var request = new RetrieveEntityChangesRequest
{
    EntityName = "account",
    Columns = new ColumnSet("name", "revenue"),
    PageInfo = new PagingInfo { Count = 5000, PageNumber = 1 }
    // DataVersion = "<previous_token>" for delta sync
};

var response = (RetrieveEntityChangesResponse)svc.Execute(request);
string newToken = response.EntityChanges.DataToken;

foreach (var change in response.EntityChanges.Changes)
{
    if (change.Type == ChangeType.NewOrUpdated)
    {
        var entity = ((NewOrUpdatedItem)change).NewOrUpdatedEntity;
    }
    else if (change.Type == ChangeType.RemoveOrDeleted)
    {
        var removedId = ((RemovedOrDeletedItem)change).RemovedItem.Id;
    }
}
```

**Limitations:** Max 300K changes per page. If changes exceed threshold, a full resync (no DataVersion) is required. Filter expressions are not supported on delta queries.

---

## Alternate Keys

Alternate keys allow referencing records by business-meaningful columns instead of the primary key GUID.

### Definition

Define via the Maker portal (table > Keys) or programmatically. Key columns must be unique, non-null, and immutable for best results. Supports composite keys (multiple columns).

**Supported column types:** Single line of text, Whole number, Decimal, Lookup, Date/Time, Choice (option set).

**Limitation:** Max 5 alternate keys per table. Key creation is asynchronous -- the system builds an index. Check `EntityKeyMetadata.EntityKeyIndexStatus` for `Active` before using.

### Web API Usage

Reference a record by alternate key instead of GUID:

```http
GET [base]/accounts(accountnumber='ABC123')

PATCH [base]/accounts(accountnumber='ABC123')
Content-Type: application/json
{ "revenue": 5000000 }
```

**Composite key** (multiple columns):

```http
GET [base]/custom_entities(field1='value1',field2=42)
```

### Upsert with Alternate Keys

Particularly powerful for data integration scenarios -- upsert by business key without needing to know the GUID:

```http
PATCH [base]/accounts(accountnumber='ABC123')
Content-Type: application/json

{
  "name": "Contoso Ltd",
  "revenue": 5000000,
  "accountnumber": "ABC123"
}
```

If the record with `accountnumber='ABC123'` exists, it updates. If not, it creates. Combine with `If-Match: *` or `If-None-Match: *` to control behavior.

### Binding via Alternate Key

Use alternate keys in navigation property bindings:

```http
POST [base]/opportunities
Content-Type: application/json

{
  "name": "New Opportunity",
  "customerid_account@odata.bind": "/accounts(accountnumber='ABC123')"
}
```

---

## File and Image Columns

Dataverse supports file columns (any file type) and image columns (image data) as first-class column types.

### File Columns

**Max file size:** Configurable per column, up to 10 GB (default 32 MB).
**Storage:** Azure Blob Storage managed by Dataverse.

**Upload (small file, single request):**

```http
PATCH [base]/accounts(<id>)/myfilecolumn
Content-Type: application/octet-stream

<binary file content>
```

**Upload (large file, chunked):**

Step 1 -- Initialize upload:
```http
POST [base]/accounts(<id>)/myfilecolumn?x-ms-file-name=document.pdf
Content-Type: application/json
{ }
```

Response returns a `fileContinuationToken`.

Step 2 -- Upload chunks (in sequence):
```http
PATCH [base]/accounts(<id>)/myfilecolumn?x-ms-file-name=document.pdf
  &x-ms-chunk-offset=0&x-ms-chunk-size=4194304
  &x-ms-file-continuation-token=<token>
Content-Type: application/octet-stream

<binary chunk>
```

Step 3 -- Commit:
```http
PATCH [base]/accounts(<id>)/myfilecolumn?x-ms-file-name=document.pdf
  &x-ms-file-continuation-token=<token>&x-ms-commit=true
Content-Type: application/json
{ }
```

**Download:**

```http
GET [base]/accounts(<id>)/myfilecolumn/$value
```

Returns binary stream. Supports `Range` header for partial downloads.

**Delete file:**

```http
DELETE [base]/accounts(<id>)/myfilecolumn
```

### Image Columns

Similar API surface. Image columns auto-generate thumbnails. Retrieve full image:

```http
GET [base]/accounts(<id>)/entityimage/$value
```

Thumbnail (default): query without `/$value` returns Base64-encoded thumbnail in JSON.

**Max size:** 30 MB for full image. Thumbnail is always 144x144 pixels.

---

## Elastic Tables

Elastic tables use Azure Cosmos DB as the backend store, designed for high-volume, low-latency scenarios with semi-structured data.

### Key Characteristics

| Feature | Standard Tables | Elastic Tables |
|---------|----------------|----------------|
| Backend | SQL Server | Azure Cosmos DB |
| Max rows | Billions (perf degrades) | Billions (horizontal scale) |
| Default page size | 5,000 | 500 |
| Transactions | Full ACID | Per-partition |
| Schema | Fixed columns | Fixed + JSON columns |
| Cost | Included in license | Capacity-based |

### Partitioning

Every elastic table has a `partitionid` column. Records with the same partition ID are stored together for efficient querying.

```http
POST [base]/contoso_sensors
Content-Type: application/json

{
  "contoso_sensorid": "S-001",
  "contoso_reading": 42.5,
  "partitionid": "\"region-west\""
}
```

**Important:** `partitionid` values must be wrapped in escaped double quotes in JSON.

**Querying by partition:**

```http
GET [base]/contoso_sensors?partitionId='region-west'
  &$filter=contoso_reading gt 40
```

### Session Tokens

Elastic tables use session consistency. Each write returns a `x-ms-session-token` header. Pass it on subsequent reads to guarantee read-your-write consistency:

```http
GET [base]/contoso_sensors(<id>)?partitionId='region-west'
x-ms-session-token: <token-from-previous-write>
```

Without session tokens, reads may return stale data due to eventual consistency.

### JSON Columns

Elastic tables support JSON columns for storing semi-structured data without schema changes:

```http
POST [base]/contoso_iotevents
Content-Type: application/json

{
  "contoso_deviceid": "D-100",
  "contoso_payload": "{\"temperature\": 72.5, \"humidity\": 45, \"tags\": [\"indoor\"]}"
}
```

JSON columns are stored as strings. Query JSON properties using `contains()` or filter on the string representation. For indexed querying on JSON properties, use Cosmos DB directly.

### CRUD Differences from Standard Tables

- **Create:** Must include `partitionid` if the table uses custom partitioning.
- **Read by ID:** Must include `partitionId` query parameter: `GET [base]/contoso_sensors(<id>)?partitionId='region-west'`
- **Update/Delete:** Must include `partitionId` as well.
- **Query:** Without `partitionId`, queries scan all partitions (cross-partition query, slower).
- **Bulk:** `CreateMultiple` / `UpdateMultiple` supported; all records in a single request should share the same partition for best performance.
- **No support for:** Calculated columns, rollup columns, business rules, classic workflows, duplicate detection.

### Time-to-Live (TTL)

Elastic tables can auto-delete records after a specified duration:

```http
POST [base]/contoso_logs
Content-Type: application/json

{
  "contoso_message": "Event occurred",
  "partitionid": "\"app-logs\"",
  "ttlinmilliseconds": 2592000000
}
```

The `ttlinmilliseconds` field sets per-record expiration. `2592000000` = 30 days.

---

## SDK for .NET (Organization Service)

### IOrganizationService

Implementations: `ServiceClient` (recommended, MSAL) and `CrmServiceClient` (legacy, ADAL).

```csharp
Guid id = svc.Create(entity);
Entity e = svc.Retrieve("account", id, new ColumnSet("name"));
EntityCollection results = svc.RetrieveMultiple(query);
svc.Update(entity);
svc.Delete("account", id);
OrganizationResponse resp = svc.Execute(request);
```

**NuGet packages:**
- `Microsoft.PowerPlatform.Dataverse.Client` (recommended, .NET Framework + .NET Core)
- `Microsoft.CrmSdk.CoreAssemblies` (.NET Framework only)

**Connection strings:**

```
AuthType=ClientSecret;url=https://org.crm.dynamics.com;ClientId=<appId>;Secret=<secret>
AuthType=Certificate;url=https://org.crm.dynamics.com;ClientId=<appId>;thumbprint=<thumbprint>
AuthType=OAuth;url=https://org.crm.dynamics.com;Username=<user>;Password=<pass>;ClientId=<appId>
```

### Early-Bound vs Late-Bound Entities

**Late-bound** (default): Use `Entity` class with string-based attribute access.

```csharp
var account = new Entity("account");
account["name"] = "Contoso Ltd";
account["revenue"] = new Money(5000000);
svc.Create(account);

// Read
string name = account.GetAttributeValue<string>("name");
```

**Early-bound**: Use generated strongly-typed classes for compile-time safety.

```csharp
var account = new Account();
account.Name = "Contoso Ltd";
account.Revenue = new Money(5000000);
svc.Create(account);
```

**Code generation** using `pac modelbuilder build`:

```bash
pac modelbuilder build --outdirectory ./EarlyBound
  --entitynamesfilter "account;contact;opportunity"
  --generateActions
```

This generates C# classes with typed properties for each column and relationship. Regenerate when schema changes.

**When to use which:**
- Early-bound: Application code, plug-ins with known schema, CI/CD pipelines
- Late-bound: Dynamic/generic utilities, metadata-driven logic, when schema is unknown at compile time

### ExecuteMultiple

Batch multiple SDK requests in a single service call. Not transactional -- each request executes independently.

```csharp
var requests = new ExecuteMultipleRequest
{
    Requests = new OrganizationRequestCollection(),
    Settings = new ExecuteMultipleSettings
    {
        ContinueOnError = true,
        ReturnResponses = true
    }
};

for (int i = 0; i < 200; i++)
{
    var entity = new Entity("account") { ["name"] = $"Account {i}" };
    requests.Requests.Add(new CreateRequest { Target = entity });
}

var response = (ExecuteMultipleResponse)svc.Execute(requests);

foreach (var item in response.Responses)
{
    if (item.Fault != null)
        Console.WriteLine($"Request {item.RequestIndex} failed: {item.Fault.Message}");
}
```

**Limits:** Max 1,000 requests per `ExecuteMultiple` call. Cannot nest `ExecuteMultiple` inside another `ExecuteMultiple`.

### ExecuteTransaction

Like `ExecuteMultiple` but fully transactional -- all requests succeed or all roll back.

```csharp
var txnRequest = new ExecuteTransactionRequest
{
    Requests = new OrganizationRequestCollection(),
    ReturnResponses = true
};

txnRequest.Requests.Add(new CreateRequest
{
    Target = new Entity("account") { ["name"] = "Parent Corp" }
});
txnRequest.Requests.Add(new CreateRequest
{
    Target = new Entity("contact") { ["firstname"] = "Jane", ["lastname"] = "Doe" }
});

try
{
    var txnResponse = (ExecuteTransactionResponse)svc.Execute(txnRequest);
}
catch (FaultException<OrganizationServiceFault> ex)
{
    // All operations rolled back
    int failedIndex = ((ExecuteTransactionFault)ex.Detail).FaultedRequestIndex;
    Console.WriteLine($"Transaction failed at request {failedIndex}");
}
```

**Key difference from ExecuteMultiple:** No `ContinueOnError` option -- first failure aborts and rolls back everything. Max 1,000 requests.

---

## Plug-in Development

### Pipeline Stages

| Stage | Value | Timing | Transaction |
|-------|-------|--------|-------------|
| PreValidation | 10 | Before main operation | Outside DB transaction |
| PreOperation | 20 | Before main operation | Inside transaction |
| MainOperation | 30 | Core operation | Inside (Custom API only) |
| PostOperation | 40 | After main operation | Inside (sync) or outside (async) |

### IPlugin Template

```csharp
public class MyPlugin : IPlugin
{
  public void Execute(IServiceProvider serviceProvider)
  {
    var context = (IPluginExecutionContext)
      serviceProvider.GetService(typeof(IPluginExecutionContext));

    var factory = (IOrganizationServiceFactory)
      serviceProvider.GetService(typeof(IOrganizationServiceFactory));
    var orgService = factory.CreateOrganizationService(context.UserId);

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
  }
}
```

Must target .NET Framework 4.6.2. Classes must be **stateless**.

### Key Context Properties

| Property | Description |
|----------|-------------|
| `InputParameters` | Message request parameters (e.g., `Target` entity) |
| `OutputParameters` | Message response parameters |
| `PreEntityImages` | Snapshots of record before operation |
| `PostEntityImages` | Snapshots of record after operation |
| `MessageName` | Operation name (Create, Update, Delete) |
| `Stage` | Pipeline stage (10, 20, 30, 40) |
| `Depth` | Execution depth (detects recursion) |

### Entity Image Availability

| Stage | Pre Image | Post Image |
|-------|-----------|------------|
| PreValidation | Yes (Update/Delete) | No |
| PreOperation | Yes (Update/Delete) | No |
| PostOperation | Yes (Update/Delete) | Yes (Create/Update) |

Specify only needed columns in images (never all columns).

### Registration (Plug-in Registration Tool)

Key step fields: Message, Primary Entity, Filtering Attributes, Execution Mode (Sync/Async), Execution Order, Run in User's Context, Unsecure/Secure Config.

---

## OAuth Authentication

### App Registration (Microsoft Entra ID)

1. Register app in Azure Portal > Microsoft Entra ID > App registrations
2. Set redirect URI
3. Grant API permission: Dynamics CRM > user_impersonation (delegated)
4. For S2S: create client secret or certificate; create application user in Dataverse

### MSAL Interactive Auth

```csharp
var authBuilder = PublicClientApplicationBuilder.Create(clientId)
    .WithAuthority(AadAuthorityAudience.AzureAdMultipleOrgs)
    .WithRedirectUri("http://localhost")
    .Build();
var token = authBuilder.AcquireTokenInteractive(
    new[] { "https://org.crm.dynamics.com/user_impersonation" }).ExecuteAsync().Result;

headers.Authorization = new AuthenticationHeaderValue("Bearer", token.AccessToken);
```

**S2S scope:** `<environment-url>/.default` with client secret or certificate.

Use `DelegatingHandler` to auto-refresh tokens on each HTTP request.

---

## Quick Reference: Common HTTP Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Prefer: return=representation` | Return created/updated record in response | POST, PATCH |
| `Prefer: odata.include-annotations="*"` | Include formatted values, lookup names | GET |
| `Prefer: odata.maxpagesize=100` | Set page size | GET |
| `Prefer: odata.track-changes` | Enable change tracking delta link | GET |
| `If-Match: *` | Prevent create on upsert (update only) | PATCH |
| `If-None-Match: *` | Prevent update on upsert (create only) | PATCH |
| `MSCRM.SuppressDuplicateDetection: false` | Run duplicate detection | POST, PATCH |
| `MSCRM.MergeLabels: true` | Preserve unset label languages on update | PATCH (labels) |
| `CallerObjectId: <AAD-object-id>` | Impersonate via Azure AD object ID | Any |
| `x-ms-session-token` | Session consistency for elastic tables | GET (elastic) |
| `OData-MaxVersion: 4.0` | Required OData version header | All |
