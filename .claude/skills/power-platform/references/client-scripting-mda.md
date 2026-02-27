# Client Scripting in Model-Driven Apps Reference

> Distilled from Microsoft Learn Client API documentation

---

## Form Events

All events in model-driven apps, organized by category.

### Form-Level Events

| Event | Trigger | Handler Signature |
|-------|---------|-------------------|
| `OnLoad` | Form loads or data refreshes | `function(executionContext) {}` |
| `OnSave` | Form saves (before server call) | `function(executionContext) {}` |
| `Loaded` | Form data finishes loading | `function(executionContext) {}` |

### Column Events

| Event | Trigger | Handler Signature |
|-------|---------|-------------------|
| `OnChange` | Field value changes | `function(executionContext) {}` |

### Control Events

| Event | Trigger | Applies To |
|-------|---------|------------|
| `OnOutputChange` | Control output changes | PCF controls |
| `OnReadyStateComplete` | IFRAME finishes loading | IFRAME controls |
| `OnLookupTagClick` | Lookup tag clicked | Lookup controls |
| `PreSearch` | Before lookup search executes | Lookup controls |
| `OnResultOpened` | KB search result opened | KB search control |
| `OnSelection` | KB search result selected | KB search control |
| `PostSearch` | KB search completes | KB search control |

### Tab Events

| Event | Trigger | Handler Signature |
|-------|---------|-------------------|
| `TabStateChange` | Tab expand/collapse | `function(executionContext) {}` |

### Grid/Subgrid Events

| Event | Trigger | Grid Type |
|-------|---------|-----------|
| `OnLoad` | Subgrid refreshes (including sort) | Read-only grid |
| `OnChange` | Cell value changes and loses focus | Editable grid |
| `OnRecordSelect` | Single row selected | Editable grid |
| `OnSave` | Before sending updated data to server | Editable grid |

### Process (BPF) Events

| Event | Trigger |
|-------|---------|
| `OnProcessStatusChange` | BPF status changes |
| `OnPreProcessStatusChange` | Before BPF status changes (can cancel) |
| `OnStageChange` | Active stage changes |
| `OnPreStageChange` | Before active stage changes (can cancel) |
| `OnStageSelected` | Stage selected in BPF control |

### Registering Event Handlers

Attach JavaScript via **Script web resource** (type 3, `.js` file). Register handlers through form properties in the maker portal, or programmatically:

```javascript
// Register OnLoad handler
function onFormLoad(executionContext) {
    var formContext = executionContext.getFormContext();
    // Register OnChange for a specific column
    var nameAttr = formContext.getAttribute("name");
    nameAttr.addOnChange(onNameChange);

    // Register OnSave
    formContext.data.entity.addOnSave(onFormSave);

    // Register form data OnLoad (fires on data refresh)
    formContext.data.addOnLoad(onDataRefresh);
}

function onNameChange(executionContext) {
    var attr = executionContext.getEventSource();
    console.log("Name changed to: " + attr.getValue());
}

function onFormSave(executionContext) {
    var saveEvent = executionContext.getEventArgs();
    var saveMode = saveEvent.getSaveMode();
    // saveMode 1 = Save, 2 = SaveAndClose, 59 = SaveAndNew
    if (someCondition) {
        saveEvent.preventDefault(); // cancel the save
    }
}
```

### Save Modes Reference

| Value | Description |
|-------|-------------|
| 1 | Save |
| 2 | Save and Close |
| 5 | Deactivate |
| 6 | Reactivate |
| 7 | Send (email) |
| 15 | Disqualify (lead) |
| 16 | Qualify (lead) |
| 47 | Assign |
| 58 | Save as Completed (activity) |
| 59 | Save and New |
| 70 | Auto Save |

---

## Client API Object Model

### Execution Context

The `executionContext` is passed to event handlers and provides access to the form/grid context.

| Method | Returns | Description |
|--------|---------|-------------|
| `getFormContext()` | formContext | The form context object |
| `getEventSource()` | Object | The object that raised the event |
| `getEventArgs()` | Object | Event arguments (e.g., save event args) |
| `getDepth()` | Number | Depth of the handler in the call chain |
| `getSharedVariable(key)` | Object | Gets a shared variable value |
| `setSharedVariable(key, value)` | void | Sets a shared variable |

### Xrm Namespace

```
Xrm
 +-- App                    // App-level APIs (addGlobalNotification, clearGlobalNotification)
 +-- Copilot                // Copilot APIs
 +-- Device                 // Camera, barcode, geolocation, pickFile
 +-- Encoding               // xmlAttributeEncode, xmlEncode, htmlEncode, htmlDecode
 +-- Navigation             // navigateTo, openForm, openAlertDialog, openConfirmDialog,
 |                          // openErrorDialog, openFile, openUrl, openWebResource
 +-- Panel                  // loadPanel (side panel control)
 +-- Utility                // getGlobalContext, getEntityMetadata, lookupObjects,
 |                          // getResourceString, closeProgressIndicator, showProgressIndicator
 +-- WebApi                 // createRecord, retrieveRecord, retrieveMultipleRecords,
                            // updateRecord, deleteRecord, execute, executeMultiple
                            // Sub-namespaces: .online, .offline
```

### formContext

```
formContext
 +-- data
 |    +-- entity            // Record data: getId, getEntityName, save, addOnSave, getDataXml,
 |    |                     //   getEntityReference, getIsDirty, getPrimaryAttributeValue, isValid,
 |    |                     //   addOnPostSave, removeOnPostSave, removeOnSave
 |    +-- process           // BPF: getActiveProcess, setActiveProcess, getActiveStage,
 |    |                     //   setActiveStage, moveNext, movePrevious, getProcessInstances,
 |    |                     //   setActiveProcessInstance, addOnStageChange, etc.
 |    +-- attributes        // Non-table data collection on the form
 |    +-- addOnLoad()       // Register handler for form data load
 |    +-- removeOnLoad()    // Remove handler
 |    +-- getIsDirty()      // Check if form data modified
 |    +-- isValid()         // Check if all form data is valid
 |    +-- refresh()         // Async refresh without page reload
 |    +-- save()            // Save the record
 +-- ui
 |    +-- controls          // All controls on the form (collection)
 |    +-- formSelector      // getCurrentItem, items collection
 |    +-- navigation        // Navigation items collection
 |    +-- process           // BPF UI control
 |    +-- quickForms        // Quick view controls collection
 |    +-- tabs              // Tabs collection, each containing sections
 |    +-- addOnLoad()       // Form UI OnLoad handler
 |    +-- removeOnLoad()    // Remove UI OnLoad handler
 |    +-- clearFormNotification()
 |    +-- close()           // Close the form
 |    +-- getFormType()     // 0=Undefined, 1=Create, 2=Update, 3=ReadOnly, 4=Disabled, 11=BulkEdit
 |    +-- getViewPortHeight() / getViewPortWidth()
 |    +-- refreshRibbon()   // Re-evaluate ribbon/command bar
 |    +-- setFormNotification(message, level, uniqueId)
 |    +-- setFormEntityName(name)
 +-- getAttribute(name)     // Shortcut to access column values
 +-- getControl(name)       // Shortcut to access controls
```

