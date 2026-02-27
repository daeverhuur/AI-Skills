# Custom Connectors Reference

> Distilled from Microsoft Learn documentation on custom connectors

---

## Overview

Custom connectors extend Power Automate, Power Apps, Logic Apps, and Copilot Studio to connect to any REST API. Defined using **OpenAPI 2.0** (Swagger) format. OpenAPI 3.0 is **not** supported. Spec file must be < 1 MB. If there are multiple security definitions, the connector picks the top security definition.

Key facts:
- Custom connectors are **Premium** -- users need a Premium license to use them
- Maximum of **10,000 custom connectors** per Azure AD tenant
- Connectors created in Power Automate are available in Power Apps and Copilot Studio (and vice versa)
- Logic Apps connectors must be created separately
- Custom connectors support VNet-linked environments (connectors created before VNet association need to be re-saved)

---

## Creation Methods

| Method | Description |
|--------|-------------|
| Import OpenAPI file | Upload an OpenAPI 2.0 (Swagger) JSON/YAML definition |
| Import from Postman | Import a Postman Collection V1 (export from Postman, import into wizard) |
| From blank | Build from scratch using the connector wizard UI |
| From Azure service | Create from Azure App Service, Azure Functions, or API Management |
| CLI (paconn) | Use the Power Platform Connectors CLI for programmatic create/update |

### Import Steps

1. Navigate to **Power Apps/Automate > Data > Custom connectors > + New custom connector**
2. Choose import method (OpenAPI file, Postman collection, from URL, or blank)
3. Walk through the wizard pages: General, Security, Definition, Code, Test
4. Select **Create connector** to save
5. Test by creating a connection and invoking an operation

---

## OpenAPI 2.0 Definition Structure

### Minimal Template

```json
{
  "swagger": "2.0",
  "info": {
    "title": "MyAPI",
    "version": "1.0.0",
    "description": "API description here",
    "contact": {
      "name": "Support",
      "url": "https://support.example.com"
    }
  },
  "host": "api.example.com",
  "basePath": "/v1",
  "schemes": ["https"],
  "consumes": ["application/json"],
  "produces": ["application/json"],
  "securityDefinitions": {},
  "paths": {},
  "definitions": {}
}
```

### Paths, Parameters, and Responses

```json
{
  "paths": {
    "/items": {
      "get": {
        "operationId": "ListItems",
        "summary": "List all items",
        "description": "Returns a paginated list of items",
        "x-ms-visibility": "important",
        "parameters": [
          {
            "name": "status",
            "in": "query",
            "type": "string",
            "required": false,
            "x-ms-summary": "Status Filter",
            "description": "Filter by status",
            "enum": ["active", "inactive", "archived"]
          },
          {
            "name": "$top",
            "in": "query",
            "type": "integer",
            "required": false,
            "x-ms-summary": "Page Size",
            "x-ms-visibility": "advanced"
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "schema": {
              "$ref": "#/definitions/ItemList"
            }
          },
          "400": {
            "description": "Bad Request"
          },
          "401": {
            "description": "Unauthorized"
          }
        }
      },
      "post": {
        "operationId": "CreateItem",
        "summary": "Create a new item",
        "x-ms-visibility": "important",
        "parameters": [
          {
            "name": "body",
            "in": "body",
            "required": true,
            "schema": {
              "$ref": "#/definitions/NewItem"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "Created",
            "schema": {
              "$ref": "#/definitions/Item"
            }
          }
        }
      }
    },
    "/items/{id}": {
      "get": {
        "operationId": "GetItem",
        "summary": "Get item by ID",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "type": "string",
            "required": true,
            "x-ms-summary": "Item ID",
            "x-ms-url-encoding": "single"
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "schema": {
              "$ref": "#/definitions/Item"
            }
          },
          "404": {
            "description": "Not Found"
          }
        }
      }
    }
  }
}
```

### Schema Definitions

