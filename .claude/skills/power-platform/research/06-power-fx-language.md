# Power Fx Language Reference Research
## Sources: 18/20 successfully fetched (3 URLs returned 404, alternatives found)

---

## 1. Overview

Power Fx is the low-code language across Microsoft Power Platform. General-purpose, strong-typed, declarative, and functional.

### Key Design Principles
- **Think spreadsheet**: Inspired by Excel. Formulas bind expressions to identifiers. Changes propagate automatically.
- **Always live**: No compile/run mode. Incremental compiler keeps program in sync.
- **Declarative**: Maker defines *what*, system determines *how* and *when*.
- **Functional**: Pure functions without side effects preferred.
- **Strongly typed**: All types known at compile time. Type inference from usage.
- **Not object-oriented**: `Len("Hello")` not `"Hello".length`.
- **No undefined value**: Uninitialized = blank. All types can be blank.
- **Locale-sensitive**: Decimal separator cascades to list separator and chaining operator.

### Separator Rules by Locale

| Decimal separator | List separator | Chaining operator |
|---|---|---|
| `.` (dot) | `,` (comma) | `;` (semicolon) |
| `,` (comma) | `;` (semicolon) | `;;` (double semicolon) |

---

## 2. Data Types

### Complete Type Table

| Type | Description | Example |
|---|---|---|
| **Boolean** | true/false | `true` |
| **Choice** | Choice from set, backed by number | `ThisItem.OrderStatus` |
| **Color** | Color with alpha | `Color.Red`, `RGBA(255,128,0,0.5)` |
| **Currency** | Floating-point with currency format | `123`, `4.56` |
| **Date** | Date without time, user's time zone | `Date(2019,5,16)` |
| **DateTime** | Date with time | `DateTimeValue("May 16, 2019 1:23 PM")` |
| **Decimal** | High precision, base 10, limited range | `Decimal("1.2345")` |
| **Dynamic** | Type varies at runtime | `ParseJSON("{}").Field` |
| **Float** | Standard precision, base 2, wide range | `8.903e121` |
| **GUID** | Globally unique identifier | `GUID()` |
| **Hyperlink** | Text string with hyperlink | `"https://..."` |
| **Image** | URI to image | `"https://example.com/logo.jpg"` |
| **Media** | URI to video/audio | `"https://example.com/intro.mp4"` |
| **Number** | Alias for Decimal (most) or Float (Canvas) | `123` |
| **Record** | Named fields | `{ Company: "Northwind", Staff: 35 }` |
| **Record reference** | Reference to record in table | `First(Accounts).Owner` |
| **Table** | Collection of records | `Table({ Name: "A" }, { Name: "B" })` |
| **Text** | Unicode string | `"Hello, World"` |
| **Time** | Time without date | `Time(11,23,45)` |
| **Void** | No return (behavior UDFs) | `Hi(): Void = { Notify("Hello!") }` |
| **Yes/No** | Two-option, backed by boolean | `ThisItem.Taxable` |

### Blank
All types can be blank. `Blank()` to set, `IsBlank()` to test, `Coalesce()` for fallback.

### Decimal vs Float
- **Decimal**: Base 10, 28 digits, range 10^28. Best for business.
- **Float**: Base 2 (IEEE 754), 15 digits, range 10^308. Best for scientific.
- Mixing: Decimal converts to Float (may lose precision).

### String Interpolation
```powerfx
$"We have {Apples} apples and {Bananas} bananas, total {Apples+Bananas}."
```

---

## 3. Operators and Identifiers

| Symbol | Type | Description |
|---|---|---|
| `.` | Property | `Slider1.Value` |
| `+` `-` `*` `/` `^` | Arithmetic | Math operations |
| `%` | Percentage | `20%` = `* 1/100` |
| `=` `<>` `>` `>=` `<` `<=` | Comparison | Compare values |
| `&` | Concatenation | `"hello" & " world"` |
| `&&` / `And` | Logical AND | `Price < 100 && Qty > 0` |
| `\|\|` / `Or` | Logical OR | Either condition |
| `!` / `Not` | Logical NOT | Negate condition |
| `in` | Membership (case-insensitive) | `"The" in "The keyboard"` |
| `exactin` | Membership (case-sensitive) | `"Windows" exactin text` |
| `@` | Disambiguation | `Table[@field]`, `[@GlobalVar]` |
| `As` | Rename | `AllCustomers As Customer` |
| `Self` | Current control | `Self.Fill` |
| `Parent` | Parent container | `Parent.Fill` |
| `ThisItem` | Gallery/form record | `ThisItem.FirstName` |
| `ThisRecord` | Record scope | `ThisRecord.FirstName` |

### Identifier Names
- Simple: `SimpleName`
- With spaces: `'Name with spaces'`
- Escape quotes: `'Name with ''quotes'''`
- Display names map to logical names automatically

---

## 4. Tables

### Creating Tables
```powerfx
// Inline table
Table({ Value: "Strawberry" }, { Value: "Vanilla" })

// Single-column shorthand
[ "Strawberry", "Vanilla" ]  // Column named "Value"

// Inline record
{ Name: "Strawberries", Price: 7.99 }
```

