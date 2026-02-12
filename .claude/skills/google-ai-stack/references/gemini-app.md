# Gemini App Features

## Table of Contents
- [Overview](#overview)
- [Pricing Tiers](#pricing-tiers)
- [Gems (Custom AI Assistants)](#gems)
- [Deep Research](#deep-research)
- [Canvas](#canvas)
- [Connected Apps](#connected-apps)
- [Scheduled Actions](#scheduled-actions)
- [Gemini Live](#gemini-live)
- [Personal Intelligence](#personal-intelligence)
- [Dynamic View](#dynamic-view)
- [Image Generation & Editing](#image-generation--editing)
- [Video Generation](#video-generation)
- [Gemini Agent](#gemini-agent)

## Overview

The Gemini app (gemini.google.com) is Google's consumer AI assistant, replacing Google Assistant as the primary AI interface. Available on web, Android, and iOS.

**Key settings**:
- Model selection (Flash for speed, Pro for quality, Deep Think for reasoning)
- Custom instructions (persistent persona/behavior preferences)
- Extensions toggle (Google Workspace, Maps, YouTube, Flights, Hotels)
- Tools toggle (image generation, code execution, Google Search)

## Pricing Tiers

| Tier | Price (US) | Key Features |
|------|------------|-------------|
| Free | $0 | Gemini Flash, limited Thinking/Pro access, 32K context, capped Deep Research |
| Google AI Plus | Mid-tier | More Gemini 3 Pro access, limited Veo 3.1 Fast |
| Google AI Pro | $19.99/month | 100 prompts/day (Thinking/Pro), 20 Deep Research reports/day, 1M context, 2TB Google One storage |
| Google AI Ultra | $249.99/month | 500 prompts/day, 200 Deep Research reports/day, Veo 3.1, Deep Think, highest access |
| Enterprise | $30/user/month | Agentic platform, internal AI agents, connectors, workflow automation |
| Business | $21/user/month | Subset of Enterprise features |

**Note**: Google One slashed prices 50% for 2026 AI Pro plans.

## Gems

Custom AI assistants (similar to GPTs in ChatGPT). Available on **all plans including free**.

**Creating a Gem**:
1. Go to Gems section in Gemini sidebar
2. Name your Gem and describe its purpose
3. Define instructions (persona, knowledge constraints, output format)
4. Optionally upload reference files (up to 10 per Gem)
5. Save and use from sidebar

**Key capabilities**:
- Unlimited Gems with free Google account (uses Gemini 2.5 Flash)
- Up to 10 file uploads per Gem, Google Drive integration
- Persistent custom instructions across conversations
- Shareable with specific people or via link (Drive-style sharing, since Sep 2025)
- Enterprise-level sharing with permission controls
- Available within Gmail, Docs, Sheets, Slides, and Drive via Gemini side panel
- Can connect directly to Google Drive as living documents
- Pre-built Gems: Learning Coach, Brainstormer, Career Guide, Writing Editor, Coding Partner

**Limitations vs ChatGPT Custom GPTs**: 10 files per Gem, no voice mode, no public marketplace, no API connections. But Gems are free vs $20/month for GPTs.

**Best uses**: Brand voice assistant, domain-specific Q&A, standardized report generator, team-specific workflows

## Deep Research

Multi-step autonomous research agent optimized for long-running context gathering and synthesis. Reasoning core uses Gemini 3 Pro, specifically trained to reduce hallucinations.

**How it works**:
1. Provide a research question or topic
2. Gemini creates a research plan (editable before execution)
3. Iteratively: formulates queries, reads results, identifies knowledge gaps, searches again
4. Navigates deep into sites for specific data
5. Produces a comprehensive research report with citations

**Output formats**: Visual reports with charts, data tables, interactive elements, cited sources

**Benchmarks**: 46.4% on Humanity's Last Exam, 66.1% on DeepSearchQA, 59.2% on BrowseComp

**Key features**:
- Editable research plan before execution
- Progress tracking during research
- Citation of all sources
- Multimodal input: images, PDFs, audio, video
- File upload and Google Drive linking
- Workspace integration: pulls from emails, chats, Workspace content
- Available on Flash (free, limited) and Pro/Ultra plans (full)
- Coming to Google Search, NotebookLM, and Google Finance

**Developer access**: Available via the **Interactions API** for embedding research into applications

## Canvas

Interactive workspace within Gemini for writing and coding.

**Writing Canvas**:
- Side-by-side editing environment
- Gemini suggests edits, expansions, rewrites
- Adjust tone, length, reading level
- Export to Google Docs

**Coding Canvas (App Builder)**:
- Describe an app in natural language, Gemini builds it
- Live preview of working app within the canvas
- Iterative refinement: describe changes, see updates instantly
- "Add Gemini features" button to enhance apps with AI capabilities
- **"Vibe coding"**: build fully functional apps with Gemini-powered features, persistent data, and multi-user sharing
- Generate and preview React or HTML code directly
- Export/download code or deploy directly
- Powered by Gemini 2.5 Pro (complex) and Flash (speed)

**Create menu**: Transform text into custom web pages, visual infographics, engaging quizzes, and Audio Overviews

**What Canvas can build**: Web apps, games, interactive quizzes, dashboards, calculators, infographics, data visualizers, 3D worlds, portfolio sites, landing pages

**Pricing**: Free to all Gemini users worldwide

## Connected Apps

Integrates Gemini with Google services for contextual assistance. Pro plan required.

**Personal data connections** (require opt-in):
- **Gmail**: Search emails, draft replies, summarize threads
- **Google Drive**: Search and analyze documents, spreadsheets, presentations
- **Google Calendar**: Check schedule, create events, find availability
- **Google Photos**: Search photos by description, create collages

**Public data integrations** (built-in, no @mention needed since Oct 2025):
- **YouTube**: Search videos, get summaries, find specific moments
- **Google Maps**: Get directions, find places, plan routes
- **Google Flights/Hotels**: Search and compare travel options

**Note**: As of Oct 2025, @YouTube, @Google Maps, @Google Flights, and @Google Hotels were removed as separate @mentions. Their data is now integrated directly—just ask naturally. Available in 40+ languages.

**Privacy**: User controls which apps are connected. Data used only for the current conversation context.

## Scheduled Actions

Recurring automated tasks executed by Gemini on a schedule. Launched June 6, 2025. Pro and Ultra plans only.

**Constraints**:
- Maximum 10 active scheduled actions per account
- Minimum 15-minute interval between executions

**Examples**:
- Daily morning briefing (weather, calendar, news)
- Weekly email digest summaries
- Periodic research updates on specific topics
- Sports team update alerts
- One-off event summaries (e.g., recap award show the next day)

**Setup**: Describe the action and schedule in natural language. Gemini configures the automation.

**Roadmap**: Third-party API call support coming soon.

## Gemini Live

Real-time voice conversation with Gemini. Available on mobile (Android/iOS) in 45+ languages across 150+ countries.

**Features**:
- Natural conversational flow (interrupt mid-sentence, follow-up naturally)
- Multiple voice options, character voices, and accents
- Camera sharing: point phone camera at objects for real-time identification and guidance
- Screen sharing: share what's on your phone screen for contextual help
- Native audio processing (audio-to-audio, no text intermediary)
- Visual overlay: can highlight objects on screen
- Low-latency responses (milliseconds)
- Adaptive speech control (speed up/slow down responses)
- Language learning support (quizzes, conversation practice, phrase rehearsal)

**Coming 2026**: Live speech-to-speech translation via Gemini API (single-voice, multi-speaker, and bidirectional conversation translation).

**Use cases**: Hands-free assistance, real-time translation, visual identification, cooking guidance, DIY help, learning

## Personal Intelligence

Launched January 14, 2026 (beta, US only). Connects Gemini to personal Google apps for deeply personalized assistance. Available on AI Pro and AI Ultra plans.

**How it works**: Gemini reasons across personal data sources:
- Gmail (email content and context)
- Google Photos (visual memories)
- YouTube (watch history and interests)
- Google Search (search patterns)
- Custom instructions and past conversations

**Key capabilities**:
- Retrieves specific details from emails or photos to answer personal questions
- Reasons across complex sources combining text, photos, and video
- Surfaces proactive insights from user data (powered by Gemini 3)
- Off by default; users opt in and choose which apps to connect
- Gemini does not train on personal data

**Coming**: Personal Intelligence expanding to AI Mode (Google Search) later in 2026.

## Dynamic View

Interactive visual layouts for presenting information. Gemini automatically formats complex responses into engaging visual formats.

**Formats include**: Interactive cards, expandable sections, tabbed views, visual comparisons, step-by-step guides with progress indicators

**When triggered**: Automatically when Gemini determines visual presentation would improve understanding (tutorials, comparisons, multi-step instructions)

## Image Generation & Editing

Powered by Nano Banana (Imagen 4) directly within Gemini.

**Generation**:
- Text-to-image with natural language prompts
- Supports text rendering in images (logos, infographics, memes)
- Multiple styles: photorealistic, illustration, painting, neon, etc.
- Character consistency across multiple generations

**Editing** (upload existing image + describe changes):
- Background replacement/modification
- Object removal (intelligently fills removed area)
- Style transfer (change artistic style while preserving content)
- Local edits (blur background, change colors, add/remove elements)
- Pose alteration
- Black & white to color restoration
- Multi-image fusion (combine elements from multiple images)

**Key advantage**: Conversational editing - make sequential edits in the same chat, Gemini maintains context across edits.

## Video Generation

Powered by Veo 3 / Veo 3.1 within Gemini.

- Text-to-video generation
- Image-to-video (animate still images)
- Includes native audio/sound effects
- Up to 1080p resolution
- Available on YouTube Shorts for free (Veo 3 Fast)
- Speech-to-song capability (remix quotes into music via Lyria 2)

## Gemini Agent

Multi-step task automation within Gemini. The AI autonomously:
1. Plans a sequence of actions
2. Executes steps (web browsing, searching, tool use)
3. Reports results

**Computer Use**: Gemini can control a browser - click buttons, fill forms, navigate websites, extract data. Useful for: data scraping, form filling, price monitoring, competitive research.

**Examples**: Book a haircut, order groceries, compare products across websites, fill out applications
