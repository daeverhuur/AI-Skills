# Copilot and AI Features Reference

## Copilot in Power Apps

### Overview

Copilot enables natural language app creation. Makers describe business needs and Copilot generates a working app with data model. Powered by Azure OpenAI Service (GPT-4o family). No coding or screen design required -- describe what you need in plain language and Copilot produces Dataverse tables, relationships, sample data, and a canvas app.

### Prerequisites

- Azure OpenAI Service powers all Copilot features.
- Some features are in preview and subject to supplemental terms of use.
- Availability varies by region and language. Check "Copilot features by geography and languages" for your region.
- Usage limits or capacity throttling may apply.
- Dataverse database required in the environment for table generation.
- System Customizer security role required for the maker.

### Key Capabilities

- **Natural language app generation**: Describe what you need, get a working app + Dataverse data model with tables, relationships, and sample rows. Accessed via Power Apps home > Start with data > Create new data.
- **Copilot control for canvas apps**: AI chat assistant embedded in canvas apps; end users ask questions about app data in natural language. Data source: Dataverse tables only.
- **Copilot for model-driven apps**: AI assistance within model-driven app experiences, including rich text editor refinement.
- **Copilot Studio integration**: Customize copilot behavior through Copilot Studio (topics, actions, articles).
- **Build apps through conversation**: Multi-turn conversation in the "Create new tables" workspace. Copilot generates one or more Dataverse tables; maker reviews tables, edits columns, creates relationships, and then saves to generate the app.

### Building Apps with Copilot (Detailed Flow)

1. Sign in to Power Apps, select **Start with data** > **Create new data**.
2. The "Create new tables" workspace opens with a blank table and Copilot panel.
3. Enter a prompt describing the business scenario (e.g., "Create tables to track hotel housekeeping tasks including room numbers, task types, staff assignments, and task status").
4. Copilot generates one or more Dataverse tables with columns, relationships, and sample data.
5. Review generated tables using workspace options:
   - **New table**: Add additional tables.
   - **Existing table**: Include existing Dataverse tables.
   - **View data**: Inspect generated sample rows.
   - **Create relationships**: Define table relationships.
   - **Remove**: Remove unwanted tables.
6. Use the Copilot panel to iterate: ask Copilot to add columns, change data types, import data, or restructure.
7. Select **Save and exit** to create the app.

### Copilot Panel Options in Table Editor

| Option | Description |
|---|---|
| Create | Describe tables, columns, rows, and relationships to generate them |
| Import data | Import from external sources into Dataverse tables |
| Make changes | Modify existing tables, add/remove columns via natural language |

### Copilot Control (Canvas Apps)

> As of February 2, 2026, the Copilot control cannot be added to new canvas apps. Microsoft 365 Copilot Chat in canvas apps is the recommended replacement.

- **Setup**: Enable in Power Platform admin center + turn on Copilot component in app settings.
- **Data source**: Dataverse tables only.
- **Customization**: Use Copilot Studio to define topics, actions, and responses.
- **Migration path**: Existing apps with the Copilot control continue to work, but new implementations should use M365 Copilot Chat.

### Copilot Control in Model-Driven Apps (Rich Text Editor)

The Copilot control is available by default in the email form's rich text editor toolbar. To add it to other forms:

1. Open the rich text editor's advanced configuration file for the target form.
2. In the `defaultSupportedProps` section, add `copilotrefinement` to the `extraPlugins` property.
3. Add `CopilotRefinement` to the `toolbar` property items array.

```json
"defaultSupportedProps": {
  "extraPlugins": "computedfont,...,copilotrefinement",
  "toolbar": [{ "items": ["CopyFormatting", "...", "CopilotRefinement"] }]
}
```

4. Save the configuration file and publish changes.

### Admin Controls

| Scope | Setting | Default | How to Change |
|---|---|---|---|
| Environment | Copilot toggle (preview features) | On | Power Platform admin center > Environments > Settings > Features > Copilot toggle |
| Tenant | Copilot in Power Apps (preview) | On | Power Platform admin center > Settings > Tenant settings > Copilot in Power Apps toggle |
| GA features | Cannot be turned off by admin | On | Contact Microsoft Support |

