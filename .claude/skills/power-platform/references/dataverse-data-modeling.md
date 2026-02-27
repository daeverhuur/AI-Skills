# Dataverse Data Modeling Reference

> Distilled from research/04-dataverse-tables-columns.md
> Cross-references: dataverse-business-logic.md, dataverse-security-admin.md

---

## Terminology (Post-Nov 2020)

Entity = Table, Field/Attribute = Column, Record = Row, Option Set/Picklist = Choice, Two Options = Yes/No.
API names unchanged (e.g., `CreateEntityRequest`).

---

## Table Types

| Type | Storage | Key Characteristics |
|---|---|---|
| **Standard** | Dataverse relational | Default. Customizable when `IsCustomizable=true`. |
| **Activity** | Dataverse relational | Primary field always `Subject`. User/Team owned only. Cannot change type after save. |
| **Virtual** | External (runtime fetch) | No replication. OData v4 provider (port 443). Organization-owned only. |
| **Elastic** | Azure Cosmos DB | Auto-scaling. Tens of millions of rows. TTL support. Eventually consistent across sessions. |

### Table Ownership (immutable after creation)

| Ownership | Security Model | Use When |
|---|---|---|
| **User or Team** | Row-level security applies | Most business data requiring per-user access control |
| **Organization** | Org-level access only | Reference/config data visible to all |
| **None** | System tables only | Privilege table, etc. |
| **Business Unit** | System tables only | Business Unit, Calendar, Team, Security Role |

> See dataverse-security-admin.md for role-based security, BU hierarchy, column-level security.

---

## Column Data Types -- Complete Mapping

| Power Apps Type | API Type | Notes |
|---|---|---|
| Text | `StringType` | Max 4,000 chars. Default 100. |
| Text Area | `StringType` | Max 4,000 chars. Multiline display. |
| Email | `StringType` | Email format validation. |
| URL | `StringType` | URL format. |
| Phone | `StringType` | Phone format. |
| Ticker Symbol | `StringType` | Ticker format. |
| Multiline Text | `MemoType` | Max 1,048,576 chars. Default 150. |
| Whole Number | `IntegerType` | Max ~2.1B. Formats: None, Duration, Timezone, Language. |
| Duration | `IntegerType` | Whole Number with Duration format. |
| Timezone | `IntegerType` | Whole Number with Time Zone format. |
| Language | `IntegerType` | Whole Number with Language format. |
| Decimal Number | `DecimalType` | Up to 10 decimal places. Use for exact calculations. |
| Floating Point | `DoubleType` | Up to 5 decimal places. Approximate only. |
| Currency | `MoneyType` | Configurable precision (Pricing/Currency/0-4). |
| Date and Time | `DateTimeType` | Behaviors: User Local, TZ Independent, Date Only. |
| Date Only | `DateTimeType` | Date Only behavior variant. |
| Choice | `PicklistType` | Single-select option set. |
| Choices | `MultiSelectPicklistType` | Multi-select. Cannot sort, chart, rollup, or use in BPFs. |
| Yes/No | `BooleanType` | Two-option field. |
| Lookup | `LookupType` | 1:N relationship reference. |
| Customer | `CustomerType` | Polymorphic: Account or Contact. |
| Owner | `OwnerType` | Polymorphic: User or Team. |
| Image | `ImageType` | Max 30 MB. Stored as .jpg. Thumbnail always 144x144. |
| File | `FileType` | Max 10 GB configurable (default 32 MB). Blob storage. |
| Formula | Power Fx | Evaluated at fetch time. Max 1,000 chars. No Currency output. |
| Unique Identifier | `UniqueidentifierType` | Primary key (GUID). |
| Status | `StateType` | Active/Inactive state. |
| Status Reason | `StatusType` | Substatus linked to Status. |
| Big Integer | `BigIntType` | Max 9.2 quintillion. Not supported in canvas/MDA apps. |

### Number Type Decision Guide