```json
{
  "definitions": {
    "Item": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "x-ms-summary": "Item ID",
          "x-ms-visibility": "internal"
        },
        "name": {
          "type": "string",
          "x-ms-summary": "Name"
        },
        "status": {
          "type": "string",
          "x-ms-summary": "Status",
          "enum": ["active", "inactive"]
        },
        "createdDate": {
          "type": "string",
          "format": "date-time",
          "x-ms-summary": "Created Date"
        }
      }
    },
    "NewItem": {
      "type": "object",
      "required": ["name"],
      "properties": {
        "name": {
          "type": "string",
          "x-ms-summary": "Name"
        },
        "description": {
          "type": "string",
          "x-ms-summary": "Description"
        }
      }
    },
    "ItemList": {
      "type": "object",
      "properties": {
        "value": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Item"
          }
        },
        "nextLink": {
          "type": "string",
          "x-ms-summary": "Next Page URL"
        }
      }
    }
  }
}
```

### Trigger Definitions

```json
{
  "/webhooks": {
    "x-ms-notification-content": {
      "description": "Webhook payload",
      "schema": {
        "$ref": "#/definitions/WebhookPayload"
      }
    },
    "post": {
      "operationId": "OnNewItem",
      "summary": "When a new item is created",
      "x-ms-trigger": "single",
      "x-ms-visibility": "important",
      "parameters": [
        {
          "name": "body",
          "in": "body",
          "required": true,
          "schema": {
            "type": "object",
            "required": ["callbackUrl"],
            "properties": {
              "callbackUrl": {
                "type": "string",
                "x-ms-notification-url": true,
                "x-ms-visibility": "internal"
              }
            }
          }
        }
      ],
      "responses": {
        "201": {
          "description": "Subscription created"
        }
      }
    }
  }
}
```

Trigger types:
- **`x-ms-trigger: "single"`** -- fires once per event (webhook-based)
- **`x-ms-trigger: "batch"`** -- returns array of items (polling-based)
- Polling triggers must return `Retry-After` header to control interval

---

## Authentication Types

### No Authentication

No credentials required. Anonymous access to the API.

### Basic Authentication

User provides username and password at connection creation time. Sent as `Authorization: Basic <base64>` header.

### API Key

API key sent as header or query parameter on every request.

```json
{
  "securityDefinitions": {
    "api_key": {
      "type": "apiKey",
      "in": "header",
      "name": "X-API-Key"
    }
  }
}
```

- `in` can be `header` or `query`
- The `name` field specifies the header/parameter name

### OAuth 2.0 -- Authorization Code Flow (Most Common)

Used for delegated user access (e.g., Microsoft Entra ID, Google, GitHub).

```json
{
  "securityDefinitions": {
    "oauth2": {
      "type": "oauth2",
      "flow": "accessCode",
      "authorizationUrl": "https://login.microsoftonline.com/common/oauth2/v2.0/authorize",
      "tokenUrl": "https://login.microsoftonline.com/common/oauth2/v2.0/token",
      "scopes": {
        "https://graph.microsoft.com/.default": "Access Microsoft Graph"
      }
    }
  }
}
```

Wizard configuration fields for OAuth 2.0:

| Field | Description |
|-------|-------------|
| Identity Provider | Generic OAuth 2, Azure AD, GitHub, Google, etc. |
| Client ID | App registration client/application ID |
| Client Secret | App registration secret |
| Authorization URL | OAuth authorize endpoint |
| Token URL | OAuth token endpoint |
| Refresh URL | Token refresh endpoint (usually same as token URL) |
| Scope | Space-separated list of requested scopes |
| Redirect URL | Auto-generated; register in your app registration |

### OAuth 2.0 -- Microsoft Entra ID (Azure AD) Pattern

For Entra ID specifically:

1. Register an app in Azure portal > App registrations
2. Add a redirect URI: `https://global.consent.azure-apim.net/redirect`
3. Create a client secret
4. Configure API permissions as needed
5. In the connector wizard, set Identity Provider to **Azure Active Directory**
6. Enter Client ID, Client Secret, Resource URL (e.g., `https://graph.microsoft.com`)

### OAuth 2.0 -- Implicit Flow

Used for client-side apps (less common for connectors). Set `"flow": "implicit"` in OpenAPI spec. Not recommended for production connectors.

### Windows Authentication

For on-premises APIs accessed via the on-premises data gateway. Requires:
- On-premises data gateway installed and configured
- Gateway cluster registered in Power Platform admin center
- Users provide Windows credentials at connection time

