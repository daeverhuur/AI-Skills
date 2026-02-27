# PCF (Power Apps Component Framework) Reference

> Distilled from research/12-pcf-developer.md

---

## Overview

PCF enables code components for model-driven and canvas apps. Components render as part of the same context as other platform components (unlike HTML web resources), providing seamless UX.

**Component types:**

| Type | `control-type` | Interface | Container |
|------|---------------|-----------|-----------|
| Standard | `standard` | `StandardControl<IInputs, IOutputs>` | Receives empty `div` in `init()` |
| React/Virtual | `virtual` | `ReactControl<IInputs, IOutputs>` | No `div`; returns `ReactElement` from `updateView()` |

**Property binding:**
- `bound` -- bound to a column value
- `input` -- bound to a column or allows a static value

---

## Component Lifecycle

```
init() --> updateView() --> [user interaction] --> getOutputs() --> updateView() --> ... --> destroy()
```

| Method | Purpose |
|--------|---------|
| `init(context, notifyOutputChanged, state, container)` | One-time initialization. Set up DOM, event listeners, store references. |
| `updateView(context)` | Called when any property bag value changes (field values, datasets, container resize). |
| `getOutputs()` | Return output values matching `IOutputs` interface. |
| `destroy()` | Cleanup: remove event listeners, cancel remote calls. |

---

## StandardControl Template

```typescript
export class MyControl implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  private _value: number;
  private _notifyOutputChanged: () => void;
  private _container: HTMLDivElement;
  private _context: ComponentFramework.Context<IInputs>;

  constructor() {}

  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ): void {
    this._context = context;
    this._notifyOutputChanged = notifyOutputChanged;
    this._container = container;
    // Create DOM elements, attach to container
  }

  public updateView(context: ComponentFramework.Context<IInputs>): void {
    this._value = context.parameters.myProperty.raw!;
  }

  public getOutputs(): IOutputs {
    return { myProperty: this._value };
  }

  public destroy(): void {
    // Remove event listeners
  }
}
```

---

## ReactControl Template

```typescript
export class MyReactControl implements ComponentFramework.ReactControl<IInputs, IOutputs> {
  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary
  ): void { }

  public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
    return React.createElement(MyComponent, {
      value: context.parameters.myProp.raw
    });
  }

  public getOutputs(): IOutputs { return {}; }
  public destroy(): void { }
}
```

React controls use platform-shared React and Fluent UI (no bundling your own). Create with `pac pcf init -fw react`. Cannot be used in Power Pages.

**Platform library versions:**

| Library | npm Package | Version |
|---------|-------------|---------|
| React | react | 17.0.2 (Model) / 16.14.0 (Canvas) |
| Fluent 8 | @fluentui/react | 8.29.0 or 8.121.1 |
| Fluent 9 | @fluentui/react-components | 9.68.0 |

Fluent 8 and 9 cannot coexist in the same manifest.

---

## React Controls Deep Dive

### Shared React Instance

Virtual (React) controls share the platform's React instance rather than bundling their own copy. This provides:
- Reduced bundle size (React + ReactDOM not included in component output)
- Single React tree for the entire app, avoiding context/provider conflicts
- Consistent Fluent UI theme alignment with the host application

The platform injects `React` and `ReactDOM` at runtime. Install matching versions as **devDependencies** for local development and type checking, but they will not be included in the final bundle:

```bash
npm install react@17.0.2 react-dom@17.0.2 --save-dev
```

### Fluent UI v8 vs v9

| Aspect | Fluent UI v8 | Fluent UI v9 |
|--------|-------------|-------------|
| Package | `@fluentui/react` | `@fluentui/react-components` |
| Architecture | Class components, SCSS-in-JS | Griffel (atomic CSS-in-JS), hooks-based |
| Theming | `ThemeProvider`, `ITheme` | `FluentProvider`, `tokens` |
| Tree-shaking | Partial | Full (each component independently importable) |
| Direction | Maintenance mode | Active development |
| Platform version | 8.29.0 or 8.121.1 | 9.68.0 |

**Rule:** You cannot declare both Fluent 8 and Fluent 9 platform libraries in the same manifest. Choose one per component.

