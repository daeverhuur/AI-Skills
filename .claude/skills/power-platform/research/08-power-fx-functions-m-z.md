# Power Fx Functions M-Z Reference

> Source: Microsoft Learn Power Fx documentation
> URL base: https://learn.microsoft.com/en-us/power-platform/power-fx/reference/

## Lower, Upper, Proper

- `Lower( String )` -- Converts all uppercase letters to lowercase
- `Upper( String )` -- Converts all lowercase letters to uppercase
- `Proper( String )` -- Converts first letter of each word to uppercase, rest to lowercase
- All accept single strings or single-column tables. Returns: String or table of strings
- Example: `Proper("E. E. CummINGS")` returns `"E. E. Cummings"`

## Mod

- `Mod( Number, Divisor )` -- Returns the remainder of a division
- Result has the same sign as the divisor
- Example: `Mod(25, 4)` returns `1`; `Mod(-25, 4)` returns `3`

## Navigate, Back

- `Navigate( Screen [, Transition [, UpdateContextRecord ]] )` -- Changes displayed screen
- `Back( [Transition] )` -- Returns to the previously displayed screen
- Transitions: `ScreenTransition.Cover`, `.CoverRight`, `.Fade`, `.None` (default), `.UnCover`, `.UnCoverRight`
- Navigate can set context variables on the target screen via the third argument record
- Back uses the inverse transition by default
- Example: `Navigate(Details, ScreenTransition.Fade, { ID: 12 })`

## Notify

- `Notify( Message [, NotificationType [, Timeout ]] )` -- Displays a banner message to the user
- Types: `NotificationType.Error`, `.Information` (default), `.Success`, `.Warning`
- Timeout: milliseconds, default 10000 (10s). Use 0 for indefinite display
- Character limit: 500 characters. Always returns true
- Example: `Notify("Save successful", NotificationType.Success, 4000)`

## Now, Today, IsToday

- `Now()` -- Returns current date and time (local timezone). Volatile function
- `Today()` -- Returns current date with time set to midnight. Volatile function
- `IsToday( DateTime )` -- Tests if a date/time is between midnight today and midnight tomorrow. Returns: Boolean
- UTC variants: `UTCNow()`, `UTCToday()`, `IsUTCToday()` (Dataverse formula columns only)
- Example: `Text(Now(), "mm/dd/yyyy hh:mm:ss")` returns `"07/11/2021 20:58:00"`

## Abs, Exp, Ln, Power, Log, Sqrt

- `Abs( Number )` -- Returns absolute (non-negative) value
- `Exp( Number )` -- Returns e raised to the power of Number
- `Ln( Number )` -- Returns natural logarithm (base e)
- `Power( Base, Exponent )` -- Returns Base raised to Exponent (equivalent to `^` operator)
- `Log( Number [, Base] )` -- Returns logarithm; Base defaults to 10
- `Sqrt( Number )` -- Returns square root
- All accept single-column tables. Undefined results return blank
- Example: `Power(5, 3)` returns `125`; `Log(64, 2)` returns `6`

## Round, RoundDown, RoundUp, Int, Trunc

- `Round( Number, DecimalPlaces )` -- Rounds up if next digit is 5+, else down
- `RoundDown( Number, DecimalPlaces )` -- Always rounds toward zero
- `RoundUp( Number, DecimalPlaces )` -- Always rounds away from zero
- `Int( Number )` -- Rounds down to nearest integer (away from zero for negatives)
- `Trunc( Number )` -- Truncates to integer (toward zero for negatives)
- DecimalPlaces: positive = right of decimal, 0 = whole number, negative = left of decimal
- Key difference: `Int(-4.3)` = `-5`, `Trunc(-4.3)` = `-4`
- Example: `Round(12.37, 1)` returns `12.4`

## Launch, Param

- `Launch( Address [, Params...] )` -- Launches a webpage or canvas app
- `Param( ParameterName )` -- Retrieves a parameter passed when the app was launched. Returns: String (always text)
- Launch targets: `LaunchTarget.New` (default in browser), `LaunchTarget.Replace`, or custom name
- Parameters can be name-value pairs or a record: `Launch("https://bing.com/search", { q: "Power Apps" })`
- Param returns blank if parameter was not passed. Param names are case-sensitive
- Example: `Param("Navigate")` returns `"Second Screen"` if passed at launch