**Important**: Turning off Copilot at the tenant level turns off Copilot for **makers only**. It does not turn off the Copilot control for canvas apps or Copilot for model-driven apps.

### Disabling Copilot Preview Features

**Per environment:**
1. Sign in to Power Platform admin center.
2. Select Environments > choose environment.
3. Command bar > Settings > Features.
4. Set the **Copilot** toggle to **Off**.

**Per tenant:**
1. Sign in to Power Platform admin center.
2. Select Settings > Tenant settings.
3. Select **Copilot in Power Apps (preview)** > toggle **Off**.
4. Select Save.

---

## Copilot in Power Automate

### Overview

Copilot in Power Automate accelerates automation adoption by allowing users to describe automation needs in natural language. Copilot surfaces possible solutions and stays with the maker throughout the creation process to guide and refine the flow.

### Cloud Flows

Create automation using natural language through multi-step conversational experience. Describe what you need and Copilot generates flow steps. Edit and refine through continued conversation.

- **Create a cloud flow using Copilot**: Describe your automation scenario; Copilot generates a complete flow with triggers, actions, and connections.
- **Contextual help**: Get flow-specific help from the Copilot Studio bot embedded in the designer.
- **Flows as plugins**: Use flows as plugins in Copilot for Microsoft 365 (preview), enabling M365 Copilot to trigger Power Automate flows on behalf of users.

### Desktop Flows

- **Natural language creation**: Create desktop flows using plain language descriptions.
- **Record with Copilot (preview)**: AI-assisted recording of desktop actions. Copilot helps identify and record UI interactions.
- **Natural language to script**: Convert plain language instructions to automation scripts for Power Automate for desktop.
- **Error repair (preview)**: AI-powered fix suggestions for runtime errors. When a desktop flow fails, Copilot analyzes the error and suggests corrections.
- **Activity analysis (preview)**: Analyze desktop flow runs with natural language queries. Ask questions like "Which flows failed last week?" or "What is the average run time?"
- **Product Q&A**: Ask Copilot product-related questions about Power Automate for desktop features and capabilities.

### Process Mining

- **Ingestion**: Copilot guides users through the data ingestion experience in Process Mining, helping configure data sources and mappings.
- **Process analytics**: Generate insights through natural language queries. Copilot summarizes findings quantitatively (metrics, KPIs) and qualitatively (bottlenecks, patterns).

### Automation Center

Retrieve information about past flow runs, work queue performance, and product features by asking natural language questions. Designed for makers, business analysts, and Center of Excellence team members.

### Admin Controls

| Region Type | GPU Availability | Copilot Default | How to Disable |
|---|---|---|---|
| UK, Australia, US, India | Has GPUs | On by default | Contact Support; PowerShell script at tenant level only |
| All other regions (non-sovereign) | No GPUs | On via cross-geo data sharing | Toggle off cross-geo data sharing in Power Platform admin center (tenant level) |
| Sovereign clouds | N/A | Off | N/A |

**Note**: Environment-level disable is not available for regions with GPUs. Only tenant-level control through Support.

---

## AI Functions in Power Fx

### Overview

Dataverse provides ready-to-use AI functions that are preconfigured and require no data collection, building, or training. These prebuilt AI functions integrate directly into canvas apps, AI Builder, and low-code plugins via the Power Fx formula bar.

### Available Functions (Full Reference)

| Function | Signature | Return Column | Description |
|---|---|---|---|
| `AIClassify` | `AIClassify(Text, Categories)` | `Classification` | Classifies text into one of the provided categories |
| `AIExtract` | `AIExtract(Text, Entity)` | `ExtractedData` (table) | Extracts specified entities from text (registration numbers, phone numbers, names) |
| `AIReply` | `AIReply(Text)` | `PreparedResponse` | Drafts a reply to the provided message |
| `AISentiment` | `AISentiment(Text)` | `AnalyzedSentiment` | Returns "Positive", "Neutral", or "Negative" |
| `AISummarize` | `AISummarize(Text)` | `SummarizedText` | Summarizes the provided text |
| `AISummarizeRecord` | `AISummarizeRecord(Entity)` | `SummarizedText` | Summarizes information from a Dataverse record |
| `AITranslate` | `AITranslate(Text, TargetLanguage)` | `TranslatedText` | Translates text to the target language (auto-detects source) |

