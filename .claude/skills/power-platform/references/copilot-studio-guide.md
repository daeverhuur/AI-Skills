# Copilot Studio Reference Guide

## Overview

Microsoft Copilot Studio is a graphical, low-code platform for building AI agents and agent flows. Available as a standalone web app at `copilotstudio.microsoft.com` and as a Teams app (Teams app supports classic chatbots only).

**Key capabilities:**
- Build intelligent conversational agents without data scientists or developers
- Agents engage across websites, mobile apps, Facebook, Teams, and Azure Bot Service channels
- Agents coordinate language models, instructions, context, knowledge, topics, tools, and triggers
- Agent flows automate repetitive tasks via natural language or visual editor
- Can extend Microsoft 365 Copilot with enterprise data and scenarios

## Agent Creation

1. Sign in at `copilotstudio.microsoft.com`
2. Enter a description of what the agent should do (up to 1,024 characters)
3. Copilot Studio provisions the agent automatically
4. Configure: name (max 42 chars), instructions (up to 8,000 chars), knowledge sources, suggested prompts

### Agent Configuration

- **Instructions** -- define conversation style, tone, and behavior
- **Knowledge** -- add public websites, documents, SharePoint, Dataverse as sources
- **Suggested prompts** -- up to 10 prompts for Teams/M365 conversations
- **Icon** -- PNG, under 72 KB, max 192x192 pixels

### Testing

- Built-in test chat panel during authoring
- Demo website for stakeholder testing (not for production)
- Start new test sessions to verify changes

## Topics

A topic defines how a conversation progresses. Contains one or more nodes on an authoring canvas.

### Topic Types

| Type | Description |
|------|-------------|
| System | Predefined essential behaviors (greeting, escalation, end conversation); cannot be created/deleted but can be customized |
| Custom | User-created or predefined behaviors; fully editable and removable |

### Node Types

| Node | Description |
|------|-------------|
| Message | Send a message to the customer |
| Question | Ask a question and store the response |
| Adaptive Card | Show interactive card with response buttons or input fields |
| Condition | Branch conversation based on a condition |
| Variable Management | Set, parse, or clear variables |
| Topic Management | Redirect, transfer to agent, or end topic/conversation |
| Tool | Call Power Automate flow, Excel Online, connector, or other tool |
| Advanced | Generative answers, HTTP requests, events |

### Creating Topics

- Add from blank or describe desired behavior for AI generation
- Add 5-10 trigger phrases to train NLU
- Avoid periods in topic names (blocks solution export)
- Upload trigger phrases from text file (max 3 MB)
- Code editor available for YAML-based editing

## Triggers

Triggers determine when a topic executes.

| Trigger | Description |
|---------|-------------|
| The agent chooses | Generative orchestration: fires on topic name/description match |
| User says a phrase | Classic orchestration: fires on trigger phrase match |
| A message is received | Fires on any message activity |
| A custom client event occurs | Fires on event activity (filterable by event name) |
| An activity occurs | Fires on any activity type |
| The conversation changes | Fires on conversation update activity |
| It's invoked | Fires on invoke activity (common in Teams) |
| It's redirected to | Fires when called by another topic |
| The user is inactive | Fires after configured inactivity period |
| A plan completes | Generative: fires after all planned steps complete |
| AI response about to be sent | Generative: fires before sending generated response |

### Trigger Priority

1. An activity occurs
2. A message is received / Custom client event / Conversation changes / Invoked
3. The agent chooses / User says a phrase

Triggers support conditions (including Power Fx formulas) and priority configuration.

## Variables

Store customer responses and create dynamic conversation logic.

### Scopes

| Scope | Description |
|-------|-------------|
| Topic | Limited to current topic; default for new variables |
| Global | Available across all topics; cannot convert back to topic scope |
| System | Built-in (User.DisplayName, User.ID, Activity data) |

### Data Types

String, Number, Boolean, Table, Record, Date/Time, Duration, Multiple Choice, custom entity types. Power Fx formulas available for complex manipulation.

### Operations

- **Create** -- automatically via Question nodes or manually via Set Variable Value
- **Set value** -- literal, existing variable, or Power Fx formula
- **Parse value** -- convert between types (e.g., JSON string to Record)
- **Pass between topics** -- receive values from or return values to other topics
- **Clear** -- remove variable values including conversation history

