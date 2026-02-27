# Power Platform Performance Optimization Reference

> Patterns and techniques for building fast, scalable Power Platform solutions. Covers canvas apps, model-driven apps, Power Automate, and Dataverse.

---

## 1. Canvas App Performance

### App.Formulas vs OnStart

`App.Formulas` (named formulas) are declarative and recalculate automatically. `App.OnStart` runs imperatively at app load. Prefer `App.Formulas` for most scenarios.

| Aspect | App.Formulas | App.OnStart |
|--------|-------------|-------------|
| **Execution** | Lazy -- evaluated when first referenced | Eager -- runs before first screen shows |
| **Recalculation** | Automatic when dependencies change | Manual -- must call `Set()` again |
| **Blocking** | Does not block app load | Blocks app load until complete |
| **Use case** | Derived values, user context, lookups | One-time side effects (e.g., `ClearCollect`) |

```powerfx
// App.Formulas -- preferred for most data
UserEmail = User().Email;
UserProfile = LookUp(Employees, Email = UserEmail);
IsManager = CountRows(Filter(Employees, ManagerId = UserProfile.EmployeeId)) > 0;
ActiveProjects = Filter(Projects, Status = "Active" && OwnerId = UserProfile.EmployeeId);
```

```powerfx
// App.OnStart -- only for imperative caching
Concurrent(
    ClearCollect(colDepartments, Departments),
    ClearCollect(colCategories, Categories),
    ClearCollect(colSettings, Filter(AppSettings, Active = true))
);
```

### Concurrent() for Parallel Data Loading

`Concurrent()` runs multiple data calls simultaneously instead of sequentially.

```powerfx
// Slow: sequential loading (~3 seconds total)
ClearCollect(col1, DataSource1);   // ~1s
ClearCollect(col2, DataSource2);   // ~1s
ClearCollect(col3, DataSource3);   // ~1s

// Fast: parallel loading (~1 second total)
Concurrent(
    ClearCollect(col1, DataSource1),
    ClearCollect(col2, DataSource2),
    ClearCollect(col3, DataSource3)
)
```

**Rules for Concurrent:**
- Each expression inside `Concurrent()` must be independent (no shared variables)
- Cannot use `Set()` inside `Concurrent()` -- use `ClearCollect()` instead
- Order of completion is not guaranteed
- Works best when each operation hits a different data source or endpoint

### Gallery Optimization

Galleries are the most common performance bottleneck. Key optimization strategies:

| Technique | Impact | Implementation |
|-----------|--------|---------------|
| **Limit visible items** | High | Set `Items` to `FirstN(Source, 100)` or use pagination |
| **Minimize controls per row** | High | Target fewer than 6 controls per gallery item |
| **Avoid nested galleries** | High | Use `Concat()` to flatten data instead |
| **Use `DelayOutput`** | Medium | Set `DelayOutput = true` on search boxes (300ms debounce) |
| **Simplify templates** | Medium | Remove unused labels, icons, images from gallery template |
| **Disable `LoadingSpinner`** | Low | Set `LoadingSpinner = LoadingSpinner.None` when not needed |

```powerfx
// Paginated gallery pattern
Set(varPage, 1);
Set(varPageSize, 50);

// Gallery Items property
FirstN(
    Skip(
        SortByColumns(
            Filter(DataSource, SearchBox.Text in Name),
            "Name", SortOrder.Ascending
        ),
        (varPage - 1) * varPageSize
    ),
    varPageSize
)
```

### Image Optimization

| Problem | Solution |
|---------|----------|
| Large images in galleries | Use thumbnail URLs or resize server-side |
| Images from SharePoint | Use `?width=200&height=200` query parameter on image URLs |
| Multiple image loads | Set `Image.Visible` to load only when scrolled into view |
| Base64 images | Avoid; use URL references instead |
| App icon/splash images | Compress to under 100 KB before upload |

### Minimizing Data Calls

```powerfx
// Bad: calls DataSource twice
Gallery.Items = Filter(DataSource, Category = "A")
Label.Text = CountRows(Filter(DataSource, Category = "A"))

// Good: call once, reuse collection
ClearCollect(colFiltered, Filter(DataSource, Category = "A"));
Gallery.Items = colFiltered
Label.Text = CountRows(colFiltered)
```