**Note**: `AIExtract` is still in development and may not operate properly in all scenarios.

### Function Parameter Details

**AIClassify(Text, Categories)**
- `Text` (required, string): The text to classify.
- `Categories` (required, single-column table): Table of text categories. Example categories: "Problem", "Billing", "How To", "Licensing".

**AIExtract(Text, Entity)**
- `Text` (required, string): The text to extract data from.
- `Entity` (required, string): The name of the entity to extract.
- Returns a table of zero or more rows matching the provided entity.

**AIReply(Text)**
- `Text` (required, string): The message to respond to (e.g., a customer review or inquiry).

**AISentiment(Text)**
- `Text` (required, string): The text to analyze for sentiment.
- Returns one of: "Positive", "Neutral", "Negative".

**AISummarize(Text)**
- `Text` (required, string): The text to summarize.

**AISummarizeRecord(Entity)**
- `Entity` (required, Dataverse record): The record to summarize.

**AITranslate(Text, TargetLanguage)**
- `Text` (required, string): The text to translate.
- `TargetLanguage` (required, string): Language tag, e.g., "fr" for French, "de" for German. Source language is auto-detected.

### Prerequisites for AI Functions

- Your environment must be in a supported region.
- Copilot Credits are required.
- Microsoft Dataverse must be installed on the environment.

### Using AI Functions in Canvas Apps

In canvas apps, AI functions live in the `Environment` namespace. You must:

1. Add the **Environment** data source (Data pane > Add data > Environment).
2. Call functions using `Environment.FunctionName(...)` syntax.
3. Pass arguments as **named columns in a record** (single argument).
4. These are **behavior functions** -- they cannot be used directly in data-binding properties (e.g., `Text` property of a label). Use `Set()` to store the result in a global variable.

### Canvas App Setup Example

```
// Step 1: Add the Environment data source from the Data pane

// Step 2: Add a Button control, set OnSelect to:
Set(
    Summary,
    Environment.AISummarize(
        { Text: "2, 4, 6, 8, 10, 12, 14, 16" }
    ).SummarizedText
)

// Step 3: Add a Text label, set its Text property to:
Summary
```

### Detailed Formula Examples

```
// Classify customer feedback
Set(
    FeedbackCategory,
    Environment.AIClassify(
        {
            Text: TextInput_Feedback.Text,
            Categories: Table(
                { Value: "Problem" },
                { Value: "Billing" },
                { Value: "How To" },
                { Value: "Licensing" },
                { Value: "Praise" }
            )
        }
    ).Classification
)

// Analyze sentiment of a review
Set(
    ReviewSentiment,
    Environment.AISentiment(
        { Text: TextInput_Review.Text }
    ).AnalyzedSentiment
)

// Extract entities from text
Set(
    ExtractedEntities,
    Environment.AIExtract(
        {
            Text: TextInput_Document.Text,
            Entity: "phone number"
        }
    ).ExtractedData
)

// Draft a reply to a customer message
Set(
    DraftReply,
    Environment.AIReply(
        { Text: TextInput_CustomerMessage.Text }
    ).PreparedResponse
)

// Translate text to French
Set(
    TranslatedText,
    Environment.AITranslate(
        {
            Text: TextInput_Source.Text,
            TargetLanguage: "fr"
        }
    ).TranslatedText
)

// Summarize a Dataverse record
Set(
    RecordSummary,
    Environment.AISummarizeRecord(
        { Entity: LookUp(Customers, CustomerID = selectedID) }
    ).SummarizedText
)
```

### Legacy AI Builder Functions (Prebuilt Models)

These older AI Builder model calls still work but the newer Power Fx AI functions above are preferred:

| Function | Type | Description |
|---|---|---|
| Sentiment analysis | Prebuilt | Detect positive/negative/neutral sentiment |
| Entity extraction | Prebuilt + Custom | Recognize data elements in text |
| Key phrase extraction | Prebuilt | Identify main talking points |
| Language detection | Prebuilt | Identify text language |
| Category classification | Prebuilt + Custom | Classify text into categories |

