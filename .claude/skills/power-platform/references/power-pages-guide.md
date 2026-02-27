# Power Pages Reference Guide

## Overview

Power Pages is a secure, enterprise-grade, low-code SaaS platform for creating external-facing business websites. Built on the ASP.NET portal engine (successor to Power Apps Portals), it uses Dataverse as its shared data store.

**Key characteristics:**
- Low-code design studio for makers and pro developers
- External-facing sites (customers, partners, communities)
- Built-in security, authentication, and table permissions
- Liquid templating engine for dynamic content
- Progressive Web App (PWA) support
- Copilot AI-assisted site building

## Site Creation

1. Navigate to `make.powerpages.microsoft.com`
2. Select a Dataverse environment (avoid the default environment)
3. Choose a template (business-specific, starter layout, or blank)
4. Preview across device form factors
5. Set site name and web address

### Required Roles

- Read-Write Access Mode user account
- System Administrator role
- Permissions to register an app in Microsoft Entra
- If site creation is disabled: Dynamics 365 Administrator or Power Platform Administrator

## Web Pages

Pages represent URLs and form the site hierarchy through parent-child relationships.

### Key Attributes

| Attribute | Description |
|-----------|-------------|
| Name | Page title (required) |
| Partial URL | URL path segment; root page must be `/` |
| Page Template | Controls rendering (required) |
| Publishing State | Published/Draft workflow |
| Parent Page | Hierarchy position |
| Hidden from Sitemap | Hides from nav; URL stays accessible |
| Display Order | Integer controlling sibling sort |

### Design Studio Page Management

- Add pages via Pages workspace with **+ Page**
- Choose blank layout or Copilot-generated
- Add components: Text, Spacer, Button, Image, List, Form, Multistep Form
- Move pages between Main Navigation and Other Pages
- Make subpages to create hierarchy; URL reflects nesting

## Lists (Entity Lists)

Display Dataverse records in a grid format without custom code.

- Select a Dataverse table and one or more model-driven app views
- Grid supports sorting and pagination (configurable page size)
- Multiple views render as a dropdown for user switching
- **Web Page for Details View** links records to detail pages
- Detail form mode (read-only/edit) determined by form config and table permissions
- Filtering by current portal user, parent account, or website

**Liquid inclusion:**
```liquid
{% include 'entity_list' key: '<<list name>>' %}
```

## Basic Forms (Entity Forms)

Collect or display data from a single Dataverse table record.

### Form Modes

| Mode | Purpose |
|------|---------|
| Insert | Create a new record |
| Edit | Modify an existing record |
| ReadOnly | Display without editing |

### Record Source Types

- **Query String** -- record ID via URL parameter
- **Current Portal User** -- logged-in user's contact record
- **Record Associated to Current Portal User** -- related record via relationship

### Features

- Captcha support, file attachments (Note or Azure Blob Storage)
- Geolocation with map control, custom JavaScript injection
- On Success: display message or redirect
- Actions: Delete, Workflow, Create Related Record, Activate, Deactivate
- Table permissions required for CRUD access

**Liquid inclusion:**
```liquid
{% entityform name: '<<basic form name>>' %}
```

## Multistep Forms (Web Forms)

Collect data across multiple sequential steps with session tracking.

### Step Types

| Type | Description |
|------|-------------|
| Load Form | Renders a Dataverse form for data entry |
| Load Tab | Loads a specific form tab |
| Condition | Evaluates an expression to branch flow |
| Redirect | Navigates to a URL or web page |

### Features

- Conditional branching based on user input
- Session persistence -- users can resume where they left off
- Progress indicators: Title, Numeric (Step x of n), Progress Bar
- Authentication Required option; Multiple Records Per User Permitted
- Edit Expired State/Status prevents editing completed records

**Liquid inclusion:**
```liquid
{% webform name: '<<My Multistep Form>>' %}
```

## Templates

### Page Templates

Bridge web pages to rendering logic. Two types:

| Type | Description |
|------|-------------|
| Rewrite | Points to a physical ASP.NET `.aspx` page |
| Web Template | Points to a Liquid-based web template record |

### Web Templates

Store Liquid source content as Dataverse records. Primary mechanism for custom layouts.

| Attribute | Description |
|-----------|-------------|
| Name | Used in `{% include %}` and `{% extends %}` |
| Source | Liquid/HTML template code |
| MIME Type | Defaults to `text/html`; set to other types for non-HTML output |

### Built-in Templates

- `layout_1_column` / `layout_2_column_wide_left` -- page layouts via `{% extends %}`
- `breadcrumbs`, `page_copy`, `top_navigation`, `side_navigation`, `search` -- via `{% include %}`
- `snippet` -- `{% include 'snippet' snippet_name:'Name' %}`
- Header/Footer can be overridden on the website record