---

## 2. Delegation Patterns

Delegation pushes query processing to the data source (server-side). Non-delegable operations pull all data to the client, capped at 500 or 2,000 rows (configurable max).

### Delegation Matrix by Data Source

#### Dataverse (Best Delegation Support)

| Operation | Delegable | Notes |
|-----------|-----------|-------|
| `Filter` | Yes | All comparison operators supported |
| `Sort` / `SortByColumns` | Yes | Single or multiple columns |
| `Search` | Yes | Uses Dataverse Relevance Search |
| `LookUp` | Yes | |
| `in` operator | Yes | For option sets and lookups |
| `StartsWith` | Yes | |
| `=`, `<>`, `<`, `>`, `<=`, `>=` | Yes | |
| `And`, `Or`, `Not` | Yes | |
| `Sum`, `Min`, `Max`, `Avg` | Yes | Via aggregate functions |
| `CountRows` | Yes | When used with delegable filter |
| `EndsWith` | No | Use calculated column workaround |
| `IsBlank` on related field | No | Check at source level |
| `Trim`, `Lower`, `Upper` in filter | No | Use calculated columns |

#### SharePoint

| Operation | Delegable | Notes |
|-----------|-----------|-------|
| `Filter` with `=`, `<>`, `<`, `>` | Yes | Single columns only |
| `StartsWith` | Yes | Text columns |
| `Sort` / `SortByColumns` | Yes | Single column only |
| `IsBlank` | Yes | |
| `Search` | No | Use `Filter` + `StartsWith` instead |
| `Or` in Filter | No | Limited; split into separate filters |
| Lookup columns in filter | Partial | Only ID comparison is delegable |
| `CountRows` | No | Collect first, then count |

#### SQL Server

| Operation | Delegable | Notes |
|-----------|-----------|-------|
| `Filter` with comparisons | Yes | Standard operators |
| `Sort` / `SortByColumns` | Yes | |
| `Search` | No | Use stored procedures for full-text |
| `Sum`, `Min`, `Max`, `Avg` | Yes | |
| `StartsWith` | Yes | |
| `EndsWith` | No | |
| `IsBlank` | Yes | |
| `in` operator | Yes | |

### Workarounds for Non-Delegable Operations

**Pattern 1: Pre-cache with ClearCollect (small datasets < 2,000 rows)**

```powerfx
// Cache once at startup or on screen load
ClearCollect(colAllProducts, Products);

// Now all operations are local and unrestricted
Filter(colAllProducts, EndsWith(SKU, "-XL") && Rating > 4)
```

**Pattern 2: Calculated columns in Dataverse**

For operations like `EndsWith`, `Len`, `Trim` that are not delegable:
1. Create a calculated or formula column in Dataverse
2. The column pre-computes the value server-side
3. Filter on the calculated column (which IS delegable as an equality check)

```
Example: Column "SKUSuffix" = Right(SKU, 3)
Filter(Products, SKUSuffix = "-XL")  // Delegable
```

**Pattern 3: Dataverse views**

Create server-side views for complex queries, then use the view as the data source in the app.

```powerfx
// Use a pre-filtered Dataverse view
Filter(
    'Active Accounts (High Value)',  // Dataverse view name
    Region = varSelectedRegion
)
```

**Pattern 4: Power Automate intermediary**

For complex queries that cannot be delegated:
1. Canvas app calls a Power Automate flow
2. Flow uses FetchXML or Web API for complex server-side queries
3. Flow returns filtered results as JSON
4. App parses with `ParseJSON()` or receives as a typed collection

### Collection Caching Strategy

| Strategy | When to Use | Refresh Pattern |
|----------|-------------|-----------------|
| **Load once** | Reference data (countries, categories) | App startup only |
| **Load per screen** | Screen-specific data | `Screen.OnVisible` |
| **Load on demand** | User-triggered data | Button press or search submit |
| **Timer refresh** | Near-real-time data | `Timer.OnTimerEnd` every N seconds |
| **Stale-while-revalidate** | Show cached, refresh in background | Display collection, then `ClearCollect` again |

