# Canvas Apps Complete Reference

> Building custom business apps on a drag-and-drop canvas using Power Fx formulas, connectors, and data sources.

## Quick Start

1. Sign in at `make.powerapps.com` (requires Environment Maker security role)
2. Create > Start from blank (responsive/tablet/phone) or from data source
3. Build in Power Apps Studio: insert controls, bind data, write formulas
4. Save > Publish > Share

## App Creation Methods

| Method | When to Use | Notes |
|--------|-------------|-------|
| Blank canvas | Full control | Choose responsive/tablet/phone format |
| Excel/CSV upload | Quick table app | Creates Dataverse table; max 5 GB |
| External Excel | Data stays in cloud | Uses Excel Online (Business) connector |
| SharePoint list | CRUD over existing list | Generates Browse/Details/Edit screens |
| Dataverse table | Enterprise data with roles | Best delegation support |
| Copilot | Natural language | Generates starter app from prompt |

**SharePoint**: From Power Apps (Home > Start with data > SharePoint) or from SharePoint (list > Integrate > Power Apps > Create).

## Screens and Navigation

| Template | Contains |
|----------|----------|
| Table and form | Gallery + form with New/Edit/Delete/Submit |
| Header and gallery | Product catalog layout |
| Header and form | Full-screen form with submit/cancel |
| Approval request | Form + gallery with predefined stages |

```powerfx
Navigate(TargetScreen, ScreenTransition.Fade)
Navigate(Screen1, None, { ParamName: "value" })   // Pass context variables
Back()                                             // Return to previous screen
```

Set `App.StartScreen` for the initial screen. Reorder screens via Tree View overflow menu.

> See also: canvas-controls-reference.md for all control properties and events.

## Data Binding Patterns

```powerfx
// Gallery: search + sort
SortByColumns(
    Search(DataSource, TextSearchBox1.Text, "ColumnName"),
    "ColumnName",
    If(SortDescending1, SortOrder.Descending, SortOrder.Ascending))

// Gallery: filter + sort
Sort(
    Filter(DataSource,
        IsBlank(SearchBox.Text) || SearchBox.Text in Text(Name)),
    Name,
    If(SortDescending1, SortOrder.Descending, SortOrder.Ascending))

// Highlight selected row
If(ThisItem.IsSelected, LightCyan, White)

// Set default selection
LookUp(DataSource, Category = "Hardwood")
```

## CRUD Operations

```powerfx
// Form-based CRUD
NewForm(EditForm1); Navigate(EditScreen, None)     // Create mode
EditForm(EditForm1); Navigate(EditScreen, None)    // Edit mode
SubmitForm(EditForm1)                              // Save (create or update)
ResetForm(EditForm1)                               // Discard changes
Remove(DataSource, Gallery1.Selected)              // Delete
Refresh(DataSource)                                // Reload data

// Direct record manipulation
Patch(DataSource, Defaults(DataSource), { Title: "New", Status: "Active" })
Patch(DataSource, LookUp(DataSource, ID = 5), { Status: "Closed" })

// Chain actions with semicolons (sequential execution)
UpdateContext({ Saving: true }); SubmitForm(EditForm1); Navigate(BrowseScreen, None)
```

## Delegation (Critical for Large Data)

Delegation = data source processes the query server-side. Without it, Power Apps retrieves only first **500 records** (max 2,000 via settings) and processes locally.

### Delegable Data Sources

Dataverse (best support), SharePoint, SQL Server, Salesforce. Collections and imported Excel are fully in-memory (no delegation needed).

### Delegable Functions

| Category | Functions |
|----------|-----------|
| Query | Filter, Search, LookUp, First |
| Sort | Sort, SortByColumns (single column only) |
| Aggregate | Sum, Average, Min, Max, CountRows, Count |
| Operators (inside Filter/LookUp) | &&, \|\|, !, In, =, <>, >=, <=, >, <, +, - |
| String (inside Filter/LookUp) | StartsWith, EndsWith, TrimEnds, IsBlank |

### NOT Delegable (common pitfalls)

`If`, `*`, `/`, `Mod`, `Text`, `Value`, `Lower`, `Upper`, `Left`, `Mid`, `Len`, `Concatenate (&)`, `FirstN`, `Last`, `LastN`, `Collect`, `ClearCollect`, `GroupBy`, `Ungroup`

### Rules

- Entity property must be on LEFT side: `Price > 100` works, `100 < Price` does not
- Max 2 lookup levels, max 20 entity joins per query
- Yellow triangle / blue underline = delegation warning
- **Dev tip**: Set data row limit to 1 during development to surface issues early

## Variables

| Type | Scope | Set | Use Case |
|------|-------|-----|----------|
| Global | App-wide | `Set(Name, value)` | App state, preferences |
| Context | Screen | `UpdateContext({Name: value})` | Screen-local state |
| Collection | App-wide | `Collect()` / `ClearCollect()` | In-memory tables |

```powerfx
Set(Total, Total + Value(Input1.Text))               // Global
UpdateContext({ ShowPanel: true })                    // Context
Navigate(Screen2, None, { SelectedID: Gal.Selected.ID }) // Pass via nav
ClearCollect(Cache, DataSource)                      // Collection
```

**Lifetime**: Lost when app closes. Use `SaveData`/`LoadData` for persistence (Mobile only).
**Precedence**: Context > Global > Collection. Use `[@Name]` to disambiguate.

## Tables and Records

```powerfx
{ Name: "Item", Price: 7.99 }                                    // Record
Table({ Name: "A", Qty: 12 }, { Name: "B", Qty: 34 })           // Table
[ "Strawberry", "Vanilla" ]                                       // Single-column
```

