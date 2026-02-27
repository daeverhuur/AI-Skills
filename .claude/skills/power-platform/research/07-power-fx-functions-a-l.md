# Power Fx Functions Reference (A-L)
## Sources: 35 unique pages fetched, 88+ functions documented

---

## Abs
`Abs( Number )` — Returns absolute (non-negative) value. Also accepts single-column table.
Example: `Abs( -55 )` → `55`

## Acos / Acot / Asin / Atan / Atan2
- `Acos( Number )` — Inverse cosine, returns radians (0 to pi)
- `Acot( Number )` — Inverse cotangent, radians (0 to pi)
- `Asin( Number )` — Inverse sine, radians (-pi/2 to pi/2)
- `Atan( Number )` — Inverse tangent, radians (-pi/2 to pi/2)
- `Atan2( X, Y )` — Arctangent of x,y coordinates, radians (-pi to pi)

## AddColumns
`AddColumns( TableOrRecord, ColumnName1, Formula1 [, ...] )` — Adds calculated columns. Does not modify original.
Example: `AddColumns( IceCreamSales, "Revenue", UnitPrice * QuantitySold )`

## AI Functions
- `AIClassify( Text, Categories )` — Classifies text into categories
- `AIExtract( Text, Entity )` — Extracts entities (phone, names, etc.)
- `AIReply( Text )` — Drafts AI reply to message
- `AISentiment( Text )` — Returns "Positive", "Neutral", or "Negative"
- `AISummarize( Text )` — Summarizes text
- `AISummarizeRecord( Entity )` — Summarizes Dataverse record
- `AITranslate( Text, TargetLanguage )` — Translates text (auto-detect source)

## And / Or / Not
- `And( Formula1, Formula2, ... )` or `x && y` — All must be true
- `Or( Formula1, Formula2, ... )` or `x || y` — Any must be true
- `Not( Formula )` or `!x` — Negation

## Average / Min / Max / Sum / Count / CountA / CountIf / CountRows
- `Average( Num1, Num2, ... )` or `Average( Table, Formula )` — Arithmetic mean
- `Min( ... )` / `Max( ... )` — Minimum/maximum value
- `Sum( ... )` — Total sum
- `Count( SingleColumnTable )` — Count numbers only
- `CountA( SingleColumnTable )` — Count non-blank values
- `CountIf( Table, Formula )` — Count records matching condition
- `CountRows( Table )` — Count all records

## Blank
`Blank()` — Returns blank (NULL) value. Use to store NULL in data sources.

## Boolean
`Boolean( TextOrNumber )` — Converts to Boolean. "true"/"false" strings, 0=false, non-zero=true.

## Calendar / Clock
- `Calendar.MonthsLong()` / `Calendar.MonthsShort()` / `Calendar.WeekdaysLong()` / `Calendar.WeekdaysShort()` — Locale calendar info
- `Clock.AmPm()` / `Clock.AmPmShort()` / `Clock.IsClock24()` — Locale clock info

## Char / UniChar
- `Char( ASCIICode )` — ASCII code to string. `Char(65)` → "A"
- `UniChar( UnicodeCode )` — Unicode code to string. `UniChar(9829)` → heart

## Choices
`Choices( column-reference [, text-filter] )` — Returns table of possible values for lookup column.

## Clear / Collect / ClearCollect / ClearData
- `Clear( Collection )` — Delete all records from collection
- `Collect( DataSource, Item, ... )` — Add records; creates collection if needed
- `ClearCollect( Collection, Item, ... )` — Clear then add (replaces all)
- `ClearData( [Name] )` — Clear device storage

## Coalesce
`Coalesce( Value1, Value2, ... )` — Returns first non-blank, non-empty-string value.
Example: `Coalesce( Blank(), 1 )` → `1`

## Color / ColorFade / ColorValue / RGBA
- `Color.Red` — Built-in CSS color enum
- `ColorFade( Color, FadeAmount )` — Brighten (-1 to 1) or darken
- `ColorValue( "#ff0000" )` or `ColorValue( "Red" )` — CSS string to color
- `RGBA( 255, 0, 0, 1 )` — Red, Green, Blue (0-255), Alpha (0-1)

## Concat / Concatenate
- `Concat( Table, Formula, Separator )` — Join formula results across table records
  Example: `Concat( Products, Name, ", " )` → `"Violin, Cello, Trumpet"`
