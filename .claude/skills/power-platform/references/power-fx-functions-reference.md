# Power Fx Functions Reference

All Power Fx functions in compact reference format. Delegable functions marked with [D].

## Table & Record Functions

```
AddColumns(Table, ColName, Formula, ...)        — Add calculated columns (does not modify original)
DropColumns(Table, Col1, ...)                    — Remove columns from table
RenameColumns(Table, "Old", "New", ...)          — Rename columns
ShowColumns(Table, Col1, ...)                    — Keep only specified columns
Table(Record1, Record2, ...)                     — Create temporary table from records
Filter(Table, Formula1, Formula2, ...) [D]       — Return records matching all conditions
LookUp(Table, Formula, ReductionFormula) [D]     — Return first matching record or field
Search(Table, SearchString, Col1, ...) [D]       — Case-insensitive substring match across columns
Sort(Table, Formula, SortOrder) [D]              — Sort by evaluating formula per record
SortByColumns(Table, ColName, Order, ...) [D]    — Sort by column names (multi-column)
First(Table) [D]                                 — First record
Last(Table)                                      — Last record
FirstN(Table, N)                                 — First N records
LastN(Table, N)                                  — Last N records
Index(Table, Position)                           — Record at 1-based position
Distinct(Table, Formula)                         — Single-column table with duplicates removed
GroupBy(Table, Col1, ..., GroupColName)           — Group records into nested tables
Ungroup(Table, GroupColName)                      — Flatten grouped table
Shuffle(Table)                                   — Return table in random order
ForAll(Table, Formula)                           — Evaluate formula for all records, return table
Sequence(Records, Start, Step)                   — Generate sequential number table (max 50,000)
With(Record, Formula)                            — Evaluate formula with inline named values
Relate(RelatedTable, Record)                     — Link records via relationship
Unrelate(RelatedTable, Record)                   — Remove link between records
```

## Data / CRUD Functions

```
Patch(DS, BaseRecord, Changes) [D]               — Create or modify records in data source
Collect(DS, Item, ...)                           — Add records to data source or collection
ClearCollect(Collection, Item, ...)              — Clear then add (replace all records)
Clear(Collection)                                — Delete all records from collection
Remove(DS, Record, ...) [D]                      — Remove specific records
RemoveIf(DS, Condition, ...) [D]                 — Remove records matching conditions
Update(DS, OldRecord, NewRecord)                 — Replace entire record
UpdateIf(DS, Condition, ChangeRecord, ...)       — Modify matching records (partial update)
Refresh(DS)                                      — Retrieve fresh copy of data source
Revert(DS, Record)                               — Refresh and clear errors for record
Defaults(DS)                                     — Return default values as record
Validate(DS, Column, Value)                      — Check value validity (blank=valid, string=error)
Errors(DS, Record)                               — Table of errors for data source
DataSourceInfo(DS, InfoType)                     — Schema constraints for data source
Choices(ColumnRef, TextFilter)                   — Table of possible values for lookup column
```

## Form Functions

```
EditForm(Form)                                   — Switch form to edit mode
NewForm(Form)                                    — Switch form to new record mode
ViewForm(Form)                                   — Switch form to read-only mode
ResetForm(Form)                                  — Reset form to initial values
SubmitForm(Form)                                 — Save form changes to data source
Reset(Control)                                   — Reset control to its Default value
```

## Navigation Functions

```
Navigate(Screen, Transition, ContextRecord)      — Change displayed screen
Back(Transition)                                 — Return to previous screen
Exit(Signout)                                    — Exit app (optional sign out)
Launch(URL, Params...)                           — Open URL or canvas app
Param(ParameterName)                             — Retrieve app launch parameter (string)
SetFocus(Control)                                — Move input focus to control
```

## Text Functions

