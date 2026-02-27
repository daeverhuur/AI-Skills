# Dataverse Tables & Columns Reference

> Research compiled from Microsoft Learn documentation (2026-02-26)
> Source: https://learn.microsoft.com/en-us/power-apps/maker/data-platform/

---

## 1. What is Dataverse

Dataverse stores and manages data used by business applications within **tables** (rows and columns). It provides a base set of standard tables plus support for custom tables.

**Core capabilities**: Role-based security, rich metadata, server-side logic (business rules, workflows, BPFs, plugins), calculated/rollup columns, Excel/Power Query integration, Dynamics 365 data sharing.

**Terminology mapping** (since Nov 2020):

| Legacy Term | Current Term |
|---|---|
| Entity / Entities | Table / Tables |
| Field / Attribute | Column / Columns |
| Record | Row |
| Option Set / Picklist | Choice / Choices |
| Two Options | Yes/No |

> Note: API message names (e.g., `CreateEntityRequest`, `CreateAttributeRequest`) remain unchanged.

**Security model layers**: Business units, role-based security, row-level security, column-level security.

---

## 2. Types of Tables

| Type | Description |
|---|---|
| **Standard** | Out-of-box tables (Account, Contact, Task, User). Customizable when `IsCustomizable=true`. |
| **Activity** | Special tables with subject, start/stop time, duration. Owned by user/team only. Examples: Appointment, Email, Fax, Letter, Phone Call, Recurring Appointment, Task. |
| **Virtual** | Data sourced from external systems at runtime (e.g., Azure SQL). No data replication. |
| **Elastic** | Powered by Azure Cosmos DB for very large datasets (tens of millions of rows). Auto-scaling. |

**Table ownership types** (cannot be changed after creation):

| Ownership | Description |
|---|---|
| **User or Team** | Row-level security applies. Actions controlled per user. |
| **Organization** | Access controlled at organization level only. |
| **None** | Some system tables (e.g., Privilege). |
| **Business Unit** | System tables only (Business Unit, Calendar, Team, Security Role). |

**Activity tables**: Primary field is always `Subject`. Cannot be organization-owned. Once saved, type and `Display in Activity Menus` setting cannot be changed.

---

## 3. Creating Tables

**Prerequisites**: Power Platform environment with Dataverse + System Customizer role + Create/Read/Write on Entity table.

**Creation methods**:
- Start with Copilot (natural language)
- Import from Excel/CSV
- Import from SharePoint list (preview)
- Start from blank (Set advanced properties)
- Create a virtual table

**Key table properties**:

| Property | Notes |
|---|---|
| Display Name / Plural Name | Can be changed later |
| Schema Name | Includes publisher prefix. Cannot change after save. |
| Type | Standard, Activity, Virtual, Elastic |
| Record Ownership | User/Team or Organization |
| Enable Attachments | Append notes and files |
| Track Changes | Required for Azure Synapse Link |
| Audit Changes | Log changes to records over time |
| Primary Column | Used in lookups. Display name cannot change after save. |

**Data workspace limitations** (visual designer): Cannot create Rich Text, Customer, Autonumber, or Formula columns. Many-to-many relationships not supported between new tables.

---

## 4. Table Properties

Tables model business data. Standard tables follow best practices for common scenarios. Custom tables extend functionality for organization-specific needs. All table components accessible via the table hub: Columns, Relationships, Keys, Forms, Views, Charts, Dashboards, Business Rules, Commands.

---

## 5. Creating & Editing Columns

**Column properties**:

| Property | Description |
|---|---|
| Display Name | Text shown in UI |
| Name | Unique schema name with publisher prefix. Cannot change after creation. |
| Data Type | Controls storage and formatting. Cannot change after save (except Text to Autonumber). |
| Required | `SystemRequired` (API-enforced), `BusinessRequired` (app-enforced), `Optional` |
| Searchable | Appears in Advanced Find and view customization |
| Column Security | Field-level security to control access |

**Requirement levels**: `SystemRequired` columns enforced by web services. `BusinessRequired` enforced by apps only; can be overridden programmatically.

---

## 6. Column Data Types

