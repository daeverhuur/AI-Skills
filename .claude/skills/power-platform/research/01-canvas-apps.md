# Canvas Apps Core Research
## Sources: 22 of 23 successfully fetched

---

## 1. Getting Started with Canvas Apps
Canvas apps are custom business applications created in Power Apps without writing code. The canvas is a blank design surface where you drag and drop components.

### Capabilities
- Connect to data from hundreds of sources (Microsoft 365, Dataverse, SharePoint, etc.)
- Create responsive designs for browsers and mobile devices
- Use AI-powered Copilot to build apps through natural language
- Share apps securely within an organization
- Embed in SharePoint, Power BI, and Microsoft Teams

### Build Entry Points
- Plan Designer, blank canvas app, Copilot conversation, from Dataverse, from SharePoint list, from Excel data

### Prerequisites
- Power Apps license, Organization account or Microsoft Developer Program account

---

## 2. Create a Blank Canvas App
### Prerequisites
- Environment Maker security role (directly or through Dataverse team in AAD Security Group)
- Custom security roles NOT supported for canvas app maker scenarios

### Steps
1. Sign in to Power Apps (make.powerapps.com)
2. Create > Start from blank
3. Choose format: responsive, tablet, or phone
4. App opens in Power Apps Studio

---

## 3. Create from Excel / Dataverse Data

### Three Approaches

| Approach | Benefits |
|---|---|
| Upload Excel/CSV to Power Apps | Creates Dataverse table; secure cloud storage; max 5GB |
| Connect to external Excel file | Fast; data stays in place; uses Excel Online connector |
| Blank canvas app + Excel data | Full flexibility and customization |

### Upload Excel/CSV
- Max file size: 5 GB
- Converts to Dataverse table
- First 20 rows uploaded immediately; rest in background

### Connect to External Excel
- File must be in cloud (Dropbox, Google Drive, OneDrive)
- Uses Excel Online (Business) connector

### Key Formulas for Excel-Connected App
```powerfx
// Gallery Items with search and sort
SortByColumns(
    Search(Schedule, TextSearchBox1.Text, "Volunteer"),
    "Volunteer",
    If(SortDescending1, SortOrder.Descending, SortOrder.Ascending)
)

// CRUD operations
Refresh(Schedule)
NewForm(EditForm1); Navigate(ChangeScreen, ScreenTransition.None)
EditForm(EditForm1); Navigate(ChangeScreen, ScreenTransition.None)
ResetForm(EditForm1); Navigate(ViewScreen, ScreenTransition.None)
SubmitForm(EditForm1); Navigate(ViewScreen, ScreenTransition.None)
Remove(Schedule, BrowseGallery1.Selected); Navigate(ViewScreen, ScreenTransition.None)
```

---

## 4. Screens and Navigation

### Prebuilt Screen Types
- **Welcome screen**: Customizable tiles with images, titles, descriptions
- **Header and gallery**: Product catalog style
- **Header and form**: Full-screen form with submit/cancel
- **Header and table**: Data table display
- **Table and form**: Combined with built-in Power Fx (New, Edit, Delete, Submit, Cancel)
- **Approval request**: Form + submit + gallery with predefined stages

### Navigation Functions
```powerfx
Navigate(Target, Fade)        // Navigate to screen
Back()                        // Return to previous screen
```
- Set **StartScreen** property for first screen displayed
- Reorder screens via Tree View overflow menu

---

## 5. Add and Configure Controls

### Adding Controls
1. Select Insert from authoring menu
2. Choose control type (Button, Label, Gallery, etc.)
3. Control appears with six resize handles

### Configuring
- **Properties pane**: Visual configuration
- **Formula bar**: Set properties with formulas
- **Position**: X and Y coordinates (0,0 is top-left)
- **Size**: Height and Width

### Display Text Types
- Literal string: `"Hello, world"`
- Expression: `Screen2.Height`
- Formula: `Text(Now(), DateTimeFormat.ShortDateTime)`

---

## 6. Forms — Show, Edit, Add Records

### Form Types
- **Display form**: Read-only, shows all fields
- **Edit form**: Edit fields, add records, save changes

### Setup Steps
1. Add Drop down control (Items = data source, Value = display column)
2. Add Edit form control
3. Set DataSource property
4. Set Item property to `DropDown.Selected`
5. Edit fields via Properties > Edit fields