---

## formContext.data API

### formContext.data Properties and Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `addOnLoad(handler)` | void | Register handler for data load event |
| `removeOnLoad(handler)` | void | Remove data load handler |
| `getIsDirty()` | Boolean | True if any form data modified |
| `isValid()` | Boolean | True if all form data passes validation |
| `refresh(save)` | Promise | Async refresh; optionally save first |
| `save(saveOptions)` | Promise | Save the record |

### formContext.data.entity

Methods for the record displayed on the form.

| Method | Returns | Description |
|--------|---------|-------------|
| `addOnSave(handler)` | void | Register handler before save |
| `removeOnSave(handler)` | void | Remove save handler |
| `addOnPostSave(handler)` | void | Register handler after successful save |
| `removeOnPostSave(handler)` | void | Remove post-save handler |
| `getDataXml()` | String | XML of changed/always-submit columns |
| `getEntityName()` | String | Logical name of the table (e.g., `"account"`) |
| `getEntityReference()` | Lookup | `{entityType, id, name}` for the record |
| `getId()` | String | GUID of the record |
| `getIsDirty()` | Boolean | True if any columns modified |
| `getPrimaryAttributeValue()` | String | Value of the primary column |
| `isValid()` | Boolean | True if all entity data valid |
| `save(saveMode)` | void | Synchronous save. saveMode: `"saveandclose"` or `"saveandnew"` |

#### Entity Attributes Collection

Access columns on the form via `formContext.data.entity.attributes` or the shortcut `formContext.getAttribute()`.

```javascript
function manipulateColumns(formContext) {
    // Get a column value
    var name = formContext.getAttribute("name").getValue();

    // Set a column value
    formContext.getAttribute("revenue").setValue(50000);

    // Make a column required
    formContext.getAttribute("emailaddress1").setRequiredLevel("required");
    // Options: "none", "required", "recommended"

    // Control submit behavior
    formContext.getAttribute("description").setSubmitMode("always");
    // Options: "always", "never", "dirty" (default)

    // Check if column is dirty
    var isDirty = formContext.getAttribute("name").getIsDirty();

    // Get column metadata
    var attrType = formContext.getAttribute("revenue").getAttributeType();
    // Returns: "boolean", "datetime", "decimal", "double", "integer",
    //          "lookup", "memo", "money", "multiselectoptionset", "optionset", "string"

    // Get format
    var format = formContext.getAttribute("createdon").getFormat();
    // For datetime: "date", "datetime"
    // For string: "email", "phone", "text", "textarea", "tickersymbol", "url"
    // For integer: "duration", "language", "none", "timezone"
}
```

### Column Methods by Type

**All column types:**

| Method | Returns | Description |
|--------|---------|-------------|
| `addOnChange(handler)` | void | Register change handler |
| `removeOnChange(handler)` | void | Remove change handler |
| `fireOnChange()` | void | Trigger change event programmatically |
| `getAttributeType()` | String | Column data type |
| `getFormat()` | String | Column format |
| `getIsDirty()` | Boolean | Whether value has changed |
| `getName()` | String | Logical name of the column |
| `getParent()` | Object | Parent entity object |
| `getRequiredLevel()` | String | `"none"`, `"required"`, `"recommended"` |
| `setRequiredLevel(level)` | void | Set requirement level |
| `getSubmitMode()` | String | `"always"`, `"never"`, `"dirty"` |
| `setSubmitMode(mode)` | void | Set submit behavior |
| `getUserPrivilege()` | Object | `{canRead, canUpdate, canCreate}` |
| `getValue()` | varies | Current value |
| `setValue(value)` | void | Set value |
| `isValid()` | Boolean | Whether value passes validation |
| `setIsValid(valid, msg)` | void | Mark column valid/invalid with message |
| `controls` | Collection | Controls bound to this column |

**Type-specific methods:**

| Type | Method | Description |
|------|--------|-------------|
| Boolean | `getInitialValue()` | Default value defined in metadata |
| Lookup | `getIsPartyList()` | Whether it is a party list lookup |
| Choice/Choices | `getInitialValue()` | Default option value |
| Choice/Choices | `getOption(value)` | Get a single option object |
| Choice/Choices | `getOptions()` | Get all available options |
| Choice/Choices | `getSelectedOption()` | Currently selected option object |
| Choice/Choices | `getText()` | Display text of selected option |
| Number | `getMax()` | Maximum allowed value |
| Number | `getMin()` | Minimum allowed value |
| Number | `getPrecision()` | Number of decimal places |
| Number | `setPrecision(n)` | Set decimal precision |
| String | `getMaxLength()` | Maximum string length |

### formContext.data.process (Business Process Flow)

#### Active Process Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getActiveProcess()` | Process | Active process object |
| `setActiveProcess(processId, cb)` | void | Set active process |
| `getProcessInstances(cb)` | void | Get all process instances for record |
| `setActiveProcessInstance(instanceId, cb)` | void | Set active process instance |

#### Active Stage Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getActiveStage()` | Stage | Active stage object |
| `setActiveStage(stageId, cb)` | void | Set active stage |

#### Navigation Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `moveNext(cb)` | void | Move to next stage |
| `movePrevious(cb)` | void | Move to previous stage |

#### Process Object

| Method | Returns | Description |
|--------|---------|-------------|
| `getId()` | String | Process GUID |
| `getName()` | String | Process name |
| `getStages()` | Collection | Stages in the process |
| `isRendered()` | Boolean | Whether process is rendered |

#### Stage Object

