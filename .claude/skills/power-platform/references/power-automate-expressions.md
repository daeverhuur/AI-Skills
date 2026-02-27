# Power Automate Expressions Reference

## Expression Language Overview

Cloud flows use the Workflow Definition Language (shared with Azure Logic Apps). Access via the `fx` button in the designer. Syntax: `functionName(arguments)`.

## Logical Functions

| Function | Description | Example |
|----------|-------------|---------|
| `and(expr1, expr2)` | True if both are true | `and(greater(1,0), equals(0,0))` |
| `or(expr1, expr2)` | True if either is true | `or(greater(1,10), equals(0,0))` |
| `equals(val1, val2)` | True if values equal | `equals(parameters('status'), 'Active')` |
| `greater` / `greaterOrEquals` | Comparison | `greater(100, 10)` |
| `less` / `lessOrEquals` | Comparison | `less(10, 100)` |
| `empty(value)` | True if empty | `empty('')` |
| `not(expr)` | Opposite boolean | `not(contains('200 Success','Fail'))` |
| `if(expr, trueVal, falseVal)` | Conditional | `if(equals(1,1), 'yes', 'no')` |

## String Functions

`concat`, `substring`, `replace`, `split`, `indexOf`, `lastIndexOf`, `length`, `toLower`, `toUpper`, `trim`, `startsWith`, `endsWith`, `slice`, `formatNumber`, `guid`, `chunk`, `nthIndexOf`, `isFloat`, `isInt`

```
concat('Hello', ' ', 'World')
substring('Hello World', 6, 5)           -> 'World'
replace('Hello World', 'World', 'PA')
split('a,b,c', ',')                      -> ['a','b','c']
toLower('HELLO')                         -> 'hello'
formatNumber(1234.5, 'C2')              -> '$1,234.50'
```

## Collection Functions

`contains`, `empty`, `first`, `last`, `length`, `join`, `intersection`, `union`, `item`, `skip`, `take`, `sort`, `reverse`, `chunk`

```
first(variables('myArray'))
contains(variables('myArray'), 'value')
length(variables('myArray'))
take(skip(variables('myArray'), 10), 5)
join(variables('myArray'), ', ')
item()?['PropertyName']
```

## Conversion Functions

`int`, `float`, `string`, `bool`, `json`, `array`, `createArray`, `base64`, `base64ToString`, `base64ToBinary`, `binary`, `decimal`, `xml`, `dataUri`, `encodeUriComponent`, `decodeUriComponent`

```
int('42')                                -> 42
string(42)                               -> '42'
json('{"name":"John"}')
createArray('a', 'b', 'c')
base64ToString('SGVsbG8=')
bool(1)                                  -> true
```

## Math Functions

`add`, `sub`, `mul`, `div`, `mod`, `min`, `max`, `rand`, `range`

```
add(10, 5)  -> 15     sub(10, 5)  -> 5
mul(10, 5)  -> 50     div(10, 5)  -> 2
mod(10, 3)  -> 1      rand(1, 100)
range(1, 5) -> [1,2,3,4,5]
```

## Date and Time Functions

`utcNow`, `addDays`, `addHours`, `addMinutes`, `addSeconds`, `addToTime`, `subtractFromTime`, `formatDateTime`, `convertFromUtc`, `convertTimeZone`, `convertToUtc`, `dateDifference`, `dayOfMonth`, `dayOfWeek`, `dayOfYear`, `startOfDay`, `startOfHour`, `startOfMonth`, `getFutureTime`, `getPastTime`, `parseDateTime`, `ticks`

```
utcNow()
addDays(utcNow(), 7)
formatDateTime(utcNow(), 'yyyy-MM-dd')
convertFromUtc(utcNow(), 'Eastern Standard Time')
dayOfMonth(utcNow())
less(item()?['DueDate'], addDays(utcNow(), 1))
dateDifference('2024-01-01', '2024-12-31')
```

## Data Operations

| Operation | Purpose |
|-----------|---------|
| Compose | Store a value (string, object, array, expression) for reuse. Access via `outputs('Compose')` |
| Join | Convert array to delimited string |
| Select | Reshape objects in an array (rename/add/remove properties) |
| Filter array | Reduce array to matching subset (case-sensitive) |
| Create CSV table | Convert JSON array to CSV |
| Create HTML table | Convert JSON array to HTML table |

## Parse JSON

Parse a JSON string into typed dynamic content. Requires a JSON schema (generate from sample payload). Output fields become available as dynamic content in subsequent actions.

## Variable Types and Actions

Types: Boolean, Integer, Float, String, Array, Object.

| Action | Description |
|--------|-------------|
| Initialize variable | Declare name, type, initial value (top-level only, not inside loops/conditions) |
| Set variable | Assign new value |
| Increment / Decrement variable | Increase or decrease integer/float |
| Append to string variable | Concatenate text |
| Append to array variable | Add item to end |

Access: `variables('variableName')`. Variables are global. Use sequential mode in parallel loops to avoid race conditions.

## Referencing Functions

| Function | Purpose |
|----------|---------|
| `trigger()` / `triggerBody()` / `triggerOutputs()` | Access trigger data |
| `body('actionName')` / `outputs('actionName')` | Access action outputs |
| `actions('actionName')` | Action metadata and status |
| `result('scopeName')` | Array of action results within a scope |
| `item()` / `items('loopName')` | Current item in loop |
| `iterationIndexes('loopName')` | Current iteration index |
| `workflow()` | Flow run metadata |
| `parameters('name')` / `variables('name')` | Access parameters or variables |

## JSON Manipulation

`addProperty(obj, key, value)`, `removeProperty(obj, key)`, `setProperty(obj, key, value)`, `coalesce(val1, val2, ...)`, `xpath(xml, expression)`

## Common Expression Patterns

```
@equals(item()?['Status'], 'Active')
@and(equals(item()?['Status'], 'blocked'), equals(item()?['Assigned'], 'John'))
@empty(triggerBody()?['email'])
@coalesce(triggerBody()?['name'], 'Unknown')
@if(equals(triggerBody()?['priority'], 'High'), 'Urgent', 'Normal')
@body('Get_item')?['fields']?['Title']
@outputs('Compose')?[variables('propertyName')]
@and(greater(item()?['Due'], item()?['Paid']), less(item()?['dueDate'], addDays(utcNow(),1)))
```