- `Concatenate( String1, String2, ... )` — Join strings. Same as `&` operator.

## Concurrent
`Concurrent( Formula1, Formula2, ... )` — Run formulas in parallel. Improves data loading performance.
Example: `Concurrent( ClearCollect(Products, SQL), ClearCollect(Customers, SQL) )`

## Confirm
`Confirm( Message [, { ConfirmButton, CancelButton, Title, Subtitle } ] )` — Modal dialog. Returns Boolean.

## Copy
`Copy( text )` — Copies text to clipboard. Behavior formula only.

## Cos / Cot / Sin / Tan
- `Cos( Radians )` — Cosine
- `Cot( Radians )` — Cotangent
- `Sin( Radians )` — Sine
- `Tan( Radians )` — Tangent
All accept single-column tables. Input in radians.

## Date / DateTime / DateAdd / DateDiff
- `Date( Year, Month, Day )` — Creates date (time = midnight)
- `DateTime( Year, Month, Day, Hour, Minute, Second [, Ms] )` — Full date/time
- `DateAdd( DateTime, Addition [, Units] )` — Add time units (default: Days)
- `DateDiff( Start, End [, Units] )` — Difference in units (default: Days)

TimeUnit enum: Years, Quarters, Months, Days, Hours, Minutes, Seconds, Milliseconds

## DateValue / TimeValue / DateTimeValue
- `DateValue( String [, Language] )` — Parse date string
- `TimeValue( String [, Language] )` — Parse time string
- `DateTimeValue( String [, Language] )` — Parse full date/time string

## Defaults
`Defaults( DataSource )` — Returns default values for data source as record.

## Degrees / Radians / Pi
- `Degrees( Radians )` — Convert radians to degrees
- `Radians( Degrees )` — Convert degrees to radians
- `Pi()` — Returns 3.141592...

## Distinct
`Distinct( Table, Formula )` — Returns single-column table (Value) with duplicates removed.
Example: `Distinct( CityPopulations, Country )` → unique countries

## Download
`Download( Address )` — Downloads file from web to local device. Returns file location.

## DropColumns / RenameColumns / ShowColumns
- `DropColumns( Table, Col1, ... )` — Remove columns
- `RenameColumns( Table, "Old", "New", ... )` — Rename columns
- `ShowColumns( Table, Col1, ... )` — Keep only specified columns

## EditForm / NewForm / ViewForm / ResetForm / SubmitForm
- `EditForm( Form )` — Switch to FormMode.Edit
- `NewForm( Form )` — Switch to FormMode.New
- `ViewForm( Form )` — Switch to FormMode.View (read-only)
- `ResetForm( Form )` — Reset to initial values
- `SubmitForm( Form )` — Save changes to data source

## EncodeHTML / EncodeUrl
- `EncodeHTML( String )` — Escape HTML chars (<, >, &)
- `EncodeUrl( String )` — URL encode special chars (% + hex)

## Error / Errors
- `Error( { Kind: ErrorKind.Validation, Message: "..." } )` — Create/rethrow custom error
- `Errors( DataSource [, Record] )` — Table of errors (Record, Column, Message, Error columns)

## Exit
`Exit( [Signout] )` — Exit app. Optional signout (Boolean).

## Exp / Ln / Log / Power / Sqrt
- `Exp( Number )` — e^Number. `Exp(2)` → `7.389`
- `Ln( Number )` — Natural log. `Ln(100)` → `4.605`
- `Log( Number [, Base] )` — Logarithm (default base 10). `Log(100)` → `2`
- `Power( Base, Exponent )` — Same as `^`. `Power(5,3)` → `125`
- `Sqrt( Number )` — Square root. `Sqrt(9)` → `3`

## Filter / LookUp / Search
- `Filter( Table, Formula1 [, Formula2, ...] )` — Returns filtered table. **Delegable**.
  Example: `Filter( IceCream, OnOrder > 0 )`
- `LookUp( Table, Formula [, ReductionFormula] )` — First matching record. **Delegable**.
  Example: `LookUp( IceCream, Flavor = "Chocolate", Quantity )` → `100`
- `Search( Table, SearchString, Col1 [, Col2, ...] )` — Case-insensitive substring match. **Delegable**.
  Example: `Search( IceCream, "choc", Flavor )`

