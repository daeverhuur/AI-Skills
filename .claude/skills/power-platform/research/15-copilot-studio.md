# Microsoft Copilot Studio - Research Notes

> Source: Microsoft Learn documentation (learn.microsoft.com/en-us/microsoft-copilot-studio/)
> Date: 2026-02-26

## 1. Overview and Platform

Microsoft Copilot Studio is a graphical, low-code platform for building AI agents and agent flows. It enables creation of intelligent conversational agents without requiring data scientists or developers. Available as a standalone web app at copilotstudio.microsoft.com and as a Teams app (Teams app supports classic chatbots only).

Key capabilities:
- Agents engage customers/employees in multiple languages across websites, mobile apps, Facebook, Teams, and Azure Bot Service channels
- Agents coordinate language models, instructions, context, knowledge sources, topics, tools, inputs, and triggers
- Agent flows automate repetitive tasks and integrate apps/services via natural language or visual editor
- Can extend Microsoft 365 Copilot with enterprise data and scenarios

Use cases: sales support, store information, employee HR benefits, public health tracking, common business Q&A.

## 2. Getting Started and Agent Creation

### Creating an Agent
1. Sign in at copilotstudio.microsoft.com
2. Enter a brief description of what the agent should do (up to 1,024 characters)
3. Copilot Studio provisions the agent automatically
4. Configure basics: name (max 42 chars), instructions (up to 8,000 chars), knowledge sources, suggested prompts

### Agent Configuration
- **Instructions**: Define conversation style, tone, and behavior
- **Knowledge**: Add public websites, documents, SharePoint, Dataverse as knowledge sources
- **Suggested prompts**: Up to 10 prompts for Teams/M365 conversations
- **Icon**: PNG format, under 72 KB, max 192x192 pixels

### Testing
- Use the built-in test chat panel during authoring
- Start new test sessions to verify changes
- Demo website for stakeholder testing (not for production)

## 3. Topic Authoring Fundamentals

A topic defines how an agent conversation progresses. Topics contain one or more nodes on an authoring canvas that determine conversational paths.

### Topic Types
- **System topics**: Predefined essential behaviors (greeting, escalation, end conversation). Cannot be created or deleted, but can be turned off or customized.
- **Custom topics**: User-created or predefined behaviors. Can be fully edited or removed.

### Node Types (Web App)

| Node Type | Description |
|-----------|-------------|
| Message | Send a message to the customer |
| Question | Ask a question and store the response |
| Adaptive Card | Show interactive card with response buttons or input fields |
| Condition | Branch conversation based on a condition |
| Variable Management | Set, parse, or clear variables |
| Topic Management | Redirect, transfer to agent, or end topic/conversation |
| Tool | Call Power Automate flow, Excel Online, connector, or other tool |
| Advanced | Generative answers, HTTP requests, events |

### Creating Topics
- Add from blank or describe what you want and let AI create it
- Add 5-10 trigger phrases to train NLU
- Avoid periods in topic names (blocks solution export)
- Can upload trigger phrases from a text file (max 3 MB)
- Code editor available for YAML-based topic editing

## 4. Triggers

Triggers determine when a topic should execute. The default depends on the orchestration mode.

| Trigger Type | Description |
|-------------|-------------|
| The agent chooses | Generative orchestration: fires based on topic name/description match |
| User says a phrase | Classic orchestration: fires on trigger phrase match |
| A message is received | Fires on any message activity |
| A custom client event occurs | Fires on event activity (filterable by event name) |
| An activity occurs | Fires on any activity type |
| The conversation changes | Fires on conversation update activity |
| It's invoked | Fires on invoke activity (common in Teams) |
| It's redirected to | Fires when called by another topic |
| The user is inactive | Fires after configured inactivity period |
| A plan completes | Generative orchestration: fires after all planned steps complete |
| AI response about to be sent | Generative orchestration: fires before sending generated response |

### Trigger Priority (execution order)
1. An activity occurs
2. A message is received / Custom client event / Conversation changes / Invoked
3. The agent chooses / User says a phrase

Triggers support conditions (including Power Fx formulas) and priority configuration.

## 5. Variables

Variables store customer responses and create dynamic conversation logic.

### Variable Scopes

| Scope | Description |
|-------|-------------|
| Topic | Limited to the current topic; default for new variables |
| Global | Available across all topics; cannot be converted back to topic scope |
| System | Built-in variables (e.g., User.DisplayName, User.ID, Activity data) |

