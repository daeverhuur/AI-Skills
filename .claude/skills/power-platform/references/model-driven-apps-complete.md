# Model-Driven Apps - Complete Reference

## Architecture

Component-based: Data (tables, relationships, columns) > UI (app, sitemap, forms, views, custom pages) > Logic (business rules, BPFs, flows) > Visualization (charts, dashboards, Power BI).

## App Designer

Modern WYSIWYG with real-time preview.
- **Command bar**: Back, Add page, Settings, Edit form, Comments, Save, Publish, Play
- **Panes**: Pages (Navigation / All other pages), Data, Automation
- **Navigation options**: Show Home, Show Recent, Show Pinned, Enable collapsible groups, Enable Areas
- Property pane is context-sensitive to selected element

## Creating an App

1. Sign in to Power Apps > create/select environment > create solution
2. Add tables to solution
3. New > App > Model-driven app
4. Add pages (table-based, custom, dashboard, etc.)
5. Configure sitemap navigation and areas
6. Save > Publish > Play to test

Copilot can generate app descriptions in managed environments.

---

## Forms

### Form Hierarchy

Form > Tabs > Sections > Columns (fields, subgrids, components)

### Main Forms

Primary editing surface for records. Composed of tabs containing sections containing columns.
- Create: Tables > Forms > New form > Main form
- Can clone existing forms
- Editable areas: columns, sections, tabs, subgrids, header (up to 4 read-only fields), footer
- Form layout: Application header > Site map > Command bar > Form header > Form body

### Quick Create Forms

Streamlined data entry in a flyout panel.
- Always one section with three columns
- Full business rule support
- Only one quick create form active per table (set via form order)
- **Cannot include**: subgrids, quick view forms, web resources, iFrames, notes, Bing Maps
- Default tables with quick create: Account, Campaign Response, Case, Competitor, Contact, Lead, Opportunity

### Quick View Forms

Read-only display of related record data, tied to a lookup column.
- Cannot be edited by users at runtime
- Do not support form scripts or custom controls
- Create: Tables > Forms > Add form > Quick View Form
- Configure: Name, Label, Display label, Lookup Column, Related table, Quick View Form selection

---

## Form Designer

WYSIWYG editor with real-time preview.
- **Command bar**: Save, Publish, Undo, Redo
- **Left panes**: Columns, Components, Tree view, Form libraries
- **Right pane**: Property pane (context-sensitive)
- **Footer tools**: Preview size switcher, Show hidden toggle, Zoom slider

### Tab Properties

| Category | Properties |
|----------|-----------|
| Display | Name, Label, Show label, Expand by default, Visible by default, Availability for phone |
| Formatting | Layout 1-3 columns, percentage-based widths |
| Events | Form Libraries, TabStateChange event handlers |

### Section Properties

| Category | Properties |
|----------|-----------|
| Display | Name, Label, Show label, Show line at top, Column Label Width (50-250), Visibility, Availability, Lock section |
| Formatting | Layout 1-4 columns, Column Label Alignment (left/right/center), Column Label Position (side/top) |

**Reference panel**: Special single-column section containing sub-grids, quick view controls, and Knowledge Base Search rendered as vertical tabs.

### Subgrid Properties

| Category | Properties |
|----------|-----------|
| Display | Name, Label, Records (Only Related / All Record Types), Table, Default View, Search Box, Index, View Selector (Off/All/Selected), Default Chart, Chart Only, Chart Selection, Availability |
| Formatting | Column count, Number of rows, Use available space |

Subgrid behavior differs by relationship type:
- **1:N**: Show list, Add record, Delete record available
- **N:N**: Associate/disassociate behavior

### Adding/Moving/Deleting Components

- Add: Components pane via drag-and-drop or column-specific insertion
- Move: Drag-and-drop or cut-and-paste
- Delete: Command bar Delete button
- Visibility per device: Web, Mobile, Tablet

---

## Form Design Best Practices

### Productive Design Patterns

1. **Main form dialogs**: Open related records with full editing + BPF access without leaving context
2. **Form component controls**: Inline editing of related data without page navigation
3. **Quick create forms**: Rapid record creation from any context
4. **Quick view forms**: Display read-only related data inline
5. **Reference panels**: Access multiple related records in vertical tab layout
6. **Required fields**: Always keep visible and editable
7. **High-density headers**: Use flyout for additional header fields

### Performance Optimization

**Tab loading behavior**:
- Default (first) tab: Always rendered, all controls initialized immediately
- Secondary tabs: Deferred initialization until user clicks the tab
- Strategy: Put expensive controls on secondary tabs

**Expensive controls** (most costly first):
- Quick view forms
- Subgrids
- Timeline
- Assistant/Copilot controls

**JavaScript best practices**:
- Use async/await for all network requests
- Return Promises from OnLoad and OnSave handlers
- Cache data in `sessionStorage` to avoid repeated fetches
- Use stale-while-revalidate pattern for cached data
- Load scripts only when needed (lazy loading)
- Remove `console.log` in production code
- Prevent memory leaks: clean up event listeners and timers
- Avoid synchronous XMLHttpRequest calls