### FluentProvider for v9

When using Fluent UI v9 components, wrap your root element in `FluentProvider` to inherit the platform theme:

```typescript
import { FluentProvider, webLightTheme } from "@fluentui/react-components";

public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
  return React.createElement(
    FluentProvider,
    { theme: webLightTheme },
    React.createElement(MyFluentComponent, {
      value: context.parameters.myProp.raw
    })
  );
}
```

The platform provides theme tokens that automatically match the host app appearance (light/dark mode, accent colors).

### Bundling Rules for Virtual Controls

- Do **not** add `react`, `react-dom`, or `@fluentui/*` to `dependencies` -- use `devDependencies` only
- The platform-library elements in the manifest tell the framework which shared libraries to inject
- Third-party libraries (e.g., `chart.js`, `d3`) are still bundled normally in your component output
- Use `pcf-scripts` (included in scaffolded projects) for Webpack bundling; it auto-externalizes platform libraries
- Keep production builds small: `npm run build -- --buildMode production` enables tree-shaking and minification

---

## Virtual Components (Standard vs React Differences)

| Aspect | Standard (`standard`) | Virtual/React (`virtual`) |
|--------|----------------------|--------------------------|
| `init()` signature | Receives `container: HTMLDivElement` | No container parameter |
| `updateView()` return | `void` (mutate DOM directly) | `React.ReactElement` |
| DOM management | Developer creates/manages all DOM | Platform renders returned ReactElement |
| Framework bundling | Bundle your own UI framework | Platform provides React + Fluent |
| Event handling | Attach to DOM elements manually | React event system (onClick, onChange, etc.) |
| Styling | CSS files, inline styles | Fluent tokens, Griffel, or CSS files |
| Power Pages | Supported | Not supported |

**Key difference:** Virtual controls never receive a container `div`. The platform mounts your returned `ReactElement` into its own managed container. You should never use `document.createElement` or direct DOM manipulation in a virtual control.

---

## Manifest Schema (ControlManifest.Input.xml)

```xml
<?xml version="1.0" encoding="utf-8" ?>
<manifest>
  <control namespace="SampleNamespace"
    constructor="MyControl"
    version="1.0.0"
    display-name-key="MyControl_Display"
    description-key="MyControl_Desc"
    control-type="standard">

    <type-group name="numbers">
      <type>Whole.None</type>
      <type>Currency</type>
      <type>FP</type>
      <type>Decimal</type>
    </type-group>

    <property name="controlValue"
      display-name-key="Value"
      description-key="The bound value"
      of-type-group="numbers"
      usage="bound"
      required="true" />

    <data-set name="dataSet" display-name-key="DataSet" />

    <resources>
      <code path="index.ts" order="1" />
      <css path="css/styles.css" order="1" />
      <platform-library name="React" version="16.14.0" />
      <platform-library name="Fluent" version="9.46.2" />
    </resources>

    <feature-usage>
      <uses-feature name="Device.captureImage" required="true" />
    </feature-usage>

    <external-service-usage enabled="true">
      <domain>www.example.com</domain>
    </external-service-usage>
  </control>
</manifest>
```

**Key manifest elements:**

| Element | Purpose |
|---------|---------|
| `control` | Root: namespace, constructor, version, control-type |
| `property` | Bindable property (`of-type` or `of-type-group`) |
| `type-group` | Groups multiple data types a property can accept |
| `data-set` | Dataset-bound component (grids/views) |
| `resources` | Code, CSS, RESX, and platform-library references |
| `platform-library` | Shares React/Fluent from platform (virtual only) |
| `feature-usage` | Device capabilities (camera, geolocation) |
| `external-service-usage` | Marks component as premium |

### Advanced Manifest Elements

#### Property Types Reference

| `of-type` Value | Description |
|----------------|-------------|
| `Currency` | Monetary values |
| `DateAndTime.DateAndTime` | Date with time |
| `DateAndTime.DateOnly` | Date without time |
| `Decimal` | Decimal number |
| `Enum` | Enumerated values |
| `FP` | Floating point |
| `Multiple` | Multi-line text |
| `SingleLine.Text` | Single-line text |
| `SingleLine.Email` | Email address |
| `SingleLine.Phone` | Phone number |
| `SingleLine.URL` | URL |
| `TwoOptions` | Boolean |
| `Whole.None` | Whole number |
| `Lookup.Simple` | Lookup reference |
| `OptionSet` | Choice column |
| `MultiSelectOptionSet` | Multi-select choice |