### Variable Operations
- **Create**: Automatically created by Question nodes or manually via Set Variable Value node
- **Set value**: Literal value, existing variable, or Power Fx formula
- **Parse value**: Convert between types (e.g., JSON string to Record type)
- **Pass between topics**: Variables can receive values from or return values to other topics
- **Clear**: Remove variable values including conversation history

### Data Types
Variables support: String, Number, Boolean, Table, Record, Date/Time, Duration, Multiple Choice, and custom entity types. Power Fx formulas are available for complex type manipulation.

### Environment Variables
Can reference Azure Key Vault secrets. Requires Key Vault Secrets User role assignment and AllowedEnvironments/AllowedAgents tags. Cached for 5 minutes.

## 6. Conditions

Condition nodes add branching logic (if/else if/else) based on variable values.

### Condition Features
- Select variable, logical operator, and comparison value
- Operators vary by type (e.g., "is equal to" for all types, "is greater than" for numbers)
- Support AND/OR logic for cumulative or exclusive criteria
- Add multiple condition branches (else-if chains)
- Supports Power Fx formulas for complex conditions
- Can insert, reorder, and reorganize condition branches
- "All Other Conditions" branch always remains as the last branch

## 7. Power Automate / Agent Flows Integration

Agent flows extend agent capabilities using low-code drag-and-drop tools built in Copilot Studio.

### Tool Types for Agent Integration
- **Connector** (prebuilt or custom): Connect to 1000s of APIs via Power Platform Connectors
- **Agent flow**: Multi-step automation flows
- **Prompt**: Single-turn model-based prompt with knowledge references
- **REST API**: Connect to REST API endpoints
- **Model Context Protocol (MCP)**: Connect to MCP servers for tools and resources
- **Computer use**: Interact with any GUI (websites, desktop apps)
- **Skills**: Container for related tools
- **Client tool**: Send event activity for client-side actions

### Tool Configuration
- **Details**: Name, description, dynamic use toggle, end-user confirmation, authentication mode
- **Inputs**: Fill using AI dynamically or override with custom values; supports retry logic and validation
- **Completion**: Auto-generate response, author specific response, send adaptive card, or don't respond
- Max 128 tools per agent (recommended 25-30 for best performance)
- Tools require authentication: end-user credentials or maker-provided credentials

## 8. Generative Orchestration

Agents use either generative or classic orchestration (default: generative for new agents).

### Generative vs Classic Orchestration

| Behavior | Generative | Classic |
|----------|-----------|---------|
| Topic selection | Based on description | Based on trigger phrases |
| Tools | Agent auto-selects based on name/description | Only called explicitly from topics |
| Knowledge | Proactively searched for user queries | Fallback when no topics match |
| Multi-intent | Can combine topics, tools, and knowledge | Single topic selection |
| User input | Auto-generates questions for missing info | Requires authored question nodes |
| Responses | Auto-generates contextual responses | Requires authored message nodes |

### How It Works
1. User sends message; agent evaluates topics, tools, agents, and knowledge
2. Uses descriptions, names, input/output parameters to match intent
3. Can chain multiple tools/topics in sequence for multi-intent queries
4. Generates questions for missing information automatically
5. Summarizes response from all sources

### Configuration
- Toggle in Settings > Generative AI > Orchestration
- Descriptions are critical for accurate selection
- Auto-generates descriptions from trigger phrases when switching from classic
- Supports multilingual content generation in the active language

## 9. Knowledge Sources and Generative Answers

Knowledge sources ground agent responses with enterprise data.

### Supported Knowledge Sources

| Source | Type | Limit (Generative) | Limit (Classic) | Auth |
|--------|------|-------------------|-----------------|------|
| Public websites | External | 25 websites | 4 URLs | None |
| Documents | Internal (Dataverse) | All documents | Dataverse storage limit | None |
| SharePoint | Internal | 25 URLs | 4 URLs per node | Entra ID |
| Dataverse | Internal | Unlimited | 2 sources (15 tables each) | Entra ID |
| Enterprise connectors | Internal | Unlimited | 2 per agent | Entra ID |

### Additional Knowledge Settings
- **Web Search**: Uses Bing Grounding for real-time web information (requires generative orchestration)
- **General Knowledge**: Uses foundational AI knowledge for broad Q&A
- **Tenant Graph Grounding**: Semantic search via Microsoft 365 Copilot license (files up to 200 MB; 512 MB for PDF/PPTX/DOCX)
- **Content Moderation**: Configurable from Lowest to Highest (default: High); set at agent, topic, or prompt level
- **Official Sources**: Mark trusted knowledge sources for verified answers (classic orchestration only)

## 10. Messages and Rich Content

