# Power Automate Desktop Flows Reference

## Overview

Desktop flows provide robotic process automation (RPA) for automating repetitive desktop processes. Automate legacy apps, modern web/desktop apps, Excel, and file/folder operations through a drag-and-drop designer or by recording actions.

## Creating Desktop Flows

| Method | Steps |
|--------|-------|
| From console | Launch app > New flow > Enter name > Create > Design > Save |
| From examples | Examples tab > Right-click > Create a copy > Stored under My flows |
| From cloud flows | Use "Run a flow built with Power Automate for desktop" action |

## Recording

- **Standard recorder**: captures mouse/keyboard activity relative to UI elements; generates UI and browser automation actions
- **Image-based recorder**: uses image recognition and OCR (Tesseract) for apps without accessibility APIs

Desktop capturing modes: **UIA** (modern WPF/WinForms/UWP apps) and **MSAA** (legacy VB6/Win32 apps).

Features: drag-and-drop replication, drop-down handling, browser launch during recording, date/color pickers, IME support. Limitation: conditionals and loops cannot be recorded.

## Action Categories

| A-C | D-H | I-R | S-Z |
|-----|-----|-----|-----|
| Active Directory | Database | IBM Cognitive | SAP automation |
| AI Builder | Date time | Logging | Scripting |
| AWS, Azure | Email | Loops | SharePoint |
| Browser automation | Excel | Message boxes | System |
| Clipboard | Exchange Server | Microsoft Cognitive | Terminal emulation |
| Cloud connectors | File, Folder | Mouse and keyboard | Text |
| CMD session | Flow control | OCR | UI automation |
| Compression | FTP | Outlook | Variables |
| Conditionals | Google Cognitive | PDF | Windows services |
| Custom actions, Cryptography | HTTP | Run flow | Workstation, Workqueues, XML/Word |

## Variables and Data Types

### Simple Types

| Type | Notation | Example |
|------|----------|---------|
| Text | Plain text | `Hello World` |
| Numeric | Number or math expression | `42` or `%5 + 3%` |
| Boolean | `%True%` or `%False%` | `%True%` |
| Datetime | `%d"yyyy-MM-dd HH:mm:ss"%` | `%d"2022-03-25"%` |

### Advanced Types

| Type | Access Notation |
|------|-----------------|
| List | `%List[0]%`, `%List[2:4]%` (slicing) |
| Datatable | `%DT[0][1]%` or `%DT[0]['ColName']%` |
| Datarow | `%Row[0]%` or `%Row['ColName']%` |
| Custom object | `%{ 'Key1': 'Val1', 'Key2': 'Val2' }%` |

Instance types: Web browser, Window, Excel, Outlook. Connection types: SQL, Exchange, FTP.

## Loops

| Action | Purpose | Key Parameters |
|--------|---------|----------------|
| Loop | Fixed iteration count | Start from, End to, Increment by |
| Loop condition | Repeat while condition true | First operand, Operator, Second operand |
| For each | Iterate list/datatable/datarow | Value to iterate |
| Exit loop | Terminate early | - |
| Next loop | Skip to next iteration | - |

Operators: `=`, `<>`, `>`, `>=`, `<`, `<=`

## Conditionals

| Action | Purpose |
|--------|---------|
| If / Else if / Else | Conditional branching |
| Switch / Case / Default case | Multi-value dispatch |

Operators: `=`, `<>`, `>`, `>=`, `<`, `<=`, Contains, Does not contain, Is empty, Is not empty, Starts with, Ends with, Is blank, Is not blank.

## Error Handling

**Error types**: Design-time errors (prevent running) and run-time exceptions (can be handled).

### Single-Action Error Handling (On Error)

1. Retry action: set retries and interval
2. Continue flow run: go to next action, repeat action, or go to label
3. New rule: set variable or run subflow on error
4. Advanced: configure each exception separately

### Block Error Handling (On Block Error)

Wraps multiple actions in a single handler. Options: continue from beginning or end of block. Individual action handling takes precedence over block handling.

**Get last error**: retrieves Error variable with action name, location, index, subflow, details, message. Optional "Clear error" flag.

## Triggering Desktop Flows

Prerequisites: registered machine/machine group, work/school account, desktop flow connection, appropriate license.

Steps: Cloud flow > New step > "Run a flow built with Power Automate for desktop" > Select connection > Choose run mode > Select desktop flow.

Input variables (cloud-to-desktop, max 2 MB) and output variables (desktop-to-cloud). Throughput limit: 70 runs per minute per connection.

## Attended vs Unattended Runs

**Attended**: user logged in, can see flow running. Requires attended license.

**Unattended**: Power Automate creates RDP session, screen stays locked. Windows 10/11: no active user sessions allowed. User must be in Remote Desktop Users group. Requires Process plan license. Enable session reuse in Monitor > Machines > Settings.

## Web Automation

Supported browsers: Edge, Chrome, Firefox, Internet Explorer, Automation browser (built-in).

- **Form filling**: populate text field, set drop-down, click link, press button
- **Data extraction**: get details of web page/element, extract data from web page
- **Structured extraction**: CSS selectors, paging support, multi-page extraction
- **HTTP actions**: download from web (GET/POST), invoke web service, invoke SOAP

Web automation runs without moving the mouse. UI elements captured via Ctrl+Left click using CSS/HTML selectors.

## UI Automation

- **Desktop UI elements**: captured from Windows apps using UIA or MSAA selectors
- **Web UI elements**: captured from webpages for browser automation actions
- Selector system: hierarchical path with multiple selectors as fallback
- Capabilities: click, populate, press, drag-and-drop, get/set attributes, window management

## Excel Automation

Key actions: Launch/Attach Excel, Read from worksheet (cell/range/all), Write to worksheet, Save/Close, Get/Set active worksheet, Add/Delete/Rename worksheet, Get first free column/row, Insert/Delete row/column, Find and replace, Run macro, Sort/Filter, Auto fill, Lookup range.

Read modes: Typed values, Plain text, Formatted text. Save formats: .xlsx, .csv, .xlsm, .pdf, and more.

## Process Mining

Analyzes event data from systems of record to visualize actual business processes. Capabilities: process map visualization, variant comparison, root cause analysis, KPI monitoring. Components: data ingestion, transformation, visualization, process editing, sharing.