### Complete Type Mapping

| Power Apps Type | Solution Explorer Type | API Type |
|---|---|---|
| Text | Single Line of Text (Text format) | `StringType` |
| Text Area | Single Line of Text (Text Area format) | `StringType` |
| Email | Single Line of Text (Email format) | `StringType` |
| URL | Single Line of Text (URL format) | `StringType` |
| Phone | Single Line of Text (Phone format) | `StringType` |
| Ticker Symbol | Single Line of Text (Ticker format) | `StringType` |
| Multiline Text | Multiple Lines of Text | `MemoType` |
| Whole Number | Whole Number (None format) | `IntegerType` |
| Duration | Whole Number (Duration format) | `IntegerType` |
| Timezone | Whole Number (Time Zone format) | `IntegerType` |
| Language | Whole Number (Language format) | `IntegerType` |
| Decimal Number | Decimal Number | `DecimalType` |
| Floating Point Number | Floating Point Number | `DoubleType` |
| Currency | Currency | `MoneyType` |
| Date and Time | Date and Time (Date and Time format) | `DateTimeType` |
| Date Only | Date and Time (Date Only format) | `DateTimeType` |
| Choice | Option Set | `PicklistType` |
| Choices | MultiSelect Field | `MultiSelectPicklistType` |
| Yes/No | Two Options | `BooleanType` |
| Lookup | Lookup | `LookupType` |
| Customer | Customer | `CustomerType` |
| Owner | Owner | `OwnerType` |
| Image | Image | `ImageType` |
| File | File | `FileType` |
| Formula | Formula (Power Fx) | - |
| Unique Identifier | Primary Key | `UniqueidentifierType` |
| Status | Status | `StateType` |
| Status Reason | Status Reason | `StatusType` |
| Big Integer | Time Stamp | `BigIntType` |

### Text Column Limits

| Type | Default Max | Absolute Max |
|---|---|---|
| Text | 100 | 4,000 characters |
| Text Area | 100 | 4,000 characters |
| Multiline Text | 150 | 1,048,576 characters |

### Number Types Guide

| Type | Use Case | Precision |
|---|---|---|
| Whole Number | Exact integers | Max ~2.1 billion |
| Decimal Number | Exact decimals | Up to 10 decimal points |
| Floating Point | Approximate values, comparisons | Up to 5 decimal points |
| Currency | Money values | Configurable (Pricing, Currency, or 0-4 specific) |
| Big Integer | Timestamps, very large numbers | Max 9,223,372,036,854,775,807 |

> Limitation: Canvas/model-driven apps handle up to 15 digits precisely. BigInt not supported in canvas/model-driven apps.

### Lookup Types

| Type | Description |
|---|---|
| Simple | Single reference to one table type. All custom lookups. |
| Customer | Reference to Account or Contact. |
| Owner | Reference to User or Team. |
| PartyList | Multiple references to multiple tables (e.g., Email To/Cc). |
| Regarding | Single reference to multiple table types (activity regarding). |

### Searchable/Sortable Constraints

**Cannot be searched**: Formula, Image, PartyList (multivalue lookup).
**Cannot be sorted**: Choices (multi-select), Customer, File, Formula, Image, PartyList.

---

## 7. Relationships Overview

Two fundamental types: **One-to-Many (1:N)** and **Many-to-Many (N:N)**. N:1 is just 1:N viewed from the related table.

### Cascading Behaviors

| Action | Available Options |
|---|---|
| Assign | Cascade All, Active, User-Owned, None |
| Delete | Cascade All, Remove Link, Restrict |
| Reparent | Cascade All, Active, User-Owned, None |
| Share | Cascade All, Active, User-Owned, None |
| Unshare | Cascade All, Active, User-Owned, None |
| Merge | Cascade All, None |

### Parental vs Non-Parental

Parental relationships use Cascade All/Active/User-Owned for Assign, Delete (Cascade All only), Reparent, Share, Unshare. Only one parental relationship per table pair typically.

**Key limitation**: Custom table cannot be primary in a parental cascade with a related system table.

---

## 8. One-to-Many Relationships

