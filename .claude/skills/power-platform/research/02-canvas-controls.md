# Canvas Controls Reference Research
## Sources: 25/25 successfully fetched

---

## 1. Control Properties Reference (All Controls)

### Complete Controls List
- **Add picture** - Load images from local device for upload
- **Address input** - Dynamic address suggestions
- **Attachments** - Download/upload files
- **Audio** - Play audio clips
- **Barcode reader** - Scans barcodes, QR codes, data-matrix codes
- **Button** - Click/tap interaction
- **Camera** - Take and save photos
- **Card** - Display/edit individual field in form
- **Check box** - Boolean true/false
- **Column chart** - Vertical bars relative to axes
- **Combo box** - Search + multi-select from choices
- **Container** - Nested hierarchy for accessibility/responsiveness
- **Data table** - Tabular data display (preview)
- **Date picker** - Date specification
- **Display form** - Read-only record display
- **Drop down** - Single-select from list
- **Edit form** - Record editing/creation
- **Gallery** - List of records with multiple data types
- **Grid container** - Grid layout (preview)
- **HTML text** - Convert HTML tags
- **Horizontal container** - Auto-position children horizontally
- **Icon** - Graphic appeal
- **Image** - Show images
- **Label** - Text, numbers, dates, currency
- **Line chart** - Data points relative to axes
- **List box** - Select one or more items
- **Map** - Physical position of objects
- **Microphone** - Record sounds
- **PDF viewer** - PDF content (experimental)
- **Pen input** - Draw images/text
- **Pie chart** - Value relationships
- **Power BI tile** - Power BI in app
- **Radio** - Mutually exclusive options
- **Rating** - Value between 1 and max
- **Rich text editor** - WYSIWYG formatting
- **Screen** - Show/update data
- **Shape** - Arrows and geometric shapes
- **Slider** - Value by dragging handle
- **Label** - Text, numbers, dates, currency
- **Text input** - Type text/numbers
- **Timer** - Respond after time passes
- **Toggle** - True/false with modern GUI
- **Vertical container** - Auto-position children vertically
- **Video** - Play video clips

### Common Property Categories
- **Color and border** - Color/border that changes with interaction
- **Core** - Visibility and interaction
- **Image** - Image display and fill
- **Size and location** - Size/position relative to screen
- **Text** - Font, alignment, line height

### Key Properties A-Z

| Property | Description | Controls |
|----------|-------------|----------|
| AccessibleLabel | Screen reader label | Many |
| Align | Horizontal text alignment | Many |
| AllItems | All gallery items + control values | Gallery |
| AutoDisableOnSelect | Auto-disable while OnSelect runs | Button, Image |
| AutoHeight | Auto-grow to show all text | Label |
| AutoPause | Pause on navigate away | Audio, Timer, Video |
| AutoStart | Auto-play on screen load | Audio, Timer, Video |
| BorderColor/Style/Thickness | Border appearance | Many |
| Clear | "X" to clear text | Text input |
| Color | Text color | Many |
| DataField | Field name in card | Card |
| DataSource | Data source for form | Forms |
| Default | Initial value | Many |
| DefaultDate | Initial date | Date Picker |
| DefaultMode | Edit, New, or View | Edit form |
| DelayOutput | 0.5s input delay | Text input |
| Direction | First item position | Gallery |
| Disabled | User can interact | Many |
| DisplayMode | Edit, View, Disabled | Many |
| Duration | Timer duration (ms) | Timer |
| Fill | Background color | Many |
| Font/FontWeight | Font settings | Many |
| Height/Width | Dimensions | Many |
| HintText | Placeholder text | Text input |
| HtmlText | HTML content | HTML text |
| Image | Image name/URL | Image |
| ImagePosition | Fill, Fit, Stretch, Tile, Center | Many |
| Item | Record to show/edit | Forms |
| Items | Data source for list | Many |
| LastSubmit | Last submitted record | Edit form |
| Layout | Vertical/Horizontal | Gallery, Slider |
| Max/Min | Value range | Rating, Slider |
| MaxLength | Max characters | Text input |
| Mode | Edit/New, Draw/Erase, SingleLine/MultiLine/Password | Various |
| OnChange | Value change actions | Many |
| OnSelect | Click/tap actions | Many |
| OnTimerEnd | Timer finish actions | Timer |
| Overflow | Scrollbar when Wrap=true | Label |
| Photo | Captured image | Camera |
| Pressed | True while pressed | Button |
| Repeat | Timer auto-restart | Timer |
| Reset | Revert to default | Many |
| Selected | Selected item record | Drop down, Gallery |
| SelectedDate | Current date | Date Picker |
| SelectMultiple | Allow multi-select | List Box |
| ShowNavigation | Show gallery arrows | Gallery |
| ShowScrollbar | Show scrollbar | Gallery |
| ShowValue | Show value on hover | Rating, Slider |
| Snap | Gallery snap to full items | Gallery |
| Start | Start media/timer | Audio, Timer, Video |
| Stream/StreamRate | Camera auto-update | Camera |
| TemplateFill/Padding/Size | Gallery template | Gallery |
| Text | Display text | Many |
| Tooltip | Hover text | Many |
| Transparency | 0 (opaque) to 1 (transparent) | Image |
| Unsaved | Form has unsaved changes | Edit form |
| Updates | Values to write back | Edit form |
| Valid | Entries valid for submit | Card, Edit form |
| Value | Control value | Check box, Radio, Slider, Toggle |
| Visible | Show/hide | Many |
| Wrap | Text wraps | Label |
| WrapCount | Records per row | Gallery |
| X/Y | Position | Many |