#### IMG Resources

Declare image resources for use in the component:

```xml
<resources>
  <code path="index.ts" order="1" />
  <img path="img/icon.png" />
  <img path="img/logo.svg" />
</resources>
```

Access at runtime via `context.resources.getResource("img/icon.png", callback, errCallback)`.

#### RESX for Localization

Add localized string resources:

```xml
<resources>
  <code path="index.ts" order="1" />
  <resx path="strings/MyControl.1033.resx" version="1.0.0" />
  <resx path="strings/MyControl.1036.resx" version="1.0.0" />
</resources>
```

- `1033` = English, `1036` = French, `1043` = Dutch, `1031` = German
- Access strings via `context.resources.getString("key_name")`
- The `display-name-key` and `description-key` attributes on properties reference keys in these RESX files

#### Feature-Usage Reference

| Feature Name | Description |
|-------------|-------------|
| `Device.captureAudio` | Microphone access |
| `Device.captureImage` | Camera access |
| `Device.captureVideo` | Video capture |
| `Device.getBarcodeValue` | Barcode scanner |
| `Device.getCurrentPosition` | GPS location |
| `Device.pickFile` | File picker |
| `Utility.lookupObjects` | Lookup dialog |
| `WebAPI` | Dataverse Web API access (model-driven only) |

#### External-Service-Usage

When a component calls external APIs, declare the domains. This marks the component as **premium** (requires a premium license):

```xml
<external-service-usage enabled="true">
  <domain>api.example.com</domain>
  <domain>cdn.example.com</domain>
</external-service-usage>
```

---

## PCF Tooling Commands

```bash
# Create new field component
pac pcf init --namespace MyNS --name MyControl --template field --run-npm-install

# Create React component
pac pcf init -n ReactSample -ns MyNS -t field -fw react -npm

# Create dataset component
pac pcf init -n GridControl -ns MyNS -t dataset -npm

# Build
npm run build

# Production build
npm run build -- --buildMode production

# Debug with test harness (http://localhost:8181)
npm start watch

# Refresh types after manifest changes
npm run refreshTypes

# Create solution wrapper
mkdir Solutions && cd Solutions
pac solution init --publisher-name MyPub --publisher-prefix mypub
pac solution add-reference --path ../../

# Build solution zip
dotnet build
```

Template options: `field` (single value) or `dataset` (grid/view data).

---

## Context API Deep Reference

The `Context<IInputs>` object is passed to `init()` and `updateView()`. It provides access to all platform services.

### Full Context Interface

| Property | Type | Description |
|----------|------|-------------|
| `parameters` | `IInputs` | All properties declared in the manifest, typed per declaration |
| `mode` | `Mode` | Component state: visibility, disabled state, fullscreen |
| `client` | `Client` | Client info: form factor (web/tablet/phone), client type, is offline |
| `device` | `Device` | Device APIs: camera, geolocation, barcode, file picker |
| `formatting` | `Formatting` | Locale-aware formatting for dates, numbers, currency |
| `userSettings` | `UserSettings` | Current user: language, security roles, user ID, user name |
| `webAPI` | `WebApi` | Dataverse CRUD operations (model-driven only) |
| `navigation` | `Navigation` | Open forms, URLs, alert/confirm dialogs, error dialogs |
| `resources` | `Resources` | Access RESX strings and image resources from manifest |
| `factory` | `Factory` | Popup service for creating modal/modeless popups |
| `updatedProperties` | `string[]` | List of property names that changed since last `updateView()` |

### Mode Interface

```typescript
interface Mode {
  isControlDisabled: boolean;   // True if the host has disabled the control
  isVisible: boolean;           // True if the control is visible
  label: string;                // Label assigned by the form designer
  setControlState(state: Dictionary): boolean; // Persist state for reload
  setFullScreen(value: boolean): void;         // Enter/exit fullscreen
  trackContainerResize(value: boolean): void;  // Receive resize events
  allocatedHeight: number;      // Available height in pixels (-1 if unconstrained)
  allocatedWidth: number;       // Available width in pixels (-1 if unconstrained)
}
```