### Key Formula
```powerfx
SubmitForm(EditForm)
```

---

## 7. Galleries — Show Lists

### Setup
1. Insert > Gallery > Vertical
2. Set Items to data source
3. Choose Layout

### Filter and Sort
```powerfx
Sort(
    Filter(FlooringEstimates,
        IsBlank(TextSearchBox1.Text) || TextSearchBox1.Text in Text(Name)),
    Name,
    If(SortDescending1, SortOrder.Descending, SortOrder.Ascending)
)
```

### Highlight Selected
```powerfx
If(ThisItem.IsSelected, LightCyan, White)
```

### Default Selection
```powerfx
Index(FlooringEstimates, 5)
LookUp(FlooringEstimates, Category = "Hardwood")
```

---

## 8. Delegation (CRITICAL CONCEPT)

### Core Concept
- **Delegation** = Power Apps sends query to data source for server-side processing
- **Nondelegable** = can't translate; retrieves first 500 records, processes locally
- Default limit: 500 records (changeable to max 2,000)

### Delegable Data Sources
Microsoft Dataverse, SharePoint, SQL Server, Salesforce

### Data NOT Needing Delegation
Imported Excel, Collections, Context variable tables (all in memory)

### Delegable Functions
- **Filter**, **Search**, **First**, **LookUp**
- Within Filter/LookUp: And (&&), Or (||), Not (!), In, =, <>, >=, <=, >, <, +, -, TrimEnds, IsBlank, StartsWith, EndsWith
- **Sort**, **SortByColumns** (single column name only)
- Aggregates: Sum, Average, Min, Max, CountRows, Count

### NOT Delegable (Notable)
- If, *, /, Mod, Text, Value (column casting)
- Concatenate (&), ExactIn
- String: Lower, Upper, Left, Mid, Len
- FirstN, Last, LastN, Choices, Concat, Collect, ClearCollect, GroupBy, Ungroup

### Query Limitations
- Max 2 lookup levels in a query expression
- Max 20 entity joins per query
- Entity property must be on left side (LHS) of equality

### Warnings
- Yellow triangle / blue underline = delegation warning
- Set data row limit to 1 during development to detect issues

---

## 9. Connectors

### Types
- **Tables**: Auto-retrieves/updates data
- **Actions**: Manually connect; use Patch for custom updates
- **Standard**: No special licensing
- **Custom**: For services without built-in connectors

### Limits
- Max 10 connectors per canvas app
- Max 20 connection references

### Authentication Types
1. **Microsoft Entra ID**: Most secure; no extra sign-in
2. **OAuth**: Users supply credentials
3. **Shared/Secure implicit connections**: Author provides credentials, shared with users
4. **Windows Authentication**: NOT secure; for on-premises via gateway

### Data Sources in Solutions
Use connection references and environment variables for cross-environment portability

---

## 10. Working with Tables and Records

### Inline Syntax
```powerfx
// Record
{ Name: "Strawberries", Price: 7.99 }

// Table
Table(
    { Name: "Chocolate", Price: 3.95, 'Quantity on Hand': 12 },
    { Name: "Bread", Price: 4.95, 'Quantity on Hand': 34 }
)

// Single-column table (square brackets)
[ "Strawberry", "Vanilla" ]
// = Table( { Value: "Strawberry" }, { Value: "Vanilla" } )
```

### Key Table Functions
| Function | Purpose |
|---|---|
| Sort, Filter | Sort and filter records |
| FirstN, LastN | Return first/last N records |
| AddColumns, DropColumns, RenameColumns, ShowColumns | Column manipulation |
| Distinct | Remove duplicates |
| Shuffle | Random order |
| Collect, Clear, ClearCollect | Create/manage collections |
| Patch | Modify records |
| Update, UpdateIf | Update matching records |
| Remove, RemoveIf | Delete matching records |

### Disambiguation Operator (@)
- Nested scopes: `Table[@FieldName]`
- Global values: `[@ObjectName]`
- SharePoint spaces: `Column_x0020_Name`

---

## 11. Working with Variables

### Three Variable Types

| Type | Scope | Functions |
|---|---|---|
| Global variables | App-wide | `Set` |
| Context variables | Screen | `UpdateContext`, `Navigate` |
| Collections | App-wide | `Collect`, `ClearCollect` |