---

## 2. Button Control

### Key Properties
- **OnSelect**: Actions on click/tap
- **Text**: Button text
- **AutoDisableOnSelect**: Disable while OnSelect runs
- **Pressed**: True while being pressed

### Shape Customization
- Height=Width=300 for square; all Radius=150 for circle
- RadiusTopLeft+RadiusBottomRight=300 for leaf shape
- `ColorFade(Color.BlueViolet, 0.5)` for hover intensity

### Examples
```powerfx
// Navigation
Navigate(ScreenName, ScreenTransitionValue)
// Update context
UpdateContext({Total: Total + Value(Source.Text)})
// Chain actions
UpdateContext({Total: Total + Value(Source.Text)}); UpdateContext({ClearInput: ""})
```

---

## 3. Text Input Control

### Key Properties
- **Default**: Initial value
- **Text**: Current text
- **Mode**: SingleLine, MultiLine, Password
- **Format**: Number or Text
- **DelayOutput**: 0.5s delay (useful for filtering)
- **HintText**: Placeholder text
- **MaxLength**: Max characters
- **Clear**: Show "X" to clear (SingleLine only)
- **VirtualKeyboardMode**: Text or numeric keyboard

### Examples
```powerfx
// Collect from inputs
Collect(Names, {FirstName: inputFirst.Text, LastName: inputLast.Text})
// Password check
If(inputPassword.Text = "P@ssw0rd", "Access granted", "Access denied")
```

---

## 4. Drop Down Control

### Key Properties
- **Items**: Data source (max 500 items)
- **Selected**: Selected record
- **Value**: Column to display
- **AllowEmptySelection**: Allow no selection

### Examples
```powerfx
// Simple list
["Seattle", "Tokyo", "London"]
// Distinct values
Distinct(Accounts, 'Address 1: City')
// Filter gallery by dropdown
Filter(Accounts, address1_city == Cities.Selected.Result)
```

---

## 5. Combo Box Control

### Key Properties
- **Items**: Data source
- **DefaultSelectedItems**: Initial selections (replaces deprecated Default)
- **SelectedItems**: All selected items
- **Selected**: Last selected item
- **SelectMultiple**: Single or multi-select
- **IsSearchable**: Enable search (server-side, no perf impact)
- **SearchFields**: `["Col1", "Col2"]`
- **DisplayFields**: `["Col1", "Col2"]`

### Examples
```powerfx
// Default first record
First(DataSource)
// Display selections
Concat(ComboBox1.SelectedItems, 'Account Name', ", ")
```

### Notes
- Selections not maintained when scrolling gallery
- Items must be delegable; If statements in Items not supported for search
- People Picker: use Person template from Layout settings

---

## 6. Gallery Control

### Key Properties
- **Items**: Data source
- **Selected**: Selected item
- **Default**: Initial selection
- **AllItems/AllItemsCount**: Loaded items and count
- **TemplateFill/Padding/Size**: Template styling
- **WrapCount**: Items per row
- **Snap**: Auto-snap to full items
- **ShowNavigation/ShowScrollbar**: Navigation options
- **DelayItemLoading**: Defer until after screen loads

### Limitations
- Max nesting: 2 levels (no triple-nested galleries)
- Unsupported inside gallery: Display/Edit form, PDF viewer, Power BI tile, Rich text editor
- Minimum TemplateSize: 1
- ComboBox/DatePicker/Slider/Toggle with OnChange patching same source = infinite loop

---

## 7. Edit Form & Display Form Controls