### Message Node Capabilities
- Text messages with basic formatting (bold, italic, lists, hyperlinks)
- Variable insertion via {x} icon
- Message variations: agent randomly picks from multiple variants
- Images: hosted via URL with optional title
- Videos: direct MP4 link or YouTube URL
- Basic cards: text, images, interactive elements
- Adaptive Cards: JSON-based platform-agnostic UI
- Quick replies: suggest responses or actions (Send message, Open URL, Make a call, Hidden message)
- Speech overrides for voice-enabled channels with SSML support (Audio, Break, Emphasis, Prosody tags)

### Card Display Options
- Carousel (default): one card at a time
- List: vertical display of all cards

## 11. Adaptive Cards

Platform-agnostic UI snippets in JSON that adapt to their host context (dark/light mode, screen size).

### Schema Support
- Copilot Studio: supports schema versions up to 1.6
- Bot Framework Web Chat: version 1.6 (no Action.Execute)
- Teams: limited to version 1.5
- Dynamics 365 Omnichannel: limited to version 1.5

### Usage
- Interactive Adaptive Card node for collecting information
- Add to Message or Question nodes for display
- Edit via built-in card payload editor or external designers
- Use Adaptive Cards website, ChatGPT, Power Apps, or Power Automate to generate JSON

## 12. Publishing and Channels

### Publish Process
1. Select Publish from the top menu bar
2. Confirm publication; applies to all connected channels
3. Must publish at least once before connecting channels
4. Republish after any changes to update all channels

### Available Channels

| Channel | Notes |
|---------|-------|
| Teams and Microsoft 365 Copilot | Primary enterprise channel; supports suggested prompts |
| Demo Website | For testing/stakeholder review only, not production |
| Custom Website | Embed via iframe code snippet with Bot Framework Web Chat |
| SharePoint | Embedded agent |
| Facebook | Messenger integration |
| WhatsApp | Messaging integration |
| Mobile App | Native app integration (developer coding required) |
| Azure Bot Service | Slack, Telegram, Twilio, Line, Kik, GroupMe, Direct Line Speech, Email |

### Channel Experience Differences
- Website: full Adaptive Card support, markdown, welcome messages
- Teams: text-only CSAT survey, max 6 suggested actions, hero card format
- Facebook: max 13 quick replies, no welcome message
- M365 Copilot: no Conversation Start topic, no GIFs, no basic cards/video/image (use Adaptive Cards)

### Web Channel Deployment
- Demo website: customizable welcome message and conversation starters
- Live website: iframe snippet using Bot Framework Web Chat with token endpoint
- Full style customization via styleOptions object (colors, avatars, fonts, spacing)

## 13. Teams and Microsoft 365 Copilot Deployment

### Distribution Methods
- Install for yourself directly from Copilot Studio
- Share installation link with other users
- Show in Teams app store "Built with Power Platform" section (shared users only)
- Submit for admin approval for "Built for your org" section
- Download Teams app manifest (.zip) for custom upload
- Add agent to team channels for @mention usage
- Admin can use app setup policies for auto-install and pinning

### Configuration
- Customize icon, color, descriptions for Teams app store
- Add developer name, website, privacy statement, terms of use
- Enable "Allow users to add agent to a team" for collaborative use
- Configure private greeting behavior (classic chatbots only)
- New conversations start after 30 minutes of inactivity

## 14. Entities and Slot Filling

### Prebuilt Entities
Built-in entities for common information types: Age, Boolean, City, Color, Continent, Country, Currency, Date/Time, Duration, Email, Event, Geography, Language, Money, Number, Ordinal, Organization, Percentage, Person Name, Phone Number, Point of Interest, Speed, State, Street Address, Temperature, URL, Weight, Zip Code.

### Custom Entity Types

| Type | Description |
|------|-------------|
| Closed List | Define a list of items with optional synonyms; supports smart matching (fuzzy logic, autocorrect, semantic expansion) |
| Regular Expression (Regex) | Pattern matching for structured input (tracking IDs, license numbers, IP addresses); .NET regex syntax (NLU/CLU) or JavaScript syntax (NLU+) |

### Slot Filling
- Extracted entity values are stored in variables automatically
- **Proactive slot filling**: agent extracts multiple pieces of information from a single user input and fills corresponding variables, skipping redundant questions
- **Skip question** option can be set to "Ask every time" to always prompt
- **One of multiple entities**: accept one of up to 5 different entity types at a conversation turn; returns record-type variable

## 15. Analytics