## ParseJSON

- `ParseJSON( JSONString [, Type] )` -- Parses a JSON string into a Dynamic (untyped) value
- Without Type argument: returns Dynamic value requiring explicit conversion per field
- With Type argument (experimental): returns a typed object directly usable in formulas
- Convert fields: `Value()` for numbers, `Text()` for strings, `Boolean()` for booleans, `DateValue()` for dates
- Arrays: use `ForAll( ParseJSON(json).array, { id: Value(ThisRecord.id) } )` to create typed tables
- Example: `Text(ParseJSON("{ ""name"": ""hello"" }").name)` returns `"hello"`

## Patch

- `Patch( DataSource, BaseRecord, ChangeRecord1 [, ChangeRecord2, ...] )` -- Modifies or creates records
- To create: use `Defaults(DataSource)` as BaseRecord
- To modify: BaseRecord must originate from the data source
- Merge records (no data source): `Patch( Record1, Record2 )` -- later values override earlier
- Batch: pass tables of base/change records for bulk operations
- Returns: the modified or created record. Use `IfError`/`IsError` for error handling
- Example: `Patch(Customers, LookUp(Customers, Name="Contoso"), { Phone: "1-212-555-1234" })`
- Create: `Patch(Customers, Defaults(Customers), { Name: "Contoso" })`

## Rand, RandBetween

- `Rand()` -- Returns pseudo-random number >= 0 and < 1. Volatile function
- `RandBetween( Bottom, Top )` -- Returns pseudo-random integer between Bottom and Top, inclusive
- Both are volatile: re-evaluated when part of a formula with changed dependencies
- Example: `Int(Rand() * 100)` returns random integer 0-99
- Example: `RandBetween(1, 6)` simulates a dice roll

## Refresh

- `Refresh( DataSource )` -- Retrieves a fresh copy of a data source
- No return value. Behavior formula only
- Use to see changes made by other users
- Example: `Refresh(IceCream)`

## Relate, Unrelate

- `Relate( Table1RelatedTable, Table2Record )` -- Links two records via one-to-many or many-to-many relationship
- `Unrelate( Table1RelatedTable, Table2Record )` -- Removes the link between records
- For one-to-many: sets/clears the foreign key field
- For many-to-many: modifies the hidden join table
- Only the first argument's data is auto-refreshed; use `Refresh()` for the second table
- Example: `Relate(First(Products).Contacts, First(Contacts))`

## Remove, RemoveIf

- `Remove( DataSource, Record1 [, Record2, ...] [, RemoveFlags.All] )` -- Removes specific records
- `Remove( DataSource, Table [, RemoveFlags.All] )` -- Removes records from a table
- `RemoveIf( DataSource, Condition [, ...] )` -- Removes records matching all conditions
- RemoveFlags.All removes all copies (for collections with duplicates)
- Both return modified data source as a table. Behavior formulas only
- Example: `Remove(IceCream, LookUp(IceCream, Flavor="Chocolate"))`
- Example: `RemoveIf(IceCream, Quantity > 150)`

## Replace, Substitute

- `Replace( String, StartingPosition, NumberOfCharacters, NewString )` -- Replaces by position
- `Substitute( String, OldString, NewString [, InstanceNumber] )` -- Replaces by matching text
- Without InstanceNumber, Substitute replaces ALL occurrences
- Both accept single-column tables. Returns: modified string(s)
- Example: `Replace("abcdefghijk", 6, 5, "*")` returns `"abcde*k"`
- Example: `Substitute("Quarter 1, 2018", "1", "2", 1)` returns `"Quarter 2, 2018"`

## Reset

- `Reset( Control )` -- Resets a control to its Default property value, discarding user changes
- Cannot reset controls inside Gallery or Edit form from outside those controls
- No return value. Behavior formula only
- Example: `Reset(TextInput1)`

## Revert

- `Revert( DataSource [, Record] )` -- Refreshes and clears errors for a data source or single record
- Use after conflict errors from Patch to start with the conflicting version
- No return value. Behavior formula only
- Example: `Revert(IceCream, LookUp(IceCream, Flavor="Strawberry"))`

