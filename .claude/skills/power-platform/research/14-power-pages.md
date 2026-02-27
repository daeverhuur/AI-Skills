# Power Pages

> Source: Microsoft Learn -- Power Pages documentation
> Retrieved: 2026-02-26

## 1. Overview

Power Pages is a secure, enterprise-grade, low-code SaaS platform for creating, hosting, and administering external-facing business websites. It is the newest member of Microsoft Power Platform and uses Microsoft Dataverse as its shared data store -- the same data used by Power Apps, Power Automate, Power Virtual Agents, and Power BI.

Key characteristics:
- Low-code design studio for makers and pro developers
- Builds on ASP.NET-based portal engine (successor to Power Apps Portals)
- Sites are external-facing (customers, partners, communities)
- Built-in security, authentication, and table permissions
- Liquid templating engine for dynamic content
- Progressive Web App (PWA) support
- Copilot AI-assisted site building

## 2. Site Creation and Management

### Creating a Site
1. Navigate to `make.powerpages.microsoft.com`
2. Select a Dataverse environment (avoid the default environment to prevent unintentional data sharing)
3. Choose **Start with a template** -- business-specific templates, starter layouts, or blank page
4. Preview templates across device form factors before selecting
5. Set site name and web address, then select **Done**

### Required Roles
- User account with Read-Write Access Mode
- System Administrator role
- Permissions to register an app in Microsoft Entra
- If site creation is disabled: Dynamics 365 Administrator or Power Platform Administrator role

### Site Settings
- Site name and URL are modifiable after creation
- Site metadata for all templates is preloaded as website records in the Portal Management app
- Each site is bound to a Dataverse environment via website bindings

## 3. Web Pages

A web page represents a URL in the site and forms the hierarchy (site map) through parent-child relationships. Other component types (web files, shortcuts, forms, blogs) derive URLs from their parent web page.

### Key Attributes
| Attribute | Description |
|-----------|-------------|
| Name | Page title (required) |
| Partial URL | URL path segment; root page must be `/` |
| Page Template | Controls rendering (required) |
| Publishing State | Published/Draft workflow control |
| Parent Page | Hierarchy position (only root has none) |
| Title | Optional override for display name |
| Summary | Short description for navigation elements |
| Copy | Main HTML content field |
| Hidden from Sitemap | Hides from nav but keeps URL accessible |
| Display Order | Integer controlling sibling sort order |

### Comment Policy Options
Inherit, Open, Open to Authenticated Users, Moderated, Closed, None.

### Design Studio Page Management
- Add pages via Pages workspace with **+ Page**
- Choose blank layout or use Copilot to generate
- Add components: Text, Spacer, Button, Image, List, Form, Multistep Form
- Move pages in sitemap (Main Navigation vs Other Pages)
- Make pages subpages to create hierarchy; URL reflects nesting

## 4. Lists (Entity Lists)

Lists display Dataverse records on a webpage in a grid format without custom code.

### Configuration
- Select a Dataverse table and one or more model-driven app views
- Grid supports sorting and pagination (configurable page size)
- Multiple views render as a dropdown for user switching
- Filtering by current portal user, parent account, or website
- **Web Page for Details View** links each record to a detail page with ID in query string
- Detail form mode (read-only/edit) determined by form configuration and table permissions

### Adding via Liquid
```liquid
{% include 'entity_list' key: '<<list name>>' %}
```

### Search, Filtering, and OData
- Search can be enabled per list
- Advanced attribute filtering via JSON filter definitions
- Data can be filtered by portal user, account, or website attributes

## 5. Basic Forms (Entity Forms)

Basic forms collect or display data from a single Dataverse table record.

### Form Modes
- **Insert** -- create a new record
- **Edit** -- modify an existing record
- **ReadOnly** -- display without editing

### Record Source Types
- **Query String** -- record ID passed via URL parameter
- **Current Portal User** -- logged-in user's contact record
- **Record Associated to Current Portal User** -- related record via relationship

### Key Features
- Captcha support (optional for authenticated users)
- Auto-generate steps from tabs
- Tooltips from attribute descriptions
- Validation summary with configurable CSS and links
- File attachments (Note or Azure Blob Storage)
- Custom JavaScript injection at form bottom
- Geolocation with map control
- On Success: display message or redirect (to URL or web page)
- Associated Table Reference for linking records across steps
- Actions: Delete, Workflow, Create Related Record, Activate, Deactivate

### Adding via Liquid
```liquid
{% entityform name: '<<basic form name>>' %}
```

### Security
Table permissions must be configured to control CRUD access. Forms without permissions show a warning that anyone on the internet can view the data.

## 6. Multistep Forms (Web Forms)

Multistep forms collect data across multiple sequential steps with session tracking.

### Features
- Break data collection into multiple steps
- Conditional branching based on user input
- Session persistence -- users can resume where they left off
- Progress indicators: Title, Numeric (Step x of n), Progress Bar
- Configurable position: Top, Bottom, Left, Right

### Step Types
| Type | Description |
|------|-------------|
| Load Form | Renders a Dataverse form for data entry |
| Load Tab | Loads a specific form tab |
| Condition | Evaluates an expression to branch flow |
| Redirect | Navigates to a URL or web page |