```
// Legacy AI Builder syntax (still supported)
Set(result, AIBuilder.SentimentAnalysis.Predict(TextInput1.Text));
Set(entities, AIBuilder.EntityExtraction.Predict(TextInput1.Text));
```

---

## Text Generation with GPT in Power Apps (Preview)

### Overview

Text generation is powered by Azure OpenAI (GPT technology). GPT models generate human-like text from a prompt. Use cases include interactive form filling, report generation, dataset summarization, and chatbot conversations.

**Important**: This preview capability is currently only available in the **United States region**.

### Setup Steps

1. Sign in to Power Apps.
2. Create a new canvas app (Tablet or Phone format).
3. In the Data pane, select **Add data** > **AI models**.
4. Select **Create text with GPT** (or other available models).
5. If the model is not visible, contact your administrator for permissions.

### Binding to a Control

Bind the model prediction to a control event (e.g., Button.OnSelect):

```
// On a Button's OnSelect event:
Set(
    TextCompletionResult,
    'Create text with GPT'.Predict(TextInput1.Text)
);

// Display the result in a Label's Text property:
TextCompletionResult
```

The `.Predict()` method accepts a string prompt and returns generated text.

### Parameters

Input and output parameters match the Power Automate text generation action:

**Input Parameters:**

| Name | Required | Type | Description |
|---|---|---|---|
| Prompt/instructions | Yes | String | The instruction or prompt for the model |

**Output Parameters:**

| Name | Type | Description |
|---|---|---|
| Text | String | The generated text response |
| Finish reason | String | Reason the model stopped generating (e.g., "stop", "length") |

---

## Text Generation with GPT in Power Automate

### Current Status

> The old "Create text with GPT" action in Power Automate is **deprecated**. Use the new **prompt builder** action ("Create text using a prompt") instead.

### Migration from Deprecated Action

If you have flows using the old "Create text with GPT" action:

1. Copy the prompt text from the old action in your flow.
2. Go to the Power Automate portal and create a **custom prompt** using that prompt text.
3. Note: The new prompt experience requires at least one dynamic parameter. If your old prompt had none, add a dummy parameter that you leave empty at runtime.
4. Replace the old action with **"Create text using a prompt"** and select your new custom prompt.
5. Update downstream actions that reference the GPT action output.

### Building a Flow with Text Generation (Legacy Reference)

GPT prompts have two parts: the **instruction** (what the model should do) and the **context** (information needed to follow the instruction). In automation, the instruction is constant and the context comes from dynamic content.

1. Create an instant cloud flow (or automated cloud flow).
2. Add a manual trigger with a Text input.
3. Add the AI Builder **"Create text with GPT"** action (or new prompt action).
4. Enter instructions and sample context.
5. Replace sample context with dynamic content from previous steps.

### Human Oversight Pattern

AI-generated content requires human review before use. Standard pattern:

1. Generate text with GPT action.
2. Add an **Approvals** action: "Start and wait for an approval of text".
3. Add a **Condition** checking `Outcome` = "Approve".
4. If approved, proceed (e.g., send email using `Accepted text` from the approval step).
5. The reviewer can accept, edit, or reject the AI-generated text.

---

## AI Builder Prompts (Prompt Builder)

### Overview

A prompt is a natural language instruction that tells a generative AI model to perform a task. The model follows the prompt to determine the structure and content of the output text. Prompts run on language models powered by **Azure Foundry** (Azure OpenAI Service).

**Prompt builder** is a maker experience for building, testing, and saving reusable prompts. Prompts support:
- Input variables for dynamic context at runtime.
- Knowledge data sources (e.g., Dataverse) for grounded responses.
- Sharing with other makers and use in agents, workflows, or apps.

### Prerequisites

- Environment must be in a supported region.
- Copilot Credits required.
- Microsoft Dataverse installed on the environment.

### Supported Languages

Arabic, Chinese (Simplified), Czech, Danish, Dutch, English (US), Finnish, French, German, Greek, Hebrew, Italian, Japanese, Korean, Polish, Portuguese (Brazil), Russian, Spanish, Swedish, Thai, Turkish.

### Prompt Anatomy