| Function | Purpose |
|----------|---------|
| Filter, Sort, SortByColumns | Query and order |
| First, Last, FirstN, LastN, LookUp | Subset / single record |
| AddColumns, DropColumns, RenameColumns | Column manipulation |
| Distinct, Shuffle | Dedup / randomize |
| Collect, Clear, ClearCollect | Collection CRUD |
| Patch, Remove, RemoveIf | Record CRUD |
| CountRows, Sum, Average, Min, Max | Aggregates |

**Disambiguation**: `Table[@Field]` for nested scopes, `[@Object]` for globals. SharePoint spaces: `Col_x0020_Name`.

> See also: power-fx-reference.md for complete function signatures.

## Connectors

**Limits**: Max 10 connectors per app, max 20 connection references.

| Type | Behavior |
|------|----------|
| Tables | Auto-retrieves/updates data |
| Actions | Manual invocation; use Patch for updates |
| Standard | Included in base license |
| Custom | For services without built-in connector |

| Auth Type | Notes |
|-----------|-------|
| Microsoft Entra ID | SSO, no extra sign-in (most secure) |
| OAuth | User provides credentials |
| Shared/Implicit | Author credentials shared with users |
| Windows Auth | On-premises via data gateway only |

**Solution portability**: Use connection references + environment variables for cross-environment deployment.

## Components (Reusable UI)

- Create within app or in a **component library** (recommended for cross-app reuse)
- **Input property**: parent -> component. **Output property**: component -> parent.
- **Access App Scope** toggle: On = access global vars/collections/data; Off = isolated scope.
- **Limits**: No components inside galleries or forms. No UpdateContext (use Set). No flows in component libraries.

```powerfx
// Output property (in component):   Gallery1.Selected.Item
// Read output (in app):             MenuComponent_1.Selected
// Set input (in app):               MenuComponent_1.Items = Table({Item:"Home"}, {Item:"Admin"})
```

## Responsive Layout

1. Settings > Display > turn OFF "Scale to fit"
2. Screen: `Width = Max(App.Width, App.DesignWidth)` / `Height = Max(App.Height, App.DesignHeight)`

| Pattern | Formula |
|---------|---------|
| Fill width, margin N | `X = N; Width = Parent.Width - (N * 2)` |
| Align right, margin N | `X = Parent.Width - (Self.Width + N)` |
| Center horizontal | `X = (Parent.Width - Self.Width) / 2` |
| Stack below D, gap N | `Y = D.Y + D.Height + N` |

| ScreenSize Constant | Value | Device |
|---------------------|-------|--------|
| Small | 1 | Phone |
| Medium | 2 | Tablet portrait |
| Large | 3 | Tablet landscape |
| ExtraLarge | 4 | Desktop |

```powerfx
Visible = Parent.Size >= ScreenSize.Medium                         // Hide on phone
Width = Parent.Width * Switch(Parent.Size, ScreenSize.Small, 1, ScreenSize.Medium, 0.5, 0.33)
```

## Offline Support

```powerfx
If(Connection.Connected,
    ClearCollect(LocalData, DataSource); Set(Status, "Online"),
    LoadData(LocalData, "LocalData", true); Set(Status, "Offline"));
SaveData(LocalData, "LocalData");
```

**Constraints**: LoadData/SaveData = Power Apps Mobile only. Teams: 1 MB limit. General: 30-70 MB. No automatic merge conflict resolution.

## Embedding

```html
<iframe width="800" height="600"
  src="https://apps.powerapps.com/play/[AppID]?source=website&tenantid=[TenantID]"
  allow="geolocation; microphone; camera"/>
```

Read params: `Param("paramName")`. Auth: Entra ID = seamless SSO; others = sign-in prompt. Same-tenant only.

## Testing (Test Studio)

1. Studio > Advanced tools > Test > Create suite > Add cases
2. Each step: set control values + write assertion expressions
3. Run in Test Studio or browser

**Limits**: No components, PCF, nested galleries, or media controls. Not Git-compatible.

## Sharing and Publishing

1. Save (with version notes) > Publish > Share. AutoSave every 2 min.
2. **User** role = run only. **Co-Owner** = run, edit, re-share.
3. Data source permissions managed separately. Use security groups for 100+ users.

## Accessibility

Set `AccessibleLabel` on all interactive controls, `FocusBorderThickness > 0`, `ClosedCaptionsURL` on media, `Autostart = false`, descriptive screen names. Run checker via Studio toolbar icon.

## Geospatial Map

Limits: 5,000 pins (lat/long), 50 pins (geocoded), 500 shapes.

```powerfx
Items = Locations; ItemLabels = "Name"; ItemLatitude = "Lat"; ItemLongitude = "Lon"
```

Route: `UseRouting`, `RouteWaypoints_Items`, `RouteTravelMode` (car/truck), `RouteOptimization` (distance/time).
Shapes: `ShowShapes`, `Shapes_Items` (GeoJSON), events: `OnShapeCreated/Selected/Edited/Deleted`.

## Performance Guidelines

1. Move logic out of OnStart; use `App.StartScreen` instead of Navigate
2. Filter server-side (delegation), not client-side
3. Don't ClearCollect entire tables at startup
4. Use `Concurrent(action1, action2)` for parallel data loads
5. Keep connector count low (max 10)

> See also: canvas-controls-reference.md for control properties, events, and styling.
> See also: power-fx-reference.md for complete function signatures and examples.