| Need | Use | Why |
|---|---|---|
| Exact integer values | Whole Number | No rounding. ~2.1B max. |
| Exact decimal calculations/reporting | Decimal Number | 10 decimal places. No floating point errors. |
| Approximate comparisons, scientific | Floating Point | 5 decimal places. Faster but imprecise. |
| Money values | Currency | Linked to currency table. Configurable precision. |
| Very large numbers / timestamps | Big Integer | API-only access in apps. |

> Apps handle max 15 digits precisely. BigInt exceeds this -- API use only.

### Lookup Subtypes

| Subtype | Targets | Created By |
|---|---|---|
| Simple | One table | Custom lookups (most common) |
| Customer | Account or Contact | System column type |
| Owner | User or Team | System column type |
| PartyList | Multiple tables, multiple refs | Activity fields (To, Cc, Bcc) |
| Regarding | Multiple tables, single ref | Activity regarding field |

---

## Immutable Schema Decisions

These CANNOT be changed after creation/save:

| Decision | Consequence |
|---|---|
| Table ownership type | Determines security model forever |
| Column data type | Locked after save (exception: Text to Autonumber) |
| Column schema name | Includes publisher prefix, permanent |
| Table schema name | Includes publisher prefix, permanent |
| Activity table type | Cannot convert to/from Activity |
| Activity `Display in Activity Menus` | Locked after first save |
| DateTime behavior change | User Local to Date Only/TZ Independent is one-time, irreversible |

---

## Relationships

### One-to-Many (1:N)

Created automatically when adding a Lookup column. The lookup column lives on the "many" side.
Always check existing relationships before creating custom ones.

### Many-to-Many (N:N)

System creates a hidden intersect table. Key constraints:
- **No custom columns** on intersect table
- **No cascading behaviors** -- rows are peers
- Not all tables eligible
- Intersect table invisible in UI

### Cascading Behaviors (1:N only)

| Action | Options |
|---|---|
| Assign | Cascade All, Active, User-Owned, None |
| Delete | **Cascade All, Remove Link, Restrict** |
| Reparent | Cascade All, Active, User-Owned, None |
| Share | Cascade All, Active, User-Owned, None |
| Unshare | Cascade All, Active, User-Owned, None |
| Merge | Cascade All, None |

**Parental** relationships cascade All/Active/User-Owned across assign, delete, reparent, share, unshare.
**Restrict delete** = prevent parent deletion while children exist (referential integrity).
**Remove Link** = null the lookup on children when parent deleted.

> Constraint: Custom table cannot be primary in parental cascade with a related system table.

> See dataverse-business-logic.md for business rules and plug-ins that fire on relationship changes.

---

## Alternate Keys

Enable upsert by external ID instead of GUID. Essential for integration scenarios.

**Eligible column types**: Single Line of Text, Whole Number, Decimal Number, DateTime, Lookup.

**Character restrictions in key values**: `/`, `#`, `<`, `>`, `*`, `%`, `&`, `:`, `\\`, `?`, `+` break GET/PATCH.

After creation, a system job builds database indexes -- key is not immediately available.

---

## Computed Columns Comparison

| Feature | Calculated | Rollup | Formula (Power Fx) |
|---|---|---|---|
| Evaluation | Real-time | Async (hourly default) | At fetch time |
| Scope | Current row + parent | Child rows (1:N) | Current row + related |
| Functions | Date math, CONCAT, TRIM | SUM, COUNT, MIN, MAX, AVG | Full Power Fx |
| Max chain depth | 5 | N/A (no chaining) | 10 |
| Output types | Text, Choice, Yes/No, Number, Currency, DateTime | Number, Currency, DateTime | Text, Number, Float, Bool, Choice, DateTime (no Currency) |
| Triggers workflows/plugins | No | No | No |
| Limits | 50 per query/chart | 200/env, 50/table | 1,000 char formula |
| Null handling | Returns null | Returns null | Null numeric = 0 |

**Prefer Formula columns** for new development -- richer function set, Power Fx syntax.