Every prompt has two parts:

| Part | Description | Example |
|---|---|---|
| **Instruction** | What the model should do | "Summarize this email in three bullets" |
| **Context** | Information needed for an appropriate response | "The email contains customer feedback from the past week" |

### Good Prompt Characteristics

- **Clear and concise**: Easy to understand language.
- **Specific**: Guides the model in the right direction.
- **Contextual**: Provides enough context for meaningful output.
- **Relevant**: Related to the task with sufficient information.

### What to Include in a Prompt

- The topic or task.
- Keywords or phrases associated with the topic.
- Desired tone of the response.
- Target audience.
- Output format constraints (length, structure, style).

### Creating a Custom Prompt

**Access points:**
- **Power Apps**: AI hub > Prompts > Build your own prompt.
- **Power Automate**: AI hub > Prompts > Build your own prompt.
- **Copilot Studio** (multiple paths):
  - Agents > pick/create agent > Tools > Add a tool > New tool > Prompt.
  - Agents > pick/create agent > Topics > pick/create topic > Add node > Add a tool > New prompt.
  - Tools > Add a tool > New tool > Prompt (reusable across any agent).

**Steps:**
1. Enter a custom name for your prompt.
2. Write your prompt instruction or choose a template.
3. Add input variables: type `/` or select **Add content** > Text / Image / Document.
4. Optionally add a **knowledge** object (data source connection like Dataverse) for grounded responses.
5. Type sample values for each input.
6. Select **Test** to run the prompt and review its response.
7. Iterate on the prompt until satisfied.
8. Select **Save**.

### Using Prompts in Copilot Studio

In Copilot Studio, prompts can serve as:

- **Agent tools**: Improve chat experience by calling prompts during conversation.
- **Advanced AI automations**: Infuse AI actions into deterministic workflow nodes.
- **Topic actions**: Add a prompt as a node within a topic's conversation flow.

### Prompt Engineering Patterns

**Pattern 1: Structured output**
```
Analyze the following customer feedback and return a JSON object with these fields:
- sentiment: "positive", "negative", or "neutral"
- topics: array of main topics mentioned
- urgency: "high", "medium", or "low"
- suggested_action: brief recommendation

Feedback: [InputText]
```

**Pattern 2: Role-based instruction**
```
You are a professional customer service agent for [CompanyName].
Respond to the following customer inquiry in a friendly, helpful tone.
Keep the response under 150 words.
If you cannot answer, suggest the customer contact support.

Customer message: [InputMessage]
```

**Pattern 3: Chain-of-thought for classification**
```
Classify the following support ticket into exactly one category.
Think step by step:
1. Identify the main issue described.
2. Consider which category best matches.
3. Output only the category name.

Categories: Billing, Technical, Account, Feature Request, Other

Ticket: [TicketText]
```

**Pattern 4: Data extraction with format**
```
Extract the following information from the provided text.
Return the result as a numbered list.
If a field is not found, write "N/A".

Fields to extract:
- Full name
- Email address
- Phone number
- Company name
- Request type

Text: [InputDocument]
```

**Pattern 5: Summarization with constraints**
```
Summarize the following document in exactly 3 bullet points.
Each bullet should be one sentence, maximum 25 words.
Focus on actionable insights, not background information.

Document: [InputText]
```

---

## Copilot Studio Overview

Copilot Studio is the platform for customizing and extending copilot behavior across Power Platform. It enables makers to build custom agents, extend Microsoft 365 Copilot, and manage AI-powered experiences.

### Key Functions

- **Prompt builder**: Create reusable generative AI prompts with input variables and knowledge sources. Prompts use Azure OpenAI models (GPT-4o / GPT-4o mini).
- **Topic management**: Define conversation topics and responses for copilots embedded in apps.
- **Action configuration**: Connect copilot to Power Automate flows and external services.
- **Knowledge management**: Attach Dataverse data and other sources to copilot responses.

### Extending Agent Capabilities

Copilot Studio lets you extend agents using multiple mechanisms:

| Mechanism | Description |
|---|---|
| **Topics** | Define conversation flows with trigger phrases and response nodes |
| **Tools** | Connect to Power Platform connectors, custom connectors, or AI prompts |
| **Knowledge sources** | Ground responses with enterprise data from Dataverse, SharePoint, websites |
| **Other agents (preview)** | Compose multiple agents together for specialized capabilities |

