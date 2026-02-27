# Power Fx Patterns & Recipes

Common patterns for Power Apps canvas development. Each pattern is a named, reusable code block.

## CRUD with Forms

### Create New Record via Form
```powerfx
// Button: "New" on BrowseScreen
NewForm(EditForm1);
Navigate(EditScreen, ScreenTransition.None)
```

### Submit Form with Navigation
```powerfx
// Button: "Save" on EditScreen
SubmitForm(EditForm1);
// EditForm1.OnSuccess:
Notify("Saved!", NotificationType.Success);
Navigate(BrowseScreen, ScreenTransition.None)
```

### Create Record via Patch (no form)
```powerfx
Patch(
    Customers,
    Defaults(Customers),
    {
        Name: txtName.Text,
        Email: txtEmail.Text,
        Created: Now()
    }
)
```

### Update Record via Patch
```powerfx
Patch(
    Customers,
    LookUp(Customers, ID = varSelectedId),
    { Phone: txtPhone.Text, Modified: Now() }
)
```

### Delete with Confirmation
```powerfx
If(
    Confirm("Delete this record?", { Title: "Confirm Delete" }),
    Remove(Customers, Gallery1.Selected);
    Notify("Deleted", NotificationType.Success)
)
```

## Data Loading

### Concurrent Data Load (App.OnStart or Screen.OnVisible)
```powerfx
Concurrent(
    ClearCollect(colProducts, Products),
    ClearCollect(colCustomers, Customers),
    ClearCollect(colOrders, Orders)
);
Set(varDataLoaded, true)
```

### Named Formulas for Auto-Refresh Data (App.Formulas)
```powerfx
CurrentUser = LookUp(Users, Email = User().Email);
IsAdmin = CurrentUser.Role = "Admin";
ActiveProducts = Filter(Products, Status = "Active");
```

### Refresh and Reload Pattern
```powerfx
Refresh(Customers);
ClearCollect(colCustomers, Customers);
Notify("Data refreshed", NotificationType.Information)
```

## Error Handling

### Safe Patch with Error Notification
```powerfx
IfError(
    Patch(Customers, Defaults(Customers), { Name: txtName.Text }),
    Notify("Save failed: " & FirstError.Message, NotificationType.Error)
);
```

### Chained Operations (Stop on First Error)
```powerfx
IfError(
    Patch(Orders, Defaults(Orders), { CustomerID: varCustId }),
    Notify("Order failed: " & FirstError.Message, NotificationType.Error),
    Patch(OrderItems, Defaults(OrderItems), { OrderID: varOrderId }),
    Notify("Item failed: " & FirstError.Message, NotificationType.Error),
    Notify("Order created!", NotificationType.Success);
    Navigate(OrderList)
)
```

### Global Error Handler (App.OnError)
```powerfx
Trace(
    $"Error: {FirstError.Message} | Source: {FirstError.Source}",
    TraceSeverity.Error,
    { Screen: App.ActiveScreen.Name }
);
Error(FirstError)  // Rethrow to show default banner
```

### Custom Validation Error
```powerfx
If(
    txtStartDate.SelectedDate > txtEndDate.SelectedDate,
    Error({ Kind: ErrorKind.Validation, Message: "Start date must be before end date" })
)
```

## Gallery Filtering & Sorting

### Search + Filter + Sort (Delegation-Safe)
```powerfx
SortByColumns(
    Filter(
        Customers,
        StartsWith(Name, txtSearch.Text),
        Status = ddStatus.Selected.Value
    ),
    "Name",
    If(varSortAsc, SortOrder.Ascending, SortOrder.Descending)
)
```

### Multi-Column Search (Delegation-Safe)
```powerfx
Search(
    Customers,
    txtSearch.Text,
    "Name", "Email", "Company"
)
```

### Dynamic Sort Column
```powerfx
SortByColumns(
    Filter(Customers, StartsWith(Name, txtSearch.Text)),
    varSortColumn,
    If(varSortAsc, SortOrder.Ascending, SortOrder.Descending)
)
```

### Gallery with "No Results" Handling
```powerfx
// Gallery Items:
Filter(Customers, StartsWith(Name, txtSearch.Text))

// "No results" label Visible:
IsEmpty(Gallery1.AllItems)
```

## Delegation-Safe Queries

### NEVER DO THIS (Non-Delegable, Truncated Data)
```powerfx
// BAD: Lower() is not delegable
Filter(Customers, Lower(Name) = Lower(txtSearch.Text))

// BAD: Len() is not delegable
Filter(Customers, Len(Name) > 5)

// BAD: exactin is not delegable
Filter(Customers, Name exactin ["Alice", "Bob"])
```

