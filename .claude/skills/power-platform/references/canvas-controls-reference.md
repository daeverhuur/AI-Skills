# Canvas Controls Reference

> Distilled from: `research/02-canvas-controls.md`
> Related: `research/01-canvas-apps.md` (app structure), `research/06-power-fx-language.md` (formula syntax), `research/07-power-fx-functions-a-l.md` / `research/08-power-fx-functions-m-z.md` (function details)

---

## Controls Summary Table

| Control | Primary Use | Key Output Property |
|---------|------------|-------------------|
| Button | Trigger actions | `Pressed` |
| Text input | Capture text/numbers | `.Text` |
| Drop down | Single-select from list (max 500) | `.Selected.Value` |
| Combo box | Searchable multi-select | `.SelectedItems` |
| Gallery | Display record list | `.Selected` |
| Edit form | Create/update records | `.Updates`, `.Valid` |
| Display form | Read-only record view | - |
| Data table | Tabular read-only display | `.Selected` |
| Date picker | Date selection | `.SelectedDate` |
| Check box | Boolean toggle | `.Value` (bool) |
| Radio | Mutually exclusive choice | `.Selected.Value` |
| List box | Multi-select always visible | `.SelectedItems` |
| Slider | Numeric range selection | `.Value` (number) |
| Toggle | On/off switch | `.Value` (bool) |
| Rating | Star rating input | `.Value` (number) |
| Rich text editor | HTML text editing | `.HtmlText` |
| Label | Display text | `.Text` |
| Image | Display images | - |
| HTML text | Render HTML content | - |
| Timer | Time-based triggers | `.Value` (ms elapsed) |
| Camera | Capture photos | `.Photo` |
| Pen input | Freehand drawing | `.Image` |
| Container | Group with own properties | - |
| Horizontal container | Auto-layout horizontal | - |
| Vertical container | Auto-layout vertical | - |

---

## Common Properties (All Controls)

**Layout**: `X`, `Y`, `Width`, `Height`, `Visible`, `DisplayMode` (Edit/View/Disabled)
**Style**: `Fill`, `BorderColor`, `BorderStyle`, `BorderThickness`, `Color`, `Font`, `FontWeight`
**Behavior**: `OnSelect`, `OnChange`, `Disabled`, `Tooltip`, `AccessibleLabel`

---

## Input Controls

### Button
**Key props**: `Text`, `OnSelect`, `AutoDisableOnSelect`, `Pressed`
**Shape tricks**: Height=Width + all Radius=half for circle; `ColorFade(Color.BlueViolet, 0.5)` for hover
```powerfx
// Navigate with transition
Navigate(DetailScreen, ScreenTransition.Fade)
// Chain multiple actions
UpdateContext({Total: Total + Value(Source.Text)}); Navigate(NextScreen)
```

### Text Input
**Key props**: `Text`, `Default`, `HintText`, `Mode` (SingleLine/MultiLine/Password), `Format` (Text/Number), `DelayOutput`, `MaxLength`, `Clear`, `VirtualKeyboardMode`
- `DelayOutput`: adds 0.5s debounce -- use when filtering data sources
- `Clear`: shows X button (SingleLine only)
```powerfx
// Collect form data
Collect(Contacts, {Name: txtName.Text, Email: txtEmail.Text})
// Search with delay
Search(Products, txtSearch.Text, "ProductName")
```

### Date Picker
**Key props**: `DefaultDate`, `SelectedDate` (local time), `Format` (ShortDate/LongDate/custom), `StartYear`, `EndYear`, `IsEditable`, `Language`
```powerfx
// Days until deadline
"Due in " & DateDiff(Today(), dpDeadline.SelectedDate) & " days"
```

### Rich Text Editor
**Key props**: `Default` (HTML input), `HtmlText` (HTML output), `EnableSpellCheck`
**Supports**: Bold, italic, underline, text/highlight color, text size, lists, hyperlinks
**Limitations**: Strips script/style/object tags; pasted images inconsistent; hyperlinks inactive in view mode

---

## Selection Controls

### Drop Down
**Key props**: `Items` (max 500), `Selected`, `AllowEmptySelection`
```powerfx
// Static list
["Active", "Inactive", "Pending"]
// Distinct values from data source
Distinct(Accounts, 'Status')
// Filter gallery by selection
Filter(Orders, Status = ddStatus.Selected.Value)
```