## Find
`Find( FindString, WithinString [, StartPos] )` — Case-sensitive position search. Returns number or blank.
Example: `Find( "World", "Hello World" )` → `7`

## First / Last / FirstN / LastN / Index
- `First( Table )` — First record
- `Last( Table )` — Last record
- `FirstN( Table [, N] )` — First N records
- `LastN( Table [, N] )` — Last N records
- `Index( Table, Position )` — Record at 1-based position. Error if out of range.

## ForAll
`ForAll( Table, Formula )` — Evaluate formula for all records. Returns table of results.
Example: `ForAll( Squares, Sqrt( Value ) )`

## GroupBy / Ungroup
- `GroupBy( Table, Col1 [, Col2, ...], GroupColName )` — Group records, nested table in GroupCol
- `Ungroup( Table, GroupColName )` — Reverse GroupBy, flatten back

## GUID
`GUID()` — Create new GUID. `GUID( "0f8fad5b-..." )` — Parse GUID string.

## HashTags
`HashTags( String )` — Extract #hashtags. Returns single-column table.

## If / Switch
- `If( Condition, ThenResult [, DefaultResult] )` — Conditional. Multiple conditions supported.
  Example: `If( Slider1.Value = 25, "Result1", "Result2" )`
- `Switch( Formula, Match1, Result1 [, Match2, Result2, ... [, Default]] )` — Pattern matching.

## IfError / IsError / IsBlankOrError
- `IfError( Value1, Replacement1 [, ...] )` — Replace errors. Stops processing on error.
  Example: `IfError( 1/x, 0 )` → 0 on division by zero
- `IsError( Value )` — Test for error (Boolean)
- `IsBlankOrError( Value )` — Test for blank OR error

## IsBlank / IsEmpty
- `IsBlank( Value )` — True if blank or empty string
- `IsEmpty( Table )` — True if table has no records

## IsMatch / Match / MatchAll
- `IsMatch( Text, Pattern [, Options] )` — Boolean pattern test. Case-sensitive default.
  Example: `IsMatch( "joan@contoso.com", Match.Email )` → true
- `Match( Text, Pattern [, Options] )` — First match. Returns record with FullMatch, StartMatch, submatches.
- `MatchAll( Text, Pattern [, Options] )` — All matches. Returns table.

Predefined patterns: Match.Email, Match.Digit, Match.Letter, Match.NonSpace, etc.
Options: MatchOptions.IgnoreCase, MatchOptions.Multiline, etc.

## IsNumeric / IsToday
- `IsNumeric( Value )` — True if numeric
- `IsToday( DateTime )` — True if date falls on today

## JSON
`JSON( DataStructure [, Format] )` — Generate JSON text string.
Formats: JSONFormat.Compact, IndentFour, IncludeBinaryData, IgnoreBinaryData, FlattenValueTables

## Language
`Language()` — Returns user's language tag (IETF BCP-47). Example: `"en-US"`

## Launch
`Launch( Address [, ParamName1, ParamValue1, ...] )` — Open URL or canvas app.
Example: `Launch( "https://bing.com/search", "q", "Power Apps" )`
LaunchTarget: New, Replace, or custom window name

## Left / Mid / Right / Len
- `Left( String, N )` — First N characters
- `Mid( String, Start [, N] )` — Middle portion from Start position
- `Right( String, N )` — Last N characters
- `Len( String )` — String length. Blank → 0.

## LoadData / SaveData
- `LoadData( Collection, Name [, IgnoreNonexistent] )` — Load from device storage
- `SaveData( Collection, Name )` — Save to device storage
Works on: Power Apps Mobile, Windows, Teams (1MB limit). NOT in web player or Studio.

---

## Key Patterns

### Delegation-Safe Functions
Filter, LookUp, Search, Sort, SortByColumns, Sum, Average, Min, Max, CountRows, Count, First

### Common Function Chains
```powerfx
// CRUD with form
NewForm(Form1); Navigate(EditScreen, None)
SubmitForm(Form1); Navigate(BrowseScreen, None)

// Data loading
Concurrent(
    ClearCollect(Products, SQL_Products),
    ClearCollect(Customers, SQL_Customers)
)

// Error handling
IfError(
    Patch(DS, record, changes), Notify("Save failed: " & FirstError.Message),
    Navigate(SuccessScreen)
)
```