| Method | Returns | Description |
|--------|---------|-------------|
| `getCategory()` | Object | Business process flow category |
| `getEntityName()` | String | Table associated with the stage |
| `getId()` | String | Stage GUID |
| `getName()` | String | Stage name |
| `getNavigationBehavior()` | Object | Navigation behavior settings |
| `getStatus()` | String | `"active"` or `"inactive"` |
| `getSteps()` | Collection | Steps in the stage |

#### Step Object

| Method | Returns | Description |
|--------|---------|-------------|
| `getAttribute()` | String | Logical name of the associated column |
| `getName()` | String | Step name |
| `getProgress()` | Number | Progress of action step |
| `setProgress(stepProgress, msg, cb)` | void | Update action step progress |
| `isRequired()` | Boolean | Whether step is required |

#### BPF Example

```javascript
function moveBpfForward(formContext) {
    var activeStage = formContext.data.process.getActiveStage();
    console.log("Current stage: " + activeStage.getName());

    formContext.data.process.moveNext(function(result) {
        if (result === "success") {
            console.log("Moved to next stage");
        } else {
            console.log("Stage transition failed: " + result);
            // result can be: "crossEntity", "end", "invalid", "dirtyForm"
        }
    });
}
```

---

## formContext.ui API

### formContext.ui Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `addOnLoad(handler)` | void | Register form UI OnLoad handler |
| `removeOnLoad(handler)` | void | Remove UI OnLoad handler |
| `clearFormNotification(uniqueId)` | Boolean | Clear a form-level notification |
| `close()` | void | Close the form |
| `getFormType()` | Number | Form type (see table below) |
| `getViewPortHeight()` | Number | Viewport height in pixels |
| `getViewPortWidth()` | Number | Viewport width in pixels |
| `refreshRibbon()` | void | Force ribbon/command bar re-evaluation |
| `setFormNotification(msg, level, uniqueId)` | Boolean | Show form-level notification |
| `setFormEntityName(name)` | void | Set displayed table name |

#### Form Type Values

| Value | Type |
|-------|------|
| 0 | Undefined |
| 1 | Create |
| 2 | Update |
| 3 | Read Only |
| 4 | Disabled |
| 6 | Bulk Edit |
| 11 | Read Optimized |

#### Form Notification Levels

| Level | Description |
|-------|-------------|
| `"ERROR"` | Red notification bar |
| `"WARNING"` | Yellow notification bar |
| `"INFO"` | Blue notification bar |

```javascript
function showNotifications(formContext) {
    // Show form-level notification
    formContext.ui.setFormNotification(
        "Record saved successfully", "INFO", "saveNotification"
    );

    // Clear after 5 seconds
    setTimeout(function() {
        formContext.ui.clearFormNotification("saveNotification");
    }, 5000);

    // Show error notification
    formContext.ui.setFormNotification(
        "Missing required fields", "ERROR", "validationError"
    );
}
```

### formContext.ui.tabs

Tabs are a collection accessed via `formContext.ui.tabs`. Each tab contains sections.

#### Tab Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getDisplayState()` | String | `"expanded"` or `"collapsed"` |
| `setDisplayState(state)` | void | Expand or collapse the tab |
| `getLabel()` | String | Tab label text |
| `setLabel(label)` | void | Set tab label |
| `getName()` | String | Tab name |
| `getParent()` | Object | Parent form (formContext.ui) |
| `getVisible()` | Boolean | Whether tab is visible |
| `setVisible(visible)` | void | Show or hide the tab |
| `setFocus()` | void | Set focus to the tab |
| `addTabStateChange(handler)` | void | Register for tab state changes |
| `removeTabStateChange(handler)` | void | Remove tab state handler |
| `sections` | Collection | Sections within the tab |

#### Section Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getLabel()` | String | Section label |
| `setLabel(label)` | void | Set section label |
| `getName()` | String | Section name |
| `getParent()` | Object | Parent tab |
| `getVisible()` | Boolean | Whether section is visible |
| `setVisible(visible)` | void | Show or hide the section |
| `controls` | Collection | Controls in the section |

```javascript
function toggleTabVisibility(formContext) {
    var tabs = formContext.ui.tabs;

    // Iterate all tabs
    tabs.forEach(function(tab) {
        console.log("Tab: " + tab.getName() + " - " + tab.getDisplayState());
    });

    // Get a specific tab and toggle visibility
    var detailsTab = tabs.get("tab_details");
    if (detailsTab) {
        detailsTab.setVisible(!detailsTab.getVisible());
    }

    // Collapse a tab
    var notesTab = tabs.get("tab_notes");
    if (notesTab) {
        notesTab.setDisplayState("collapsed");
    }

    // Hide all sections in a tab except one
    var generalTab = tabs.get("tab_general");
    generalTab.sections.forEach(function(section) {
        section.setVisible(section.getName() === "section_summary");
    });
}
```

### formContext.ui.controls

Controls represent HTML elements on the form. Access via `formContext.ui.controls` or shortcut `formContext.getControl()`.

#### Control Types

| Type | Description |
|------|-------------|
| `standard` | Standard bound control |
| `iframe` | IFRAME control |
| `kbsearch` | Knowledge base search control |
| `lookup` | Lookup control |
| `multiselectoptionset` | Multi-select choice control |
| `optionset` | Choice control |
| `quickform` | Quick view form control |
| `subgrid` | Subgrid control |
| `timercontrol` | Timer control |
| `timelinewall` | Timeline control |
| `webresource` | Web resource control |

#### Standard Control Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `addNotification(notification)` | void | Display control notification |
| `clearNotification(uniqueId)` | Boolean | Clear a control notification |
| `getAttribute()` | Attribute | Bound column object |
| `getControlType()` | String | Control type string |
| `getDisabled()` | Boolean | Whether control is disabled |
| `setDisabled(disabled)` | void | Enable or disable the control |
| `getLabel()` | String | Control label text |
| `setLabel(label)` | void | Set control label |
| `getName()` | String | Control name |
| `getOutputs()` | Object | Control output values (PCF) |
| `getParent()` | Object | Parent section |
| `getVisible()` | Boolean | Whether control is visible |
| `setVisible(visible)` | void | Show or hide the control |
| `setFocus()` | void | Set focus to the control |
| `setNotification(msg, uniqueId)` | Boolean | Show notification on the control |

#### Lookup Control Additional Methods