---

## Power Platform OpenAPI Extensions

| Extension | Purpose | Example |
|-----------|---------|---------|
| `x-ms-summary` | Display name for parameters/properties in the UI | `"x-ms-summary": "Email Address"` |
| `x-ms-visibility` | Controls visibility in the designer | `none`, `advanced`, `internal`, `important` |
| `x-ms-trigger` | Marks operation as a trigger | `"single"` (webhook) or `"batch"` (polling) |
| `x-ms-dynamic-values` | Populate dropdown from another operation | See dynamic values example below |
| `x-ms-dynamic-schema` | Dynamic response schema from another operation | Used for operations with variable output |
| `x-ms-notification-url` | Marks a parameter as the webhook callback URL | `true` on the callbackUrl parameter |
| `x-ms-notification-content` | Describes webhook payload schema | Placed at path level |
| `x-ms-url-encoding` | Path parameter encoding | `"single"` (no double encoding) |
| `x-ms-api-annotation` | Connector metadata (status, family) | Used internally for connector catalog |
| `x-ms-capabilities` | Declares connector capabilities | Pagination, test connection, etc. |

### Dynamic Values Example

```json
{
  "name": "listId",
  "in": "path",
  "required": true,
  "type": "string",
  "x-ms-summary": "List",
  "x-ms-dynamic-values": {
    "operationId": "GetLists",
    "value-path": "id",
    "value-title": "name"
  }
}
```

### Dynamic Schema Example

```json
{
  "responses": {
    "200": {
      "description": "Success",
      "schema": {
        "x-ms-dynamic-schema": {
          "operationId": "GetItemSchema",
          "parameters": {
            "listId": {
              "parameter": "listId"
            }
          },
          "value-path": "schema"
        }
      }
    }
  }
}
```

---

## Policy Templates

Policies modify connector behavior at runtime without code changes. Configured on the **Definition** page of the connector wizard under **New Policy**.

### Available Policy Templates

| Template | Purpose | Key Parameters |
|----------|---------|----------------|
| **Set Host URL** | Override the API host at runtime | Target URL |
| **Set HTTP Header** | Add or override a request header | Header name, value |
| **Set Query String Parameter** | Add or override a query parameter | Parameter name, value |
| **Route Request** | Route requests to different backends based on operation | Routing rules, target URLs |
| **Set Property** | Set a property value in request/response body | Property path, value |
| **Convert XML to JSON** | Transform XML responses to JSON | Applied on response |
| **Convert JSON to XML** | Transform JSON requests to XML | Applied on request |

### Policy with Environment Variables

Policies support environment variables for ALM scenarios. Syntax:

```
@environmentVariables("environmentVariableName")
```

This allows the same connector definition to work across environments (dev, test, prod) with different backend URLs, API keys, etc.

### Common Policy Patterns

**Dynamic host routing** -- Use "Set Host URL" policy to route to different backends per environment:
- Dev: `api-dev.example.com`
- Prod: `api.example.com`

**Adding correlation headers** -- Use "Set HTTP Header" to inject tracking headers on every request (e.g., `X-Correlation-Id`).

**API versioning** -- Use "Set Query String Parameter" to ensure `api-version=2024-01-01` is always included.

---

## Custom Code (C# Transformations)

Custom code transforms request/response payloads beyond what policy templates support. Code takes precedence over the codeless definition. Written in C# as a `Script` class implementing `ScriptBase`.

### Script Class Structure

```csharp
public class Script : ScriptBase
{
    public override async Task<HttpResponseMessage> ExecuteAsync()
    {
        // Access operation ID
        var operationId = this.Context.OperationId;

        // Read incoming request body
        var requestBody = await this.Context.Request.Content
            .ReadAsStringAsync().ConfigureAwait(false);

        // Forward request to backend
        var response = await this.Context.SendAsync(
            this.Context.Request,
            this.CancellationToken).ConfigureAwait(false);

        // Modify response
        var responseBody = await response.Content
            .ReadAsStringAsync().ConfigureAwait(false);
        var json = JObject.Parse(responseBody);

        // Transform and return
        json["transformed"] = true;
        response.Content = CreateJsonContent(json.ToString());
        return response;
    }
}
```