```
Concatenate(Str1, Str2, ...)                     — Join strings (same as & operator)
Concat(Table, Formula, Separator)                — Join formula results across table records
Left(String, N)                                  — First N characters
Mid(String, Start, N)                            — Substring from position
Right(String, N)                                 — Last N characters
Len(String)                                      — String length
Lower(String)                                    — Convert to lowercase
Upper(String)                                    — Convert to uppercase
Proper(String)                                   — Capitalize first letter of each word
Trim(String)                                     — Remove extra spaces (internal to single)
TrimEnds(String)                                 — Remove leading/trailing spaces only
Replace(String, Start, Count, New)               — Replace by position
Substitute(String, Old, New, Instance)           — Replace by matching text
Split(Text, Separator)                           — Split into single-column table
Find(FindStr, WithinStr, StartPos)               — Case-sensitive position search
StartsWith(Text, StartText)                      — Test if text begins with value
EndsWith(Text, EndText)                          — Test if text ends with value
Text(Value, Format, Language)                    — Format number/date as text string
Value(String, Language)                          — Parse text to number
Decimal(String, Language)                        — Parse text to Decimal type
Float(String, Language)                          — Parse text to Float type
EncodeHTML(String)                               — Escape HTML characters
EncodeUrl(String)                                — URL-encode special characters
HashTags(String)                                 — Extract #hashtags to table
Char(Code)                                       — ASCII code to character
UniChar(Code)                                    — Unicode code to character
```

## Pattern Matching

```
IsMatch(Text, Pattern, Options)                  — Boolean pattern test
Match(Text, Pattern, Options)                    — First match record (FullMatch, submatches)
MatchAll(Text, Pattern, Options)                 — All matches as table
```

Predefined: `Match.Email`, `Match.Digit`, `Match.Letter`, `Match.NonSpace`, etc.
Options: `MatchOptions.IgnoreCase`, `MatchOptions.Multiline`, etc.

## Logic Functions

```
If(Condition, Then, Else)                        — Conditional (supports multiple conditions)
Switch(Formula, Match1, Result1, ..., Default)   — Pattern matching
And(F1, F2, ...) / &&                            — All must be true
Or(F1, F2, ...) / ||                             — Any must be true
Not(Formula) / !                                 — Negate boolean
Coalesce(Val1, Val2, ...)                        — First non-blank value
IsBlank(Value)                                   — Test for blank or empty string
IsEmpty(Table)                                   — Test for empty table
IsNumeric(Value)                                 — Test if numeric
IsToday(DateTime)                                — Test if date is today
```

## Error Handling

```
IfError(Value, Replacement, ...)                 — Replace errors (stops chain on error)
IsError(Value)                                   — Test for error (boolean)
IsBlankOrError(Value)                            — Test for blank or error
Error({Kind, Message})                           — Create or rethrow custom error
```

## Math Functions

```
Abs(Number)                                      — Absolute value
Round(Number, DecimalPlaces)                     — Round (5+ rounds up)
RoundDown(Number, DecimalPlaces)                 — Round toward zero
RoundUp(Number, DecimalPlaces)                   — Round away from zero
Int(Number)                                      — Round down to integer
Trunc(Number)                                    — Truncate toward zero
Mod(Number, Divisor)                             — Remainder (sign of divisor)
Power(Base, Exp) / ^                             — Exponentiation
Sqrt(Number)                                     — Square root
Exp(Number)                                      — e^Number
Ln(Number)                                       — Natural logarithm
Log(Number, Base)                                — Logarithm (default base 10)
Pi()                                             — 3.141592...
Rand()                                           — Random number >= 0 and < 1
RandBetween(Bottom, Top)                         — Random integer in range (inclusive)
```

## Trigonometry

```
Sin(Radians) / Cos(Radians) / Tan(Radians)      — Standard trig functions
Asin(N) / Acos(N) / Atan(N) / Atan2(X,Y)        — Inverse trig functions
Cot(Radians) / Acot(N)                           — Cotangent and inverse
Degrees(Radians)                                 — Convert to degrees
Radians(Degrees)                                 — Convert to radians
```

## Aggregates

```
Sum(Table, Formula) / Sum(N1, N2, ...) [D]       — Total sum
Average(Table, Formula) / Average(N1, ...) [D]   — Arithmetic mean
Min(Table, Formula) / Min(N1, ...) [D]           — Minimum value
Max(Table, Formula) / Max(N1, ...) [D]           — Maximum value
Count(SingleColTable) [D]                        — Count numbers only
CountA(SingleColTable)                           — Count non-blank values
CountIf(Table, Formula)                          — Count matching records
CountRows(Table) [D]                             — Count all records
```