### Client Interface

```typescript
interface Client {
  getClient(): string;          // "Web" | "Outlook" | "Mobile"
  getFormFactor(): number;      // 0=Unknown, 1=Desktop, 2=Tablet, 3=Phone
  isOffline(): boolean;         // True if app is running offline
  disableScroll: boolean;       // Disable scroll on the parent container
}
```

### WebApi Interface (Model-Driven Only)

```typescript
interface WebApi {
  createRecord(entityType: string, data: object): Promise<EntityReference>;
  deleteRecord(entityType: string, id: string): Promise<EntityReference>;
  updateRecord(entityType: string, id: string, data: object): Promise<EntityReference>;
  retrieveRecord(entityType: string, id: string, options?: string): Promise<Entity>;
  retrieveMultipleRecords(
    entityType: string,
    options?: string,
    maxPageSize?: number
  ): Promise<RetrieveMultipleResponse>;
}
```

### Navigation Interface

```typescript
interface Navigation {
  openForm(options: EntityFormOptions, parameters?: object): Promise<OpenFormSuccessResponse>;
  openUrl(url: string, options?: WindowOptions): void;
  openAlertDialog(alertStrings: AlertStrings, options?: DialogOptions): Promise<void>;
  openConfirmDialog(confirmStrings: ConfirmStrings, options?: DialogOptions): Promise<ConfirmResponse>;
  openErrorDialog(options: ErrorDialogOptions): Promise<void>;
  openWebResource(name: string, options?: WindowOptions, data?: string): void;
}
```

### Formatting Interface

```typescript
interface Formatting {
  formatCurrency(value: number, precision?: number, currencySymbol?: string): string;
  formatDecimal(value: number, precision?: number): string;
  formatInteger(value: number): string;
  formatDateAsFilterStringInUTC(value: Date, includeTime?: boolean): string;
  formatDateLong(value: Date): string;
  formatDateShort(value: Date, includeTime?: boolean): string;
  formatDateYearMonth(value: Date): string;
  formatLanguage(languageCode: number): string;
  formatUserDateTimeToUTC(value: Date): Date;
  formatUTCDateTimeToUserDate(value: Date): Date;
  getWeekOfYear(value: Date): number;
}
```

### UserSettings Interface

```typescript
interface UserSettings {
  dateFormattingInfo: DateFormattingInfo;
  isRTL: boolean;                    // Right-to-left language
  languageId: number;                // LCID (e.g., 1033 for English)
  numberFormattingInfo: NumberFormattingInfo;
  securityRoles: string[];           // GUIDs of user's security roles
  userId: string;                    // Current user GUID
  userName: string;                  // Current user display name
}
```

### Using updatedProperties

Check `updatedProperties` to optimize `updateView()` and avoid unnecessary re-renders:

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void {
  if (context.updatedProperties.includes("myProperty")) {
    // Only refresh when this specific property changed
    this._value = context.parameters.myProperty.raw!;
  }
  if (context.updatedProperties.includes("layout")) {
    // Container was resized
    this.handleResize(context.mode.allocatedWidth, context.mode.allocatedHeight);
  }
}
```

Common `updatedProperties` values: parameter names from manifest, `"layout"` (resize), `"dataset"` (dataset refresh), `"fullscreen_open"`, `"fullscreen_close"`.

---

## Key API Interfaces

| Interface | Description |
|-----------|-------------|
| `Context` | All properties/methods available to the component |
| `WebApi` | CRUD operations on Dataverse data (model-driven only) |
| `Navigation` | openForm, openUrl, openAlertDialog |
| `Device` | Camera, location, microphone |
| `Formatting` | Date, number, currency formatting |
| `Mode` | Component state (fullscreen, isVisible, isControlDisabled) |
| `DataSet` | Grid/view data properties and methods |
| `UserSettings` | Current user info (language, security roles) |
| `Paging` | Dataset pagination |
| `Filtering` | Dataset filter operations |

---

## Dataset Components

### Overview

Dataset components bind to views or subgrids and can display, filter, sort, and page through record collections. Create with `pac pcf init -t dataset`.

### Manifest Declaration

```xml
<control namespace="MyNS" constructor="MyGrid" version="1.0.0"
  display-name-key="MyGrid" description-key="Custom grid"
  control-type="standard">

  <data-set name="dataSetGrid" display-name-key="Records"
    description-key="The dataset of records" />

  <!-- Optional: define additional properties for configuration -->
  <property name="columnsToShow" display-name-key="Columns"
    of-type="SingleLine.Text" usage="input" required="false" />

  <resources>
    <code path="index.ts" order="1" />
    <css path="css/grid.css" order="1" />
  </resources>
