# Model-Driven Apps Research
## Sources: 26 of 28 successfully fetched

---

## 1. Build First Model-Driven App
Step-by-step tutorial: sign in to Power Apps → create environment → create solution → add Account table → create model-driven app → add pages → save/publish → run on desktop/mobile. Copilot can generate app descriptions in managed environments.

## 2. App Designer Overview
Modern WYSIWYG authoring with real-time preview.
- **Command bar**: Back, Add page, Settings, Edit form, Comments, Save, Publish, Play
- **App preview**: Shows real-time layout
- **Panes**: Pages (Navigation/All other pages), Data, Automation
- **Property pane**: Context-sensitive configuration
- **Navigation options**: Show Home, Show Recent, Show Pinned, Enable collapsible groups, Enable Areas

## 3. Model-Driven App Components
Four categories:
- **Data**: Tables, Relationships (1:N, N:1, N:N), Columns, Choice columns
- **UI**: App, Site map, Form, View, Custom page
- **Logic**: Business process flows, Workflows, Actions, Business rules, Power Automate flows
- **Visualization**: Charts, Dashboards, Embedded Power BI

## 4. Main Forms
Composed of tabs → sections → columns. Create via Tables > Forms > New form > Main form. Can clone forms. Edit columns, sections, tabs, subgrids, headers, footers, properties. Save and publish.

## 5. Quick Create Forms
Streamlined data entry with full business rule support. Always have one section with three columns. Cannot add: subgrids, quick view forms, web resources, iFrames, notes, Bing Maps. Only one quick create form can be used by everyone (set via form order). Default tables: account, campaign response, case, competitor, contact, lead, opportunity.

## 6. Quick View Forms
Read-only forms for viewing related table data. Associated with lookup columns. Cannot be edited by users. Do not support form scripts or custom controls. Create via Tables > Forms > Add form > Quick View Form. Properties: Name, Label, Display label, Lookup Column, Related table, Quick View Form.

## 7. Views
Three types:
- **Personal**: User-owned, not shared
- **System**: Quick Find, Advanced Find, Associated, Lookup — cannot be shown in view selector
- **Public**: General purpose, can be created/deleted

Grid controls: Power Apps grid control, Power Apps read-only grid, Editable grid, Read-only grid (deprecated).

## 8. System Charts
Organization-owned, available to all users with data access. Configure: chart name, Legend Entries (Series), Horizontal (Category) Axis, description. Max 50,000 records displayed. Charts can be added to dashboards.

## 9. Dashboards
Two types:
- **Standard**: Unrelated components, layouts: 2-column, 3-column, 3-column varied width, 4-column, Power BI embedded
- **Interactive**: Act on records directly

Up to 6 components per dashboard. Components: charts and lists.

## 10. Business Logic
Two major categories:
- **Business rules**: Simple interface, scope: Table/All Forms/Specific form
- **Business process flows**: Step-by-step guides
- Also: Power Automate flows (automated, button, scheduled), classic workflows, actions

## 11. Business Rules
Actions possible: Set/clear column values, set requirement levels, show/hide columns, enable/disable columns, validate data with error messages, create recommendations. Build conditions (AND/OR clauses). Scope options: Entity (all forms + server), All Forms, Specific form. Must deactivate before modifying. Unsupported: multi-select choices, composite columns, unique identifier columns, rollup columns.

## 12. Form Designer Overview
WYSIWYG with real-time preview. Areas: Command bar (Save, Publish, Undo, Redo), Form preview, Panes (Columns, Components, Tree view, Form libraries), Property pane, Preview size switcher, Show hidden toggle, Zoom slider.

## 13. Tab Properties
- **Display**: Name, Label, Show label, Expand by default, Visible by default, Availability for phone
- **Formatting**: Layout up to 3 columns with percentage widths
- **Events**: Form Libraries, TabStateChange event handlers

## 14. Section Properties
- **Display**: Name, Label, Show label, Show line at top, Column Label Width 50-250, Visibility, Availability, Lock section
- **Formatting**: Layout up to 4 columns, Column Label Alignment (left/right/center), Column Label Position (side/top)
- **Reference panel**: Single-column section with sub-grids, quick view controls, Knowledge Base Search as vertical tabs

## 15. Subgrid Properties
- **Display**: Name, Label, Display label, Records (Only Related/All Record Types), Table, Default View, Display Search Box, Display Index, View Selector (Off/Show All/Show Selected), Default Chart, Show Chart Only, Display Chart Selection, Availability
- **Formatting**: Layout columns, Number of rows, Use available space
- Behaviors: Show list, Add record, Delete record differ based on relationship type (1:N vs N:N)

