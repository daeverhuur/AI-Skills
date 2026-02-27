# Power Automate Desktop Flows & Cloud Flow Expressions

> Research compiled from Microsoft Learn documentation.
> Sources: learn.microsoft.com/en-us/power-automate/desktop-flows/* and learn.microsoft.com/en-us/power-automate/*

---

## Part 1: Desktop Flows

### 1.1 Introduction & Overview

Power Automate desktop flows provide robotic process automation (RPA) capabilities for automating repetitive desktop processes. Users interact with everyday tools like email, Excel, web browsers, and legacy applications through a drag-and-drop designer or by recording actions.

**Key capabilities:**
- Automate legacy apps (terminal emulators), modern web/desktop apps, Excel, and file/folder operations
- Interact via UI elements, images, or coordinates
- Supports Microsoft account, work/school account, and Organization premium account sign-in

### 1.2 Creating Desktop Flows

| Method | Steps |
|--------|-------|
| **From console** | Launch app > New flow > Enter name > Create > Design in flow designer > Save |
| **From examples** | Examples tab in console > Right-click > Create a copy > Stored under My flows |
| **From cloud flows** | Use "Run a flow built with Power Automate for desktop" action in a cloud flow |

The flow designer provides a drag-and-drop canvas. Actions are added from the actions pane, configured via modals, and saved to the My flows tab.

### 1.3 Recording Flows

**Recorder types:**
- **Standard recorder** -- captures mouse/keyboard activity relative to UI elements; generates both UI automation and browser automation actions
- **Image-based recorder** -- uses image recognition and OCR (Tesseract) for apps that don't expose accessibility APIs

**Capturing modes for desktop apps:**
| Mode | Framework | Best For |
|------|-----------|----------|
| **UIA (UI Automation)** | Modern Microsoft accessibility framework | WPF, WinForms, UWP apps |
| **MSAA (Microsoft Active Accessibility)** | Older accessibility technology | Legacy VB6, classic Win32 apps |

**Recorder features:**
- Drag-and-drop step replication (generates Resize/Move window actions)
- Drop-down list handling with custom selection screen
- Browser launch (Edge, Chrome, Firefox, IE) during recording
- Date picker and color picker handling via custom text fields
- IME (Input Method Editor) support for non-Latin text input
- Image-based text extraction with anchor areas

**Limitation:** Conditionals and loops cannot be recorded; must be added manually.

### 1.4 Actions Reference (All Categories)

| A-C | D-H | I-R | S-Z |
|-----|-----|-----|-----|
| Active Directory | Database | IBM Cognitive | SAP automation |
| AI Builder (Preview) | Date time | Logging | Scripting |
| AWS | Email | Loops | SharePoint |
| Azure | Excel | Message boxes | System |
| Browser automation | Exchange Server | Microsoft Cognitive | Terminal emulation |
| Clipboard | File | Mouse and keyboard | Text |
| Cloud connectors | Flow control | OCR | UI automation |
| CMD session | Folder | Outlook | Variables |
| Compression | FTP | Power Automate secret variables | Windows services |
| Conditionals | Google Cognitive | PDF | Workstation |
| Custom actions | HTTP | Run flow | Workqueues |
| Cryptography | -- | -- | XML / Word |
| CyberArk | -- | -- | -- |

### 1.5 Variable Data Types

**Simple types:**

| Type | Notation | Example |
|------|----------|---------|
| Text value | Plain text (no notation) | `Hello World` |
| Numeric value | Number or math expression | `42` or `%5 + 3%` |
| Boolean value | `%True%` or `%False%` | `%True%` |
| Datetime | `%d"yyyy-MM-dd HH:mm:ss.ff+zzz"%` | `%d"2022-03-25"%` |

**Advanced types:**

| Type | Description | Access Notation |
|------|-------------|-----------------|
| List | Single-dimension array | `%List[0]%`, `%List[2:4]%` (slicing) |
| Datatable | Two-dimensional table (rows + columns) | `%DT[0][1]%` or `%DT[0]['ColName']%` |
| Datarow | Single row from a datatable | `%Row[0]%` or `%Row['ColName']%` |
| Custom object | Key-value pairs (JSON-like) | `%{ 'Key1': 'Val1', 'Key2': 'Val2' }%` |

**Instance types:** Web browser instance, Window instance, Excel instance, Outlook instance
**Connection types:** SQL connection, Exchange connection, FTP connection

**Creating a datatable with headers:**
```
%{^['Product', 'Price'], ['Widget', '10 USD'], ['Gadget', '20 USD']}%
```

### 1.6 Loops

| Action | Purpose | Key Parameters |
|--------|---------|----------------|
| **Loop** | Iterate a fixed number of times | Start from, End to, Increment by |
| **Loop condition** | Repeat while condition is true | First operand, Operator, Second operand |
| **For each** | Iterate over list, datatable, or datarow | Value to iterate |
| **Exit loop** | Terminate the loop early | (none) |
| **Next loop** | Skip to next iteration | (none) |

**Loop condition operators:** `=`, `<>`, `>`, `>=`, `<`, `<=`

### 1.7 Conditionals

| Action | Purpose | Key Parameters |
|--------|---------|----------------|
| **If** | Execute block if condition is true | First operand, Operator, Second operand |
| **Else if** | Alternative condition after If | First operand, Operator, Second operand |
| **Else** | Fallback block if no condition met | (none) |
| **Switch** | Dispatch based on value | Value to check |
| **Case** | Match within Switch block | Operator, Value to compare |
| **Default case** | Fallback if no Case matches | (none) |

**Comparison operators for If/Else if/Case:**
`=`, `<>`, `>`, `>=`, `<`, `<=`, Contains, Does not contain, Is empty, Is not empty, Starts with, Does not start with, Ends with, Does not end with, Is blank, Is not blank

### 1.8 Error Handling

**Error types:**
- **Design-time errors** -- configuration issues (empty required fields, undefined variables); prevent flow from running
- **Run-time errors (exceptions)** -- occur during execution (e.g., invalid file path); can be handled

**Single-action error handling (On error):**
1. **Retry action** -- set number of retries and interval (default: 1 retry, 2-second interval)
2. **Continue flow run** -- Go to next action, Repeat action, or Go to label
3. **New rule** -- Set variable or Run subflow on error
4. **Advanced** -- configure each possible exception separately

**Block error handling (On block error):**
- Wraps multiple actions in a single error handler
- Same options as single-action, plus: continue from beginning or end of block
- Block retries restart from beginning of the block
- Individual action error handling takes precedence over block error handling

**Get last error action:** Retrieves an Error variable with properties: action name, location, index, subflow, details, and message. Optional "Clear error" flag.

### 1.9 Triggering Desktop Flows

**Prerequisites:** Registered machine or machine group, work/school account, desktop flow connection, appropriate license (attended) or unattended add-on.

**Steps:** Cloud flow > New step > "Run a flow built with Power Automate for desktop" > Select connection > Choose run mode (attended/unattended) > Select or create desktop flow.

**Input/Output variables:** Desktop flows use input variables (cloud-to-desktop) and output variables (desktop-to-cloud). Input size limit: 2 MB (1 MB for China regions). Throughput limit: 70 desktop flow runs per minute per connection.

### 1.10 Unattended Desktop Flows

**Key characteristics:**
- Power Automate creates an RDP session, manages and releases the Windows user session
- Screen stays locked; no one can see the flow running
- Windows 10/11: no active user sessions allowed
- Windows Server: locked session with same user causes error
- User must be in Remote Desktop Users group

**Reuse Windows session:** Enable in Monitor > Machines > Settings > "Reuse sessions for unattended runs". After flow run, session gets locked and can be reused.

**Licensing:** Requires Power Automate Process plan for unattended runs.

### 1.11 Web Automation

**Supported browsers:** Microsoft Edge, Google Chrome, Mozilla Firefox, Internet Explorer, Automation browser (built-in, IE-based).

**Browser launch actions:** Launch new Microsoft Edge, Launch new Chrome, Launch new Firefox, Launch new Internet Explorer.

**Key web actions:**
- **Form filling:** Populate text field, Set drop-down list value, Click link, Press button
- **Data extraction:** Get details of web page, Get details of element, Extract data from web page
- **Structured data extraction:** CSS selectors, paging support, multi-page extraction
- **HTTP actions:** Download from web (GET/POST), Invoke web service, Invoke SOAP web service

**Web automation runs without moving the mouse** (browser can be minimized). Physical interaction mode available for cases where JavaScript events fail.

**UI elements:** Captured via Ctrl+Left click. Web UI elements use CSS/HTML selectors. Desktop UI elements from browser chrome (address bar, tabs) use UIA/MSAA selectors.

### 1.12 UI Automation

**UI element types:**
- **Desktop UI elements** -- captured from Windows applications using UIA or MSAA selectors
- **Web UI elements** -- captured from webpages, used only in browser automation actions

**Selector system:** Each UI element has one or more selectors defining the hierarchical path. Multiple selectors provide fallback. Selectors can be edited via visual builder or text editor.

**Text-based selectors:** Capture elements by their text value using the Name attribute (desktop) or Text attribute (web). Operators: Equal to, Contains, Starts with, Ends with, etc.

**Key UI automation capabilities:**
- Click, populate, press, drag-and-drop UI elements in windows
- Get/set element attributes and values
- Window management (focus, resize, move, close)

### 1.13 Excel Automation

**Core Excel actions:**

| Action | Description |
|--------|-------------|
| Launch Excel | Open new or existing workbook; options: visible/hidden, read-only, password, load add-ins |
| Attach to running Excel | Attach to an already-open workbook |
| Read from Excel worksheet | Read single cell, range, selection, or all values; modes: Typed values, Plain text, Formatted text |
| Write to Excel worksheet | Write value/variable to specified cell or active cell |
| Save Excel | Save or Save As with 20+ format options (.xlsx, .csv, .xlsm, .pdf, etc.) |
| Close Excel | Close with option to save, save as, or discard |
| Set active Excel worksheet | Activate by name or index |
| Add new worksheet | Add as first or last worksheet |
| Get all Excel worksheets | Returns list of all worksheet names |
| Get active Excel worksheet | Returns name and index of active sheet |
| Delete/Rename/Copy worksheet | Manage worksheets by name or index |
| Get first free column/row | Find the first empty column and row |
| Get first free row on column | Find first empty row in a specific column |
| Insert/Delete row | Insert above or delete by row index |
| Insert/Delete column | Insert to left or delete by column index/letter |
| Find and replace | Search cells with case/whole-cell options; returns found cell coordinates |
| Read formula from Excel | Get the formula string from a cell |
| Run Excel macro | Execute a named macro with optional arguments |
| Activate/Select/Copy/Paste/Clear cells | Cell-level operations with absolute or relative positioning |
| Resize columns/rows | Autofit or set custom width/height |
| Set color of cells | Fill background by hex code or color name |
| Sort/Filter/Clear filters | Sort by rules, filter columns, clear filters |
| Auto fill cells | Fill destination range based on source pattern |
| Lookup range | Execute Excel LOOKUP (vector or array form) |
| Get empty cell | Find first/all empty cells in range |

### 1.14 File & Folder Automation

**File actions:**

| Action | Key Parameters | Output |
|--------|---------------|--------|
| Copy file(s) | Source files, Destination folder, If exists (do nothing/overwrite) | CopiedFiles list |
| Move file(s) | Source files, Destination folder, If exists | MovedFiles list |
| Delete file(s) | File(s) to delete | -- |
| Rename file(s) | Rename scheme: Set new name, Add text, Remove text, Replace text, Change extension, Add datetime, Make sequential | RenamedFiles list |
| Read text from file | File path, Encoding (UTF-8, ASCII, Unicode), Store as single text or list | FileContents |
| Write text to file | File path, Text, Append/Overwrite, Encoding | -- |
| Read from CSV file | File path, Encoding, Trim, First line as headers, Separator | CSVTable datatable |
| Write to CSV file | Variable, File path, Encoding, Include column names, Separator | -- |
| If file exists | File path, Exists/Doesn't exist | (conditional) |
| Wait for file | Created/Deleted, File path | -- |
| Get file path part | File path | RootPath, Directory, FileName, FileNameNoExtension, FileExtension |
| Get temporary file | -- | TempFile |
| Convert file to Base64 | File path | Base64Text |
| Convert Base64 to file | Base64 text, File path | -- |
| Convert file to/from binary data | File path or binary data | BinaryData or file |

---

## Part 2: Cloud Flow Expressions

### 2.1 Expression Language Overview

Cloud flows use the Workflow Definition Language (shared with Azure Logic Apps). Expressions are entered in the expression builder within action configuration. They follow the pattern: `functionName(arguments)`.

### 2.2 Expressions in Conditions

**Logical expression functions for conditions:**

| Expression | Description | Example |
|-----------|-------------|---------|
| `and(expr1, expr2)` | True if both arguments are true | `and(greater(1,10),equals(0,0))` returns false |
| `or(expr1, expr2)` | True if either argument is true | `or(greater(1,10),equals(0,0))` returns true |
| `equals(val1, val2)` | True if two values are equal | `equals(parameters('p1'), 'someValue')` |
| `greater(val1, val2)` | True if first > second | `greater(10,10)` returns false |
| `greaterOrEquals(val1, val2)` | True if first >= second | `greaterOrEquals(10,100)` returns false |
| `less(val1, val2)` | True if first < second | `less(10,100)` returns true |
| `lessOrEquals(val1, val2)` | True if first <= second | `lessOrEquals(10,10)` returns true |
| `empty(value)` | True if object/array/string is empty | `empty('')` returns true |
| `not(expr)` | Returns opposite boolean | `not(contains('200 Success','Fail'))` returns true |
| `if(expr, trueVal, falseVal)` | Ternary conditional | `if(equals(1, 1), 'yes', 'no')` returns "yes" |

**Combining expressions example:**
```
@and(greater(item()?['Due'], item()?['Paid']), less(item()?['dueDate'], addDays(utcNow(),1)))
```

### 2.3 Data Operations

| Operation | Purpose | Key Configuration |
|-----------|---------|-------------------|
| **Compose** | Store a value (array, object, string) for reuse | Inputs: any value or expression |
| **Join** | Convert array to delimited string | From: array, Join with: separator character |
| **Select** | Reshape objects in an array (rename/add/remove properties) | From: array, Map: key-value pairs |
| **Filter array** | Reduce array to matching subset | From: array, Filter query: condition (case-sensitive) |
| **Create CSV table** | Convert JSON array to CSV | From: array, Columns: Automatic or Custom |
| **Create HTML table** | Convert JSON array to HTML table | From: array, Columns: Automatic or Custom |

### 2.4 Cloud Flow Variables

**Variable actions:**

| Action | Description |
|--------|-------------|
| Initialize variable | Declare name, type, and optional initial value (global scope only; not inside loops/conditions) |
| Set variable | Assign a new value to an existing variable |
| Increment variable | Increase integer/float by constant value |
| Decrement variable | Decrease integer/float by constant value |
| Append to string variable | Concatenate text to end of string variable |
| Append to array variable | Add item to end of array variable |

**Supported variable types:** Boolean, Integer, Float, String, Array, Object

**Access pattern:** `@variables('variableName')` or use the `variables()` function in expressions.

**Important:** Variables are global within the flow. In parallel Apply to each loops, use sequential mode to avoid race conditions.

### 2.5 Workflow Definition Language -- Complete Function Reference

**String functions:**
`chunk`, `concat`, `endsWith`, `formatNumber`, `guid`, `indexOf`, `isFloat`, `isInt`, `lastIndexOf`, `length`, `nthIndexOf`, `replace`, `slice`, `split`, `startsWith`, `substring`, `toLower`, `toUpper`, `trim`

**Collection functions:**
`chunk`, `contains`, `empty`, `first`, `intersection`, `item`, `join`, `last`, `length`, `reverse`, `skip`, `sort`, `take`, `union`

**Logical comparison functions:**
`and`, `equals`, `greater`, `greaterOrEquals`, `if`, `isFloat`, `isInt`, `less`, `lessOrEquals`, `not`, `or`

**Conversion functions:**
`array`, `base64`, `base64ToBinary`, `base64ToString`, `binary`, `bool`, `createArray`, `dataUri`, `dataUriToBinary`, `dataUriToString`, `decimal`, `decodeBase64`, `decodeDataUri`, `decodeUriComponent`, `encodeUriComponent`, `float`, `int`, `json`, `string`, `uriComponent`, `uriComponentToBinary`, `uriComponentToString`, `xml`

**Math functions:**
`add`, `div`, `max`, `min`, `mod`, `mul`, `rand`, `range`, `sub`

**Date and time functions:**
`addDays`, `addHours`, `addMinutes`, `addSeconds`, `addToTime`, `convertFromUtc`, `convertTimeZone`, `convertToUtc`, `dateDifference`, `dayOfMonth`, `dayOfWeek`, `dayOfYear`, `formatDateTime`, `getFutureTime`, `getPastTime`, `parseDateTime`, `startOfDay`, `startOfHour`, `startOfMonth`, `subtractFromTime`, `ticks`, `utcNow`

**URI parsing functions:**
`uriHost`, `uriPath`, `uriPathAndQuery`, `uriPort`, `uriQuery`, `uriScheme`

**Referencing/Workflow functions:**
`action`, `actions`, `body`, `formDataMultiValues`, `formDataValue`, `item`, `items`, `iterationIndexes`, `listCallbackUrl`, `multipartBody`, `outputs`, `parameters`, `result`, `trigger`, `triggerBody`, `triggerFormDataValue`, `triggerMultipartBody`, `triggerFormDataMultiValues`, `triggerOutputs`, `variables`, `workflow`

**Manipulation functions (JSON/XML):**
`addProperty`, `coalesce`, `removeProperty`, `setProperty`, `xpath`

### 2.6 Process Mining

Process mining in Power Automate analyzes event data from systems of record to visualize actual business processes, identify bottlenecks, and find automation opportunities.

**Key capabilities:**
- Extract event data from systems of record
- Visualize process maps showing actual execution paths
- Compare process variants
- Root cause analysis for inefficiencies
- KPI monitoring and custom reporting

**Components:** Data requirements and ingestion, data transformation and mapping, KPI visualization and analytics, process editing and refresh, process sharing.

**Use cases:** Telecommunications (streamline activation), Financial services (compliance, fintech competition), Manufacturing (supply chain), Automotive (production quality), Customer service (standardize case handling).

---

## Quick Reference: Desktop Flow vs Cloud Flow

| Feature | Desktop Flow | Cloud Flow |
|---------|-------------|------------|
| **Runs on** | Local machine (Windows) | Cloud (Microsoft servers) |
| **Variables** | % notation (`%VarName%`) | `@variables('name')` or dynamic content |
| **Loops** | Loop, Loop condition, For each | Apply to each, Do until |
| **Conditionals** | If/Else if/Else, Switch/Case | Condition, Switch |
| **Error handling** | On error (per action/block), retry, labels | Try/Catch scope, Configure run after |
| **Trigger** | Manual, cloud flow trigger, local trigger | 400+ connectors, schedules, HTTP, events |
| **Expression language** | % notation with properties | Workflow Definition Language functions |
| **Data types** | Text, Numeric, Boolean, List, Datatable, Custom object, Datetime | String, Integer, Float, Boolean, Array, Object |