### Environment Variables

- Can reference Azure Key Vault secrets
- Requires Key Vault Secrets User role assignment
- AllowedEnvironments/AllowedAgents tags for scoping
- Cached for 5 minutes

## Conditions

Condition nodes add if/else if/else branching based on variable values.

- Select variable, logical operator, and comparison value
- Support AND/OR logic for cumulative or exclusive criteria
- Add multiple condition branches (else-if chains)
- Power Fx formulas for complex conditions
- "All Other Conditions" branch always remains as last branch

## Power Automate Integration

Agent flows extend agent capabilities using low-code tools built in Copilot Studio.

### Tool Types

| Type | Description |
|------|-------------|
| Connector | Prebuilt or custom; connect to 1000s of APIs |
| Agent flow | Multi-step automation flows |
| Prompt | Single-turn model-based prompt with knowledge references |
| REST API | Connect to REST API endpoints |
| MCP | Connect to MCP servers for tools and resources |
| Computer use | Interact with any GUI (websites, desktop apps) |
| Skills | Container for related tools |
| Client tool | Send event activity for client-side actions |

### Tool Configuration

- **Details** -- name, description, dynamic use toggle, end-user confirmation, authentication mode
- **Inputs** -- fill using AI dynamically or override with custom values; retry and validation logic
- **Completion** -- auto-generate response, author specific response, send adaptive card, or silent
- Max 128 tools per agent (recommended 25-30 for best performance)
- Tools require authentication: end-user credentials or maker-provided credentials

## Generative AI Features

### Generative vs Classic Orchestration

| Behavior | Generative | Classic |
|----------|-----------|---------|
| Topic selection | Based on description | Based on trigger phrases |
| Tools | Agent auto-selects by name/description | Only called explicitly from topics |
| Knowledge | Proactively searched for user queries | Fallback when no topics match |
| Multi-intent | Combines topics, tools, and knowledge | Single topic selection |
| User input | Auto-generates questions for missing info | Requires authored question nodes |
| Responses | Auto-generates contextual responses | Requires authored message nodes |

### How Generative Orchestration Works

1. User sends message; agent evaluates topics, tools, agents, and knowledge
2. Uses descriptions, names, input/output parameters to match intent
3. Chains multiple tools/topics in sequence for multi-intent queries
4. Generates questions for missing information automatically
5. Summarizes response from all sources

### Knowledge Sources

| Source | Generative Limit | Classic Limit | Auth |
|--------|-----------------|---------------|------|
| Public websites | 25 websites | 4 URLs | None |
| Documents (Dataverse) | All documents | Dataverse storage limit | None |
| SharePoint | 25 URLs | 4 URLs per node | Entra ID |
| Dataverse | Unlimited | 2 sources (15 tables each) | Entra ID |
| Enterprise connectors | Unlimited | 2 per agent | Entra ID |

### Additional AI Settings

- **Web Search** -- Bing Grounding for real-time web information (generative only)
- **General Knowledge** -- foundational AI knowledge for broad Q&A
- **Tenant Graph Grounding** -- semantic search via M365 Copilot license
- **Content Moderation** -- Lowest to Highest (default: High); set per agent, topic, or prompt

## Plugin Actions

Tools (formerly plugin actions) allow agents to call external services and automation:
- Power Automate cloud flows
- Power Platform connectors (prebuilt and custom)
- REST API endpoints
- MCP server connections

Configuration includes input/output schemas, authentication mode, and completion behavior.

## Adaptive Cards

Platform-agnostic UI snippets in JSON that adapt to their host context.

### Schema Support

| Channel | Max Version |
|---------|------------|
| Bot Framework Web Chat | 1.6 (no Action.Execute) |
| Teams | 1.5 |
| Dynamics 365 Omnichannel | 1.5 |
| Copilot Studio | Up to 1.6 |

### Usage

- Interactive Adaptive Card node for collecting information
- Add to Message or Question nodes for display
- Edit via built-in card payload editor or external designers
- Display options: Carousel (default) or List

## Publishing Channels

### Publish Process

1. Select Publish from top menu bar
2. Confirm; applies to all connected channels
3. Must publish at least once before connecting channels
4. Republish after any changes

### Available Channels