## Sequence

- `Sequence( Records [, Start [, Step ]] )` -- Generates a single-column table (column: Value) of sequential numbers
- Records: 0 to 50,000 (rounded down). Start defaults to 1. Step defaults to 1 (can be negative)
- Example: `Sequence(4)` returns table with values 1, 2, 3, 4
- Example: `Sequence(4, 4, -1)` returns 4, 3, 2, 1
- Common pattern: `ForAll(Sequence(10), Collect(MyData, Rand()))`

## Set

- `Set( VariableName, Value )` -- Creates or updates a global variable
- Global variables are available on all screens throughout the app
- Implicitly created on first use. Lost when app closes
- No return value. Behavior formula only
- Example: `Set(Counter, Counter + 1)`
- Example: `Set(Person, { Name: "Milton", Address: "1 Main St" })`

## SetFocus

- `SetFocus( Control )` -- Moves input focus to a specific control
- Works with: Button, Icon, Image, Label, TextInput controls
- Cannot focus controls inside Gallery, Edit form, or Container from outside
- Only works on controls on the same screen. Behavior formula only
- Example: `SetFocus(BillingName)` -- focus on a text input after enabling it

## Shuffle

- `Shuffle( Table )` -- Returns a copy of the table with records in random order
- Same columns and number of rows as input
- Example: `Shuffle(Deck)` -- randomize a card deck collection

## Sort, SortByColumns

- `Sort( Table, Formula [, SortOrder] )` -- Sorts by evaluating formula per record
- `SortByColumns( Table, ColumnName1 [, SortOrder1, ColumnName2, SortOrder2, ...] )` -- Sorts by column names
- SortOrder: `SortOrder.Ascending` (default) or `SortOrder.Descending`
- SortByColumns also supports custom sort order via a single-column table of values
- Nested Sort for multi-column: `Sort(Sort(Contacts, LastName), FirstName)`
- Example: `SortByColumns(IceCream, "Quantity", SortOrder.Descending)`

## Split

- `Split( Text, Separator )` -- Splits text into a single-column table (column: Value) of substrings
- Zero-length separator splits each character individually. No match returns entire string as one result
- Example: `Split("Apples, Oranges, Bananas", ",")` returns 3-row table
- Common: `TrimEnds(Split("Apples, Oranges, Bananas", ","))` to clean whitespace

## StartsWith, EndsWith

- `StartsWith( Text, StartText )` -- Tests if text begins with StartText. Returns: Boolean
- `EndsWith( Text, EndText )` -- Tests if text ends with EndText. Returns: Boolean
- Case insensitive (for supported data sources). Empty search text returns true
- Commonly used with Filter for search: `Filter(Customers, StartsWith(Name, SearchInput.Text))`

## Table

- `Table( RecordOrTable1 [, RecordOrTable2, ...] )` -- Creates a temporary table from records or tables
- Columns are the union of all argument records. Missing values filled with blank
- Also accepts Dynamic (untyped) values for JSON arrays
- Example: `Table({Color: "red"}, {Color: "green"}, {Color: "blue"})`
- Inline syntax: `["S", "M", "L"]` creates single-column table with Value column

## Text

- `Text( NumberOrDateTime, DateTimeFormatEnum [, ResultLanguageTag] )` -- Formats value as text
- `Text( NumberOrDateTime, CustomFormat [, ResultLanguageTag] )` -- Formats with custom placeholders
- `Text( AnyValue )` -- Converts any value to text with default format
- Predefined formats: `DateTimeFormat.LongDate`, `.ShortDate`, `.LongTime24`, `.UTC`, etc.
- Number placeholders: `0` (with leading zeros), `#` (without), `.` (decimal), `,` (thousands)
- Date placeholders: `yyyy`, `mm`, `dd`, `hh`, `ss`, `AM/PM`
- Language placeholder: `[$-en-US]` for locale-specific formatting
- Example: `Text(Now(), DateTimeFormat.ShortDate)` returns `"4/7/2020"`
- Example: `Text(1234567.89, "$ #,###.00")` returns `"$ 1,234,567.89"`