| Method | Description |
|--------|-------------|
| `addCustomFilter(filter, entityType)` | Add FetchXML filter to lookup |
| `addCustomView(viewId, entityName, viewDisplayName, fetchXml, layoutXml, isDefault)` | Add custom view |
| `addPreSearch(handler)` | Run handler before lookup search |
| `removePreSearch(handler)` | Remove pre-search handler |
| `getDefaultView()` | Get default view ID |
| `setDefaultView(viewId)` | Set default view |
| `getEntityTypes()` | Get allowed entity types array |
| `setEntityTypes(entityTypes)` | Set allowed entity types |

```javascript
function controlManipulation(formContext) {
    // Disable a control
    var phoneControl = formContext.getControl("telephone1");
    phoneControl.setDisabled(true);

    // Add notification to a control
    phoneControl.addNotification({
        messages: ["Phone number format is incorrect"],
        notificationLevel: "RECOMMENDATION", // or "ERROR"
        uniqueId: "phoneValidation"
    });

    // Filter a lookup control
    var parentAccountControl = formContext.getControl("parentaccountid");
    parentAccountControl.addPreSearch(function() {
        var filter = "<filter type='and'>" +
            "<condition attribute='statecode' operator='eq' value='0' />" +
            "</filter>";
        parentAccountControl.addCustomFilter(filter, "account");
    });

    // Hide all controls for a column
    var attr = formContext.getAttribute("description");
    attr.controls.forEach(function(control) {
        control.setVisible(false);
    });
}
```

### formContext.ui.navigation

The navigation items collection (not available on tablets).

| Method | Returns | Description |
|--------|---------|-------------|
| `getId()` | String | Navigation item ID |
| `getLabel()` | String | Navigation item label |
| `setLabel(label)` | void | Set label |
| `getVisible()` | Boolean | Whether item is visible |
| `setVisible(visible)` | void | Show or hide |
| `setFocus()` | void | Set focus |

```javascript
function hideNavigationItems(formContext) {
    var navItems = formContext.ui.navigation.items;
    navItems.forEach(function(item) {
        // Hide specific related entity navigation
        if (item.getId() === "navContacts") {
            item.setVisible(false);
        }
    });
}
```

### formContext.ui.quickForms

Quick view controls display data from a related record via a quick view form.

| Method | Returns | Description |
|--------|---------|-------------|
| `getControlType()` | String | Always `"quickform"` |
| `getDisabled()` | Boolean | Whether disabled |
| `getLabel()` | String | Label |
| `getName()` | String | Control name |
| `getVisible()` | Boolean | Whether visible |
| `setVisible(visible)` | void | Show/hide |
| `isLoaded()` | Boolean | Whether data finished loading |
| `refresh()` | void | Refresh the quick view data |

---

## Grids and Subgrids API

### Grid Types

- **Read-only grids**: Display tabular data; select a record to open its form for editing.
- **Editable grids**: Inline editing capabilities; support grouping, sorting, filtering within the grid.

### Getting the Grid Context

From a subgrid control on a form:

```javascript
function onSubgridLoad(executionContext) {
    var formContext = executionContext.getFormContext();
    var gridControl = formContext.getControl("subgrid_contacts");
    var grid = gridControl.getGrid();
    console.log("Total records: " + grid.getTotalRecordCount());
}
```

### Grid Object Hierarchy

```
GridControl
 +-- getGrid()           -> Grid
 |    +-- getRows()      -> Collection of GridRow
 |    |    +-- getData()  -> GridRowData
 |    |    |    +-- getEntity() -> GridEntity
 |    |    |    |    +-- getEntityName()
 |    |    |    |    +-- getId()
 |    |    |    |    +-- getEntityReference()
 |    |    |    |    +-- getPrimaryAttributeValue()
 |    |    |    |    +-- attributes -> Collection of GridAttribute
 |    +-- getSelectedRows() -> Collection of GridRow
 |    +-- getTotalRecordCount() -> Number
 +-- getViewSelector()   -> ViewSelector
```

### GridControl Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `addOnLoad(handler)` | void | Register handler for grid load |
| `removeOnLoad(handler)` | void | Remove grid load handler |
| `getEntityName()` | String | Logical name of the table |
| `getGrid()` | Grid | The grid object |
| `getRelationship()` | Object | Relationship info `{name, attributeName, roleType, relationshipType, navigationPropertyName}` |
| `getViewSelector()` | ViewSelector | View selector object |
| `refresh()` | void | Refresh the grid data |
| `getControlType()` | String | Returns `"subgrid"` |

### Grid Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getRows()` | Collection | All rows in the grid |
| `getSelectedRows()` | Collection | Currently selected rows |
| `getTotalRecordCount()` | Number | Total record count |

### GridEntity Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getEntityName()` | String | Logical name |
| `getEntityReference()` | Lookup | `{entityType, id, name}` |
| `getId()` | String | Record GUID |
| `getPrimaryAttributeValue()` | String | Primary column value |

### ViewSelector Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getCurrentView()` | Lookup | Current view reference |
| `setCurrentView(viewRef)` | void | Set the current view |
| `isVisible()` | Boolean | Whether view selector is visible |

### Grid Example

```javascript
function getSelectedContacts(formContext) {
    var gridControl = formContext.getControl("subgrid_contacts");
    var selectedRows = gridControl.getGrid().getSelectedRows();

    selectedRows.forEach(function(row) {
        var entity = row.getData().getEntity();
        var contactId = entity.getId();
        var contactName = entity.getPrimaryAttributeValue();
        console.log("Selected: " + contactName + " (" + contactId + ")");

        // Access specific column from editable grid row
        var emailAttr = entity.attributes.get("emailaddress1");
        if (emailAttr) {
            console.log("Email: " + emailAttr.getValue());
        }
    });
}
```

---

## Xrm.Navigation

### Methods

| Method | Description |
|--------|-------------|
| `navigateTo(pageInput, navOptions)` | Navigate to entity list, record, web resource, custom page, or dashboard |
| `openForm(entityFormOptions, formParams)` | Open entity form or quick create form |
| `openAlertDialog(alertStrings, alertOptions)` | Display alert dialog with one button |
| `openConfirmDialog(confirmStrings, confirmOptions)` | Display confirmation dialog with two buttons |
| `openErrorDialog(errorOptions)` | Display error dialog |
| `openFile(file, openFileOptions)` | Open a file |
| `openUrl(url, openUrlOptions)` | Open a URL |
| `openWebResource(webResourceName, windowOptions, data)` | Open web resource in new window |

### navigateTo

Opens inline pages or dialog pages. Unified Interface only.