Created by adding a lookup column to a table. Ways to create: Power Apps designer, form editor (add Lookup column), import solution, Power Query, or Metadata services API.

**Key consideration**: Evaluate existing relationships before creating custom ones to avoid redundancy.

---

## 9. Many-to-Many Relationships

Uses an **intersect (relationship) table** automatically created by the system. No lookup columns or cascading behaviors to configure. Rows are peers in reciprocal relationships.

**Limitations**: Cannot add custom columns to the intersect table. Not all tables are eligible. Intersect table is never visible in UI.

---

## 10. Alternate Keys

Alternate keys provide efficient data integration when external systems do not store Dataverse GUIDs.

**Supported column types for keys**: Single Line of Text, Whole Number, Decimal Number, DateTime, Lookup.

**Character restrictions**: Keys with `/`, `#`, `<`, `>`, `*`, `%`, `&`, `:`, `\\`, `?`, `+` in data will break GET/PATCH operations.

**Creation**: Select one or more columns. A system job creates database indexes after save. Key is not immediately available.

---

## 11. Import & Export Data

**Import sources**: Excel, CSV, SharePoint list, connectors (Azure, SQL Server, OData, etc.).

**Export**: Single table to CSV format. 12-minute time limit; export smaller segments if exceeded.

**Uniqueness**: Use primary key (GUID) or alternate keys for upsert logic.

**Unsupported data types for import/export**: Timezone, Choices (multi-select), Image, File.

**Unsupported system fields**: `Ownerid`, `Createdby`, `Createdonbehalfby`, `Createdon`, `Modifiedby`, `Modifiedonbehalfby`, `Modifiedon`, `Overriddencreatedon`.

**New import (preview)**: Assisted mapping with vector-based search, sheet selection, async ingestion, downloadable error logs.

---

## 12. Choices (Option Sets)

**Local choice**: Defined within a single column. Use when options apply to one place only.
**Global choice**: Shared across multiple columns/tables. Maintain in one place.

**Single select** = Choice column. **Multi-select** = Choices column.

**Choices limitations**: Cannot be used with workflows, BPFs, actions, dialogs, business rules, charts, rollup columns, or calculated columns. Not supported in Bulk Edit or Legacy forms.

---

## 13. Calculated & Rollup Columns

### Calculated Columns

Computed in real-time based on formulas using current table or related parent table columns.

**Supported data types**: Text, Choice, Yes/No, Whole Number, Decimal Number, Currency, Date Time.

**Available functions**: ADDHOURS, ADDDAYS, ADDWEEKS, ADDMONTHS, ADDYEARS, SUBTRACTHOURS, SUBTRACTDAYS, SUBTRACTWEEKS, SUBTRACTMONTHS, SUBTRACTYEARS, DIFFINDAYS, DIFFINHOURS, DIFFINMINUTES, DIFFINMONTHS, DIFFINWEEKS, DIFFINYEARS, CONCAT, TRIMLEFT, TRIMRIGHT.

**Limitations**:
- Max 5 chained calculated columns
- Cannot reference itself or create cyclic chains
- Max 50 unique calculated columns per saved query/chart/visualization
- Cannot trigger workflows or plugins
- Cannot span more than 2 tables
- Cannot change existing simple column to calculated
- Sorting disabled on columns referencing parent rows, logical columns, other calculated columns, or `Now()`

### Rollup Columns

Aggregate values from related child rows. Computed asynchronously by system jobs.

**Aggregate functions**: SUM, COUNT, MIN, MAX, AVG.

**System jobs**:
- `Mass Calculate Rollup Field`: Runs once after creation/update (12-hour delay). Recalculates all existing rows.
- `Calculate Rollup Field`: Incremental, runs hourly by default. One per table.

**Accessory columns**: Each rollup creates `_date` (DateTime) and `_state` (Integer: 0=NotCalculated, 1=Calculated, 2=OverflowError, etc.).

**Limitations**:
- Max 200 per environment, 50 per table (configurable)
- Cannot trigger workflows
- Cannot roll up over rollup columns
- Only works with 1:N relationships (not N:N)
- Online recalculation limited to 50,000 related rows
- Max hierarchy depth: 10