### Available Context Properties

| Property/Method | Description |
|-----------------|-------------|
| `Context.OperationId` | The operation being called (matches OpenAPI operationId) |
| `Context.Request` | The incoming `HttpRequestMessage` |
| `Context.CorrelationId` | Unique ID for request tracing |
| `Context.Logger` | `ILogger` instance for diagnostics |
| `Context.SendAsync()` | Sends HTTP request to backend (use instead of `HttpClient`) |
| `CancellationToken` | Cancellation token for the execution |
| `CreateJsonContent()` | Helper to create `StringContent` from serialized JSON |

### Code Limitations

- Maximum script size: **1 MB**
- Execution timeout: **5 seconds**
- Only `System`, `System.Net.Http`, `Newtonsoft.Json`, and a limited set of namespaces available
- Cannot make arbitrary external HTTP calls (must use `Context.SendAsync`)
- No file system access
- No persistent state between calls

### Common Code Patterns

**Route by operation:**

```csharp
public override async Task<HttpResponseMessage> ExecuteAsync()
{
    switch (this.Context.OperationId)
    {
        case "GetItems":
            return await HandleGetItems();
        case "TransformData":
            return await HandleTransform();
        default:
            return await this.Context.SendAsync(
                this.Context.Request,
                this.CancellationToken);
    }
}
```

**Flatten nested response:**

```csharp
private async Task<HttpResponseMessage> HandleGetItems()
{
    var response = await this.Context.SendAsync(
        this.Context.Request,
        this.CancellationToken).ConfigureAwait(false);

    var body = await response.Content.ReadAsStringAsync();
    var json = JObject.Parse(body);

    // Flatten nested "data.results" to top-level "value"
    var results = json.SelectToken("data.results");
    var output = new JObject { ["value"] = results };

    response.Content = CreateJsonContent(output.ToString());
    return response;
}
```

---

## Connector Wizard Pages

| Page | Purpose | Key Configuration |
|------|---------|-------------------|
| **General** | API host, base URL, description, icon, scheme | Host URL, base path, HTTPS required, icon upload (1x1 PNG < 20 KB), brand color |
| **Security** | Authentication type and parameters | Auth type selection, OAuth app details, API key config |
| **Definition** | Actions, triggers, request/response schemas | Add/edit operations, import from sample, set visibility, configure parameters |
| **Code (preview)** | Custom C# code for transformation | Script editor, toggle code on/off per operation |
| **Test** | Connection testing and operation invocation | Create connection, select operation, fill parameters, execute |

---

## Testing and Debugging

### In the Connector Wizard

1. Save/update the connector first
2. Go to the **Test** tab
3. Create a new connection (or select existing)
4. Choose an operation, fill in parameters
5. Click **Test operation** -- view request/response details

### Debugging Tips

- Check **response status code and body** in the test tab for API errors
- Use `Context.Logger` in custom code to write diagnostic messages
- Enable **API Management tracing** for Logic Apps connectors
- Review **connection status** in Power Automate > Data > Connections
- Common issues:
  - Wrong host URL or base path
  - Missing required headers or parameters
  - OAuth redirect URL not registered in app registration
  - CORS issues do not apply (requests go through Azure API Management)
  - OpenAPI spec validation errors on save

### Testing in Flows

1. Create a flow with a manual trigger
2. Add the custom connector action
3. Run the flow and check the run history
4. Expand the action to see raw inputs/outputs
5. Use **Peek code** to view the raw action definition

---

## Certification Process

### Prerequisites

- Must be a **verified publisher** (Microsoft Partner Network)
- Connector must be production-ready and publicly available
- API must be accessible (not internal-only)
- Must have a support contact and documentation URL

### Submission Requirements

**Connector title:**
- Must be unique, written in English, max 30 characters
- Cannot contain "API", "Connector", "Copilot Studio", or Power Platform product names
- Must end with an alphanumeric character
- Independent publishers: follow pattern `Connector Name (Independent Publisher)`

**Description:**
- 30-500 characters, written in English
- Must describe the main purpose and value
- No grammatical/spelling errors
- Cannot contain Power Platform product names

**Icon:**
- 1x1 ratio, preferably 160x160 px
- Non-white background (appears on white surface)
- Must be your brand icon