```javascript
// Open an entity record inline
Xrm.Navigation.navigateTo(
    { pageType: "entityrecord", entityName: "account", entityId: accountId },
    { target: 1 } // 1 = inline
).then(function() {
    console.log("Navigation complete");
});

// Open a record in a dialog
Xrm.Navigation.navigateTo(
    { pageType: "entityrecord", entityName: "contact", formId: "abc-def-123" },
    { target: 2, width: 800, height: 600, position: 1, title: "Edit Contact" }
).then(function(result) {
    // result.savedEntityReference available if created in dialog
    if (result && result.savedEntityReference) {
        console.log("Created: " + result.savedEntityReference[0].id);
    }
});

// Open an entity list
Xrm.Navigation.navigateTo(
    { pageType: "entitylist", entityName: "contact" },
    { target: 1 }
);

// Open a web resource in dialog
Xrm.Navigation.navigateTo(
    { pageType: "webresource", webresourceName: "new_mypage.html", data: "param=value" },
    { target: 2, width: 500, height: 400 }
);

// Open a custom page in dialog
Xrm.Navigation.navigateTo(
    { pageType: "custom", name: "new_custompage_12345", entityName: "account", recordId: recordId },
    { target: 2, width: { value: 70, unit: "%" }, height: { value: 60, unit: "%" }, position: 1 }
);

// Open a dashboard
Xrm.Navigation.navigateTo(
    { pageType: "dashboard", dashboardId: "d201a642-6283-4f1d-81b7-da4b1685e698" },
    { target: 1 }
);
```

#### pageInput Types

| pageType | Required Properties | Optional Properties |
|----------|-------------------|---------------------|
| `"entitylist"` | `entityName` | `viewId`, `viewType` |
| `"entityrecord"` | `entityName` | `entityId`, `formId`, `data`, `createFromEntity`, `relationship`, `processId`, `processInstanceId`, `selectedStageId`, `tabName` |
| `"dashboard"` | -- | `dashboardId` |
| `"webresource"` | `webresourceName` | `data` |
| `"custom"` | `name` | `entityName`, `recordId` |

#### navigationOptions

| Property | Type | Description |
|----------|------|-------------|
| `target` | Number | `1` = inline (default), `2` = dialog |
| `width` | Number or `{value, unit}` | Dialog width (px or %) |
| `height` | Number or `{value, unit}` | Dialog height (px or %) |
| `position` | Number | `1` = center (default), `2` = far side |
| `title` | String | Dialog title |

### openForm

```javascript
// Open existing record
Xrm.Navigation.openForm({
    entityName: "contact",
    entityId: "a8a19cdd-88df-e311-b8e5-6c3be5a8b200"
});

// Open new record with defaults
Xrm.Navigation.openForm(
    { entityName: "contact", useQuickCreateForm: false },
    { firstname: "John", lastname: "Doe", parentcustomerid: parentLookupValue }
);

// Open quick create form
Xrm.Navigation.openForm({
    entityName: "contact",
    useQuickCreateForm: true
}).then(function(result) {
    if (result.savedEntityReference.length > 0) {
        console.log("Created: " + result.savedEntityReference[0].id);
    }
});
```

#### entityFormOptions Properties

| Property | Type | Description |
|----------|------|-------------|
| `entityName` | String | Table logical name |
| `entityId` | String | Record GUID (omit for create) |
| `formId` | String | Specific form GUID |
| `cmdbar` | Boolean | Show command bar (requires `openInNewWindow`) |
| `navbar` | String | `"on"`, `"off"`, `"entity"` |
| `openInNewWindow` | Boolean | Open in new window/tab |
| `useQuickCreateForm` | Boolean | Use quick create form |
| `createFromEntity` | Lookup | Record providing defaults via mapped columns |
| `height` | Number | Window height in px |
| `width` | Number | Window width in px |
| `relationship` | Object | Related record relationship info |
| `selectedStageId` | String | BPF stage to select |

### openAlertDialog

```javascript
Xrm.Navigation.openAlertDialog(
    {
        text: "The record has been saved.",
        title: "Success",
        confirmButtonLabel: "OK"
    },
    { height: 150, width: 300 }
).then(function() {
    console.log("Alert closed");
});
```

### openConfirmDialog

```javascript
Xrm.Navigation.openConfirmDialog(
    {
        text: "Are you sure you want to delete this record?",
        title: "Confirm Delete",
        confirmButtonLabel: "Delete",
        cancelButtonLabel: "Cancel",
        subtitle: "This action cannot be undone."
    },
    { height: 200, width: 400 }
).then(function(result) {
    if (result.confirmed) {
        // user clicked Delete
    } else {
        // user clicked Cancel or X
    }
});
```

### openErrorDialog

```javascript
Xrm.Navigation.openErrorDialog({
    message: "An error occurred while processing your request.",
    details: "Stack trace or additional technical info here.",
    errorCode: 12345
});
```

---

## Xrm.WebApi

Provides CRUD operations and the ability to execute custom actions/functions via the Dataverse Web API. Has sub-namespaces `.online` and `.offline` for specific client modes.

### Properties

| Property | Description |
|----------|-------------|
| `online` | Methods available in online mode |
| `offline` | Methods available in offline mode |

### CRUD Methods

#### createRecord

```javascript
Xrm.WebApi.createRecord(entityLogicalName, data).then(successCallback, errorCallback);
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entityLogicalName` | String | Yes | Table logical name (e.g., `"account"`) |
| `data` | Object | Yes | JSON object with column values |

Returns: Promise resolving to `{entityType, id}`.

```javascript
// Simple create
var data = {
    "name": "Contoso Ltd",
    "revenue": 5000000,
    "accountcategorycode": 1,
    "creditonhold": false,
    "description": "Main corporate account"
};
Xrm.WebApi.createRecord("account", data).then(
    function(result) { console.log("Created: " + result.id); },
    function(error) { console.log(error.message); }
);

// Deep insert (create related records together)
var data = {
    "name": "Contoso Ltd",
    "primarycontactid": {
        "firstname": "Jane",
        "lastname": "Smith"
    },
    "opportunity_customer_accounts": [{
        "name": "Q4 Opportunity",
        "estimatedvalue": 100000
    }]
};
Xrm.WebApi.createRecord("account", data).then(
    function(result) { console.log("Account with relations: " + result.id); },
    function(error) { console.log(error.message); }
);

// Associate with existing record via @odata.bind
var data = {
    "name": "Sub Account",
    "primarycontactid@odata.bind": "/contacts(465b158c-541c-e511-80d3-3863bb347ba8)"
};
Xrm.WebApi.createRecord("account", data).then(
    function(result) { console.log("Created: " + result.id); },
    function(error) { console.log(error.message); }
);
```