---

## 14. Formula Columns (Power Fx)

Formula columns use Power Fx syntax (similar to Excel) and are evaluated at fetch time.

**Supported output types**: Text, Decimal Number, Whole Number, Float, Boolean (Yes/No), Choice, DateTime.

**Not supported**: Currency output type.

**Key operators**: +, -, *, /, %, in, exactin, &

**Limitations**:
- Max formula length: 1,000 characters
- Max depth (chain of formula/rollup references): 10
- Cannot reference itself or create cyclic chains
- Cannot trigger workflows or plugins
- Duplicate detection rules not triggered
- Currency columns require `Decimal()` wrapper function
- String format columns (Email, URL, Text Area, Ticker Symbol) not supported
- Whole Number formats (Duration, Language, Time Zone) not supported
- No mobile offline support
- Range: -100,000,000,000 to 100,000,000,000 for decimal types
- Null numeric values treated as 0 (unlike calculated columns which return null)

**AI formula suggestions** (preview): Describe formula in natural language, get GPT-generated Power Fx.

---

## 15. Virtual Tables

External data displayed in Dataverse without replication. Three components: data provider, data source row, virtual table definition.

**Built-in provider**: OData v4 Data Provider (outbound port 443).

**Virtual table columns require**: `External Name` mapping. For choice columns: `External Type Name` and `External Value`.

**Restrictions**:
- Cannot convert existing tables to virtual
- Only Name and Id system columns by default
- No Currency, Image, or Customer column types
- No auditing, change tracking, mobile offline, Dataverse search
- No business process flows, queues, duplicate detection
- Organization-owned only (no row-level security)
- No rollup or calculated columns
- Column validation (min/max) not enforced
- Cannot be activity tables

---

## 16. Elastic Tables (Azure Cosmos DB)

Designed for high-volume, high-throughput scenarios (tens of millions of rows/hour).

**Unique features**:
- Horizontal auto-scaling
- Time-to-live (TTL) automatic data removal (set in seconds per row)
- Flexible schema with JSON columns
- Included with Dataverse log capacity

**Supported features**: CRUD + bulk operations, 1:N relationships, N:1 (when N is standard), ownership (user or org), field-level security, change tracking, auditing, mobile offline, Dataverse search, file columns.

**Not supported**:
- Business rules, charts, BPFs
- N:N relationships to standard tables
- Alternate keys, duplicate detection
- Calculated/rollup columns, currency columns, formula columns
- Cascade operations (Delete, Reparent, Assign, Share, Unshare)
- Multi-record transactions (plugin errors do not roll back creates)
- Filters on related tables in queries
- Table sharing, composite indexes
- Whole Number formats: Duration, Language, Time Zone
- Customer lookup type
- Import/export of table data

**Consistency**: Strong consistency only within a logical session. Eventual consistency otherwise.

---

## 17. Solutions Overview

Solutions transport apps and components between environments (ALM mechanism).

**Types**: Managed (locked, production deployment) and Unmanaged (development/customization).

**Default solutions**: `Common Data Service Default Solution` (maker customizations), `Default Solution` (all system components).

**Solution components**: Tables, columns, relationships, forms, views, charts, dashboards, BPFs, flows, web resources, choices, site maps, security roles, etc.

**Key concepts**: Solution publisher (controls schema prefix), solution layering, managed properties (control customizability), dependencies.

**Operations**: Create, import, export, deploy (via pipelines), publish, upgrade/update/patch.

**Git integration**: Sync solutions to Azure DevOps Git repositories for source control.

---

## 18. File Columns

Optimized for binary data storage outside relational data store.

| Property | Value |
|---|---|
| Default max size | 32 MB (32,768 KB) |
| Maximum configurable size | 10 GB (10,485,760 KB) |
| Single request upload limit | 128 MB (chunking required above this) |
| Max size change after creation | Only via API, not designer |

**Storage**: File blob storage (not relational). Reduces capacity usage.

**BYOK restriction**: Files limited to 128 MB. Stored in relational storage instead of blob.

**Not supported with**: Business process flows, business rules, charts, rollup columns, calculated columns. Required field validation does not work.