```powerfx
// Stale-while-revalidate pattern
// Screen.OnVisible:
If(
    IsEmpty(colOrders),
    // First load: blocking fetch
    ClearCollect(colOrders, Filter(Orders, Status = "Open")),
    // Subsequent: non-blocking refresh (user sees stale data briefly)
    ClearCollect(colOrders, Filter(Orders, Status = "Open"))
);
Set(varLastRefresh, Now())
```

---

## 3. Model-Driven App Performance

### Form Design Best Practices

| Technique | Impact | Details |
|-----------|--------|--------|
| **Limit tabs to 3-5** | High | Each visible tab loads its controls at form open |
| **Use tab auto-expand = false** | High | Collapsed tabs defer loading until clicked |
| **Limit subgrids** | High | Each subgrid = 1+ API call; max 2-3 visible on default tab |
| **Minimize related records in header** | Medium | Header loads before form body |
| **Avoid auto-refresh on subgrids** | Medium | Set to manual refresh where possible |
| **Use quick view forms sparingly** | Medium | Each quick view = additional data fetch |
| **Minimize JavaScript on form load** | High | Defer non-critical scripts; use event-driven loading |
| **Use business rules over JavaScript** | Medium | Business rules run server-side and are more cacheable |

### Tab Loading Strategy

```
Form opens:
  1. Header loads (keep lightweight)
  2. First tab loads (primary data, 2-3 subgrids max)
  3. Other tabs: set "Expanded by default" = No
     → Load only when user clicks the tab
```

### Subgrid Optimization

| Setting | Recommendation |
|---------|---------------|
| **Records per page** | 4-10 (not 25+) for subgrids on the default tab |
| **Default view** | Use a view that selects minimal columns |
| **Quick Find columns** | Limit to 3-4 indexed columns |
| **Editable grid** | Avoid on default tab; use read-only and edit in a form |

### Custom Control Performance

- **PCF controls**: Load asynchronously, so they do not block form rendering
- **Virtual PCF controls**: Use `ReactControl` base class for better rendering performance
- **Bundle size**: Keep control bundle under 200 KB for fast initial load
- **Web API calls**: Batch multiple requests using `$batch` endpoint

### View Optimization

| Technique | Details |
|-----------|---------|
| **Limit columns** | 5-8 columns per view; more columns = wider queries |
| **Indexed filters** | Ensure view filter columns have database indexes |
| **Avoid calculated columns in views** | These compute per-row at query time |
| **System views over personal** | System views are cached more aggressively |
| **FetchXML tuning** | Use `no-lock="true"` for read-only views |

---

## 4. Power Automate Performance

### Concurrency Control

Cloud flows support parallel execution of loops and triggers.

| Setting | Location | Impact |
|---------|----------|--------|
| **Trigger concurrency** | Trigger settings > Concurrency Control | How many flow instances run simultaneously |
| **Apply to each concurrency** | Action settings > Concurrency Control | How many loop iterations run in parallel |
| **Default concurrency** | 1 (sequential) | Safe but slow |
| **Max concurrency** | 50 | Fast but watch API throttling |

```json
// Enable concurrency on Apply to each
{
  "type": "Foreach",
  "foreach": "@body('Get_items')?['value']",
  "runAfter": { "Get_items": ["Succeeded"] },
  "runtimeConfiguration": {
    "concurrency": {
      "repetitions": 20
    }
  }
}
```

**When to increase concurrency:**
- Processing independent items (no shared state)
- Target API supports high throughput
- Items do not need ordered processing

**When to keep concurrency at 1:**
- Items depend on prior item's result
- Target API has strict rate limits
- Maintaining insertion order matters

### Pagination and Large Datasets

By default, actions like "List rows" return a page of results (typically 250-5,000).

```
Enable pagination:
  Action settings > Settings > Pagination = On
  Set threshold (max 100,000 for most connectors)
```

| Connector | Default Page Size | Max with Pagination |
|-----------|-------------------|---------------------|
| Dataverse "List rows" | 5,000 | 100,000 |
| SharePoint "Get items" | 100 | 100,000 |
| SQL "Get rows" | 2,048 | 100,000 |

**For datasets exceeding 100,000 rows:**