### Examples
```powerfx
// Global
Set(RunningTotal, RunningTotal + TextInput1)

// Context
UpdateContext({ RunningTotal: RunningTotal + TextInput1 })
Navigate(Screen1, None, { RunningTotal: -1000 })

// Collections
Collect(PaperTape, TextInput1.Text)
Clear(PaperTape)
SaveData(PaperTape, "StoredPaperTape")
LoadData(PaperTape, "StoredPaperTape", true)
```

### Variable Lifetime
- Exist only while app runs; lost when app closes
- Initial value: blank
- SaveData/LoadData for persistence (Power Apps Mobile only)

### Naming Precedence
Context variable > Global variable > Collection (use `[@Name]` to disambiguate)

---

## 12. Canvas Components

### Overview
- Reusable building blocks for canvas apps
- Create within app or via component library (recommended for cross-app reuse)
- All instances update when definition changes

### Custom Properties
- **Input property**: Receives data into component
- **Output property**: Emits data or component state

### Example: Menu Component
```powerfx
// Component Items default
Table({Item:"SampleText"})

// On screen, set Items
Table({Item:"Home"}, {Item:"Admin"}, {Item:"About"}, {Item:"Help"})

// Output property (in component)
Gallery1.Selected.Item

// Reading output (in app)
MenuComponent_1.Selected
```

### Access App Scope Toggle
- On: Access global variables, collections, controls on screens, tabular data sources
- Off: Set and Collect create component-scoped variables/collections

### Limitations
- Can't insert component into gallery or form
- No UpdateContext (use Set instead)
- Can't add Power Automate flows in component libraries

---

## 13. Responsive Layouts

### Setup
1. Settings > Display > turn off **Scale to fit**

### Screen Dimensions
```powerfx
Width = Max(App.Width, App.DesignWidth)
Height = Max(App.Height, App.DesignHeight)
```

### Common Layout Patterns
```powerfx
// Fill width with margin N
X = N; Width = Parent.Width - (N * 2)

// Align right with margin N
X = Parent.Width - (C.Width + N)

// Center horizontally
X = (Parent.Width - C.Width) / 2

// Position below D with gap N
Y = D.Y + D.Height + N
```

### Screen Size Breakpoints
| Constant | Value | Device |
|---|---|---|
| ScreenSize.Small | 1 | Phone |
| ScreenSize.Medium | 2 | Tablet (vertical) |
| ScreenSize.Large | 3 | Tablet (horizontal) |
| ScreenSize.ExtraLarge | 4 | Desktop |

```powerfx
// Hide on phone
Parent.Size >= ScreenSize.Medium

// Dynamic width
Parent.Width * Switch(Parent.Size, ScreenSize.Small, 0.5, ScreenSize.Medium, 0.3, 0.25)
```

---

## 14. Offline-Capable Apps

### Connection Signal
```powerfx
Connection.Connected  // true/false
```

### LoadData/SaveData Pattern
```powerfx
// OnStart
If(Connection.Connected,
    ClearCollect(LocalData, DataSource.GetItems());
    Set(statusText, "Online data"),
    LoadData(LocalData, "LocalData", true);
    Set(statusText, "Local data")
);
SaveData(LocalData, "LocalData");
```

### Limitations
- LoadData/SaveData work ONLY in Power Apps Mobile (not Studio or web player)
- Teams apps: limited to 1 MB
- Generally 30-70 MB available memory
- No automatic merge conflict resolution

---

## 15. Performance Tips

### Key Design Principles
1. Optimize page loads: minimize/delay/eliminate startup actions
2. Small data payloads: keep bulk-retrieved data small
3. Optimize query patterns: do data mashups on server, not in app
4. Fast calculations: work with Power Fx, not against it

### Anti-Patterns to Avoid
- Loading too much data at startup
- Turning everything into collections
- Overloading OnStart

---

## 16. Share a Canvas App

### Steps
1. Save and publish app
2. Apps > Select app > Share
3. Enter users/groups
4. Choose: **User** (use only) or **Co-Owner** (use, edit, share)

### App-Level Security Roles
- App reader, App user, App maker, App admin

### Important
- Must also manage data source permissions separately
- Use security groups for 100+ users
- Dataverse tables need appropriate security roles

---

## 17. Save and Publish

### Save Options
- Save, Save with version notes, Save as, Download a copy
- AutoSave: every 2 minutes (toggle in Settings > General)