### Analytics Dashboard
- Summary area with AI-generated insights
- Overview of key metrics with drill-down capability
- Available for conversational agents and autonomous agents (event-triggered)
- Hybrid view when both session types exist
- UTC timestamps; not available for test panel activity

### Conversational Analytics
- Conversations timeout after 30 minutes of inactivity (3 minutes after End Conversation for telephony)
- Single conversation can contain multiple analytics sessions
- Session outcomes: Resolved, Escalated, Abandoned, Unengaged

### Session Transcripts
- Download CSV files from the past 29 days
- Fields: SessionID, StartDateTime, SessionOutcome, OutcomeReason, Turns, ChatTranscript, InitialUserMessage, TopicName, TopicId, ChannelId, Comments
- ChatTranscript limited to 512 characters per bot response
- Requires Bot Transcript Viewer security role
- Also available via Dataverse through Power Apps portal
- Not available for: Teams environments, developer environments, M365 Copilot agents
- SharePoint knowledge source responses not included in transcripts

## 16. Authentication

### Authentication Options

| Option | Description | Variables Available |
|--------|-------------|-------------------|
| No authentication | Anyone with the link can chat | None |
| Authenticate with Microsoft | Auto Entra ID for Teams; no manual config | User.ID, User.DisplayName |
| Authenticate manually | Full OAuth2 configuration | User.ID, User.DisplayName, User.AccessToken, User.IsLoggedIn |

### Manual Authentication Providers
- Microsoft Entra ID V2 with federated credentials
- Microsoft Entra ID V2 with certificates
- Microsoft Entra ID V2 with client secrets
- Microsoft Entra ID (v1)
- Generic OAuth 2 (any standard-compliant provider)

### Key Configuration Fields
- Authorization URL template, Client ID, Client Secret, Scopes, Token URL template, Refresh URL template
- Token Exchange URL for SSO
- Client Certificate KeyVault URL for certificate-based auth
- Require users to sign in: creates system topic for mandatory authentication

### Access Control
- No auth: anyone can chat, no control over who
- Authenticate with Microsoft: Teams only, always signed in, agent sharing controls access
- Manual with Entra ID: Require sign-in + sharing controls access
- Manual with Generic OAuth2: sign-in controls access, no per-user sharing control

## 17. Environments

### Environment Basics
- Environments store agents, data, flows, and resources
- Created via Power Platform admin center (admin.powerplatform.com)
- Each environment has separate location, roles, security, and audience
- Default environment created on first sign-in

### Environment Types
- Production: intended for production scenarios
- Trial: 30-day expiration, can convert to production
- Developer, Sandbox, and other Power Platform types

### Configuration
- Name, Region (must be supported data region), Type, Dataverse data store, Pay-as-you-go Azure billing
- Environment Maker role required for agent creation
- System Administrator role for full environment management

### Supported Operations
- Backup/restore, Delete, Recover, Copy, Reset
- NOT supported: Move between tenants

## 18. Sharing and Collaboration

### Sharing for Chat
- Share with individual users, security groups, or entire organization
- Requires: Manual authentication with Entra ID + Required user sign-in enabled
- Cannot share with M365 groups where SecurityEnabled = false

### Sharing for Collaborative Authoring
- Grants view, edit, configure, share, and publish permissions (not delete)
- Requires Copilot Studio per-user license
- Collaborators see who is editing which topic in real-time
- 30-minute inactivity timeout for editing presence
- Conflict resolution: discard changes or save as copy

### Security Roles
- **Environment Maker**: required to use Copilot Studio in an environment
- **Bot Contributor**: granted when sharing for coauthoring
- **Bot Transcript Viewer**: required to access conversation transcripts
- **System Administrator**: can assign roles when sharing agents
- Power Automate flows must be shared separately for editing access

## 19. Advanced AI Features

### Generative AI Settings
- Orchestration mode toggle (generative vs classic)
- Web search using Bing Grounding
- General knowledge (foundational AI knowledge)
- Tenant graph grounding with semantic search
- Content moderation levels: Lowest, Low, Medium, High (default), Highest
- AI-generated topic descriptions from trigger phrases

### AI-Powered Capabilities
- Natural Language Understanding (NLU) for intent matching
- Azure OpenAI GPT model for topic generation from descriptions
- Generative answers from knowledge sources
- Proactive slot filling from conversation context
- Auto-generated questions for missing tool/topic inputs
- Contextual response generation from combined sources
- Activity map for testing and debugging generative orchestration
- Power Fx formula support throughout the platform

### Conversation History
- Used for context-aware decisions and response generation
- Can be cleared via Clear Variable Values node
- Limited history window may require re-collection of older information