```
Do Until loop:
  1. List rows with $top=5000 and $skiptoken
  2. Process the batch
  3. Check if @odata.nextLink exists
  4. If yes, use the nextLink URL for the next batch
  5. If no, exit loop
```

### Chunking Large Datasets

When processing thousands of items, chunk them to avoid timeouts and memory limits.

```
// Pattern: Process in batches of 500
Initialize variable: varSkip = 0
Initialize variable: varBatchSize = 500
Initialize variable: varHasMore = true

Do Until: varHasMore equals false
  ├── List rows (top: varBatchSize, skip: varSkip)
  ├── Condition: length of results > 0
  │   ├── Yes:
  │   │   ├── Apply to each (with concurrency = 20)
  │   │   │   └── Process item
  │   │   └── Set varSkip = varSkip + varBatchSize
  │   └── No:
  │       └── Set varHasMore = false
```

### Apply to Each Optimization

| Optimization | Details |
|-------------|---------|
| **Move operations outside the loop** | Initialize variables, fetch reference data before the loop |
| **Use Select instead of Apply to each** | For data transformation without side effects |
| **Use Filter array** | Reduce items before entering the loop |
| **Batch API calls** | Collect items, then use a single batch action |

```json
// Bad: API call inside loop for each item
"Apply_to_each": {
  "actions": {
    "Get_user_profile": {
      "inputs": { "id": "@items('Apply_to_each')?['userId']" }
    }
  }
}

// Better: Batch with Select + single API call
"Select_user_ids": {
  "type": "Select",
  "inputs": {
    "from": "@body('Get_items')?['value']",
    "select": { "id": "@item()?['userId']" }
  }
}
```

### Minimize Actions and Triggers

| Tip | Reason |
|-----|--------|
| Use expressions over Compose actions | Each action adds ~0.5s overhead |
| Combine conditions with `and()`/`or()` | Fewer branching actions |
| Use `Select` and `Filter array` | Avoid loops for transformations |
| Trigger conditions | Filter at trigger level to avoid running unnecessary flow instances |

```
// Trigger condition: only run flow when Status = "Approved"
@equals(triggerBody()?['Status'], 'Approved')
```

---

## 5. API Limits and Throttling

### Request Limits Per License

| License Type | API Requests / 24 hours |
|-------------|------------------------|
| Power Apps per user | 40,000 |
| Power Apps per app | 6,000 per user per app |
| Power Automate per user | 40,000 |
| Power Automate per flow | 250,000 (shared across all users of the flow) |
| Power Apps (seeded from D365) | 40,000 |
| Dynamics 365 Enterprise | 40,000 |
| Dynamics 365 Professional | 20,000 |
| Power Platform request add-on | 50,000 per pack |
| Pay-as-you-go | $0.00004 per request over base |
| Non-licensed users (app access) | 6,000 |

**Note:** Flows using premium connectors require per-user or per-flow premium licensing. Limits are enforced per-user within a 24-hour sliding window.

### Service Protection Limits (Dataverse)

These are hard limits to protect server health. Exceeding them returns HTTP 429.

| Limit | Threshold | Window |
|-------|-----------|--------|
| **Number of requests** | 6,000 | 5-minute sliding window |
| **Execution time** | 20 minutes | 5-minute sliding window |
| **Concurrent requests** | 52 | Per user per server |

### Handling HTTP 429 (Too Many Requests)

When a 429 response is received:

1. Read the `Retry-After` header (value in seconds)
2. Wait for the specified duration
3. Retry the request
4. Use exponential backoff if no `Retry-After` header is present

**Power Automate retry configuration:**

```json
{
  "retryPolicy": {
    "type": "exponential",
    "count": 4,
    "interval": "PT7S",
    "minimumInterval": "PT5S",
    "maximumInterval": "PT1H"
  }
}
```

**Canvas app retry pattern:**

```powerfx
// Retry with notification
Set(varRetryCount, 0);
Set(varSuccess, false);

While(
    !varSuccess && varRetryCount < 3,
    IfError(
        Patch(DataSource, record, changes);
        Set(varSuccess, true),
        // On error:
        Set(varRetryCount, varRetryCount + 1);
        If(
            varRetryCount < 3,
            Notify("Retrying... attempt " & varRetryCount, NotificationType.Warning)
        )
    )
);

If(!varSuccess, Notify("Operation failed after 3 attempts", NotificationType.Error))
```