### Publish
- Command bar > Publish
- Version management: Apps > Details > Versions tab
- Live version is what all shared users see

### In-App Updates
- Users see notification: "A new version of this app is coming"
- Then "You're using an old version" with Refresh button

---

## 18. Test Studio

### Overview
- Low-code testing for canvas apps
- Write tests using Power Apps expressions or recorder
- Play back in Test Studio or web browser

### Terminology
- **Test cases**: Steps to validate functionality
- **Test suites**: Group/organize test cases; run sequentially
- **Test assertions**: Expressions evaluating to true/false

### Best Practices
1. Automate repetitive, high-impact, stable tests
2. Keep test cases small
3. Single test action per expression
4. Every case should have assertions
5. Use test suites to group similar cases

### Limitations
- No support for Components, PCF, nested galleries, media controls
- Not compatible with Git version control

---

## 19. Embed Canvas Apps

### URI Format
```
https://apps.powerapps.com/play/[AppID]?source=iframe
```

### Parameters
- `tenantid`: For guest access
- `screenColor`: RGBA for loading screen
- Custom parameters via `Param()` function

### HTML
```html
<iframe width="[W]" height="[H]"
  src="https://apps.powerapps.com/play/[AppID]?source=website"
  allow="geolocation; microphone; camera"/>
```

### Auth
- Entra ID sites: no additional sign-in
- Other sites: sign-in prompt on iframe
- Only same-tenant users can access

---

## 20. Behavioral Formulas

### Concept
Most formulas calculate values. Behavioral formulas change app state, triggered by user actions.

### Behavioral Functions
- Navigation: `Back()`, `Navigate()`
- Data CRUD: `Refresh()`, `Update()`, `UpdateIf()`, `Patch()`, `Remove()`, `RemoveIf()`
- Context: `UpdateContext()`
- Collections: `Collect()`, `Clear()`, `ClearCollect()`

### Chaining (Semicolons)
```powerfx
UpdateContext({ x: 1 }); Back()
```
- Actions execute sequentially; next waits for current to complete

---

## 21. Accessibility Checker

### Severity Levels
- **Errors**: Make app difficult/impossible for disabled users
- **Warnings**: Difficult for most users with disabilities
- **Tips**: Improve experience

### Common Issues
| Issue | Fix |
|---|---|
| Missing accessible label | Set accessible-label property |
| Focus not showing | Set FocusBorderThickness > 0 |
| Missing captions | Set ClosedCaptionsURL |
| Autostart on | Set Autostart to false |
| Bad screen names | Give descriptive names |

---

## 22. Create App from SharePoint

### Two Methods
1. **From Power Apps**: Home > Start with data > SharePoint > enter URL > select list > Create
2. **From SharePoint**: Open list > Integrate > Power Apps > Create an app

### Generated App (3 screens)
- Browse screen, Details screen, Edit screen
- Bidirectional sync with SharePoint

---

## 23. Geospatial Map Component

### Features
- Plot markers from addresses or lat/long
- Pin clustering, current position, route calculation
- Road/satellite views, shape drawing (GeoJSON)

### Limits
- Max 5,000 pins from lat/long
- Max 50 pins from addresses (geocoding)
- Max 500 shapes

### Key Properties
```powerfx
Items = Locations
ItemLabels = "Name"
ItemLongitude = "Longitude"
ItemLatitude = "Latitude"
```

### Route Properties
- UseRouting, RouteWaypoints_Items, RouteTravelMode (car/truck)
- RouteOptimization (distance/time/none)

### Shape Properties
- ShowShapes, Shapes_Items (GeoJSON), ShapeDrawing, ShapeEditingDeleting
- Events: OnShapeCreated, OnShapeSelected, OnShapeEdited, OnShapeDeleted

---

## Key Patterns
- Canvas apps use a declarative formula model (like Excel) with behavioral formulas for state changes
- Delegation is the #1 performance concept — always design for server-side processing
- Max 10 connectors, max 20 connection references per app
- Three variable types: Global (Set), Context (UpdateContext), Collections (Collect)
- Components enable reuse; component libraries for cross-app sharing
- Responsive design requires disabling Scale to Fit and using formula-based positioning
- Offline support via LoadData/SaveData (mobile only) or Dataverse offline-first
- Test Studio for automated testing with assertions