</control>
```

### DataSet Interface Methods

| Method / Property | Return | Description |
|-------------------|--------|-------------|
| `columns` | `Column[]` | All columns in the dataset (name, displayName, dataType, order, visibility) |
| `sortedRecordIds` | `string[]` | Record IDs in current sort order |
| `records` | `{ [id: string]: EntityRecord }` | Map of record ID to record data |
| `error` | `boolean` | Whether an error occurred loading data |
| `errorMessage` | `string` | Error description |
| `loading` | `boolean` | Whether data is still loading |
| `paging` | `Paging` | Pagination controls |
| `sorting` | `SortStatus[]` | Current sort status |
| `filtering` | `Filtering` | Filter operations |
| `linking` | `Linking` | Table relationship information (model-driven) |
| `getSelectedRecordIds()` | `string[]` | IDs of records the user has selected |
| `setSelectedRecordIds(ids: string[])` | `void` | Programmatically select records |
| `openDatasetItem(entityRef: EntityReference)` | `void` | Open the record form |
| `refresh()` | `void` | Force a data refresh |
| `getTitle()` | `string` | View display name |
| `getViewId()` | `string` | Current view GUID |

### Paging Interface

```typescript
interface Paging {
  totalResultCount: number;   // Total records matching the query
  hasNextPage: boolean;       // True if next page exists
  hasPreviousPage: boolean;   // True if previous page exists
  pageSize: number;           // Records per page
  loadNextPage(): void;       // Load next page
  loadPreviousPage(): void;   // Load previous page
  setPageSize(pageSize: number): void; // Change page size
  reset(): void;              // Return to first page
  loadExactPage(pageNumber: number): void; // Jump to specific page
}
```

### Sorting

```typescript
interface SortStatus {
  name: string;       // Column logical name
  sortDirection: 0 | 1; // 0 = ascending, 1 = descending
}

// Apply sorting from updateView
const dataset = context.parameters.dataSetGrid;
dataset.sorting = [{ name: "createdon", sortDirection: 1 }];
dataset.refresh();
```

### Filtering

```typescript
interface Filtering {
  getFilter(): FilterExpression;
  setFilter(expression: FilterExpression): void;
  clearFilter(): void;
}

interface FilterExpression {
  conditions: ConditionExpression[];
  filterOperator: 0 | 1;  // 0 = And, 1 = Or
  filters?: FilterExpression[]; // Nested filter groups
}

interface ConditionExpression {
  attributeName: string;
  conditionOperator: number; // See ConditionOperator enum
  value: any;
  entityAliasName?: string;
}
```

**ConditionOperator values (commonly used):**

| Value | Operator | Description |
|-------|----------|-------------|
| 0 | Equal | Equals the value |
| 1 | NotEqual | Not equal |
| 2 | GreaterThan | Greater than |
| 4 | LessThan | Less than |
| 6 | Like | Pattern match (use % wildcard) |
| 8 | In | In a list of values |
| 12 | Null | Is null |
| 13 | NotNull | Is not null |
| 25 | On | On a specific date |
| 33 | Contains | Contains substring |
| 49 | BeginsWith | Starts with |
| 51 | EndsWith | Ends with |

### Dataset Component Example (Standard)

```typescript
export class SimpleGrid implements ComponentFramework.StandardControl<IInputs, IOutputs> {
  private _container: HTMLDivElement;
  private _context: ComponentFramework.Context<IInputs>;