## 16. Embedded Canvas Apps
Two methods: modern Unified Interface and classic experience.
- **Modern**: Components > Display > Canvas app. Properties: Entity name, App name, App ID
- **Classic**: Uses ModelDrivenFormIntegration control for data context
- Canvas app has full access via `ModelDrivenFormIntegration.Item`
- Only one canvas app per form
- **Custom pages recommended over embedded canvas apps**

## 17. Command Designer (Modern Commanding)
Commands = buttons users interact with. Command bar locations: Main grid, Main form, Subgrid view, Associated view, Quick actions.
- **Command types**: Command, Dropdown, Group, Split button
- **Modern vs Classic**: Modern supports Power Fx, uses command designer, app-specific commands, standard ALM
- Power Fx replaces many classic visibility rules (CustomRule, EntityPrivilegeRule, RecordPrivilegeRule, FormStateRule, SelectionCountRule)

## 18. Create/Manage Apps Using Code
Programmatic approach via Web API:
- Create AppModule entity
- AddAppComponents/RemoveAppComponents actions
- ValidateApp function
- PublishXml action
- Associate security roles via appmoduleroles_association
- Client APIs: `getCurrentAppName`, `getCurrentAppProperties`, `getCurrentAppUrl`

## 19. Custom Pages
Canvas-based pages within model-driven apps. Uses: full pages, dialogs (center/side), app side panes.
- GA features: runtime, solution/ALM, connectors, modern controls, code components, monitor support
- Licensing: follows model-driven app license, doesn't count toward app limits
- **Max 25 custom pages per app**
- Different from embedded canvas apps: tighter integration, better performance, separate solution element

## 20. Productive Form Design
Main form layout: Application header → Site map → Command bar → Form header (table name, record, 4 read-only fields, tabs) → Form body.
Key patterns:
- **Main form dialogs**: Full related record access with BPF
- **Form component controls**: Inline editing without navigation
- **Quick create forms**: Rapid record creation
- **Quick view forms**: Read-only related data
- **Reference panels**: Multi-related record access
Best practices: required fields always visible/editable, use high-density headers with flyout

## 21. Performant Form Design
- Default tab always rendered, controls initialized
- Secondary tabs defer initialization until opened
- Data-driven controls (quick view, subgrid, timeline, assistant) are most expensive
- **JavaScript best practices**: Use async network requests, return Promises from OnLoad/OnSave, cache data in sessionStorage, stale-while-revalidate pattern, load code only when needed, avoid console.log in production, prevent memory leaks, clean up event listeners/timers
- Tools: Performance insights, Solution checker, Object checker

## 22. Sharing Model-Driven Apps
Role-based security. Steps: identify security roles → assign roles/people to app → share link. Prerequisites: Power Platform admin exists, sharer has admin privileges, users exist in environment, correct license assigned. Can use Microsoft Entra groups for access management.

## 23. Distributing Model-Driven Apps
Via solutions. Steps: add app to solution → export solution (managed or unmanaged .zip) → import in target environment.
- **Managed**: For non-dev environments
- **Unmanaged**: Source for dev
- Solution checker runs on export by default

## 24. Reporting Overview
- **Simple**: Table views, Charts
- **Advanced**: SSRS reports (pixel-perfect, PDF/CSV/Excel export), Power BI (embedded reports, system/user dashboards), Excel integration (PowerView, PowerPivot, PowerQuery)

## 25. Form Navigation for Related Entities
Classic form designer > Navigation > Relationship Explorer. Filter by Available Relationships, 1:N, N:N. Drag related table to Navigation Pane.

## 26. Specify Default Views
Any public view can be set as default via Solutions > table > Views > More commands > Set as default view. Users can pin a different personal default.

## 27. Pass Current Record to Embedded Canvas App
Use ModelDrivenFormIntegration control. Data available via `ModelDrivenFormIntegration.Data` (list of records). Use `First()` for single record. Access columns via `ModelDrivenFormIntegration.Item.columnname`. App refreshes when record changes on host form.

## 28. Add/Move/Configure/Delete Components on Form
Add via Components pane (drag-and-drop or column-specific). Configure via property pane. Move via drag-and-drop or cut-and-paste. Delete via command bar Delete button. Show component on: Web, Mobile, Tablet.

---

## Key Patterns
- Model-driven apps follow component-based architecture: data → UI → logic → visualization
- Forms hierarchy: Form > Tabs > Sections > Columns
- Three form types: Main (full editing), Quick Create (streamlined entry), Quick View (read-only related)
- Business rules provide no-code form logic; Power Automate handles complex automation
- Custom pages = convergence of canvas + model-driven, recommended over embedded canvas
- Modern commanding replaces classic ribbon customization with Power Fx
- Performance: default tab management, deferred loading, async JS, sessionStorage caching
- Distribution via solution-based ALM (managed/unmanaged exports)
- Security is role-based; sharing requires proper security role assignment