### DO THIS INSTEAD (Delegable Alternatives)
```powerfx
// GOOD: StartsWith is delegable
Filter(Customers, StartsWith(Name, txtSearch.Text))

// GOOD: Search is delegable for substring matching
Search(Customers, txtSearch.Text, "Name")

// GOOD: Use direct comparison operators
Filter(Customers, Name = txtSearch.Text)

// GOOD: Entity property on LEFT side
Filter(Orders, CustomerID = varSelectedCustId)
```

### Delegation-Safe Aggregation
```powerfx
// These are delegable against supported sources:
CountRows(Filter(Orders, Status = "Pending"))
Sum(Filter(Orders, CustomerID = varCustId), Amount)
Average(Filter(Scores, Subject = "Math"), Grade)
```

## Variable Management

### Initialize Variables on App Start
```powerfx
// App.OnStart (for imperative setup):
Set(varCurrentUser, User().Email);
Set(varIsOnline, Connection.Connected)

// App.Formulas (preferred for derived values):
varUserRecord = LookUp(Employees, Email = User().Email);
varUserRole = varUserRecord.Role;
varIsManager = varUserRole in ["Manager", "Director", "VP"];
```

### Toggle Pattern
```powerfx
// Button.OnSelect:
Set(varShowPanel, !varShowPanel)

// Panel.Visible:
varShowPanel
```

### Screen Navigation with Context
```powerfx
// From gallery:
Navigate(
    DetailScreen,
    ScreenTransition.Fade,
    { ctxRecordId: Gallery1.Selected.ID }
)

// On DetailScreen:
// Label.Text = LookUp(Customers, ID = ctxRecordId).Name
```

### Multi-Select with Collection
```powerfx
// Gallery item OnSelect (toggle selection):
If(
    ThisItem.ID in colSelected.ID,
    Remove(colSelected, LookUp(colSelected, ID = ThisItem.ID)),
    Collect(colSelected, ThisItem)
)

// Selected count:
CountRows(colSelected)

// Check if item is selected (for icon/highlight):
ThisItem.ID in colSelected.ID
```

## Responsive Formulas

### Responsive Width
```powerfx
// Container width based on screen size
If(
    App.Width >= 1024, App.Width * 0.6,
    App.Width >= 768, App.Width * 0.8,
    App.Width
)
```

### Show/Hide Based on Screen Size
```powerfx
// Sidebar.Visible:
App.Width >= 768

// Mobile header.Visible:
App.Width < 768
```

## Offline Patterns

### Cache Data for Offline
```powerfx
// Screen.OnVisible (when online):
If(
    Connection.Connected,
    ClearCollect(colCustomers, Customers);
    SaveData(colCustomers, "CustomersCache"),
    LoadData(colCustomers, "CustomersCache", true)
)
```

### Queue Changes for Sync
```powerfx
// Save locally when offline:
Collect(colPendingChanges, {
    Table: "Customers",
    RecordId: Gallery1.Selected.ID,
    Field: "Phone",
    Value: txtPhone.Text,
    Timestamp: Now()
});
SaveData(colPendingChanges, "PendingSync")
```

### Sync When Online
```powerfx
// Sync button or timer:
If(
    Connection.Connected && !IsEmpty(colPendingChanges),
    ForAll(
        colPendingChanges,
        Patch(Customers, LookUp(Customers, ID = RecordId), { Phone: Value })
    );
    Clear(colPendingChanges);
    SaveData(colPendingChanges, "PendingSync");
    Notify("Synced!", NotificationType.Success)
)
```

## JSON & External Data

### Parse JSON to Typed Table
```powerfx
ForAll(
    ParseJSON(varJsonString).items,
    {
        id: Value(ThisRecord.id),
        name: Text(ThisRecord.name),
        date: DateValue(Text(ThisRecord.date))
    }
)
```

### Generate JSON for API
```powerfx
Set(
    varPayload,
    JSON(
        { name: txtName.Text, email: txtEmail.Text },
        JSONFormat.IndentFour
    )
)
```

## Form Validation

### Pre-Submit Validation Chain
```powerfx
If(
    IsBlank(txtName.Text),
        Notify("Name is required", NotificationType.Error);
        SetFocus(txtName),
    !IsMatch(txtEmail.Text, Match.Email),
        Notify("Invalid email", NotificationType.Error);
        SetFocus(txtEmail),
    Value(txtAge.Text) < 0 || Value(txtAge.Text) > 150,
        Notify("Age must be 0-150", NotificationType.Error);
        SetFocus(txtAge),
    // All valid — submit
    SubmitForm(EditForm1)
)
```

## Local Calculations with With()

### Inline Named Values
```powerfx
With(
    {
        total: Sum(colOrders, Amount),
        count: CountRows(colOrders)
    },
    If(count > 0, total / count, 0)
)
```

### Capture Patch Result
```powerfx
With(
    { result: Patch(Customers, Defaults(Customers), { Name: "New" }) },
    If(
        !IsError(result),
        Notify("Created: " & result.Name);
        Navigate(DetailScreen, None, { ctxId: result.ID })
    )
)
```
