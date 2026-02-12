# Workspace & Enterprise

## Table of Contents
- [Google Workspace Flows](#google-workspace-flows)
- [Gemini in Chrome](#gemini-in-chrome)
- [Gemini TV](#gemini-tv)
- [Vertex AI](#vertex-ai)
- [Vertex AI Agent Builder](#vertex-ai-agent-builder)
- [Agent Payments Protocol (AP2)](#agent-payments-protocol-ap2)
- [Enterprise Features](#enterprise-features)

## Gemini in Google Workspace (Docs, Sheets, Slides)

Gemini AI features included in all Business and Enterprise Workspace plans at no additional cost (since Jan 2025). Accessible via side panel in Gmail, Docs, Sheets, Slides, Drive, and Chat.

**Docs**: "Help me refine" AI writing tool, full audio versions of documents, podcast-style overviews
**Sheets**: Auto-analyze data, surface key insights, multi-step tasks with expanded editing (Oct 2025)
**Slides**: Image generation from descriptions, slide generation, content rewriting via side panel
**Gmail**: Smart replies, email summaries, draft generation
**Drive**: File search and summarization across documents

## Google Workspace Flows / Workspace Studio

No-code AI automation platform. Originally launched as "Workspace Flows" (flows.workspace.google.com), rebranded to **Google Workspace Studio** (workspace.google.com/studio/).

**What it does**: Build automated workflows using AI-powered agents ("Gems") that connect Google Workspace apps with third-party services. No code or complex logic configuration needed.

**Key capabilities**:
- AI-powered custom agents that understand context, analyze data, generate content
- Natural language task description for workflow creation
- Cross-app triggers: Gmail actions from Calendar events, Sheets updates from Drive shares, auto-scheduling from emails
- Email automation (auto-respond, sort, summarize, draft)
- Meeting summaries and action item extraction
- Document processing and data extraction
- CRM integration workflows
- Multi-step conditional automations

**Example workflows**:
- Auto-summarize meeting notes and email to attendees
- Extract invoice data from emails, populate Sheets
- Monitor Gmail for specific topics, create calendar events
- Weekly report generation from multiple data sources

**Availability**: GA with all Business and Enterprise Workspace plans (late 2025). Early adopter Karcher reported 90% reduction in drafting time.

## Gemini in Chrome

Gemini AI integrated directly into the Chrome browser. Rolling out to all US Chrome users for free.

**Access**: Sparkle icon in top-right corner of Chrome.

**Key features**:
- **Page-aware AI**: Understands the content of your current web page
- **Multi-tab awareness**: Can see and synthesize information across all open tabs
- **Browsing history search**: Semantic search of past browsing (find pages by description, not just keywords)
- **Omnibox AI mode**: Ask complex questions directly in the address bar
- **Contextual suggestions**: Relevant actions based on page content (convert recipe measurements, find better prices, etc.)
- **Scam detection**: AI-powered identification of phishing, fake alerts, suspicious sites
- **Text highlighting**: Select text on any page for instant AI analysis

**Multi-tab example**: Planning a trip with 5 tabs open (flights, hotels, restaurants, activities, weather). Ask Gemini to create a complete itinerary synthesizing all tabs.

**Integration with Google apps**: Ask Gemini to add an event to Calendar from a web page, find a moment in a YouTube video, get directions from a mentioned address.

**Availability**: Starting with English/US on Mac and Windows desktop. Mobile (Android/iOS) coming soon. Enterprise via Google Workspace with data protection controls.

**AI agents in Chrome** (coming soon): Autonomous agents that can complete web tasks (book haircuts, order groceries, fill forms) while you stay in control.

## Gemini TV

Gemini AI built into Google TV (first available on TCL QM9K series TVs).

**Key features**:
- Full conversational AI on TV (not just voice commands)
- Presence sensing: TV detects when you enter/leave the room
- Content discovery: describe preferences for personalized recommendations
- Educational assistant: explain topics at any level, show relevant videos
- Show recaps: get season summaries for any show
- Connected to YouTube, Google Search, and all Google data
- Faster responses than old Google Assistant

**Hardware**: TCL QM9K series (65" starts at ~$3,000). More brands coming (Hisense, Sony).

**Privacy controls**: Disable always-listening, turn off presence sensing, delete conversation history.

## Vertex AI

Google Cloud's unified enterprise AI platform for deploying and managing AI at scale.

**Key services**:
- **Model Garden**: 200+ enterprise-ready models (Gemini 3, Anthropic Claude, Llama, open-source)
- **Agent Engine**: GA. Build production AI agents with tool orchestration
- **Model tuning**: Fine-tune Gemini and Gemma on your data (Gemini 2.0 Flash fine-tuning GA)
- **Model evaluation**: Compare model performance on your tasks
- **Vector search**: Build RAG applications with managed embeddings
- **Pipelines**: MLOps for training and deployment workflows
- **Endpoints**: Deploy models with auto-scaling
- **Feature Store**: Managed feature engineering
- **Prompt optimizer**: GA. Auto-optimize prompts for better performance
- **Context caching**: GA for Gemini models (reduced cost for repeated queries)

**Gemini on Vertex**:
- Same models as AI Studio but with enterprise SLAs
- VPC-SC support for data residency
- Customer-managed encryption keys (CMEK)
- Audit logging and monitoring
- Higher rate limits and quotas
- Batch prediction for processing large datasets
- Veo 3 and Veo 3 Fast (GA for video generation)
- Tool governance via Agent Builder Console

**Pricing**: Pay-per-use (per token for Gemini, per node-hour for custom models) plus infrastructure costs.

## Vertex AI Agent Builder

Build and deploy production AI agents on Google Cloud.

**Components**:
- **Agent Development Kit (ADK)**: Build production-ready agents in under 100 lines of code (Python, Java, more coming)
- **Agent Engine**: Fully-managed runtime with Sessions, Memory Bank, and Code Execution services
- **Agent Designer**: Low-code visual canvas for orchestrating agents/subagents; exportable to ADK code
- **Agent Garden**: Library of sample agents and prebuilt solutions for common use cases
- **Tools**: Function calling, data store search, code execution, Google Search
- **Data stores**: Connect structured/unstructured data for RAG

**Governance**: Cloud API Registry integration for tool governance — administrators manage available tools across organizations via Agent Builder Console.

**Integration**: Works with Dialogflow CX for complex conversational flows. Connects to Cloud Functions, BigQuery, Firestore, and any REST API.

**Pricing** (Jan 28, 2026): Memory $0.009/GB-hr, Sessions/Memory Bank $0.25/1K events, first 10K search queries/month free, $300 free credit for 90 days for new customers.

## Agent Payments Protocol (AP2)

Google's protocol enabling AI agents to handle financial transactions autonomously.

**How it works**:
1. **Intent mandate**: Captures what you want to purchase
2. **Cart mandate**: Provides final approval with exact details
3. **Detailed mandates**: Set conditions for auto-purchase (budget limits, preferences)

**Security**: Cryptographically signed digital contracts (mandates). User maintains control at every step.

**Backed by**: 60+ companies including Mastercard, PayPal, American Express, Coinbase.

**Use cases**:
- AI agent finds best deals and completes purchases
- Automated subscription management
- Office supply auto-reordering
- Vendor contract renewals
- Price monitoring and opportunistic buying

## Agent Protocols & Interoperability

Google's protocol stack for AI agent ecosystems:

- **Model Context Protocol (MCP)**: Google officially adopted MCP. Managed MCP servers launched Dec 2025 for enterprise-ready agent connectivity across all Google services.
- **Agent2Agent (A2A)**: Protocol for AI agents to communicate, exchange information, and coordinate actions across platforms.
- **A2UI (Agent-to-UI)**: Open project enabling agents to generate the best-suited UI for the current conversation and send it to a front-end app.
- **Universal Commerce Protocol** (Jan 2026): Open-source standards for AI agents to execute purchases across retail platforms without custom merchant integrations.

## Enterprise Features

**Data protection**:
- Data residency controls
- No training on enterprise data (Workspace/Vertex)
- VPC Service Controls
- Customer-managed encryption keys
- DLP integration
- Audit logging

**Admin controls**:
- User-level access management
- Usage monitoring and reporting
- Content filtering policies
- Model access restrictions
- API quota management

**Security tools**:
- **Model Armor**: Proactively screens for malicious/unsafe interactions
- **Client-side encryption (CSE)**: Protected data indecipherable to third parties including Google
- **External Key Manager (EKM)** and **HSM with CMEK**: GA (with allowlist)

**Compliance**: ISO 42001, ISO 27001, SOC 2, PCI DSS, HIPAA (Vertex AI + NotebookLM Enterprise), FedRAMP High, BSI C5

**Support**: 24/7 enterprise support with dedicated account teams for Vertex AI Enterprise