### Key Properties
- **Authentication Required** -- redirects anonymous users to sign-in
- **Start New Session On Load** -- forces fresh start vs resume
- **Multiple Records Per User Permitted** -- allows repeat submissions
- **Edit Expired State/Status** -- prevents editing completed records

### Conditional Steps
Configured in Portal Management app using logical column names and values:
```
craxx_degreetype == 124860001
```
Set **Next Step** for condition met, **Next Step If Condition Fails** for unmet.

### Adding via Liquid
```liquid
{% webform name: '<<My Multistep Form>>' %}
```

## 7. Page Templates

Page templates bridge web pages to their rendering logic. Two types:

| Type | Description |
|------|-------------|
| **Rewrite** | Points to a physical ASP.NET `.aspx` page |
| **Web Template** | Points to a Liquid-based web template record |

### Attributes
- Name, Website, Type, Rewrite URL or Web Template reference
- Is Default, Table Name (usually `adx_webpage`), Description

## 8. Web Templates

Web templates store Liquid source content as Dataverse records. They are the primary mechanism for custom layouts and dynamic rendering.

### Attributes
- **Name** -- used in `{% include %}` and `{% extends %}` tags
- **Source** -- Liquid/HTML template code
- **MIME Type** -- defaults to `text/html`; set to other types (e.g., `application/rss+xml`) for non-HTML output

### Use Cases
- Custom page layouts (via page template association)
- Custom headers and footers (set on Website record)
- Reusable components (include in other templates)
- Non-HTML content (RSS feeds, JSON, XML)

### Built-in Templates
| Template | Usage |
|----------|-------|
| Layout 1 Column | `{% extends 'layout_1_column' %}{% block main %}...{% endblock %}` |
| Layout 2 Column Wide Left | `{% extends 'layout_2_column_wide_left' %}{% block main %}...{% endblock %}{% block aside %}...{% endblock %}` |
| Breadcrumbs | `{% include 'breadcrumbs' %}` |
| Page Copy | `{% include 'page_copy' %}` |
| Top Navigation | `{% include 'top_navigation' %}` |
| Side Navigation | `{% include 'side_navigation' %}` |
| Search | `{% include 'search' %}` |
| Snippet | `{% include 'snippet' snippet_name:'Name' %}` |
| Child Link List Group | `{% include 'child_link_list_group' %}` |

### Header/Footer Override
Set **Header Template** or **Footer Template** on the website record to use a custom web template instead of the default.

## 9. Liquid Templating

Liquid is an open-source template language integrated into Power Pages for dynamic content rendering.

### Syntax Basics
- **Output**: `{{ variable }}` -- renders values
- **Tags**: `{% tag %}` -- logic and control flow
- **Filters**: `{{ value | filter }}` -- transform output
- **Whitespace control**: `{%- tag -%}` -- strips whitespace

### Key Liquid Objects
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
| `website` | Portal website record |
| `now` | Current UTC date/time |

### Accessing Dataverse Records
```liquid
{% assign account = entities.account['936DA01F-9ABD-4d9d-80C7-02AF85C822A8'] %}
{% if account %}
  {{ account.name | escape }}
{% endif %}
```

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
**Array**: batch, concat, where, except, order_by, then_by, select, group_by, first, last, join, size, skip, take, shuffle, random
**String**: append, prepend, upcase, downcase, capitalize, remove, replace, split, strip_html, strip_newlines, truncate, truncate_words, newline_to_br
**Math**: plus, minus, times, divided_by, modulo, ceil, floor, round
**Date**: date (format), date_add_days/hours/minutes/months/seconds/years, date_to_iso8601, date_to_rfc822
**Escape**: escape (HTML), url_escape, xml_escape, html_safe_escape
**URL**: add_query, remove_query, base, host, path, path_and_query, port, scheme
**Type**: boolean, decimal, integer, string
**Special**: default, file_size, has_role, liquid (render string as Liquid code)

### Entity Permissions in Liquid
```liquid
{% if entity.permissions.can_read %}
  {{ entity.name | escape }}
{% endif %}
```

## 10. Content Snippets

Reusable content blocks (Text or HTML) managed in Dataverse. Referenced in Liquid:
```liquid
{{ snippets['Header'] }}
{% assign footer = snippets['Footer'] %}
{% if footer %}{{ footer }}{% else %}No footer found.{% endif %}
```

## 11. Authentication

Power Pages uses Dataverse contact records for site users. ASP.NET Identity provides the authentication framework.

### Supported Identity Providers
| Provider | Protocol |
|----------|----------|
| Microsoft Entra ID | OpenID Connect, SAML 2.0, WS-Federation |
| Microsoft Entra External ID | OpenID Connect |
| Azure AD B2C | OpenID Connect |
| AD FS | SAML 2.0, WS-Federation |
| Microsoft | OAuth 2.0 |
| LinkedIn | OAuth 2.0 |
| Facebook | OAuth 2.0 |
| Google | OAuth 2.0 |
| Twitter | OAuth 2.0 |
| Local authentication | Username/password (not recommended) |