### Combo Box
**Key props**: `Items`, `DefaultSelectedItems`, `SelectedItems`, `SelectMultiple`, `IsSearchable`, `SearchFields` (`["Col1","Col2"]`), `DisplayFields`
- Search is server-side (no perf impact on large datasets)
- Use `DefaultSelectedItems` instead of deprecated `Default`
- People picker: select Person template in Layout settings
```powerfx
// Show selected items as text
Concat(cbCategories.SelectedItems, Name, ", ")
```
**Gotcha**: Selections lost when scrolling in a gallery; `If` statements in Items break search

### Radio
**Key props**: `Items`, `Selected`, `Value`, `Layout` (Vertical/Horizontal), `RadioSize`, `RadioSelectionFill`
```powerfx
// Conditional pricing
If(rdPlan.Selected.Value = "Premium", 200, 100)
```

### List Box
**Key props**: `Items`, `SelectMultiple`, `Selected`, `SelectedItems`
Always shows all items (unlike Drop down which collapses).
```powerfx
// Check if specific item selected
"Carpet" in lbCategories.SelectedItems.Value
```

### Check Box
**Key props**: `Default`, `Value` (bool), `Text`, `CheckboxSize`, `CheckmarkFill`, `OnCheck`, `OnUncheck`
```powerfx
// Conditional visibility on another control
Visible = chkShowDetails.Value
```

### Toggle
**Key props**: `Default`, `Value` (bool), `TrueText`, `FalseText`, `TrueFill`, `FalseFill`, `HandleFill`, `ShowLabel`, `OnCheck`, `OnUncheck`
```powerfx
// Price with discount
If(tglDiscount.Value, Price * 0.75, Price)
```

### Slider
**Key props**: `Min`, `Max`, `Default`, `Value`, `Layout` (Vertical/Horizontal), `ShowValue`
```powerfx
// Filter by threshold
Filter(Cities, Population > sldMinPop.Value)
```

### Rating
**Key props**: `Max`, `Default`, `Value`, `RatingFill`, `ReadOnly`, `ShowValue`
```powerfx
// Adaptive follow-up
If(rtFeedback.Value > 3, "What did you like?", "How can we improve?")
```

---

## Data Display Controls

### Gallery
**Key props**: `Items`, `Selected`, `Default`, `AllItems`, `AllItemsCount`, `TemplateFill`, `TemplatePadding`, `TemplateSize` (min 1), `WrapCount`, `Snap`, `ShowNavigation`, `ShowScrollbar`, `DelayItemLoading`, `Direction`
**Limitations**:
- Max nesting: 2 levels (no gallery inside gallery inside gallery)
- Cannot contain: Edit/Display form, PDF viewer, Power BI tile, Rich text editor
- OnChange patching same data source from ComboBox/DatePicker/Slider/Toggle inside gallery = infinite loop
```powerfx
// Filtered gallery
Filter(Products, Category = ddCategory.Selected.Value)
// Gallery with search
Search(Contacts, txtSearch.Text, "FullName", "Email")
```

### Edit Form
**Key props**: `DataSource`, `Item` (e.g. `Gallery.Selected`), `DefaultMode` (FormMode.Edit/New/View), `Mode`, `Error`, `ErrorKind`, `LastSubmit`, `Unsaved`, `Updates`, `Valid`
**ErrorKind values**: `.Conflict` (concurrent edit), `.None` (unknown), `.Sync` (data source), `.Validation`
```powerfx
// Full CRUD pattern
NewForm(frmContact)                        // Create mode
EditForm(frmContact)                       // Edit mode
ViewForm(frmContact)                       // View mode
SubmitForm(frmContact)                     // Save
ResetForm(frmContact)                      // Cancel

// Conditional save button
DisplayMode = If(frmContact.Valid, DisplayMode.Edit, DisplayMode.Disabled)

// OnSuccess handler
Notify("Saved!"); Back()

// Manual patch from form values
Patch(Contacts, frmContact.Updates)
```

### Display Form
Same data binding as Edit form (`DataSource`, `Item`) but read-only. Use `ViewForm()` to switch an Edit form to view mode instead of using a separate Display form.

### Data Table
**Key props**: `Items`, `Selected`, `NoDataText`
Read-only tabular display. Single row always selected. Supports hyperlinks and adjustable column widths.
**Cannot**: Style individual columns, nest in forms, change row height, show images, inline edit, multi-select

### Label
**Key props**: `Text`, `AutoHeight`, `Wrap`, `Overflow` (scrollbar when Wrap=true), `Live` (Off/Polite/Assertive for screen readers), `Role` (Heading 1, etc.)
```powerfx
// Dynamic text
"Total: $" & Text(Sum(Cart, Price * Qty), "#,##0.00")
```