| Channel | Notes |
|---------|-------|
| Teams and M365 Copilot | Primary enterprise channel; supports suggested prompts |
| Demo Website | Testing/stakeholder review only |
| Custom Website | Embed via iframe with Bot Framework Web Chat |
| SharePoint | Embedded agent |
| Facebook | Messenger integration |
| WhatsApp | Messaging integration |
| Mobile App | Native integration (developer coding required) |
| Azure Bot Service | Slack, Telegram, Twilio, Line, Kik, GroupMe, Direct Line Speech, Email |

### Channel Differences

- Website: full Adaptive Card support, markdown, welcome messages
- Teams: text-only CSAT survey, max 6 suggested actions, hero card format
- Facebook: max 13 quick replies, no welcome message
- M365 Copilot: no Conversation Start topic, no GIFs, no basic cards/video/image

### Teams Distribution

- Install for yourself from Copilot Studio
- Share installation link with users
- Show in Teams app store "Built with Power Platform" section
- Submit for admin approval for "Built for your org" section
- Download Teams app manifest (.zip) for custom upload
- Admin can use app setup policies for auto-install and pinning

## Entities and Slot Filling

### Prebuilt Entities

Age, Boolean, City, Color, Continent, Country, Currency, Date/Time, Duration, Email, Event, Geography, Language, Money, Number, Ordinal, Organization, Percentage, Person Name, Phone Number, Point of Interest, Speed, State, Street Address, Temperature, URL, Weight, Zip Code.

### Custom Entity Types

| Type | Description |
|------|-------------|
| Closed List | Items with optional synonyms; supports smart matching (fuzzy logic, autocorrect, semantic expansion) |
| Regular Expression | Pattern matching for structured input; .NET or JavaScript regex syntax |

### Slot Filling

- Extracted entity values stored in variables automatically
- **Proactive slot filling** -- agent extracts multiple pieces from a single input, skipping redundant questions
- **Skip question** option: "Ask every time" to always prompt
- **One of multiple entities** -- accept up to 5 different entity types at a turn; returns record-type variable

## Analytics

### Dashboard

- AI-generated summary insights with drill-down capability
- Available for conversational and autonomous (event-triggered) agents
- UTC timestamps; not available for test panel activity

### Session Outcomes

Resolved, Escalated, Abandoned, Unengaged. Conversations timeout after 30 minutes of inactivity.

### Session Transcripts

- Download CSV from past 29 days
- Fields: SessionID, StartDateTime, SessionOutcome, Turns, ChatTranscript, TopicName, ChannelId
- ChatTranscript limited to 512 characters per bot response
- Requires Bot Transcript Viewer security role
- Not available for: Teams environments, developer environments, M365 Copilot agents

## Authentication

### Options

| Option | Description | Variables Available |
|--------|-------------|-------------------|
| No authentication | Anyone with the link can chat | None |
| Authenticate with Microsoft | Auto Entra ID for Teams; no manual config | User.ID, User.DisplayName |
| Authenticate manually | Full OAuth2 configuration | User.ID, User.DisplayName, User.AccessToken, User.IsLoggedIn |

### Manual Authentication Providers

- Microsoft Entra ID V2 (federated credentials, certificates, or client secrets)
- Microsoft Entra ID (v1)
- Generic OAuth 2 (any standard-compliant provider)

### Key Configuration

- Authorization URL, Client ID, Client Secret, Scopes, Token URL, Refresh URL
- Token Exchange URL for SSO
- "Require users to sign in" creates system topic for mandatory authentication

## Security

### Access Control

- No auth: anyone can chat, no control
- Authenticate with Microsoft: Teams only, always signed in, agent sharing controls access
- Manual with Entra ID: require sign-in + sharing controls access
- Manual with Generic OAuth2: sign-in controls access, no per-user sharing

### Sharing

- Share for chat: individual users, security groups, or entire organization
- Share for coauthoring: grants view, edit, configure, share, publish permissions
- Collaborators see who is editing which topic in real-time
- Conflict resolution: discard changes or save as copy

### Security Roles

| Role | Purpose |
|------|---------|
| Environment Maker | Required to use Copilot Studio in an environment |
| Bot Contributor | Granted when sharing for coauthoring |
| Bot Transcript Viewer | Required to access conversation transcripts |
| System Administrator | Can assign roles when sharing agents |
