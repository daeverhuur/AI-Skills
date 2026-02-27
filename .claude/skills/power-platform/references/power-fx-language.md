# Power Fx Language Reference

## Overview

Power Fx is the low-code language across Microsoft Power Platform. Strongly typed, declarative, functional, inspired by Excel.

**Design principles**: Think spreadsheet (formulas bind expressions to identifiers, changes propagate automatically). Always live (no compile/run). Declarative (define what, not how). Functional (pure functions preferred). Not object-oriented (`Len("Hello")` not `"Hello".length`). No undefined value (uninitialized = blank).

## Locale Separator Rules

| Decimal | List separator | Chaining operator |
|---------|---------------|-------------------|
| `.` dot | `,` comma | `;` semicolon |
| `,` comma | `;` semicolon | `;;` double semicolon |

Function names, property names, enumerations, operators are ALWAYS English regardless of locale.

## Data Types

| Type | Example |
|------|---------|
| Boolean | `true`, `false` |
| Text | `"Hello"` |
| Number | `123` (alias for Decimal or Float) |
| Decimal | High precision, base 10, range 10^28, 28 digits |
| Float | IEEE 754, base 2, range 10^308, 15 digits |
| Date | `Date(2024,5,16)` — no time, user timezone |
| Time | `Time(11,23,45)` |
| DateTime | `DateTimeValue("May 16, 2024 1:23 PM")` |
| Currency | Floating-point with currency format |
| Color | `Color.Red`, `RGBA(255,128,0,0.5)` |
| Record | `{ Company: "Northwind", Staff: 35 }` |
| Table | `Table({ Name: "A" }, { Name: "B" })` |
| Choice | Choice from set, backed by number |
| GUID | `GUID()` |
| Hyperlink/Image/Media | Text strings with URI semantics |
| Dynamic | Runtime-typed, from `ParseJSON()` |
| Void | No return, for behavior UDFs |

**Blank**: All types can be blank. `Blank()` to set, `IsBlank()` to test, `Coalesce()` for fallback.

**Decimal vs Float**: Mixing causes Decimal to convert to Float (may lose precision). Use Decimal for business, Float for scientific.

**String interpolation**: `$"We have {Apples} apples and {Bananas} bananas."`

## Operators

| Symbol | Purpose |
|--------|---------|
| `.` | Property access: `Slider1.Value` |
| `+` `-` `*` `/` `^` | Arithmetic |
| `%` | Percentage: `20%` = `* 1/100` |
| `=` `<>` `>` `>=` `<` `<=` | Comparison |
| `&` | String concatenation |
| `&&` / `And` | Logical AND |
| `\|\|` / `Or` | Logical OR |
| `!` / `Not` | Logical NOT |
| `in` | Membership (case-insensitive) |
| `exactin` | Membership (case-sensitive) |
| `@` | Disambiguation: `Table[@field]`, `[@GlobalVar]` |
| `As` | Rename in scope: `AllCustomers As Customer` |

**Context keywords**: `Self` (current control), `Parent` (container), `ThisItem` (gallery/form record), `ThisRecord` (record scope).

**Identifiers**: Simple `MyName`, with spaces `'Name with spaces'`, escape quotes `'It''s here'`.

## Tables

```powerfx
// Inline table
Table({ Value: "Strawberry" }, { Value: "Vanilla" })
// Single-column shorthand (column named "Value")
[ "Strawberry", "Vanilla" ]
// Inline record
{ Name: "Strawberries", Price: 7.99 }
```

**Record scope**: Functions like Filter create a scope where fields are top-level identifiers:
`Filter(Products, 'Qty Requested' > 'Qty Available')`

**Disambiguation**: `Value` = innermost scope, `X[@Value]` = outer scope X, `[@Value]` = global scope.

## Variables (3 Types)

| Type | Scope | Set with | Use case |
|------|-------|----------|----------|
| Global | App-wide | `Set(var, val)` | Any value, all screens |
| Context | Screen | `UpdateContext({var: val})` | Screen parameters |
| Collection | App-wide | `Collect()`, `ClearCollect()` | Mutable tables |

```powerfx
Set(MyVar, 1)                                          // Global
UpdateContext({ Total: Total + 1 })                    // Context
Navigate(Screen1, None, { RunningTotal: -1000 })       // Context via nav
Collect(PaperTape, TextInput1.Text)                    // Collection
ClearCollect(MyCollection, dataSource)                 // Replace collection
```

**Lifetime**: In memory while app runs, lost on close. Persist with SaveData/LoadData (mobile only) or Patch to data source.

**Precedence**: Context > Global > Collection. Use `[@Name]` to disambiguate.

## Imperative Logic

**Declarative** (property formulas): Calculate values, recalculate automatically (Label.Text, Control.Fill).
**Imperative** (behavior formulas): Change state, triggered by events (Button.OnSelect, Screen.OnVisible).