### Key Properties
- **DataSource**: Table data source
- **Item**: Record to show/edit (e.g., `Gallery.Selected`)
- **DefaultMode**: FormMode.Edit, FormMode.New, FormMode.View
- **Mode**: Current mode
- **Error/ErrorKind**: Error info after SubmitForm
- **LastSubmit**: Last successful submission
- **Unsaved**: Has unsaved changes
- **Updates**: Record of values to write back
- **Valid**: All cards valid for submission

### ErrorKind Values
- ErrorKind.Conflict: Another user changed same record
- ErrorKind.None: Unknown error
- ErrorKind.Sync: Data source error
- ErrorKind.Validation: Validation issue

### CRUD Pattern
```powerfx
NewForm(Form1)          // Switch to New mode
EditForm(Form1)         // Switch to Edit mode
ViewForm(Form1)         // Switch to View mode
SubmitForm(Form1)       // Save changes
ResetForm(Form1)        // Cancel changes

// Enable save only when valid
If(Form.Valid, DisplayMode.Edit, DisplayMode.Disabled)

// Manual update with Patch
Patch(DataSource, Form1.Updates)
```

---

## 8. Data Table Control

### Key Properties
- **Items**: Data source
- **Selected**: Selected row (read-only display)
- **NoDataText**: Message when empty

### Capabilities
- Read-only data, single row always selected, hyperlinks, adjustable column widths
- NOT available: individual column styling, inside forms, row height changes, images, inline editing, multi-row select

---

## 9. Date Picker Control

### Key Properties
- **DefaultDate**: Initial date
- **SelectedDate**: Current date (local time)
- **Format**: ShortDate, LongDate, or custom (yyyy/mm/dd)
- **Language**: e.g., "en-us", "fr-fr"
- **StartYear/EndYear**: Allowed range
- **IsEditable**: Direct text editing or calendar only

### Examples
```powerfx
DateDiff(Today(), Deadline.SelectedDate) & " days to go!"
```

---

## 10. Check Box Control

### Key Properties
- **Default**: Initial value
- **Value**: Current boolean
- **Text**: Label text
- **CheckboxSize**: Width/height of box
- **CheckmarkFill**: Checkmark color
- **OnCheck/OnUncheck**: State change actions

### Example
```powerfx
If(chkReserve.Value = true, true)  // Conditional visibility
```

---

## 11. Radio Control

### Key Properties
- **Items**: Data source
- **Selected**: Selected record
- **Value**: Current value
- **Layout**: Vertical or Horizontal
- **RadioSize**: Circle diameter
- **RadioSelectionFill**: Selected circle color

### Example
```powerfx
If("Premium" in Pricing.Selected.Value, "$200/day", "$150/day")
```

---

## 12. List Box Control

### Key Properties
- **Items**: Data source (always shows all items, unlike Drop down)
- **SelectMultiple**: Allow multi-select
- **Selected**: Single selected item
- **SelectedItems**: All selected items (multi-select)

### Example
```powerfx
If("Carpet" in CategoryList.SelectedItems.Value, true)
```

---

## 13. Slider Control

### Key Properties
- **Min/Max**: Value range
- **Default**: Initial value
- **Value**: Current value
- **Layout**: Vertical or Horizontal
- **ShowValue**: Display value on hover
- **HandleActiveFill/Fill/HoverFill**: Handle styling
- **RailFill/ValueFill**: Rail styling

### Example
```powerfx
Filter(CityPopulations, Population > MinPopulation)
```

---

## 14. Toggle Control

### Key Properties
- **Default/Value**: Boolean state
- **FalseFill/TrueFill**: State colors
- **FalseText/TrueText**: State labels
- **HandleFill**: Handle color
- **ShowLabel**: Show text label
- **OnCheck/OnUncheck**: State change actions

### Example
```powerfx
If(MemberDiscount.Value = true, "Price: $75", "Price: $100")
```

---

## 15. Rating Control

### Key Properties
- **Max**: Maximum stars
- **Default**: Initial value
- **RatingFill**: Star color
- **ReadOnly**: Prevent changes
- **ShowValue**: Display value

### Example
```powerfx
If(Quantitative.Value > 3, "What did you like?", "How can we improve?")
```

---

## 16. Rich Text Editor Control

### Key Properties
- **Default**: Initial HTML text (input)
- **HtmlText**: Resulting HTML (output)
- **EnableSpellCheck**: Browser spell check

### Supported Features
Bold, italic, underline, text/highlight color, text size, numbered/bulleted lists, hyperlinks, clear formatting

### Limitations
- Removes script, style, object tags
- Pasted images may not appear consistently
- Hyperlinks don't open in view mode
- List styles may be removed in model-driven apps

---