## Liquid Templating

Open-source template language for dynamic content rendering.

### Syntax

| Type | Syntax | Purpose |
|------|--------|---------|
| Output | `{{ variable }}` | Render values |
| Tags | `{% tag %}` | Logic and control flow |
| Filters | `{{ value \| filter }}` | Transform output |
| Whitespace | `{%- tag -%}` | Strip whitespace |

### Key Objects

| Object | Description |
|--------|-------------|
| `page` | Current page (title, url, breadcrumbs, children, Dataverse attributes) |
| `user` | Current authenticated user (contact record); null if anonymous |
| `request` | HTTP request (params, path, url, query) |
| `entities` | Load any Dataverse table by ID |
| `settings` | Load site settings by name |
| `sitemap` | Site map (root, current, navigation nodes) |
| `sitemarkers` | Load site markers by name |
| `snippets` | Load content snippets by name |
| `weblinks` | Load web link sets by name or ID |
| `now` | Current UTC date/time |

### FetchXML Queries

```liquid
{% fetchxml query %}
<fetch version="1.0" mapping="logical">
  <entity name="contact">
    <attribute name="fullname"/>
    <attribute name="emailaddress1"/>
  </entity>
</fetch>
{% endfetchxml %}
{% for contact in query.results.entities %}
  {{ contact.fullname | escape }}
{% endfor %}
```

### Common Filters

- **Array:** batch, concat, where, except, order_by, group_by, first, last, join, size, skip, take, shuffle
- **String:** append, prepend, upcase, downcase, capitalize, remove, replace, split, strip_html, truncate
- **Math:** plus, minus, times, divided_by, modulo, ceil, floor, round
- **Date:** date (format), date_add_days/hours/minutes/months/seconds/years, date_to_iso8601
- **Escape:** escape (HTML), url_escape, xml_escape
- **URL:** add_query, remove_query, base, host, path, port, scheme
- **Type:** boolean, decimal, integer, string
- **Special:** default, file_size, has_role, liquid (render string as Liquid code)

### Entity Permissions in Liquid

```liquid
{% if entity.permissions.can_read %}
  {{ entity.name | escape }}
{% endif %}
```

### Content Snippets

Reusable content blocks (Text or HTML) managed in Dataverse:
```liquid
{{ snippets['Header'] }}
```

## Security

### Authentication

Uses Dataverse contact records for site users with ASP.NET Identity framework.

| Provider | Protocol |
|----------|----------|
| Microsoft Entra ID | OpenID Connect, SAML 2.0, WS-Federation |
| Azure AD B2C | OpenID Connect |
| AD FS | SAML 2.0, WS-Federation |
| Microsoft, LinkedIn, Facebook, Google, Twitter | OAuth 2.0 |
| Local authentication | Username/password (not recommended) |

- Open registration allows sign-up without invitation codes
- Registration creates a Dataverse contact record
- Users assigned web roles for permissions beyond anonymous access

### Table Permissions

Control access to Dataverse records displayed via forms, lists, Liquid, and Web API.

| Access Type | Scope |
|-------------|-------|
| Global | All records of the table |
| Contact | Records associated with signed-in user |
| Account | Records associated with user's parent account |
| Self | Only the user's own contact record |

- Assign CRUD privileges: Create, Read, Write, Delete, Append, AppendTo
- Associate with web roles (Authenticated Users, Anonymous Users, custom)
- Support parent-child permission hierarchies

### Page Security

| Rule Type | Effect |
|-----------|--------|
| Restrict Read | Limits page viewing to users with specific web roles |
| Grant Change | Allows content publishing for users with specific web roles |

- Child pages inherit parent permissions by default
- Grant Change takes precedence over Restrict Read
- Do not restrict home page child files (breaks CSS/JS loading)

### Web API

REST endpoints for client-side CRUD operations against Dataverse tables.

**Endpoint pattern:**
```
[Portal URI]/_api/<EntitySetName>
[Portal URI]/_api/<EntitySetName>(<GUID>)
```

| Operation | HTTP Method |
|-----------|-------------|
| Create | POST |
| Read | GET |
| Update | PATCH |
| Delete | DELETE |
| Associate/Disassociate | POST/DELETE to $ref |

- Uses `__RequestVerificationToken` for CSRF protection
- Authenticated via portal session
- Table permissions govern record access
- Requires explicit site settings per table to enable operations

## PWA Support

Power Pages sites can be enabled as Progressive Web Apps.

- Cross-platform: Android, iOS, Windows, Chromebooks
- Installable from browser or app stores
- Pin to home screen on mobile devices
- Offline support for selected pages (read-only content)
- Enable via **Set up** workspace in the design studio