Behavior functions: `Back()`, `Navigate()`, `Refresh()`, `Patch()`, `Remove()`, `RemoveIf()`, `Update()`, `UpdateIf()`, `Set()`, `UpdateContext()`, `Collect()`, `Clear()`, `ClearCollect()`.

**Chaining**: `UpdateContext({ x: 1 }); Back()` — sequential execution with semicolons.

## Delegation (CRITICAL)

Delegation = Power Apps translates the query to run server-side. Non-delegable = fetches first 500 records (max configurable to 2,000), processes locally. THIS IS THE MOST COMMON SOURCE OF DATA BUGS.

### Delegable data sources
Dataverse, SharePoint, SQL Server, Salesforce.

### Delegable functions
- **Filter**, **Search**, **LookUp**, **First**
- Within Filter/LookUp: `And`, `Or`, `Not`, `In`, `=`, `<>`, `>=`, `<=`, `>`, `<`, `+`, `-`, `TrimEnds`, `IsBlank`, `StartsWith`, `EndsWith`
- **Sort** (single column), **SortByColumns**
- Aggregates: `Sum`, `Average`, `Min`, `Max`, `CountRows`, `Count`

### NOT delegable (runs locally, data truncated)
`If`, `*`, `/`, `Mod`, `Text`, `Value`, `Concatenate`, `&`, `exactin`, `Lower`, `Upper`, `Left`, `Mid`, `Len`, `FirstN`, `Last`, `LastN`, `Choices`, `Concat`, `Collect`, `ClearCollect`, `GroupBy`, `Ungroup`

### Delegation limits
- Max 2 lookup levels deep
- Max 20 entity joins
- Entity property must be on LEFT side of equality
- Sort: single column name only
- Warning indicators: yellow triangle / blue underline in Studio

**Dev tip**: Set data row limit to 1 during development to catch delegation issues early.

## Named Formulas

Defined in `App.Formulas`. Bind name to expression, reusable throughout app:

```powerfx
App.Formulas:
    BGColor = ColorValue(Param("BackgroundColor"));
    UserEmail = User().Email;
    UserInfo = LookUp(Users, 'Primary Email' = User().Email);
    UserTitle = UserInfo.Title;
```

**Advantages over OnStart variables**: Always available (no timing dependency), always up to date (auto-recalculate), immutable (single source of truth), deferred calculation (only when needed), independent evaluation (up to 80% faster Studio load).

**Migration**: `Set(varColor, RGBA(0,0,0,1))` becomes `varColor = RGBA(0,0,0,1);`

## User-Defined Functions (UDFs)

Defined in `App.Formulas`:

```powerfx
FunctionName(Param1: Type1, Param2: Type2): ReturnType = Formula;

// Pure function
LibraryGenre(Genre: Text): LibraryType = Filter(Library, Genre = Genre);

// Behavior UDF (side effects)
Spend(Amount: Number): Void = {
    If(Amount > Savings,
        Error($"{Amount} exceeds savings"),
        Set(Savings, Savings - Amount);
        Set(Spent, Spent + Amount)
    );
}
```

**Limitations**: No recursion. User-defined types are experimental.

## Error Handling

| Function | Purpose |
|----------|---------|
| `IfError(Value, Replacement, ...)` | Test for errors, provide replacement |
| `IsError(Value)` | Returns Boolean |
| `IsBlankOrError(Value)` | Blank OR error check |
| `Error({ Kind: ErrorKind.X, Message: "..." })` | Create/rethrow custom error |

**Error chaining** (if first fails, second NOT attempted):
```powerfx
IfError(
    Patch(DS1, ...), Notify("problem in first"),
    Patch(DS2, ...), Notify("problem in second")
)
```

**Error record fields**: Kind (ErrorKind enum), Message, Source, Observed, Details.

**App.OnError** (global handler):
```powerfx
Trace($"Error {FirstError.Message} in {FirstError.Source}");
Error(FirstError)  // Rethrow to show default banner
```

## Expression Grammar

**Comments**: `// single line`, `/* multi-line */`
**Literals**: `true`, `false`, `123`, `1.23e10`, `"Hello"`, `"She said ""Hi"""`

## YAML Formula Grammar (Source Files)

Leading `=` required: `Visible: =true`. For multi-line: use YAML block scalar `|`.
Pitfalls: `#` in single-line = YAML comment (use multiline), `:` in values = YAML name map (use multiline).

## Data Sources

**Types**: Tabular (Excel, SharePoint, SQL, Dataverse), Action-based (email, calendars), Collections (local).

**CRUD**: Create (`Patch`, `Collect`), Read (`Refresh`, auto-load), Update (`Patch`, `Update`, `UpdateIf`), Delete (`Remove`, `RemoveIf`).

**Validation**: `DataSourceInfo()` for schema, `Validate()` for field/record checks, `Errors()` for error info.