## 17. Image Control

### Key Properties
- **Image**: Name or URL (HTTPS, anonymous access)
- **ImagePosition**: Fill, Fit, Stretch, Tile, Center
- **ImageRotation**: None, CW 90, CCW 90, CW 180
- **Transparency**: 0 (opaque) to 1 (transparent)
- **FlipHorizontal/FlipVertical**: Flip before display
- **ApplyEXIFOrientation**: Auto-apply EXIF data

---

## 18. Label Control

### Key Properties
- **Text**: Display text
- **AutoHeight**: Auto-grow to fit text
- **Wrap**: Multi-line text wrapping
- **Overflow**: Scrollbar when Wrap=true
- **Live**: Screen reader mode (Off, Polite, Assertive)
- **Role**: Semantic role (e.g., Heading 1)

---

## 19. HTML Text Control

### Key Properties
- **HtmlText**: HTML content to render
- **AutoHeight**: Auto-grow (max 7680)

### Important
- Content is relatively positioned by default
- For absolute positioning: `"<div style='position:relative'>" & content & "</div>"`
- Browser default styles may be stripped; use inline styles

---

## 20. Timer Control

### Key Properties
- **Duration**: Run time in ms (max 24 hours, default 60s)
- **Repeat**: Auto-restart
- **AutoStart**: Start on screen load
- **AutoPause**: Pause on navigate away
- **Start**: Whether running
- **OnTimerStart/OnTimerEnd**: Event handlers

### Examples
```powerfx
// Countdown
"Seconds remaining: " & RoundUp(10 - Timer.Value/1000, 0)
// Fade animation
ColorFade(Color.BlueViolet, Timer.Value/5000)
```

### Notes
- Set Visible=false for background timers
- Only runs in Preview mode in Studio

---

## 21. Camera Control

### Key Properties
- **Photo**: Captured image
- **Stream**: Auto-updated preview (based on StreamRate)
- **StreamRate**: 100ms to 3,600,000ms
- **AvailableDevices**: Table of cameras (Id, Name)
- **Camera**: Camera ID to use

### Image Usage
```powerfx
Image1.Image = Camera1.Photo           // Display
Set(myPhoto, Camera1.Photo)            // Variable
Collect(MyPix, Camera1.Photo)          // Collection
JSON(Camera1.Photo)                     // Base64
```

### Limitations
- Max resolution: 640x480 (use Add picture for full res)
- Supported: Edge, Chrome, Firefox, Opera + mobile

---

## 22. Pen Input Control

### Key Properties
- **Image**: Output drawing
- **Color**: Stroke color
- **Mode**: Draw or Erase
- **ShowControls**: Show draw/erase/clear icons

### Not accessible to screen readers or keyboard users — always provide alternative input

---

## 23. Container Control

Groups controls with own properties (unlike simple groups).

| Feature | Container | Group |
|---------|-----------|-------|
| Own properties | Yes | No |
| Affects layout | Yes | No |
| Screen reader structure | Yes | No |

### Limitations
- Don't work within forms
- Unsupported: Data table, PDF viewer, Web barcode scanner

---

## 24. Horizontal Container

### Key Properties
- **Direction**: Horizontal/Vertical layout
- **Justify**: Primary axis: Start, End, Center, Space Between
- **Align**: Cross axis: Start, Center, End, Stretch
- **Gap**: Space between children (px)
- **Horizontal/Vertical Overflow**: Scroll or Hide
- **Wrap**: Content wraps to new rows

### Child Properties
- **Align in container**: Override parent alignment
- **Fill portions**: Proportional growth (A=1, B=2 → A gets 1/3, B gets 2/3)
- **Minimum width**: Minimum size

---

## 25. Vertical Container

Same properties as Horizontal Container but distributes space vertically. Children auto-positioned — no manual X/Y needed.

---

## Cross-Control Patterns

### Data Binding
```powerfx
Gallery.Items = DataSource
Form.Item = Gallery.Selected
Form.DataSource = DataSource
```

### CRUD Operations
```powerfx
NewForm(Form1)                              // Create
Form.Item = Gallery.Selected                // Read
EditForm(Form1); SubmitForm(Form1)         // Update
Remove(DataSource, Gallery.Selected)        // Delete
```

### Conditional Visibility
```powerfx
If(Checkbox1.Value, true, false)
If(Dropdown1.Selected.Value = "Option1", true, false)
```

### Data Filtering
```powerfx
Filter(DataSource, Column = Dropdown1.Selected.Value)
Filter(DataSource, NumericColumn > Slider1.Value)
Search(DataSource, TextInput1.Text, "ColumnName")
```