### Connectors as Tools and Knowledge

Tools and knowledge sources that access external services use **connectors**:

- **Prebuilt connectors**: Ready-to-use integrations (SharePoint, Outlook, SQL Server, etc.)
- **Custom connectors**: Connect to your own APIs and enterprise systems.

Connectors can link to:
- Data sources within Microsoft 365 productivity cloud.
- Business data in Dynamics 365.
- Analytical data in Microsoft Fabric.
- Non-Microsoft enterprise data sources.

### Extending Microsoft 365 Copilot

You don't extend M365 Copilot directly with tools/knowledge. Instead:

1. **Create an agent** in Copilot Studio.
2. **Add tools and knowledge** to the agent.
3. **Publish the agent** and make it available to Microsoft 365 Copilot.

### Requirements for Extending Agents

| Requirement | Details |
|---|---|
| Maker access | Access to the agent you want to extend |
| License | Copilot Studio license for the maker |
| Data sources | Enterprise data sources to integrate |
| Connection info | Connector details, API endpoints, credentials |
| Admin approval | Administrator must enable the extension after publishing |

### Integration Points

- Customize Copilot control behavior in canvas apps.
- Customize model-driven app copilot responses.
- Build standalone copilot agents with custom logic.
- Manage AI prompts used across Power Apps and Power Automate.
- Extend Microsoft 365 Copilot with purpose-built agents.
- Use Power Platform connectors as both tools and knowledge sources.

---

## GPT Model Selection and Configuration

### Available Models

AI Builder and Copilot Studio prompts use Azure OpenAI models. The platform manages model selection, but understanding the underlying models helps with prompt design:

| Model | Use Case | Characteristics |
|---|---|---|
| GPT-4o | Complex reasoning, multi-step tasks | Higher accuracy, more capable, higher token cost |
| GPT-4o mini | Simple classification, extraction, translation | Faster, lower cost, good for high-volume scenarios |

**Note**: Model selection is managed by the platform. Makers do not directly choose which model runs their prompt. The platform routes requests based on task complexity and availability.

### Token and Length Considerations

- Prompts have input token limits. Keep instructions concise and context focused.
- Output length can be influenced by prompt instructions (e.g., "respond in 50 words or less").
- Very long inputs may be truncated. For document-heavy scenarios, consider chunking text before passing to the model.

### Temperature and Creativity

- The platform manages temperature settings (creativity vs. determinism).
- For more deterministic outputs, use explicit format constraints in your prompt (e.g., "Return only JSON", "Answer with exactly one word").
- For creative outputs, use open-ended instructions (e.g., "Write a friendly response", "Suggest ideas for...").

---

## Governance and Administration

### Copilot Feature Lifecycle

| Stage | Admin Control | Description |
|---|---|---|
| Preview | Toggle Off available | Admin can disable at environment or tenant level |
| Generally Available | Cannot toggle Off | Contact Microsoft Support to disable |
| Deprecated | N/A | Feature removed; migrate to replacement |

### Data Residency and Cross-Geo Sharing

- In regions **with** GPU infrastructure (US, UK, Australia, India): AI processing occurs within the region. Copilot is on by default.
- In regions **without** GPU infrastructure: Cross-geo data sharing is enabled by default to route requests to the nearest GPU-equipped region. Disable by toggling off cross-geo sharing at the tenant level.
- **Sovereign clouds**: Copilot features are not available.

### Admin Control Matrix

| Feature | Environment Toggle | Tenant Toggle | Support Request | Notes |
|---|---|---|---|---|
| Copilot in Power Apps (preview) | Yes | Yes | No | Affects makers only |
| Copilot in Power Apps (GA) | No | No | Yes | Contact Support to disable |
| Copilot control in canvas apps | Separate setting | Separate setting | No | Independent of maker Copilot toggle |
| Copilot in model-driven apps | Separate setting | Separate setting | No | Independent of maker Copilot toggle |
| Copilot in Power Automate (GPU regions) | No | No | Yes (PowerShell) | Tenant-level only |
| Copilot in Power Automate (non-GPU regions) | No | Yes (cross-geo toggle) | No | Toggle off cross-geo sharing |
| AI Builder prompts | Environment region | Copilot credits | No | Requires supported region + credits |