## Date & Time Functions

```
Date(Year, Month, Day)                           — Create date
DateTime(Y, M, D, H, Min, S, Ms)                — Create datetime
Time(Hour, Minute, Second)                       — Create time value
DateAdd(DateTime, Addition, Units)               — Add time units
DateDiff(Start, End, Units)                      — Difference in units
DateValue(String, Language)                       — Parse date string
TimeValue(String, Language)                       — Parse time string
DateTimeValue(String, Language)                   — Parse datetime string
Now()                                            — Current date and time (volatile)
Today()                                          — Current date at midnight (volatile)
Year(DT) / Month(DT) / Day(DT)                  — Extract date parts
Hour(DT) / Minute(DT) / Second(DT)              — Extract time parts
Weekday(DT, StartOfWeek)                         — Day of week number
IsToday(DT)                                      — Test if date is today
Calendar.MonthsLong/Short()                      — Locale month names
Calendar.WeekdaysLong/Short()                    — Locale weekday names
Clock.AmPm() / Clock.IsClock24()                 — Locale clock info
```

TimeUnit enum: Years, Quarters, Months, Days, Hours, Minutes, Seconds, Milliseconds.

## Color Functions

```
Color.Red / Color.Blue / ...                     — Built-in CSS color enum
ColorFade(Color, Amount)                         — Brighten (negative) or darken (positive)
ColorValue("#ff0000") / ColorValue("Red")        — CSS string to color
RGBA(R, G, B, Alpha)                             — Color from components (0-255, alpha 0-1)
```

## JSON & Data

```
JSON(DataStructure, Format)                      — Generate JSON text string
ParseJSON(JSONString, Type)                      — Parse JSON to Dynamic/typed value
```

JSONFormat: Compact, IndentFour, IncludeBinaryData, IgnoreBinaryData, FlattenValueTables.

## AI Functions

```
AIClassify(Text, Categories)                     — Classify text into categories
AIExtract(Text, Entity)                          — Extract entities (phone, names, etc.)
AIReply(Text)                                    — Draft AI reply to message
AISentiment(Text)                                — "Positive", "Neutral", or "Negative"
AISummarize(Text)                                — Summarize text
AISummarizeRecord(Entity)                        — Summarize Dataverse record
AITranslate(Text, TargetLanguage)                — Translate text
```

## Type Conversion

```
Boolean(TextOrNumber)                            — Convert to Boolean
Value(String, Language)                          — Convert text to number
Text(Value, Format)                              — Convert to formatted text
DateValue/TimeValue/DateTimeValue(String)         — Convert text to date/time
GUID() / GUID(String)                            — Create or parse GUID
```

## App & System

```
User()                                           — Current user (.Email, .FullName, .Image, .EntraObjectId)
Language()                                       — User's IETF BCP-47 language tag
Blank()                                          — Return blank (NULL) value
Concurrent(F1, F2, ...)                          — Run formulas in parallel
Copy(Text)                                       — Copy text to clipboard
Confirm(Message, Options)                        — Modal dialog, returns Boolean
Download(URL)                                    — Download file to device
Notify(Message, Type, Timeout)                   — Display banner message
Trace(Message, Severity, CustomRecord)           — Diagnostic logging (Monitor/AppInsights)
Set(VarName, Value)                              — Create/update global variable
UpdateContext({Var: Value})                       — Create/update context variable (screen scope)
SaveData(Collection, Name)                       — Save to device storage
LoadData(Collection, Name, IgnoreNonexistent)    — Load from device storage
ClearData(Name)                                  — Clear device storage
```

## Signals

```
Acceleration.X / .Y / .Z                        — Device acceleration (g units)
Compass.Heading                                  — Magnetic north heading (degrees)
Connection.Connected / .Metered                  — Network status
Location.Latitude / .Longitude / .Altitude       — GPS coordinates
App.ActiveScreen                                 — Current screen object
```