  public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
  ): void {
    this._context = context;
    this._container = container;
    // Enable resize tracking for responsive layout
    context.mode.trackContainerResize(true);
  }

  public updateView(context: ComponentFramework.Context<IInputs>): void {
    this._context = context;
    const dataset = context.parameters.dataSetGrid;

    if (dataset.loading) return;

    // Clear previous render
    this._container.innerHTML = "";

    // Build table header from columns
    const table = document.createElement("table");
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");

    const visibleColumns = dataset.columns
      .filter(col => !col.isHidden)
      .sort((a, b) => a.order - b.order);

    visibleColumns.forEach(col => {
      const th = document.createElement("th");
      th.textContent = col.displayName;
      th.addEventListener("click", () => {
        // Toggle sort on column click
        const currentSort = dataset.sorting.find(s => s.name === col.name);
        dataset.sorting = [{
          name: col.name,
          sortDirection: currentSort?.sortDirection === 0 ? 1 : 0
        }];
        dataset.refresh();
      });
      headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Build rows from records
    const tbody = document.createElement("tbody");
    dataset.sortedRecordIds.forEach(recordId => {
      const record = dataset.records[recordId];
      const row = document.createElement("tr");

      visibleColumns.forEach(col => {
        const td = document.createElement("td");
        td.textContent = record.getFormattedValue(col.name) ?? "";
        row.appendChild(td);
      });

      row.addEventListener("click", () => {
        dataset.openDatasetItem(record.getNamedReference());
      });

      tbody.appendChild(row);
    });
    table.appendChild(tbody);
    this._container.appendChild(table);

    // Paging controls
    if (dataset.paging.hasNextPage || dataset.paging.hasPreviousPage) {
      const pagingDiv = document.createElement("div");
      if (dataset.paging.hasPreviousPage) {
        const prevBtn = document.createElement("button");
        prevBtn.textContent = "Previous";
        prevBtn.addEventListener("click", () => dataset.paging.loadPreviousPage());
        pagingDiv.appendChild(prevBtn);
      }
      if (dataset.paging.hasNextPage) {
        const nextBtn = document.createElement("button");
        nextBtn.textContent = "Next";
        nextBtn.addEventListener("click", () => dataset.paging.loadNextPage());
        pagingDiv.appendChild(nextBtn);
      }
      this._container.appendChild(pagingDiv);
    }
  }

  public getOutputs(): IOutputs { return {}; }
  public destroy(): void { this._container.innerHTML = ""; }
}
```

### EntityRecord Methods

| Method | Return | Description |
|--------|--------|-------------|
| `getFormattedValue(columnName)` | `string` | Formatted display value (respects user locale) |
| `getValue(columnName)` | `any` | Raw value |
| `getRecordId()` | `string` | Record GUID |
| `getNamedReference()` | `EntityReference` | Entity reference for navigation |

---

## Debugging PCF Components

### Test Harness (localhost:8181)

Run `npm start watch` to launch the local test harness at `http://localhost:8181`. The harness provides:

- **Property input panel** on the right side to set property values
- **Container resizing** to test responsive layouts
- **Mock data** for dataset components (set via the Data Inputs section)
- **Hot reload** -- changes to `.ts` and `.css` files trigger automatic rebuild and browser refresh

**Watch mode behavior:**
- Watches for changes in source files and the manifest
- Rebuilds automatically on save
- Opens browser on first start; subsequent rebuilds just refresh

### Common Test Harness Limitations

- `context.webAPI` methods are **not available** in the harness (returns empty results)
- `context.navigation` methods are limited (no form navigation)
- Dataset components show a mock data editor to define test records
- `context.userSettings` returns default values

### Browser Developer Tools

1. Open DevTools (F12) while the test harness is running
2. Source maps are enabled by default -- set breakpoints in your `.ts` files
3. Use the Console to inspect `ComponentFramework` objects
4. Network tab to debug external API calls

### Debugging in Model-Driven Apps (Fiddler Approach)

To debug a deployed component in a live environment:

1. Open Fiddler and enable HTTPS decryption
2. Create an AutoResponder rule that maps the component's bundle URL to your local file:
   - Match: `regex:(?insx).*controls.*MyNamespace\.MyControl.*bundle\.js`
   - Respond: Path to your local `out/controls/MyControl/bundle.js`
3. Clear browser cache and reload the form
4. Set breakpoints in browser DevTools using the local source

### Common Build Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `TS2304: Cannot find name` | Missing type definitions | Run `npm run refreshTypes` after manifest changes |
| `Module not found` | Missing dependency | Run `npm install` |
| `Property 'X' does not exist on type 'IInputs'` | Property not declared in manifest | Add property to `ControlManifest.Input.xml`, then `refreshTypes` |
| `Bundle size too large` | Third-party libraries too big | Use tree-shaking, lazy loading, or lighter alternatives |
| `getOutputs() return mismatch` | Output interface mismatch | Ensure returned keys match manifest `property` names with `usage="bound"` |

### Debug Tips

- Use `console.log(JSON.stringify(context.parameters, null, 2))` to inspect all parameter values
- Check `context.updatedProperties` array to see what triggered `updateView()`
- For dataset components, log `dataset.sortedRecordIds.length` and `dataset.paging.totalResultCount` to verify data loading
- Enable verbose logging: `npm start watch -- --verbose`

---

## Canvas App Components

### Key Differences from Model-Driven

| Aspect | Model-Driven | Canvas |
|--------|-------------|--------|
| React version | 17.0.2 | 16.14.0 |
| `context.webAPI` | Available | Not available |
| `context.navigation` | Full support | Limited (no openForm) |
| Dataset support | Full | Supported (tables, collections, connectors) |
| Property binding | Bound to Dataverse columns | Bound to any data source or static |
| Sizing | Controlled by form layout | Controlled by app maker (Width/Height properties) |
| Component library | Added via Import Component | Added via Import > Code |
| `Utility.lookupObjects` | Available | Not available |

### Manifest Requirements for Canvas

Canvas apps require all properties to be fully described with `display-name-key` and `description-key` since app makers configure them in the properties panel.

For canvas compatibility, use `usage="input"` (not `bound`) for properties that should accept both static values and data-bound expressions:

```xml
<property name="backgroundColor"
  display-name-key="Background Color"
  description-key="Sets the background color"
  of-type="SingleLine.Text"
  usage="input"
  required="false"
  default-value="#FFFFFF" />
```

**Canvas-specific property types:**

| of-type | Canvas behavior |
|---------|----------------|
| `SingleLine.Text` | Text input or expression |
| `Whole.None` | Numeric input |
| `TwoOptions` | Toggle switch |
| `Enum` | Dropdown (define values in manifest) |
| `Multiple` | Multiline text input |
| `DataSet` | Bind to collection, table, or connector |

### Adding PCF to Canvas Apps

1. Navigate to **Settings > Upcoming Features > Experimental** and enable **Allow publishing of canvas apps with code components** (or check admin-level setting)
2. In canvas app editor: **Insert > Get more components > Code** tab
3. Select your imported component
4. Configure properties in the right panel
5. Bind data sources or static values to component properties

### Canvas Dataset Binding

In canvas apps, dataset components can bind to:
- **Collections** (`ClearCollect(myData, ...)`)
- **Dataverse tables** directly
- **Connector results** (SharePoint lists, SQL tables, etc.)

The dataset property appears as a regular data source binding in the canvas app maker experience.

---

## Common Patterns

### Editable Grid

A dataset component that allows inline editing of records:

```typescript
// In updateView: create editable cells
const input = document.createElement("input");
input.value = record.getFormattedValue(col.name) ?? "";
input.addEventListener("change", (e) => {
  const target = e.target as HTMLInputElement;
  // Use webAPI to update the record
  this._context.webAPI.updateRecord(
    entityName,
    record.getRecordId(),
    { [col.name]: target.value }
  ).then(() => {
    dataset.refresh(); // Reload to reflect server-side changes
  });
});
```

Key considerations:
- Call `notifyOutputChanged()` after edits if exposing selected values
- Handle concurrent edit conflicts with optimistic concurrency
- Disable editing when `context.mode.isControlDisabled` is true

### File Upload Component

```typescript
// Use Device.pickFile to select files
public init(context: ComponentFramework.Context<IInputs>,
  notifyOutputChanged: () => void, state: Dictionary, container: HTMLDivElement): void {

  const uploadBtn = document.createElement("button");
  uploadBtn.textContent = "Upload File";
  uploadBtn.addEventListener("click", async () => {
    try {
      const files = await context.device.pickFile({
        accept: "image/*",      // MIME type filter
        allowMultipleFiles: false,
        maximumAllowedFileSize: 10485760 // 10 MB
      });
      if (files && files.length > 0) {
        const file = files[0];
        // file.fileName, file.fileSize, file.mimeType, file.fileContent (base64)
        this._selectedFile = file;
        notifyOutputChanged();
      }
    } catch (err) {
      console.error("File pick cancelled or failed", err);
    }
  });
  container.appendChild(uploadBtn);
}
```

Declare in manifest:
```xml
<feature-usage>
  <uses-feature name="Device.pickFile" required="true" />
</feature-usage>
```

### Map / Chart Component

For map or chart components, integrate third-party libraries:

```typescript
// Example: Chart.js integration in a standard control
import Chart from "chart.js/auto";

public updateView(context: ComponentFramework.Context<IInputs>): void {
  const dataset = context.parameters.dataSetGrid;
  if (dataset.loading) return;

  // Extract data from dataset records
  const labels: string[] = [];
  const values: number[] = [];
  dataset.sortedRecordIds.forEach(id => {
    const record = dataset.records[id];
    labels.push(record.getFormattedValue("name") ?? "");
    values.push(Number(record.getValue("revenue")) || 0);
  });

  // Create or update chart
  if (!this._chart) {
    const canvas = document.createElement("canvas");
    this._container.appendChild(canvas);
    this._chart = new Chart(canvas, {
      type: "bar",
      data: { labels, datasets: [{ label: "Revenue", data: values }] }
    });
  } else {
    this._chart.data.labels = labels;
    this._chart.data.datasets[0].data = values;
    this._chart.update();
  }
}
```

**Note:** Third-party libraries like Chart.js, D3, Leaflet are bundled into your component (not shared via platform-library). Keep bundle size in check.

### Lookup Control Pattern

A field component that provides a custom lookup experience:

```typescript
// Trigger the platform lookup dialog
private async openLookup(): Promise<void> {
  try {
    const results = await this._context.utils.lookupObjects({
      entityTypes: ["contact"],
      defaultEntityType: "contact",
      allowMultiSelect: false,
      defaultViewId: "00000000-0000-0000-0000-000000000000",
      viewIds: [],
      filters: [{
        entityLogicalName: "contact",
        filterXml: "<filter><condition attribute='statecode' operator='eq' value='0' /></filter>"
      }]
    });
    if (results && results.length > 0) {
      this._selectedId = results[0].id;
      this._selectedName = results[0].name;
      this._notifyOutputChanged();
    }
  } catch {
    // User cancelled the lookup dialog
  }
}
```

Declare in manifest:
```xml
<feature-usage>
  <uses-feature name="Utility.lookupObjects" required="true" />
</feature-usage>
```

**Note:** `lookupObjects` is only available in model-driven apps, not canvas apps.

---

## Adding Components to Apps

**Field-level:** Form Editor > double-click field > Controls tab > Add Control > configure for Web/Phone/Tablet.

**Entity-level (dataset):** Settings > Customizations > Entity > Controls tab > Add Control > select dataset component.

Always bump `version` in manifest when updating. Publish customizations after import.

---

## Quick Reference: Solution Packaging

```bash
# Full workflow: build component, package solution, deploy
npm run build -- --buildMode production
cd Solutions
dotnet build --configuration Release

# Deploy to environment
pac auth create --url https://myorg.crm.dynamics.com
pac solution import --path bin/Release/Solutions.zip --publish-all

# For iterative development (push without solution)
pac pcf push --publisher-prefix mypub
```

**`pac pcf push`** is a shortcut for development -- it creates a temporary unmanaged solution, imports the component, and publishes it. Not recommended for production deployments.