### Minimizing API Consumption

| Strategy | Savings |
|----------|---------|
| Use `$select` to request only needed columns | 20-50% fewer bytes, faster responses |
| Use `$filter` server-side instead of client-side Filter | Avoids pulling entire tables |
| Batch operations (up to 1,000 per batch in Dataverse) | 1 API call instead of 1,000 |
| Cache reference data in collections | Eliminates repeated lookups |
| Use `$top` to limit result sets | Prevents over-fetching |
| Debounce search inputs with `DelayOutput` | Prevents rapid-fire queries |

---

## 6. Batch Processing Patterns

### ForAll with Patch (Canvas Apps)

```powerfx
// Bulk create/update records
ForAll(
    colItemsToSave As item,
    Patch(
        TargetTable,
        Defaults(TargetTable),
        {
            Name: item.Name,
            Amount: item.Amount,
            Category: item.Category
        }
    )
);
```

**Limitations of ForAll + Patch:**
- Each `Patch` inside `ForAll` is a separate API call (not batched)
- For 100+ records, this is slow and consumes many API requests
- No built-in concurrency in ForAll

**Better approach for bulk operations:**

```powerfx
// Use Patch with a table argument (single batch call)
Patch(
    TargetTable,
    Table(
        { Name: "Item1", Amount: 100 },
        { Name: "Item2", Amount: 200 },
        { Name: "Item3", Amount: 300 }
    )
)
// Sends one batch request to Dataverse (up to 1,000 records)
```

### Bulk Operations in Power Automate

**Dataverse batch operations:**

```
// Perform a changeset (batch) action
Action: "Perform a bound action" or HTTP request to Dataverse
URL: /api/data/v9.2/$batch
Content-Type: multipart/mixed; boundary=batch_id

Each batch can contain up to 1,000 operations
Operations in a changeset are transactional (all succeed or all fail)
```

**Practical pattern with Apply to Each + batching:**

```
1. Get all source records
2. Select: transform to target format
3. Initialize varBatch as empty array
4. Apply to each:
   a. Append current item to varBatch
   b. Condition: length(varBatch) >= 500
      Yes:
        - Call child flow / HTTP batch endpoint with varBatch
        - Set varBatch = empty array
      No: continue
5. After loop: process remaining items in varBatch
```

---

## 7. Dataverse Query Optimization

### Select Minimal Columns

Every column requested increases response size and query cost.

```powerfx
// Canvas app: use explicit column selection
// In the Items property, reference only needed columns:
ShowColumns(
    Filter(Accounts, Revenue > 1000000),
    "name", "revenue", "primarycontactid"
)
```

```http
// Web API: use $select
GET /api/data/v9.2/accounts?$select=name,revenue&$filter=revenue gt 1000000
```

**In Power Automate:**
- Use "Select columns" parameter in the "List rows" action
- Specify exact column names separated by commas
- This sends `$select` to Dataverse, reducing payload size by 60-80%

### Indexed Filters

Dataverse automatically indexes primary key, lookup, and some standard columns. For custom columns used frequently in filters:

| Index Type | How to Create |
|-----------|---------------|
| **Automatic** | Primary key, lookup columns, status columns |
| **Custom** | Solution > Entity > Keys/Indexes > Add |
| **Composite** | Create a key with multiple columns for multi-column filters |

**Check if your filter columns are indexed:**
1. Navigate to `make.powerapps.com` > Tables > [Table] > Keys
2. Review existing keys (each key creates an index)
3. Add keys for frequently filtered column combinations

### Avoid Expensive Query Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| `Filter(Accounts, "contoso" in name)` | `in` (contains) cannot use index | Use `StartsWith` or full-text search |
| Filtering on calculated columns | Computes per-row at query time | Use stored/pre-computed values |
| Cross-entity filters without lookups | Causes joins or sub-selects | Use lookup columns for related filtering |
| `Sort` on non-indexed column | Full table scan | Add index on sort column |
| No `$top` on large tables | Returns max page, transfers excess data | Always set a reasonable limit |
| `Distinct` on large tables | Scans entire table | Use aggregation or pre-compute distinct values |