**Performance tools**:
- Performance insights (built-in analytics)
- Solution checker (static analysis)
- Object checker (component validation)

---

## Views

### View Types

| Type | Ownership | Shareable | Notes |
|------|-----------|-----------|-------|
| Personal | User | No | User-created, private |
| System | Organization | N/A | Quick Find, Advanced Find, Associated, Lookup - cannot appear in view selector |
| Public | Organization | Yes | General purpose, fully customizable |

### Grid Controls

- **Power Apps grid control**: Modern, full-featured (recommended)
- **Power Apps read-only grid**: Modern, read-only
- **Editable grid**: Inline editing support
- **Read-only grid**: Deprecated

### Default Views

Set via Solutions > table > Views > More commands > Set as default view. Users can pin a different personal default that overrides the system default.

---

## Charts

Organization-owned system charts available to all users with data access.
- Configure: Chart name, Legend Entries (Series), Horizontal (Category) Axis, Description
- Maximum 50,000 records displayed
- Can be added to dashboards

---

## Dashboards

### Standard Dashboards

- Components are independent (unrelated data)
- Layouts: 2-column, 3-column, 3-column varied width, 4-column, Power BI embedded
- Up to 6 components per dashboard
- Component types: Charts, Lists

### Interactive Dashboards

- Allow acting on records directly from the dashboard
- Contextual filtering across components

---

## Business Rules

No-code logic applied to forms and tables.

### Available Actions

- Set / clear column values
- Set requirement levels (required/optional/recommended)
- Show / hide columns
- Enable / disable columns
- Validate data with error messages
- Create recommendations (AI Builder)

### Scope Options

| Scope | Runs on | Server-side |
|-------|---------|-------------|
| Entity (table) | All forms + server | Yes |
| All Forms | All forms | No |
| Specific Form | One form only | No |

### Rules

- Build conditions with AND/OR clauses
- Must deactivate before modifying
- **Unsupported columns**: Multi-select choices, composite columns, unique identifiers, rollup columns

---

## Modern Commanding

Replaces classic ribbon customization. Uses Power Fx for logic.

### Command Bar Locations

- Main grid
- Main form
- Subgrid view
- Associated view
- Quick actions

### Command Types

- Command (single button)
- Dropdown
- Group
- Split button

### Power Fx Advantages

Replaces classic visibility rules:
- `CustomRule` > Power Fx expressions
- `EntityPrivilegeRule` > Power Fx privilege checks
- `RecordPrivilegeRule` > Power Fx record checks
- `FormStateRule` > Power Fx form state
- `SelectionCountRule` > Power Fx selection count

Commands are app-specific and follow standard ALM (solutions).

---

## Custom Pages

Canvas-based pages running inside model-driven apps. Recommended over embedded canvas apps.

### Use Cases

- Full pages within the app
- Center dialogs
- Side dialogs
- App side panes

### Key Facts

- Maximum **25 custom pages per app**
- Licensed under model-driven app license (no extra cost)
- Does not count toward canvas app limits
- Supports: connectors, modern controls, code components, Monitor debugging
- Tighter integration, better performance than embedded canvas apps
- Each custom page is a separate solution component

### Embedded Canvas Apps (Legacy)

- Use `ModelDrivenFormIntegration.Item` for host record data
- Access columns: `ModelDrivenFormIntegration.Item.columnname`
- Only one canvas app per form
- Custom pages are the recommended replacement

---

## Programmatic App Management

Web API operations for managing apps in code:
- Create: `AppModule` entity
- Modify: `AddAppComponents` / `RemoveAppComponents` actions
- Validate: `ValidateApp` function
- Publish: `PublishXml` action
- Security: Associate roles via `appmoduleroles_association`
- Client APIs: `getCurrentAppName()`, `getCurrentAppProperties()`, `getCurrentAppUrl()`

---

## Security and Sharing

Role-based access control.

**Prerequisites for sharing**:
1. Power Platform admin exists in environment
2. Sharer has admin privileges on the app
3. Target users exist in the environment
4. Users have correct license assigned

**Steps**: Identify security roles > Assign roles/people to app > Share link.

Use Microsoft Entra (Azure AD) groups for bulk access management.

---

## Distribution (ALM)

Apps are distributed via solutions.

1. Add app to a solution
2. Export solution as `.zip`
3. Import in target environment

| Solution Type | Use Case |
|---------------|----------|
| Managed | Production / non-dev environments (locked) |
| Unmanaged | Development (editable source) |

Solution checker runs automatically on export.

---

## Reporting Options

| Complexity | Tools |
|-----------|-------|
| Simple | Table views, System charts |
| Advanced | SSRS reports (pixel-perfect, PDF/CSV/Excel export) |
| Analytics | Power BI (embedded reports, system/user dashboards) |
| Ad-hoc | Excel integration (PowerView, PowerPivot, PowerQuery) |

---

## Form Navigation for Related Entities

Configure in classic form designer: Navigation > Relationship Explorer.
- Filter by: Available Relationships, 1:N, N:N
- Drag related table to Navigation Pane to expose it on the form