---

## 19. Image Columns

Optimized for image binary data, stored outside relational data store.

| Property | Value |
|---|---|
| Default max size | 10 MB (10,240 KB) |
| Maximum configurable size | 30 MB (30,720 KB) |
| Thumbnail dimensions | Always 144 x 144 px (cropped square) |
| Supported upload formats | jpg, jpeg, gif, bmp, png |
| Stored format | Converted to .jpg |

**Primary image**: One per table. Displayed in upper-right corner of model-driven app forms. Set via `IsPrimaryImage` property.

**`CanStoreFullImage`**: When false, only thumbnails stored. Full images stored in Azure blob.

**Limitations**: Same as file columns regarding business rules, BPFs, charts, rollup/calculated columns.

---

## 20. Date/Time Behavior & Format

### Behavior Types

| Behavior | Storage | Display | Use Case |
|---|---|---|---|
| **User Local** | UTC with conversion | Adjusted to user's time zone | Default for Date and Time format |
| **Time Zone Independent** | UTC without conversion | Same value for all users | Hotel check-in times |
| **Date Only** | Date portion only (no time) | Same date for all users | Birthdays, anniversaries |

### Behavior Change Rules

- User Local can be changed to Date Only or TZ Independent (one-time, irreversible)
- Existing values remain as UTC; may need developer conversion
- `CanChangeDateTimeBehavior` managed property can prevent changes
- Changes affect only new/modified values after the change

### Date Only Query Restrictions

These operators are **invalid** for Date Only behavior:
- Older Than X Minutes / Hours
- Last X Hours
- Next X Hours

### Display Examples (stored value: `2023-10-15T07:30:00Z`, user in UTC-8)

| Behavior | Format | Displayed As |
|---|---|---|
| User Local | Date and Time | October 14, 2023, 11:30 PM |
| User Local | Date Only | October 14, 2023 |
| TZ Independent | Date and Time | October 15, 2023, 7:30 AM |
| TZ Independent | Date Only | October 15, 2023 |
| Date Only | - | October 15, 2023 |

> Warning: Avoid Date Only format with User Local behavior. Users in different time zones may see different dates.

---

## Key Patterns & Best Practices

### Table Design
1. **Choose ownership type carefully** -- cannot change after creation. Use User/Team for row-level security needs.
2. **Use standard tables first** -- check if existing tables meet requirements before creating custom ones.
3. **Activity tables** are special -- always owned by user/team, primary field is always Subject, cannot change type after save.
4. **Enable Track Changes** on tables that will use Azure Synapse Link or data sync features.

### Column Design
5. **Data type is immutable** after save (except Text to Autonumber). Plan column types carefully.
6. **Schema name** includes publisher prefix and cannot change. Use meaningful names.
7. **Choose the right number type**: Decimal for exact calculations/reporting, Float for approximate comparisons, Currency for money.
8. **Global choices** for shared option sets across multiple columns; **local choices** for single-use options.
9. **Formula columns** (Power Fx) are preferred over calculated columns for new development -- evaluated at fetch time with richer function support.

### Relationship Design
10. **1:N relationships** are the foundation -- created automatically when adding lookup columns.
11. **N:N relationships** use hidden intersect tables -- no custom columns, no cascading behaviors.
12. **Configure cascading behaviors** thoughtfully -- parental cascades affect delete, assign, share, reparent, unshare operations.
13. **Restrict delete** to prevent orphaned records when referential integrity is critical.

### Performance & Scale
14. **Elastic tables** for datasets exceeding tens of millions of rows -- accept eventual consistency and limited features.
15. **Virtual tables** for real-time external data without replication -- accept no offline, no security, no auditing.
16. **File/Image columns** store binary data outside relational storage -- reduces capacity, improves performance.
17. **Rollup columns** run on scheduled jobs -- not real-time. Design dashboards accordingly.

### Data Integration
18. **Alternate keys** are essential for integration with systems that do not use GUIDs.
19. **Import/export** does not support Timezone, Choices (multi-select), Image, or File columns.
20. **Solutions** are the ALM mechanism -- always develop in unmanaged solutions, deploy as managed.