### Rollup Specifics
- `_date` and `_state` accessory columns created automatically
- State values: 0=NotCalculated, 1=Calculated, 2=OverflowError
- Mass Calculate job: 12-hour delay after creation, recalculates all rows
- Online recalculation: max 50,000 related rows
- Only works with 1:N (not N:N)

---

## DateTime Behavior

| Behavior | Storage | Display | Use Case |
|---|---|---|---|
| User Local | UTC + conversion | User's timezone | Default. Meetings, deadlines. |
| TZ Independent | UTC raw | Same everywhere | Hotel check-in, scheduled events. |
| Date Only | Date only (no time) | Same everywhere | Birthdays, anniversaries. |

**Behavior change**: User Local can convert to Date Only or TZ Independent (one-way, irreversible).
Existing values stay as UTC -- may need developer migration.
`CanChangeDateTimeBehavior` managed property can lock behavior.

---

## Virtual Table Constraints

No: Currency/Image/Customer columns, auditing, change tracking, mobile offline, Dataverse search, BPFs, queues, duplicate detection, rollup/calculated columns, row-level security, activity tables.
Organization-owned only. Columns require `External Name` mapping.

---

## Elastic Table Constraints

No: Business rules, charts, BPFs, N:N to standard, alternate keys, duplicate detection, calculated/rollup/formula/currency columns, cascade operations, multi-record transactions, composite indexes, import/export.
Supported: CRUD, bulk ops, 1:N, ownership, field-level security, change tracking, auditing, file columns.
Strong consistency within logical session only.

---

## File & Image Columns

| Property | File | Image |
|---|---|---|
| Default max | 32 MB | 10 MB |
| Configurable max | 10 GB | 30 MB |
| Storage | Blob (outside relational) | Blob (outside relational) |
| Upload limit | 128 MB per request (chunk above) | -- |
| Formats | Any | jpg, jpeg, gif, bmp, png (stored as .jpg) |
| Primary per table | N/A | One (shown on MDA forms) |

Not supported with: BPFs, business rules, charts, rollup, calculated columns.
BYOK: Files limited to 128 MB, stored in relational instead of blob.

---

## Choices (Option Sets)

- **Local**: Single column use. Defined inline.
- **Global**: Shared across columns/tables. Maintain centrally.
- **Multi-select (Choices)**: Cannot use in workflows, BPFs, business rules, charts, rollup, calculated columns, bulk edit.

---

## Import/Export Constraints

**Unsupported types**: Timezone, Choices (multi-select), Image, File.
**Unsupported system fields**: Ownerid, Createdby, Createdonbehalfby, Createdon, Modifiedby, Modifiedonbehalfby, Modifiedon, Overriddencreatedon.
Export: CSV only, 12-minute time limit.
Upsert: Uses primary key (GUID) or alternate keys.

---

## Schema Design Checklist

1. **Ownership**: Decide User/Team vs Organization before creation -- cannot change
2. **Standard first**: Check existing tables before creating custom
3. **Column types**: Plan carefully -- immutable after save
4. **Schema names**: Use meaningful names with proper publisher prefix -- permanent
5. **Number types**: Decimal for exact, Float for approximate, Currency for money
6. **Choices scope**: Global for reuse, Local for single-use
7. **Relationships**: 1:N via Lookup (configurable cascade), N:N for peer associations (no cascade, no custom columns)
8. **Cascade delete**: Restrict for referential integrity, Remove Link for soft references
9. **Alternate keys**: Define early for integration endpoints
10. **Computed columns**: Formula (Power Fx) over Calculated for new work
11. **DateTime behavior**: Choose at creation -- conversion is one-way
12. **Track Changes**: Enable on tables needing Synapse Link or sync
13. **Elastic/Virtual**: Accept feature trade-offs -- review constraints above

> See dataverse-business-logic.md for business rules, plug-ins, workflows, BPFs.
> See dataverse-security-admin.md for roles, BU hierarchy, column security, environment admin.