### FetchXML Optimization (Advanced)

```xml
<!-- Optimized FetchXML: select only needed columns, use indexed filters, limit results -->
<fetch top="50" no-lock="true" distinct="false">
  <entity name="account">
    <attribute name="name" />
    <attribute name="revenue" />
    <attribute name="primarycontactid" />
    <filter type="and">
      <condition attribute="statecode" operator="eq" value="0" />
      <condition attribute="revenue" operator="gt" value="1000000" />
    </filter>
    <order attribute="revenue" descending="true" />
    <link-entity name="contact" from="contactid" to="primarycontactid" link-type="inner">
      <attribute name="fullname" />
      <attribute name="emailaddress1" />
    </link-entity>
  </entity>
</fetch>
```

**FetchXML performance tips:**
- Use `no-lock="true"` for read-only queries (avoids shared locks)
- Use `top` to limit results
- Use `link-type="inner"` instead of `outer` when you only want matched records
- Avoid `distinct="true"` unless absolutely necessary
- Place the most selective filter condition first

---

## 8. Cross-Cutting Performance Patterns

### Monitor Tool (Canvas Apps)

Use the built-in Monitor to identify performance bottlenecks:

1. Open the app in Power Apps Studio
2. Go to **Advanced tools > Monitor**
3. Play the app and interact with it
4. Review the waterfall chart for:
   - Long-running data calls (> 500ms)
   - Redundant API calls (same endpoint called multiple times)
   - Large response payloads (> 1 MB)
   - Non-delegable warnings

### Solution Checker Performance Rules

Run Solution Checker before deploying. It flags:

| Rule | Description |
|------|-------------|
| `app-formula-issues-rule` | Non-delegable formulas that hit row limits |
| `app-OnStart-rule` | Excessive logic in OnStart blocking app load |
| `web-use-async` | Synchronous XHR calls in JavaScript |
| `web-avoid-window-top` | Deprecated `window.top` usage |
| `web-use-client-api` | Direct DOM manipulation instead of client API |

### Network Optimization

| Technique | Where | Impact |
|-----------|-------|--------|
| **Reduce app size** | Canvas apps | Remove unused media, screens, and controls |
| **Enable app preloading** | Model-driven apps | Admin center > Environment settings |
| **CDN for static assets** | Power Pages | Serve images/CSS from CDN |
| **Compress images** | All | Use WebP format, max 150 KB per image |
| **Minimize custom fonts** | All | Each font file adds 50-200 KB to load time |

### Performance Testing Checklist

1. Test with realistic data volumes (not 10 rows; use 10,000+)
2. Test on the slowest target device (mobile on 4G)
3. Test with the target user's security role (RLS adds query overhead)
4. Measure app load time (target: under 4 seconds)
5. Measure gallery scroll performance (target: no visible lag)
6. Measure form save time (target: under 2 seconds)
7. Monitor API request count per session (target: under 200 for typical workflow)
8. Check for delegation warnings in the formula bar (fix all blue underlines)

---

## 9. Performance Quick Reference

### Canvas App Load Time Targets

| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| App launch | < 3s | 3-6s | > 6s |
| Screen navigation | < 1s | 1-3s | > 3s |
| Gallery load (50 items) | < 2s | 2-4s | > 4s |
| Form submit | < 2s | 2-4s | > 4s |
| Search results | < 1s | 1-3s | > 3s |

### Top 10 Performance Fixes (Highest Impact First)

1. Move data loading from `OnStart` to `App.Formulas` or `Screen.OnVisible`
2. Use `Concurrent()` for parallel data fetches
3. Ensure all gallery `Filter` operations are delegable
4. Add `$select` (explicit columns) to all data operations
5. Cache reference data in local collections
6. Reduce controls per gallery row to fewer than 6
7. Enable concurrency on Power Automate `Apply to each` loops
8. Use batch `Patch` (table argument) instead of `ForAll` + `Patch`
9. Collapse non-default form tabs (auto-expand = false)
10. Add Dataverse indexes on frequently filtered columns

> See also: canvas-apps-complete.md for app patterns, power-automate-cloud-flows.md for flow patterns, dataverse-developer-api.md for API details.
