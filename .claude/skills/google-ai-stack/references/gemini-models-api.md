# Gemini Models & API Reference

## Table of Contents
- [Model Family Overview](#model-family-overview)
- [Gemini 2.5 Pro](#gemini-25-pro)
- [Gemini 2.5 Flash](#gemini-25-flash)
- [Gemini Deep Think](#gemini-deep-think)
- [Gemma Open-Source Models](#gemma-open-source-models)
- [API Basics](#api-basics)
- [Pricing](#pricing)
- [Function Calling](#function-calling)
- [Grounding with Google Search](#grounding-with-google-search)
- [Structured Output](#structured-output)
- [System Instructions](#system-instructions)
- [Context Caching](#context-caching)
- [Safety Settings](#safety-settings)
- [File Upload API](#file-upload-api)
- [Multimodal Capabilities](#multimodal-capabilities)

## Model Family Overview

| Model | Best For | Context Window | Speed |
|-------|----------|---------------|-------|
| Gemini 3 Pro | Flagship reasoning, agentic tasks, complex coding | 1M tokens (output: 65K) | Medium |
| Gemini 3 Flash | Speed-optimized frontier intelligence, default model | 1M tokens | Very Fast (218 tok/s) |
| Gemini 3 Deep Think | Parallel reasoning, Olympiad-level problem solving | 1M tokens | Slow (deliberate) |
| Gemini 2.5 Pro | Complex reasoning, coding, long-context tasks | 1M tokens | Medium |
| Gemini 2.5 Flash | Cost-efficient, real-time apps | 1M tokens | Fast |
| Gemma 3 | On-device, open-source, fine-tuning | Varies (8K-128K) | Fast |

**Gemini 3** (announced Nov 18, 2025) is the current generation. Accepts text, images, video, audio, PDFs. Supports Computer Use tool natively. Unified across consumer and enterprise platforms.

## Gemini 3 Pro

- State-of-the-art reasoning and multimodal understanding
- 1M token context window (2M for enterprise), 65K token output cap
- >99% retrieval accuracy across full context window (~1,500 pages of text, ~50K lines of code)
- Strong agentic and coding capabilities
- Native Computer Use support
- Natively multimodal: processes text, images, video, audio, PDFs in single architecture
- Available via Gemini API, AI Studio, Gemini CLI, Android Studio, Vertex AI, Gemini Enterprise

## Gemini 3 Flash (released Dec 17, 2025)

- Frontier intelligence optimized for speed; default model in Gemini app
- 3x faster than Gemini 2.5 Pro, 218 tokens/second
- 69% cheaper than Gemini 2.5 Pro, <25% cost of Gemini 3 Pro
- Beats Gemini 2.5 Pro on 18 out of 20 benchmarks
- Key benchmarks: GPQA Diamond 90.4%, SWE-bench Verified 78%
- Best value model for most workloads

## Gemini 2.5 Pro

- Previous-gen flagship, still widely available
- 1M token context window
- Strong at code generation, analysis, structured output, long-document understanding
- Native tool use (function calling, code execution, Google Search grounding)

## Gemini 2.5 Flash

- Previous-gen speed model
- Same 1M context window
- "Thinking" mode available (configurable thinking budget)
- Ideal for Build mode in AI Studio where fast iteration matters

## Gemini Deep Think

- Advanced parallel reasoning mode: generates many ideas simultaneously, revises and combines them
- Gemini 3 Deep Think (Dec 2025), major upgrade Feb 12, 2026
- Achievements: Gold medal at ICPC World Finals (10/12 problems, solved Problem C no human team could), Gold medal at International Math, Physics, and Chemistry Olympiads
- Found a logical flaw in a math paper that passed human peer review
- Available to AI Ultra subscribers and via API with thinking budget parameter
- Best for: complex open-ended challenges, science, engineering, enterprise workflows

## Gemma Open-Source Models

Google's open-weight model family, built from the same research powering Gemini.

**Gemma 3 sizes**: 270M, 1B, 4B, 12B, 27B parameters

**Key specs**:
- 128K token context window (16x larger than previous Gemma)
- Multimodal (image + text) on 4B, 12B, 27B; text-only on 270M, 1B
- 35+ languages out-of-the-box, 140+ pretrained
- Function calling support with specific syntax
- Outperforms Llama3-405B, DeepSeek-V3, o3-mini on LMArena human preference

**Deployment**: Most capable model that runs on a single GPU/TPU. Quantized versions run on consumer GPUs, laptops, and smartphones.

**Available on**: Hugging Face, Kaggle, Google AI Studio

**Gemma 3n** (preview mid-2025): Mobile-first architecture
- E2B (~2GB RAM) and E4B (~3GB RAM) variants, despite 5B/8B raw parameters
- MatFormer nested transformer for elastic inference; Per-Layer Embeddings (PLE) for RAM reduction
- 13x speedup over Gemma 3 with quantization; 4x smaller memory footprint
- Multimodal: text, vision, and audio input; MobileNet-V5 vision encoder

**Ideal for**: On-device deployment, privacy-sensitive apps, custom fine-tuning, research, edge computing

## API Basics

**Base URL**: `https://generativelanguage.googleapis.com/v1beta/`

**Authentication**: API key (free tier available) or OAuth for Vertex AI

**SDKs (GA since May 2025)**: Python, JavaScript/TypeScript, Go, Java

**Quick start (Python)**:
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-pro")
response = model.generate_content("Your prompt here")
print(response.text)
```

**Quick start (REST)**:
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent?key=YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"Your prompt"}]}]}'
```

**Additional SDKs**: Dart/Flutter, Swift, Android (Kotlin/Java)

**API key setup**: Get free key at aistudio.google.com > "Get API Key"

**Gemini 3 API features**:
- `thinking_level` parameter: controls max depth of model reasoning before responding
- **Thought Signatures**: encrypted representations of internal thought process, passable in subsequent API calls to maintain reasoning chains
- **Interactions API**: embed Deep Research agent capabilities into applications
- Gemini 3 knowledge cutoff: January 2025

**Deprecation notice**: Gemini 2.0 Flash and Flash-Lite retire **March 31, 2026** (some services discontinue Flash-Lite on Feb 25, 2026). Migrate to `gemini-2.5-flash` or `gemini-3.0-pro`. Post-deprecation, API calls will fail with errors. Gemini 2.5 Flash is cost-competitive with 2.0 versions.

## Pricing

**Free tier** (AI Studio, Feb 2026):
- Gemini 2.5 Pro: 5 RPM, 250K TPM, 100 requests/day
- Gemini 2.5 Flash: 10 RPM, 250K TPM, 250 requests/day
- No credit card required; generous for prototyping

**Pay-as-you-go** (approximate, check latest):
- Gemini 2.5 Flash: ~$0.15/M input tokens, ~$0.60/M output tokens
- Gemini 2.5 Pro: ~$2.50/M input tokens, ~$15/M output tokens
- Thinking tokens billed separately at reduced rates
- Image generation: per-image pricing
- Context caching: reduced input pricing for cached portions

**Vertex AI pricing**: Similar per-token pricing, plus infrastructure costs, enterprise SLAs

## Function Calling

Enables Gemini to call external functions/APIs structured as tools.

```python
tools = [
    genai.types.Tool(
        function_declarations=[{
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"}
                },
                "required": ["location"]
            }
        }]
    )
]
model = genai.GenerativeModel("gemini-2.5-pro", tools=tools)
```

- Model decides when to call functions based on conversation context
- Supports parallel function calls
- Works with any external API or local function
- Combine with grounding for real-time data retrieval
- **Built-in MCP support**: Gemini SDKs have native Model Context Protocol support, reducing boilerplate for MCP tools

## Grounding with Google Search

Connects Gemini to real-time web data via Google Search.

```python
model = genai.GenerativeModel(
    "gemini-2.5-pro",
    tools=[genai.types.Tool(google_search_retrieval=genai.types.GoogleSearchRetrieval())]
)
```

- Provides cited, up-to-date information
- Response includes source URLs for verification
- Reduces hallucination for factual queries
- Combines with function calling for hybrid retrieval
- **Gemini 3 pricing**: $14 per 1,000 search queries (down from $35/1K flat rate), usage-based for agentic workflows
- Also available through Firebase AI Logic for client-side apps

## Structured Output

Force Gemini to return JSON matching a specific schema.

```python
response = model.generate_content(
    "Extract product info from this text...",
    generation_config=genai.types.GenerationConfig(
        response_mime_type="application/json",
        response_schema={
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "number"},
                "category": {"type": "string"}
            }
        }
    )
)
```

- Guarantees valid JSON output
- Full JSON Schema support (Nov 2025): `anyOf`, `$ref`, property ordering preserved
- Pydantic (Python) and Zod (TypeScript) work out-of-the-box
- Essential for programmatic consumption of AI output

## System Instructions

Set persistent behavior and persona for the model.

```python
model = genai.GenerativeModel(
    "gemini-2.5-pro",
    system_instruction="You are a helpful coding assistant. Always provide code examples in Python. Be concise."
)
```

- Persists across the entire conversation
- More reliable than putting instructions in user messages
- Use for: persona, output format, domain constraints, safety guardrails

## Context Caching

Cache large inputs (documents, code) to reduce cost and latency on repeated queries.

```python
cache = genai.caching.CachedContent.create(
    model="gemini-2.5-pro",
    contents=[large_document],
    ttl=datetime.timedelta(hours=1)
)
model = genai.GenerativeModel.from_cached_content(cache)
```

- Minimum 32K tokens to cache
- Cached tokens billed at reduced rate
- TTL-based expiration (configurable)
- Ideal for: chatbots over fixed documents, repeated analysis of same codebase

## Safety Settings

Configure content filtering thresholds per category.

```python
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
```

- Four harm categories with configurable thresholds
- BLOCK_NONE, BLOCK_ONLY_HIGH, BLOCK_MEDIUM_AND_ABOVE, BLOCK_LOW_AND_ABOVE
- Enterprise users can set more permissive thresholds
- Safety ratings returned with every response

## File Upload API

Upload files for multimodal processing (images, audio, video, documents).

```python
file = genai.upload_file("document.pdf", display_name="My Document")
response = model.generate_content(["Summarize this document", file])
```

- Supports: images (PNG, JPEG, WebP, GIF), audio (MP3, WAV, FLAC), video (MP4, MOV), documents (PDF, plain text)
- **API**: Up to 50MB and 1,000 pages per PDF; **Consumer app**: Up to 100MB, 10 files per prompt
- Files stored temporarily (48h default)
- PDF: native vision-based processing (text, images, diagrams, charts, tables, scanned handwriting)
- Video: can process hours of video content
- Audio: supports transcription and analysis
- Drive enhancements: PDF summary cards (Jun 2025), audio PDF summaries (Nov 2025)

## Live API (Real-Time Streaming)

Low-latency, real-time voice and video interactions with Gemini.

**Key features**:
- WebSocket-based bidirectional streaming (audio, video, text)
- Voice Activity Detection (automatic speech detection)
- Tool use and function calling during live conversations
- Session management for long-running conversations
- Ephemeral tokens for secure client-side auth
- 30 HD voices in 24 languages
- Server-to-server architecture: client → backend → Live API

**Current model**: `gemini-2.5-flash-native-audio-preview-12-2025`

**Use cases**: Voice assistants, real-time translation, manufacturing monitoring, customer service, interactive tutoring

## Multimodal Capabilities

Gemini natively processes multiple input types in a single request:

- **Text + Image**: Describe, analyze, extract text (OCR), compare images
- **Text + Video**: Summarize videos, find specific moments, answer questions about video content
- **Text + Audio**: Transcribe, translate, analyze tone, answer questions about audio
- **Text + PDF**: Extract tables, summarize, answer questions about documents
- **Image + Text generation**: Generate images from text descriptions (via Imagen/Nano Banana integration)
- **Live API**: Real-time bidirectional audio/video streaming for conversational AI with camera input