### Copilot Credits

AI Builder prompts and AI functions consume **Copilot Credits** (formerly AI Builder credits). Key points:
- Credits are pooled at the tenant level.
- Different AI operations consume different amounts of credits.
- Monitor usage in the Power Platform admin center under Capacity.
- When credits are exhausted, AI features stop working until the next billing cycle or additional credits are purchased.

### Security and Compliance Considerations

- AI-generated content should always undergo **human oversight** before external use.
- Data sent to Azure OpenAI models is processed according to Microsoft's data processing terms.
- Prompts and responses are not used to train or improve Microsoft's foundation models.
- Audit logs track AI feature usage within the environment.
- DLP policies can be configured to control which connectors and AI capabilities are available in each environment.

---

## Common Patterns

### Pattern 1: Copilot-Enhanced Canvas App

Build canvas app with Dataverse data > Add Copilot control (or migrate to M365 Copilot Chat) > Connect Dataverse tables > Customize in Copilot Studio > End users interact via natural language.

### Pattern 2: Power Fx + AI Functions in Canvas Apps

Use the `Environment` namespace in the formula bar to call AI functions directly on control events. No component insertion required. Store results in global variables with `Set()`.

```
// On a button press, classify and analyze customer feedback
Set(Category, Environment.AIClassify({
    Text: txtFeedback.Text,
    Categories: Table(
        {Value: "Bug"}, {Value: "Feature"}, {Value: "Question"}
    )
}).Classification);

Set(Sentiment, Environment.AISentiment({
    Text: txtFeedback.Text
}).AnalyzedSentiment);
```

### Pattern 3: AI Prompts in Automation

Create reusable prompt in Copilot Studio > Use "Create text using a prompt" action in Power Automate > Pass dynamic content as input > Use output for summarization, classification, or response generation > Include human approval step before external use.

### Pattern 4: Multi-AI Pipeline in Power Automate

Chain multiple AI actions in a single flow:

1. **Trigger**: When a new email arrives.
2. **Sentiment analysis**: Determine if the email is positive, negative, or neutral.
3. **Classification**: Categorize the email (billing, support, sales).
4. **Text generation**: Draft an appropriate response using a custom prompt.
5. **Approval**: Route the draft for human review.
6. **Send**: If approved, send the response.

### Pattern 5: Copilot Studio Agent with Tools and Knowledge

1. Create a custom agent in Copilot Studio.
2. Add **knowledge sources** (Dataverse tables, SharePoint sites) for grounded responses.
3. Add **tools** (Power Automate flows, custom connectors) for actions.
4. Define **topics** for structured conversation flows.
5. Add **prompts** as tools for flexible AI-powered responses.
6. Publish and deploy to Teams, websites, or M365 Copilot.

### Pattern 6: Document Processing Pipeline

1. Receive document (email attachment, SharePoint upload).
2. Extract text from document.
3. Use `AISummarize` to create a brief summary.
4. Use `AIExtract` to pull out key entities (names, dates, amounts).
5. Use `AIClassify` to categorize the document type.
6. Store results in Dataverse for downstream processing.

---

## Regional Availability Quick Reference

| Feature | US | UK | Australia | India | EU (non-GPU) | Other |
|---|---|---|---|---|---|---|
| Copilot in Power Apps | Yes | Yes | Yes | Yes | Yes (cross-geo) | Varies |
| Copilot in Power Automate | Yes | Yes | Yes | Yes | Yes (cross-geo) | Varies |
| AI Functions in Power Fx | Yes | Yes | Yes | Yes | Check docs | Check docs |
| Text Generation (preview) | Yes | No | No | No | No | No |
| AI Builder Prompts | Yes | Yes | Yes | Yes | Yes | Check region list |
| Copilot Studio | Yes | Yes | Yes | Yes | Yes | Check region list |

**Note**: Availability changes frequently. Always verify current availability at "Explore Copilot features by geography and languages" in Microsoft Learn.