### Registration
- Open registration allows sign-up without invitation codes
- Users choose external identity or local account
- Registration creates a Dataverse contact record
- Users are assigned web roles for permissions beyond anonymous access

## 12. Table Permissions

Table permissions control access to Dataverse records displayed via forms, lists, Liquid, and Web API.

### Access Types
| Type | Scope |
|------|-------|
| **Global** | All records of the table |
| **Contact** | Records associated with signed-in user |
| **Account** | Records associated with user's parent account |
| **Self** | Only the user's own contact record |

### Configuration
- Assign CRUD privileges: Create, Read, Write, Delete, Append, AppendTo
- Associate with web roles (Authenticated Users, Anonymous Users, custom roles)
- Support parent-child permission hierarchies
- Child permissions inherit roles from parent
- Configure from design studio Security workspace, form/list components, or Portal Management app

## 13. Page Security

Page permissions control access to specific web pages and their children.

### Access Control Rule Types
| Type | Effect |
|------|--------|
| **Restrict Read** | Limits page viewing to users with specific web roles |
| **Grant Change** | Allows content publishing for users with specific web roles |

### Key Behaviors
- Child pages inherit parent permissions by default
- Grant Change rules take precedence over Restrict Read rules
- Web file permissions can inherit from parent page
- Scope options: All content, Exclude direct child web files
- Do not restrict home page child files (breaks CSS/JS loading)

## 14. Web API

The Power Pages Web API enables client-side CRUD operations against Dataverse tables using REST endpoints.

### Endpoint Pattern
```
[Portal URI]/_api/<EntitySetName>
[Portal URI]/_api/<EntitySetName>(<GUID>)
```

### Supported Operations
| Operation | HTTP Method |
|-----------|-------------|
| Create | POST |
| Read | GET |
| Update | PATCH |
| Update single property | PUT |
| Delete | DELETE |
| Associate | POST (to $ref) |
| Disassociate | DELETE (from $ref) |

### Site Settings to Enable
Web API requires explicit site settings per table to enable operations. Table permissions must also be configured.

### Security
- Uses `__RequestVerificationToken` for CSRF protection
- Authenticated via portal session
- Table permissions govern which records users can access
- Web roles must be correctly assigned

### AJAX Pattern
```javascript
webapi.safeAjax({
  type: "POST",
  url: "/_api/accounts",
  contentType: "application/json",
  data: JSON.stringify({ "name": "Sample Account" }),
  success: function (res, status, xhr) {
    console.log("entityID: " + xhr.getResponseHeader("entityid"));
  }
});
```

## 15. Progressive Web Apps (PWA)

Power Pages sites can be enabled as PWAs for native app-like experiences.

### Capabilities
- Cross-platform: Android, iOS, Windows, Chromebooks
- All form factors: mobile, desktop, tablet
- Installable from browser or app stores
- Pin to home screen on mobile devices
- Offline support for selected pages (read-only content)

### Configuration
Enable via the **Set up** workspace in the design studio. Select pages for offline availability.

## 16. Copilot (AI Features)

### For Makers
- **Create site** -- describe your site in natural language
- **Create webpage** -- AI-generated page layout and content
- **Create forms** -- describe data to collect; Copilot generates the form
- **Create multistep forms** -- AI-assisted multi-step form design
- **Generate text** -- AI-written content for pages
- **Color themes** -- AI-generated design themes
- **Ask Copilot** -- get answers about Power Pages capabilities

### For Developers
- **AI-generated code** -- Copilot writes Liquid/HTML/CSS/JS
- **Data summarization API** -- AI-powered data summaries

### For Site Users
- **AI-powered agent** -- conversational chatbot on the site
- **Generative AI search** -- natural language site search
- **AI form fill assistance** -- helps users complete forms
- **AI summary in lists** -- AI-generated record summaries

## 17. Administration

### Admin Center Access
Access via design studio **Set up** workspace > **Open admin center**, or directly from Power Platform admin center > Resources > Power Pages sites.

### Site Actions
- Restart, Shut down, Delete site
- Disable custom errors, Enable diagnostic logs
- Enable maintenance mode
- Manage Dynamics 365 instance
- Import metadata translations

### Site Configuration
- Custom domain names
- SSL/custom certificates
- Content Delivery Network (CDN)
- Web Application Firewall (WAF)
- IP address restrictions
- Website authentication key management
- Site visibility controls (public/private)
- Power BI integration (visualization and embedded service)
- SharePoint integration for document management

### Conversion and Licensing
- Convert trial sites to production
- Application types: Trial or Production
- Early upgrade opt-in for development/testing environments
- Site health monitoring via Site Checker

## 18. Portal Management App

The Portal Management app provides advanced configuration beyond the design studio:

- **Content**: Web Pages, Web Files, Content Snippets, Web Links, Web Templates
- **Security**: Web Roles, Table Permissions, Web Page Access Control Rules
- **Configuration**: Site Settings, Site Markers, Page Templates, Basic Forms, Multistep Forms, Lists
- **Metadata**: Form metadata, Multistep form steps, Subgrid configuration

Access via design studio ellipsis menu > Portal Management, or directly from model-driven app.