### Image
**Key props**: `Image` (name or HTTPS URL, anonymous access), `ImagePosition` (Fill/Fit/Stretch/Tile/Center), `ImageRotation`, `Transparency` (0-1), `FlipHorizontal`, `FlipVertical`, `ApplyEXIFOrientation`

### HTML Text
**Key props**: `HtmlText`, `AutoHeight` (max 7680px)
- Content positioned relatively by default
- Wrap in `<div style='position:relative'>` for absolute positioning inside
- Browser default styles may be stripped; use inline styles

---

## Media & Sensor Controls

### Camera
**Key props**: `Photo`, `Stream`, `StreamRate` (100-3,600,000 ms), `AvailableDevices`, `Camera` (device ID)
Max resolution: 640x480. Use Add Picture control for full resolution.
```powerfx
Set(capturedPhoto, Camera1.Photo)          // Save to variable
Collect(Photos, Camera1.Photo)             // Add to collection
JSON(Camera1.Photo)                        // Convert to Base64
```

### Pen Input
**Key props**: `Image` (output), `Color`, `Mode` (Draw/Erase), `ShowControls`
Not accessible to screen readers or keyboard. Always provide an alternative input method.

### Timer
**Key props**: `Duration` (ms, max 24h, default 60s), `Repeat`, `AutoStart`, `AutoPause`, `Start`, `OnTimerStart`, `OnTimerEnd`
- Set `Visible=false` for background timers
- Only runs in Preview mode inside Studio
```powerfx
// Countdown display
"Seconds left: " & RoundUp(10 - Timer1.Value/1000, 0)
// Color fade animation
Fill = ColorFade(Color.BlueViolet, Timer1.Value/5000)
// Auto-refresh pattern: Repeat=true, Duration=30000, OnTimerEnd=Refresh(DataSource)
```

---

## Layout Controls

### Container
Groups controls with own properties (Fill, Visible, etc.). Provides semantic structure for screen readers.

| Feature | Container | Group |
|---------|-----------|-------|
| Own properties | Yes | No |
| Affects layout | Yes | No |
| Screen reader structure | Yes | No |

**Cannot contain**: Data table, PDF viewer, Web barcode scanner. Does not work inside forms.

### Horizontal / Vertical Container
**Key props**: `Direction`, `Justify` (Start/End/Center/SpaceBetween), `Align` (Start/Center/End/Stretch), `Gap` (px), `Wrap`, `HorizontalOverflow`, `VerticalOverflow`
**Child props**: `AlignInContainer` (override parent), `FillPortions` (proportional sizing), `MinimumWidth`
```
// FillPortions example: Child A=1, Child B=2
// A gets 1/3 of space, B gets 2/3
```
Children are auto-positioned. No manual X/Y needed.

---

## Cross-Control Patterns

### Gallery + Form Data Binding
```powerfx
// Standard master-detail pattern
Gallery1.Items = Contacts                  // Gallery shows list
frmDetail.Item = Gallery1.Selected         // Form shows selected record
frmDetail.DataSource = Contacts            // Form writes to same source
```

### CRUD Operations
```powerfx
NewForm(frmDetail)                         // C: prepare new record
frmDetail.Item = Gallery1.Selected         // R: bind to selected
EditForm(frmDetail); SubmitForm(frmDetail) // U: edit and save
Remove(Contacts, Gallery1.Selected)        // D: delete selected
```

### Conditional Visibility
```powerfx
// Show section based on checkbox
sectionContainer.Visible = chkShowAdvanced.Value
// Show based on dropdown
panelPremium.Visible = ddTier.Selected.Value = "Premium"
```

### Data Filtering
```powerfx
// Dropdown filter
Filter(Products, Category = ddCategory.Selected.Value)
// Slider threshold
Filter(Cities, Population > sldMinPop.Value)
// Text search
Search(Contacts, txtSearch.Text, "FullName")
// Combined filters
Filter(Products,
    Category = ddCategory.Selected.Value,
    Price <= sldMaxPrice.Value,
    StartsWith(Name, txtSearch.Text)
)
```

### Input Validation Pattern
```powerfx
// Enable submit only when form is valid and required fields filled
btnSubmit.DisplayMode = If(
    frmEdit.Valid && !IsBlank(txtName.Text),
    DisplayMode.Edit,
    DisplayMode.Disabled
)
```