## Trace

- `Trace( Message [, TraceSeverity [, CustomRecord [, TraceOptions ]]] )` -- Records diagnostic info
- Output appears in Power Apps Live Monitor and optionally Azure Application Insights
- Severity: `TraceSeverity.Information` (default), `.Warning`, `.Error`, `.Critical`
- CustomRecord: optional record for custom telemetry data
- Behavior formula only (use debug buttons for data property tracing)
- Example: `Trace("Button clicked", TraceSeverity.Information, { Screen: "Home" })`

## Trim, TrimEnds

- `Trim( String )` -- Removes all extra spaces (leading, trailing, and between words to single space)
- `TrimEnds( String )` -- Removes spaces from start and end only, leaving internal spaces intact
- Both accept single-column tables. Returns: trimmed string(s)
- Example: `Trim("  Hello   World  ")` returns `"Hello World"`
- Example: `TrimEnds("  Hello   World  ")` returns `"Hello   World"`

## Update, UpdateIf

- `Update( DataSource, OldRecord, NewRecord [, RemoveFlags.All] )` -- Replaces an entire record
- `UpdateIf( DataSource, Condition, ChangeRecord [, Condition2, ChangeRecord2, ...] )` -- Modifies matching records
- Update replaces the whole record (missing properties become blank)
- UpdateIf modifies only specified properties, leaving others unchanged
- Both return modified data source as table. Behavior formulas only
- Example: `UpdateIf(IceCream, Quantity > 175, { Quantity: Quantity + 10 })`

## UpdateContext

- `UpdateContext( { Var1: Value1 [, Var2: Value2, ...] } )` -- Creates/updates context variables (screen-scoped)
- Context variables are scoped to the current screen (unlike Set which is global)
- Implicitly created on first use. Lost when app closes
- Can also be set via Navigate's third argument
- No return value. Behavior formula only
- Example: `UpdateContext({ ShowLogo: true, Counter: Counter + 1 })`

## User

- `User()` -- Returns a record with info about the current user
- Properties: `.Email` (UPN, not SMTP), `.FullName`, `.Image` (blob URL), `.EntraObjectId` (GUID)
- Example: `User().Email` returns `"john.doe@contoso.com"`
- Example: `User().FullName` returns `"John Doe"`

## Validate

- `Validate( DataSource, Column, Value )` -- Checks if a value is valid for a column
- `Validate( DataSource, OriginalRecord, Updates )` -- Validates a complete record update
- Returns: blank if valid, error message string if invalid
- Uses data source metadata (required fields, min/max, string length, etc.)
- Example: `Validate(Scores, Percentage, 120)` returns `"Values must be between 0 and 100."`

## Value (Decimal, Float)

- `Value( String [, LanguageTag] )` -- Converts text to a number
- `Decimal( String [, LanguageTag] )` -- Converts to Decimal type specifically
- `Float( String [, LanguageTag] )` -- Converts to Float type specifically
- Handles currency symbols (current language), percentage signs (divides by 100), scientific notation
- LanguageTag affects decimal/thousands separator interpretation
- Returns error if format is invalid
- Example: `Value("123.456")` returns `123.456`
- Example: `Value("12.34%")` returns `0.1234`

## Day, Month, Year, Hour, Minute, Second, Weekday

- `Day( DateTime )` -- Returns day (1-31)
- `Month( DateTime )` -- Returns month (1-12)
- `Year( DateTime )` -- Returns year (starting 1900)
- `Hour( DateTime )` -- Returns hour (0-23)
- `Minute( DateTime )` -- Returns minute (0-59)
- `Second( DateTime )` -- Returns second (0-59)
- `Weekday( DateTime [, WeekdayFirst] )` -- Returns weekday number (default: 1=Sunday to 7=Saturday)
- WeekdayFirst options: `StartOfWeek.Sunday` (default), `.Monday`, `.MondayZero`, `.Tuesday`, etc.
- Example: `Month(Now())` returns `4` (for April)

## With