### Key Table Functions
- **Filter**, **LookUp**, **Search** — Select records
- **Sort**, **SortByColumns** — Order records
- **AddColumns**, **DropColumns**, **RenameColumns**, **ShowColumns** — Reshape
- **FirstN**, **LastN**, **First**, **Last** — Subset
- **Distinct** — Remove duplicates
- **ForAll** — Iterate (can have side effects)
- **Concat** — Join strings from records

### Record Scope
Functions create a scope where fields are top-level identifiers:
```powerfx
Filter(Products, 'Quantity Requested' > 'Quantity Available')
```

### Disambiguation
- `Value` alone = innermost scope
- `X[@Value]` = outer scope X
- `[@Value]` = global scope

---

## 5. Variables

### Three Variable Types

| Type | Scope | Functions | Use Case |
|---|---|---|---|
| Global | App-wide | `Set` | Any value, accessible anywhere |
| Context | Screen | `UpdateContext`, `Navigate` | Screen parameters |
| Collections | App-wide | `Collect`, `ClearCollect` | Tables, modifiable |

### Examples
```powerfx
// Global
Set(MyVar, 1)

// Context
UpdateContext({ RunningTotal: RunningTotal + TextInput1.Text })
Navigate(Screen1, None, { RunningTotal: -1000 })

// Collections
Collect(PaperTape, TextInput1.Text)
ClearCollect(MyCollection, dataSource)
Clear(PaperTape)
```

### Lifetime
- In memory while app runs, lost on close
- Initial value: blank
- Persist: SaveData/LoadData (mobile only) or Patch to data source
- Precedence: Context > Global > Collection (use `[@Name]` to disambiguate)

### Reserved Names
ActiveScreen, DesignHeight, DesignWidth, Height, MinScreenHeight, MinScreenWidth, SizeBreakpoints, StudioVersion, TestCaseId, Testing, TestSuiteId, Theme, Width

---

## 6. Imperative Logic

### Declarative vs Imperative
- **Declarative**: Calculate values, recalculate automatically (Label.Text, Control.Fill)
- **Imperative/Behavior**: Change state, triggered by events (Button.OnSelect, Screen.OnVisible)

### Behavior Functions
- Navigation: `Back()`, `Navigate()`
- Data: `Refresh()`, `Update()`, `UpdateIf()`, `Patch()`, `Remove()`, `RemoveIf()`
- Variables: `Set()`, `UpdateContext()`
- Collections: `Collect()`, `Clear()`, `ClearCollect()`

### Chaining
```powerfx
UpdateContext({ x: 1 }); Back()
```
Sequential execution. Next starts after current completes.

---

## 7. Global Support

### Always English
Function names, control property names, enumeration names, signal records, operators

### Maker-Customizable (Localizable)
Control names, collection names, context variable names

### Formatting Functions
- `Text()` — Format numbers/dates by locale
- `Value()` — Parse number from text
- `DateValue()`, `TimeValue()`, `DateTimeValue()` — Parse dates
- `Language()` — Returns user's language tag (e.g., "en-GB")

---

## 8. Expression Grammar

### Comments
```powerfx
// Single-line comment
/* Multi-line
   comment */
```

### Literals
- Logical: `true`, `false`
- Number: `123`, `1.23`, `1.23e10`
- Text: `"Hello"`, escape with `"She said ""Hi"""`

### Identifiers
- Regular: letters, `_`, digits
- Quoted: `'Name with spaces'` (escape with `''`)
- Context: `Parent`, `Self`, `ThisItem`, `ThisRecord`

---

## 9. YAML Formula Grammar

### Leading Equal Sign Required
```yaml
Visible: =true
X: =34
Text: |
    ="Hello, " & "World"
```

### Component Instances
```yaml
Gallery1 As Gallery.horizontalGallery:
    Fill: =Color.White
    Label1 As Label:
        Text: ="Hello, World"
```

### Pitfalls
- `#` in single-line = YAML comment (use multiline)
- `:` in values = YAML name map (use multiline)
- Normal YAML escaping NOT supported

---

## 10. Formula Reference Overview

Power Fx available in: Canvas apps, Dataverse (formula columns, plug-ins), Model-driven apps, Power Automate (desktop flows), Power Pages, Power Platform CLI. Each function doc shows "Applies to" section.

---

## 11. Delegation (CRITICAL)

### Core Concept
Delegation = Power Apps translates query to run on data source server-side. Non-delegable = gets first 500 records (max 2,000), processes locally.

### Delegable Data Sources
Microsoft Dataverse, SharePoint, SQL Server, Salesforce

### Delegable Functions
- **Filter**, **Search**, **First**, **LookUp**
- Within Filter/LookUp: And (&&), Or (||), Not (!), In, =, <>, >=, <=, >, <, +, -, TrimEnds, IsBlank, StartsWith, EndsWith
- **Sort** (single column), **SortByColumns**
- Aggregates: Sum, Average, Min, Max, CountRows, Count

### NOT Delegable
If, *, /, Mod, Text, Value, Concatenate, &, ExactIn, Lower, Upper, Left, Mid, Len, FirstN, Last, LastN, Choices, Concat, Collect, ClearCollect, GroupBy, Ungroup