#### retrieveRecord

```javascript
Xrm.WebApi.retrieveRecord(entityLogicalName, id, options).then(successCallback, errorCallback);
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entityLogicalName` | String | Yes | Table logical name |
| `id` | String | Yes | Record GUID |
| `options` | String | No | OData query (`$select`, `$expand`) |

```javascript
// Basic retrieve with select
Xrm.WebApi.retrieveRecord("account", accountId,
    "?$select=name,revenue,accountnumber"
).then(
    function(result) {
        console.log("Name: " + result.name);
        console.log("Revenue: " + result.revenue);
    },
    function(error) { console.log(error.message); }
);

// Retrieve with expanded navigation property
Xrm.WebApi.retrieveRecord("account", accountId,
    "?$select=name&$expand=primarycontactid($select=contactid,fullname)"
).then(
    function(result) {
        console.log("Contact: " + result.primarycontactid.fullname);
    },
    function(error) { console.log(error.message); }
);
```

#### retrieveMultipleRecords

```javascript
Xrm.WebApi.retrieveMultipleRecords(entityLogicalName, options, maxPageSize)
    .then(successCallback, errorCallback);
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entityLogicalName` | String | Yes | Table logical name |
| `options` | String | No | OData query or FetchXML (`?fetchXml=...`) |
| `maxPageSize` | Number | No | Records per page (default 5000 standard, 500 elastic) |

Returns: Promise resolving to `{entities[], nextLink?, fetchXmlPagingCookie?}`.

Supported OData options: `$select`, `$top`, `$filter`, `$expand`, `$orderby`.

```javascript
// Basic query with filter and select
Xrm.WebApi.retrieveMultipleRecords("contact",
    "?$select=fullname,emailaddress1&$filter=statecode eq 0&$orderby=fullname asc",
    10
).then(
    function(result) {
        for (var i = 0; i < result.entities.length; i++) {
            console.log(result.entities[i].fullname);
        }
        // Handle paging
        if (result.nextLink) {
            console.log("More records available");
        }
    },
    function(error) { console.log(error.message); }
);

// Query with FetchXML
var fetchXml = "?fetchXml=" + encodeURIComponent(
    "<fetch top='5'>" +
    "  <entity name='account'>" +
    "    <attribute name='name' />" +
    "    <attribute name='revenue' />" +
    "    <filter>" +
    "      <condition attribute='revenue' operator='gt' value='1000000' />" +
    "    </filter>" +
    "  </entity>" +
    "</fetch>"
);
Xrm.WebApi.retrieveMultipleRecords("account", fetchXml).then(
    function(result) {
        result.entities.forEach(function(r) { console.log(r.name); });
    },
    function(error) { console.log(error.message); }
);
```

#### updateRecord

```javascript
Xrm.WebApi.updateRecord(entityLogicalName, id, data).then(successCallback, errorCallback);
```

```javascript
var data = {
    "name": "Updated Account Name",
    "revenue": 7500000,
    "creditonhold": true
};
Xrm.WebApi.updateRecord("account", accountId, data).then(
    function(result) { console.log("Updated: " + result.id); },
    function(error) { console.log(error.message); }
);
```

#### deleteRecord

```javascript
Xrm.WebApi.deleteRecord(entityLogicalName, id).then(successCallback, errorCallback);
```

```javascript
Xrm.WebApi.deleteRecord("account", accountId).then(
    function(result) { console.log("Deleted: " + result.id); },
    function(error) { console.log(error.message); }
);
```

### execute and executeMultiple

Execute custom actions, functions, or CRUD operations. Online mode only (`Xrm.WebApi.online`).

```javascript
Xrm.WebApi.online.execute(request).then(successCallback, errorCallback);
Xrm.WebApi.online.executeMultiple(requests).then(successCallback, errorCallback);
```

The `request` object must implement a `getMetadata()` method returning:

| Property | Type | Description |
|----------|------|-------------|
| `boundParameter` | String | `null` (unbound), `undefined` (CRUD), or `"entity"` (bound) |
| `operationName` | String | Action/function name, or `"Create"/"Retrieve"/"Update"/"Delete"` |
| `operationType` | Number | `0` = Action, `1` = Function, `2` = CRUD |
| `parameterTypes` | Object | Parameter metadata (typeName, structuralProperty) |

```javascript
// Execute a custom unbound action
var myRequest = {};
myRequest.InputParam = "some value";
myRequest.getMetadata = function() {
    return {
        boundParameter: null,
        operationName: "new_MyCustomAction",
        operationType: 0,
        parameterTypes: {
            "InputParam": {
                typeName: "Edm.String",
                structuralProperty: 1 // PrimitiveType
            }
        }
    };
};

Xrm.WebApi.online.execute(myRequest).then(
    function(response) {
        if (response.ok) {
            return response.json();
        }
    }
).then(function(result) {
    console.log("Action result: " + JSON.stringify(result));
});
```

### isAvailableOffline

```javascript
var isOffline = Xrm.WebApi.isAvailableOffline("account"); // returns Boolean
```

---

## Web Resources

Virtual files stored in Dataverse, accessible via unique URLs. They are solution-aware and can be exported/imported between environments.

### Types

| Type | Extension | Type Value | Description |
|------|-----------|------------|-------------|
| Webpage (HTML) | .htm, .html | 1 | HTML pages displayed inline or in dialogs |
| CSS | .css | 2 | Stylesheets for HTML web resources |
| JavaScript | .js | 3 | Script libraries for form events, ribbon commands |
| XML | .xml | 4 | Data files consumed by other web resources |
| PNG | .png | 5 | Image resources |
| JPG | .jpg | 6 | Image resources |
| GIF | .gif | 7 | Image resources |
| XAP (Silverlight) | .xap | 8 | Deprecated; avoid in new development |
| XSL/XSLT | .xsl, .xslt | 9 | Stylesheet transformations for XML |
| ICO | .ico | 10 | Icon files |
| SVG | .svg | 11 | Scalable vector graphics |
| RESX (strings) | .resx | 12 | Localized string resources |

### Reference Methods

