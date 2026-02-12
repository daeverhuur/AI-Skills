# Google AI Studio

## Table of Contents
- [Overview](#overview)
- [Build Mode](#build-mode)
- [Chat Mode](#chat-mode)
- [Prompt Engineering](#prompt-engineering)
- [API Key Management](#api-key-management)
- [App Deployment](#app-deployment)
- [Voice Agents](#voice-agents)
- [Showcase](#showcase)

## Overview

Google AI Studio (aistudio.google.com) is Google's free web IDE for prototyping and building AI-powered applications with Gemini models. It serves as both:
1. An API playground for testing prompts and configurations
2. A full app builder for creating deployable web applications

**Access**: Free with Google account. No credit card required for basic usage.

## Build Mode

The most powerful feature of AI Studio. Creates complete web applications from natural language descriptions.

**How to use**:
1. Go to aistudio.google.com
2. Click "Build" in the left sidebar
3. Describe what you want to build in natural language
4. AI Studio generates a complete app with live preview
5. Iterate by describing changes in the chat panel

**What it builds**:
- Full HTML/CSS/JS web applications
- Apps with Gemini API integration (image generation, text processing, etc.)
- Interactive tools, calculators, dashboards
- Games (2D, basic 3D with Three.js)
- Data visualizers, chart generators
- Photo editors (using Nano Banana API)
- Content generators, SEO tools, meme creators

**Key features**:
- Split-screen: code on left, live preview on right
- Side-by-side app building (work on multiple apps simultaneously)
- Suggested features panel: AI recommends enhancements you can add with one click
- Automatic checklist tracking as features are built
- Uses Gemini 2.5 Pro for code generation
- Apps can use Nano Banana API for image generation/editing within the app

**Code assistance panel**: Shows the generated code, allows manual editing, suggests additional features

**Example prompt**: "Build a photo editor app that uses Nano Banana to edit uploaded images based on text prompts. Include upload button, text input for edit instructions, before/after comparison, and download button."

## Chat Mode

Standard chat interface for interacting with Gemini models.

- Select model (Flash, Pro, etc.)
- Configure temperature, top-p, top-k, max tokens
- Test system instructions
- Upload files for multimodal testing
- Enable tools (Google Search, code execution)
- View token counts and latency metrics

## Prompt Engineering

AI Studio provides tools for iterative prompt development:

- **System instruction editor**: Define persistent model behavior
- **Few-shot examples**: Add input/output pairs to guide the model
- **Temperature control**: 0.0 (deterministic) to 2.0 (creative)
- **Token counter**: Real-time tracking of input/output tokens
- **Safety settings panel**: Configure content filtering per category
- **Structured output schema**: Define JSON schema for guaranteed structured responses

**Best practices**:
- Start with system instructions for consistent behavior
- Use few-shot examples for complex formatting requirements (but not too many — risk of overfitting)
- **Gemini 3 note**: Keep temperature at default 1.0 (values below may cause unexpected behavior). Short, direct instructions work better than verbose prompts.
- Lower temperature for Gemini 2.5: 0.0-0.3 for factual/coding tasks, 0.7-1.0 for creative
- Test with edge cases before deploying

## API Key Management

- Generate API keys directly from AI Studio
- Keys are project-scoped (one per Google Cloud project)
- Free tier: generous daily limits for prototyping
- Monitor usage in the AI Studio dashboard
- Rotate keys regularly for security
- Never commit keys to version control - use environment variables

## App Deployment

**Export options**:
1. **Download**: Export as HTML/CSS/JS files, host anywhere (Netlify, Vercel, GitHub Pages)
2. **Cloud Run** (one-click): Deploy directly to Google Cloud Run — fully managed, request-based billing at 100ms granularity. Free tier: 2M requests/month.
3. **Share link**: Publish and get a shareable URL (hosted by Google)
4. **Firebase**: Deploy to Firebase for full backend support

**Deployment steps (Netlify example)**:
1. Click download/export in AI Studio
2. Go to netlify.com, create new project
3. Drag and drop exported folder
4. Get instant subdomain URL

**Deployment steps (Firebase)**:
1. In AI Studio, select "Deploy to Firebase"
2. Select or create Firebase project
3. App deployed with Google-managed hosting

## Voice Agents

Build real-time voice-interactive AI agents in AI Studio.

**Setup**:
1. Select a model with native audio support
2. Configure system instructions for the voice agent persona
3. Set up tools the agent can use (function calling, Google Search)
4. Test with built-in microphone input
5. Deploy via Live API for production use

**Live API features**:
- WebSocket-based bidirectional streaming
- Audio-to-audio (no text intermediary)
- Real-time interruption handling
- Video input support (camera feed)
- Multiple concurrent tool calls during conversation
- Configurable voice selection

## Prompt Gallery

Free collection of templates to explore ideas and jump-start development with the Gemini API.

**Features**:
- Preconfigured samples with specified model and parameter values
- Customizable: modify predefined prompts directly for your projects
- Actively maintained (last updated Feb 2026)

**Template categories**: Audio transcription with speaker details, video Q&A, JSON recipe generation from images, schema-based JSON output, educational content, code optimization, image analysis, advertising copy

## Showcase

Browse apps built by the community in AI Studio's showcase section. Useful for:
- Inspiration for what's possible
- Learning prompt patterns from working examples
- Forking and customizing existing apps