### Query Limits
- Max 2 lookup levels
- Max 20 entity joins
- Entity property must be on LEFT side of equality
- Sort: single column name only

### Warnings
Yellow triangle / blue underline. Set data row limit to 1 during dev to catch issues.

---

## 12. Working with Formulas

- No leading `=` sign (unlike Excel)
- Formulas recalculate automatically
- Property formulas (calculate values) vs Behavior formulas (take actions)
- Chain with semicolons: `UpdateContext({x:1}); Back()`

---

## 13. Working with Tables (Canvas)

### Table Operations (Pure, return new tables)
```powerfx
AddColumns(table, "ColName", formula)
DropColumns(table, "ColName")
RenameColumns(table, "Old", "New")
ShowColumns(table, "Col1", "Col2")
```

### Record Scope Functions
AddColumns, Average/Max/Min/Sum, Filter, LookUp, Concat, Distinct, ForAll, Sort, With

---

## 14. Working with Variables (Canvas)

Same as Section 5 with canvas-specific context. Key: context variables take precedence over global variables over collections.

---

## 15. Collections

```powerfx
// Create multi-column
Collect(ProductList, { Product: ProductName.Text, Color: Colors.Selected.Value })

// Remove items
Remove(ProductList, ThisItem)
Clear(ProductList)

// Load from data source
Collect(MySPCollection, ListName)
```

---

## 16. Error Handling

### Functions
| Function | Purpose |
|---|---|
| `IfError(Value, Replacement, ...)` | Test for errors, provide replacement |
| `IsError(Value)` | Returns Boolean |
| `IsBlankOrError(Value)` | Blank OR error |
| `Error(ErrorRecord)` | Create/rethrow custom error |

### IfError for Chaining
```powerfx
IfError(
    Patch(DS1, ...), Notify("problem in first"),
    Patch(DS2, ...), Notify("problem in second")
)
```
If first fails, second NOT attempted.

### Error Records
Fields: Kind (ErrorKind enum), Message (Text), Source (Text), Observed (Text), Details (Record)

### Custom Errors
```powerfx
If(StartDate > EndDate,
    Error({ Kind: ErrorKind.Validation, Message: "Start must be before End" }))
```

### App.OnError
Global error handler. Evaluated when any error occurs:
```powerfx
Trace($"Error {FirstError.Message} in {FirstError.Source}");
Error(FirstError)  // Rethrow to show default banner
```

---

## 17. Named Formulas

Defined in `App.Formulas`. Bind name to expression, reusable throughout app:
```powerfx
App.Formulas:
    BGColor = ColorValue(Param("BackgroundColor"));
    UserEmail = User().Email;
    UserInfo = LookUp(Users, 'Primary Email' = User().Email);
    UserTitle = UserInfo.Title;
```

### Advantages Over Variables
1. Always available (no timing dependency)
2. Always up to date (recalculate automatically)
3. Immutable (single source of truth)
4. Deferred calculation (only when needed)
5. Independent (up to 80% faster Studio load)

### Migration from OnStart
**Before**: `Set(varColor, RGBA(0,0,0,1));`
**After**: `varColor = RGBA(0,0,0,1);`

---

## 18. User-Defined Functions

Defined in `App.Formulas`:
```powerfx
FunctionName(Param1: Type1, Param2: Type2): ReturnType = Formula;
```

### Example
```powerfx
LibraryType := Type([ { Title: Text, Author: Text, Genre: Text } ]);
LibraryGenre(SelectedGenre: Text): LibraryType = Filter(Library, Genre = SelectedGenre);
```

### Behavior UDFs (Side Effects)
```powerfx
Spend(Amount: Number): Void = {
    If(Amount > Savings,
        Error($"{Amount} exceeds savings"),
        Set(Savings, Savings - Amount);
        Set(Spent, Spent + Amount)
    );
}
```

### Limitations
- Recursion NOT yet supported
- User-defined types are experimental

---

## 19. Working with Data Sources

### Types
1. **Tabular**: Tables (Excel, SharePoint, SQL, Dataverse)
2. **Action-based**: Email, calendars, Twitter
3. **Collections**: Local, app-specific

### CRUD Operations
| Operation | Functions |
|---|---|
| Create | `Patch()`, `Collect()` |
| Read | `Refresh()`, automatic loading |
| Update | `Patch()`, `Update()`, `UpdateIf()` |
| Delete | `Remove()`, `RemoveIf()` |

### Validation
- `DataSourceInfo()` — Schema constraints
- `Validate()` — Check value of column or record
- `Errors()` — Error info for specific records/columns

---

## Key Patterns
- Power Fx is Excel-like: declarative formulas that recalculate automatically
- Use named formulas (App.Formulas) over OnStart variables for better performance
- Delegation is THE critical concept — always design for server-side processing
- Three variable types with clear scope rules: Global > Context > Collection
- Error handling: IfError for chaining, App.OnError for global handling
- UDFs support both pure and behavior (side-effect) functions
- Locale affects separators: dot-decimal uses comma-list, comma-decimal uses semicolon-list