| Method | Usage | Notes |
|--------|-------|-------|
| `$webresource:` directive | SiteMap, ribbon XML, form definitions | Creates solution dependency; recommended for declarative use |
| `Xrm.Navigation.openWebResource()` | JavaScript | Opens in new window; includes cache-busting token |
| Relative URL | Between web resources | Use consistent publisher prefix naming |
| Full URL | Direct browser access | `https://<org>.crm.dynamics.com/WebResources/<name>` |

### Naming Convention

Use your publisher prefix: `new_/scripts/account_form.js`, `new_/images/logo.png`. Directory separators (`/`) create a virtual folder structure in the solution explorer.

### Accessing Context in HTML Web Resources

HTML web resources can access the Client API via `ClientGlobalContext.js.aspx`:

```html
<!-- In the HTML web resource -->
<html>
<head>
    <script src="ClientGlobalContext.js.aspx"></script>
    <script>
        function init() {
            var context = GetGlobalContext();
            var orgUrl = context.getClientUrl();
            var userId = context.userSettings.userId;
            var userName = context.userSettings.userName;
            var lcid = context.userSettings.languageId;
        }
    </script>
</head>
<body onload="init()">
    <!-- content -->
</body>
</html>
```

### Passing Data to Web Resources

```javascript
// From form script, open web resource with data
Xrm.Navigation.openWebResource("new_/pages/details.html",
    { height: 400, width: 600 },
    "recordId=" + recordId + "&entityName=account"
);

// In the web resource, read data
var dataParam = new URLSearchParams(
    window.location.search.substring(
        window.location.search.indexOf("Data=") > -1
            ? window.location.search.indexOf("Data=") + 5
            : 0
    )
);
```

### Limitations

- No server-side code execution (no .aspx); static files only
- Max file size governed by `Organization.MaxUploadFileSize` (default 5 MB)
- Cannot directly access the Dataverse Web API from an HTML web resource without using ADAL/MSAL or the `ClientGlobalContext.js.aspx` approach
- Subject to same-origin restrictions for cross-domain calls
- RESX web resources must be associated with a form to be loaded by `Xrm.Utility.getResourceString()`

---

## Ribbon / Command Bar Customization

### Overview

Model-driven apps display commands via a command bar (or ribbon in legacy views). Both use the same underlying XML schema (`RibbonDiffXml`).

There are two approaches to customization:
1. **Modern commanding** (recommended): Visual designer in the maker portal; no XML editing required.
2. **Classic ribbon XML**: Define `RibbonDiffXml` in the solution `customizations.xml`; supports full control over visibility rules, enable rules, and actions.

### Modern Commanding

Create and edit command bar buttons in Power Apps maker portal under a table's **Commands** section. Supports:
- **Visibility**: Show/hide using Power Fx expressions
- **Action**: Run JavaScript, open URL, or Power Fx
- **Location**: Main form, main grid, subgrid, associated view, quick action

### Classic Ribbon XML Elements

| Element | Purpose |
|---------|---------|
| `<CommandDefinition>` | Defines a command with actions and enable/display rules |
| `<RibbonDiffXml>` | Root element for ribbon customizations in solution XML |
| `<CustomAction>` | Add, modify, or hide ribbon buttons |
| `<EnableRule>` | Conditions for enabling a button (e.g., record selected, form state) |
| `<DisplayRule>` | Conditions for showing/hiding a button |
| `<JavaScriptFunction>` | Reference a JS web resource function as the command action |

### JavaScript Actions in Ribbon Commands

Ribbon buttons execute JavaScript functions from web resource libraries. The function receives a `PrimaryControl` (formContext or gridContext) parameter automatically when configured.

```javascript
// Ribbon command handler for a form button
function onCustomButtonClick(primaryControl) {
    var formContext = primaryControl; // on form, primaryControl = formContext
    var recordId = formContext.data.entity.getId();
    var entityName = formContext.data.entity.getEntityName();

    Xrm.Navigation.openConfirmDialog({
        text: "Run custom action on this record?",
        title: "Confirm"
    }).then(function(result) {
        if (result.confirmed) {
            // Call a custom action
            var request = {};
            request.entity = {
                entityType: entityName,
                id: recordId
            };
            request.getMetadata = function() {
                return {
                    boundParameter: "entity",
                    operationName: "new_ProcessRecord",
                    operationType: 0,
                    parameterTypes: {
                        "entity": {
                            typeName: "mscrm." + entityName,
                            structuralProperty: 5
                        }
                    }
                };
            };
            Xrm.WebApi.online.execute(request).then(
                function(response) {
                    if (response.ok) {
                        Xrm.Navigation.openAlertDialog({ text: "Action completed." });
                        formContext.data.refresh();
                    }
                },
                function(error) {
                    Xrm.Navigation.openErrorDialog({ message: error.message });
                }
            );
        }
    });
}

// Ribbon command handler for a grid button
function onGridButtonClick(selectedItems, primaryControl) {
    // selectedItems = SelectedControlSelectedItemReferences (classic ribbon)
    // For modern commanding, use primaryControl as gridContext
    var gridContext = primaryControl;
    var selectedRows = gridContext.getGrid().getSelectedRows();
    selectedRows.forEach(function(row) {
        var id = row.getData().getEntity().getId();
        console.log("Processing: " + id);
    });
}

// Enable rule function (return true to enable, false to disable)
function isRecordActive(primaryControl) {
    var formContext = primaryControl;
    var stateCode = formContext.getAttribute("statecode").getValue();
    return stateCode === 0; // 0 = Active
}
```

### Ribbon Command Parameters (Classic XML)

| CrmParameter | Value Passed | Context |
|--------------|-------------|---------|
| `PrimaryControl` | formContext or gridContext | Form or grid |
| `SelectedControl` | The subgrid control | Subgrid |
| `FirstPrimaryItemId` | GUID of the first selected record | Grid |
| `SelectedControlSelectedItemCount` | Number of selected records | Grid |
| `SelectedControlSelectedItemReferences` | Array of selected items `{Id, TypeCode, TypeName}` | Grid |

### Refreshing the Command Bar

After changing data that affects enable/display rules, refresh the ribbon:

```javascript
formContext.ui.refreshRibbon();
```

---

## Common Patterns

### Form OnLoad with Role-Based Logic