### Submission Steps

1. Develop and test the connector thoroughly
2. Export connector files using `paconn` CLI or Power Platform
3. Prepare required artifacts:
   - `apiDefinition.swagger.json` (OpenAPI definition)
   - `apiProperties.json` (connector metadata, icon, branding)
   - `icon.png` (connector icon)
   - `settings.json` (environment settings)
4. Submit via the Microsoft Partner Center or GitHub open-source connectors repo
5. Microsoft reviews: functional testing, security review, compliance check
6. Address any feedback from the review team
7. Connector published to the public gallery upon approval

### Independent Publisher Program

- Open to anyone (no Partner Network requirement)
- Connector marked with `(Independent Publisher)` suffix
- Connector source published on the open-source connectors GitHub repo
- Community-supported (not by the API provider)
- Fastest path to public certification

---

## Error Handling

### Common Error Patterns

| Error | Cause | Resolution |
|-------|-------|------------|
| 401 Unauthorized | Token expired or invalid credentials | Refresh connection, check OAuth config |
| 403 Forbidden | Insufficient permissions/scopes | Update API permissions in app registration |
| 404 Not Found | Wrong base URL or path | Verify host, basePath, and path parameters |
| 429 Too Many Requests | API throttling | Implement retry-after logic in the flow |
| 500 Internal Server Error | Backend API failure | Check API logs, verify request payload |
| Connection timeout | Network or gateway issues | Check on-prem gateway status, VNet config |

### Error Handling in Custom Code

```csharp
public override async Task<HttpResponseMessage> ExecuteAsync()
{
    try
    {
        var response = await this.Context.SendAsync(
            this.Context.Request,
            this.CancellationToken).ConfigureAwait(false);

        if (!response.IsSuccessStatusCode)
        {
            var errorBody = await response.Content
                .ReadAsStringAsync().ConfigureAwait(false);

            // Return a structured error
            var error = new JObject
            {
                ["error"] = true,
                ["statusCode"] = (int)response.StatusCode,
                ["message"] = errorBody
            };
            response.Content = CreateJsonContent(error.ToString());
        }

        return response;
    }
    catch (Exception ex)
    {
        var errorResponse = new HttpResponseMessage(
            HttpStatusCode.InternalServerError);
        errorResponse.Content = CreateJsonContent(
            new JObject { ["error"] = ex.Message }.ToString());
        return errorResponse;
    }
}
```

### Retry Patterns in Flows

When using custom connectors in Power Automate:
- Configure **retry policy** on the action (fixed interval, exponential backoff, or none)
- Default: 4 retries with exponential backoff
- Respect `Retry-After` headers from the API
- Use **Scope + Try/Catch** pattern for complex error handling

---

## Distribution and ALM

### Solution Packaging

- Package custom connectors in a **Dataverse solution** for transport across environments
- Use **connection references** so credentials are not embedded in the solution
- Use **environment variables** to parameterize host URLs, API keys, and other config

### Sharing

| Scope | Method |
|-------|--------|
| Within environment | Share with specific users or security groups |
| Across environments | Export/import in a managed solution |
| Entire organization | Deploy via managed solution to all environments |
| Public (certified) | Submit for Microsoft certification |

### CLI Management (paconn)

```bash
# Install the CLI
pip install paconn

# Login
paconn login

# Download connector files
paconn download -e <environment-id> -c <connector-id>

# Create connector
paconn create -e <environment-id> -s settings.json

# Update connector
paconn update -e <environment-id> -c <connector-id> -s settings.json

# Validate connector
paconn validate -s settings.json
```

---

## Limits and Constraints

| Constraint | Limit |
|-----------|-------|
| OpenAPI spec file size | < 1 MB |
| Custom connectors per tenant | 10,000 |
| Custom code script size | 1 MB |
| Custom code execution timeout | 5 seconds |
| Request payload size | 5 MB (10 MB for chunked transfers) |
| Response timeout | 120 seconds (2 minutes) |
| Connections per connector | No hard limit (per user) |
| Operations per connector | No hard limit (practical: < 500) |
| Parameters per operation | No hard limit (practical: < 100) |
| Webhook registrations | Managed automatically per flow |