- `With( Record, Formula )` -- Evaluates a formula for a single record, acting as inline named values
- Use to create local variables in expressions without global/context variables
- Use to capture return values from Patch, Match, etc.
- Can nest With for complex calculations
- Example: `With({ radius: 10, height: 15 }, Pi() * radius^2 * height)`
- Example: `With(Match("PT2H1M39S", "PT(?:(?<hours>\d+)H)?..."), Time(Value(hours), Value(minutes), Value(seconds)))`

## App Object

- `App.ActiveScreen` -- Returns the currently displayed screen object
- `App.BackEnabled` -- Controls device back gesture behavior in Power Apps Mobile
- `App.ConfirmExit` -- Boolean; when true, shows confirmation dialog before app closes
- `App.ConfirmExitMessage` -- Custom message for the exit confirmation dialog
- `App.OnStart` -- Runs when app loads (use for caching data, setting global variables)
- `App.StartScreen` -- Sets which screen shows first (evaluated once at load)
- `App.Formulas` -- Defines named formulas reusable throughout the app (preferred over OnStart+Set)
- `App.OnError` -- Global error handler; intercepts errors before default banner display
- `App.StudioVersion` -- Returns the Power Apps Studio version used to publish
- Named formulas example: `App.Formulas: BGColor = ColorValue(Param("BackgroundColor"));`

## Signals

Signals are values that change independently of user interaction, causing automatic recalculation.

### Acceleration
- `Acceleration.X` -- Right/left acceleration (right = positive)
- `Acceleration.Y` -- Forward/back (forward = positive)
- `Acceleration.Z` -- Up/down (up = positive)
- Measured in g units (9.81 m/s^2). Returns zero in browser

### Compass
- `Compass.Heading` -- Magnetic north heading in degrees (0-360, 0 = north)

### Connection
- `Connection.Connected` -- Boolean: device connected to Wi-Fi or cellular
- `Connection.Metered` -- Boolean: connection is metered
- `Connection.Sync` -- ConnectionSync enum for offline-enabled apps (Connected, NotConnected, etc.)

### Location
- `Location.Latitude` -- Degrees from equator (-90 to 90, positive = north)
- `Location.Longitude` -- Degrees from Greenwich (-180 to 180, positive = east)
- `Location.Altitude` -- Meters above sea level
- Use `Enable`/`Disable` functions to control GPS for battery conservation

---

## Key Patterns

### Data CRUD Pattern
```
// Create
Patch(DataSource, Defaults(DataSource), { Field: "Value" })

// Read with filter
Filter(DataSource, StartsWith(Name, SearchInput.Text))

// Update specific fields
Patch(DataSource, LookUp(DataSource, ID = selectedId), { Field: newValue })

// Delete
Remove(DataSource, LookUp(DataSource, ID = selectedId))
```

### Screen Navigation with Context
```
Navigate(DetailScreen, ScreenTransition.Fade, { RecordID: Gallery1.Selected.ID });
// On DetailScreen: LookUp(DataSource, ID = RecordID)
```

### Form Validation Chain
```
If(
    IsBlank(Name), Notify("Name required", NotificationType.Error); SetFocus(Name),
    IsBlank(Email), Notify("Email required", NotificationType.Error); SetFocus(Email),
    Patch(DataSource, Defaults(DataSource), { Name: Name.Text, Email: Email.Text });
    Notify("Saved!", NotificationType.Success);
    Navigate(ListScreen)
)
```

### JSON Parsing to Typed Table
```
ForAll(
    ParseJSON(jsonString).items,
    { id: Value(ThisRecord.id), name: Text(ThisRecord.name) }
)
```

### Local Variables with With
```
With(
    { total: Sum(Orders, Amount), count: CountRows(Orders) },
    { Average: total / count, Total: total, Count: count }
)
```

### Named Formulas (App.Formulas)
```
CurrentUser = LookUp(Users, Email = User().Email);
IsAdmin = CurrentUser.Role = "Admin";
AppTheme = If(IsAdmin, Color.DarkBlue, Color.LightBlue);
```

### Search Pattern with Delegation
```
SortByColumns(
    Filter(Contacts, StartsWith(Name, SearchBox.Text)),
    "Name", SortOrder.Ascending
)
```

### Timer-Driven Refresh
```
// Timer.OnTimerEnd:
Set(CurrentTime, Now()); Refresh(DataSource)
```