```javascript
function onAccountFormLoad(executionContext) {
    var formContext = executionContext.getFormContext();
    var userRoles = Xrm.Utility.getGlobalContext().userSettings.securityRoles;

    // Check for a specific security role by name
    var isManager = userRoles.some(function(role) {
        return role.name === "Sales Manager";
    });

    if (!isManager) {
        // Hide sensitive fields
        formContext.getControl("revenue").setVisible(false);
        formContext.getControl("creditlimit").setVisible(false);
    }

    // Set field requirement based on form type
    if (formContext.ui.getFormType() === 1) { // Create
        formContext.getAttribute("emailaddress1").setRequiredLevel("required");
    }
}
```

### Cascading Lookups (Filter Child Lookup Based on Parent)

```javascript
function onParentAccountChange(executionContext) {
    var formContext = executionContext.getFormContext();
    var parentAccount = formContext.getAttribute("parentaccountid").getValue();

    if (parentAccount) {
        var parentId = parentAccount[0].id.replace("{", "").replace("}", "");

        // Filter contact lookup to show only contacts of the parent account
        formContext.getControl("primarycontactid").addPreSearch(function() {
            var filter = "<filter type='and'>" +
                "<condition attribute='parentcustomerid' operator='eq' value='" + parentId + "' />" +
                "</filter>";
            formContext.getControl("primarycontactid").addCustomFilter(filter, "contact");
        });
    }
}
```

### Auto-Save Prevention for Specific Conditions

```javascript
function onFormSave(executionContext) {
    var formContext = executionContext.getFormContext();
    var saveEvent = executionContext.getEventArgs();
    var saveMode = saveEvent.getSaveMode();

    // Prevent auto-save (mode 70) if validation fails
    if (saveMode === 70) {
        var revenue = formContext.getAttribute("revenue").getValue();
        var category = formContext.getAttribute("accountcategorycode").getValue();

        if (category === 1 && (!revenue || revenue < 10000)) {
            saveEvent.preventDefault();
            formContext.ui.setFormNotification(
                "Preferred customers must have revenue >= 10,000",
                "WARNING",
                "revenueValidation"
            );
        }
    }
}
```

### Async OnSave with Validation

```javascript
function asyncOnSave(executionContext) {
    var eventArgs = executionContext.getEventArgs();
    // Request a delay so async validation can run before save proceeds
    eventArgs.preventDefaultOnError();

    var formContext = executionContext.getFormContext();
    var accountName = formContext.getAttribute("name").getValue();

    // Check for duplicate via WebApi
    Xrm.WebApi.retrieveMultipleRecords("account",
        "?$select=accountid&$filter=name eq '" + accountName + "'"
    ).then(function(result) {
        if (result.entities.length > 0) {
            eventArgs.preventDefault();
            formContext.ui.setFormNotification(
                "An account with this name already exists.",
                "ERROR",
                "duplicateCheck"
            );
        }
    });
}
```

---

## Xrm.Utility (Selected Methods)

| Method | Description |
|--------|-------------|
| `getGlobalContext()` | Returns the global context (client URL, org settings, user settings) |
| `getEntityMetadata(entityName, attributes)` | Returns metadata for a table |
| `lookupObjects(lookupOptions)` | Opens a lookup dialog |
| `showProgressIndicator(message)` | Shows a progress spinner overlay |
| `closeProgressIndicator()` | Closes the progress spinner |
| `getResourceString(webResourceName, key)` | Gets a localized string from a RESX web resource |

```javascript
// Show progress indicator during long operation
Xrm.Utility.showProgressIndicator("Processing records...");

Xrm.WebApi.retrieveMultipleRecords("contact",
    "?$select=fullname&$top=100"
).then(function(result) {
    // process results
    Xrm.Utility.closeProgressIndicator();
}).catch(function(error) {
    Xrm.Utility.closeProgressIndicator();
    Xrm.Navigation.openErrorDialog({ message: error.message });
});

// Get entity metadata
Xrm.Utility.getEntityMetadata("account", ["name", "revenue"]).then(
    function(metadata) {
        console.log("Display name: " + metadata.DisplayName);
        console.log("Primary ID: " + metadata.PrimaryIdAttribute);
    }
);

// Open a lookup dialog
Xrm.Utility.lookupObjects({
    defaultEntityType: "contact",
    entityTypes: ["contact"],
    allowMultiSelect: false,
    filters: [{
        entityLogicalName: "contact",
        filterXml: "<filter><condition attribute='statecode' operator='eq' value='0' /></filter>"
    }]
}).then(function(result) {
    if (result && result.length > 0) {
        console.log("Selected: " + result[0].name + " (" + result[0].id + ")");
    }
});
```

---

## Xrm.Device

| Method | Description |
|--------|-------------|
| `captureImage(options)` | Open camera to capture an image |
| `captureAudio()` | Record audio |
| `captureVideo()` | Record video |
| `getBarcodeValue()` | Scan a barcode |
| `getCurrentPosition()` | Get GPS coordinates |
| `pickFile(options)` | Open file picker |

```javascript
// Scan a barcode (mobile only)
Xrm.Device.getBarcodeValue().then(
    function(result) {
        formContext.getAttribute("new_barcode").setValue(result);
    },
    function(error) { console.log(error.message); }
);

// Get current GPS position
Xrm.Device.getCurrentPosition().then(
    function(pos) {
        formContext.getAttribute("address1_latitude").setValue(pos.coords.latitude);
        formContext.getAttribute("address1_longitude").setValue(pos.coords.longitude);
    }
);
```

---

## Best Practices

1. **Use `formContext` instead of `Xrm.Page`** -- `Xrm.Page` is deprecated; always obtain `formContext` from the execution context.
2. **Prefer business rules** for simple show/hide, set required, set default value logic; use JavaScript only when business rules are insufficient.
3. **Always use `$select`** in WebApi calls to limit returned columns for performance.
4. **Use `async/await` pattern** with `.then()` chains for readability when supported.
5. **Namespace your functions** to avoid global scope pollution (e.g., `Contoso.Account.onLoad`).
6. **Register OnChange handlers in OnLoad**, not in form properties, for better control over lifecycle.
7. **Avoid direct DOM manipulation** -- the DOM is unsupported and may change between releases.
8. **Use `setSubmitMode("always")`** for calculated fields that must be saved even if not user-modified.
9. **Handle errors** in all WebApi calls; unhandled promise rejections cause silent failures.
10. **Use `formContext.ui.refreshRibbon()`** after programmatic data changes that affect command visibility.
