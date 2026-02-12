# Developer Tools & Coding

## Table of Contents
- [Gemini CLI](#gemini-cli)
- [Gemini Code Assist](#gemini-code-assist)
- [Anti-gravity IDE](#anti-gravity-ide)
- [Chrome DevTools MCP](#chrome-devtools-mcp)
- [Firebase Genkit](#firebase-genkit)
- [Jules (AI Coding Agent)](#jules)
- [Project IDX](#project-idx)
- [Agent Development Kit (ADK)](#agent-development-kit)
- [Google Colab AI](#google-colab-ai)

## Gemini CLI

Terminal-based AI agent that runs locally. Open source, free (1,000 requests/day with personal Google account).

**Installation**:
```bash
npm install -g @google/generative-ai-cli
# or
npx @google/generative-ai-cli
```

**Authentication**: Login with Google account or provide API key.

**Key capabilities**:
- Read/write files in your project directory
- Execute shell commands
- Launch apps in browser
- Google Search integration
- Analyze entire codebases
- Multi-file refactoring
- Build complete apps from descriptions
- Generate and run tests
- Code review and debugging

**Custom commands** (via TOML config, `~/.gemini/commands/`):
```toml
[command]
name = "review"
description = "Review code for issues"
prompt = "Review the current codebase for bugs, security issues, and performance problems."
```

**Extensions**:
- Install via: `gemini extensions install <url>`
- Genkit extension: `gemini extensions install https://github.com/gemini-cli-extensions/genkit`
- Data Cloud extensions for Cloud SQL, AlloyDB, BigQuery
- List installed: `gemini extensions list`
- Each extension includes a built-in "playbook" giving AI immediate knowledge of connected tools
- Partner ecosystem: Dynatrace, Elastic, Figma, Harness, Postman, Shopify, Snyk, Stripe

**VS Code integration**: Run Gemini CLI within VS Code terminal for context-aware coding assistance.

**Model selection**: Uses Gemini 2.5 Pro by default. May fall back to Flash during high demand.

**Tips**:
- Be specific with prompts for better output
- Use `--model` flag to force a specific model
- Create project-specific commands in `.gemini/` directory
- Save work frequently (files are modified in-place)

## Gemini Code Assist

AI-powered coding assistance for the full software development lifecycle. Available in VS Code and IntelliJ.

**Editions**:
- **Free**: Individual developers, basic code assist features
- **Standard**: Enhanced features for teams
- **Enterprise**: Integration with Google Cloud services, additional features outside IDE

**Features**:
- **Agent Mode** (launched Oct 2025): autonomous multi-step coding, replaces previous tools-based approach
- Multiple concurrent chat sessions
- Codebase-aware suggestions (understands project structure)
- Inline code completion
- Code explanation and documentation
- Refactoring suggestions
- Bug detection and fix proposals
- Checkpoint system: roll back to previous states if AI changes break something
- Test generation
- Natural language to code
- Powered by Gemini 2.5 Pro and Flash (both GA)

**Also available**: Gemini Code Assist for GitHub (GA).

**Setup**: Install from VS Code/IntelliJ marketplace, authenticate with Google account.

**Best for**: Day-to-day coding assistance, code review, learning new codebases

## Anti-gravity IDE

Google's agentic IDE (similar to Cursor/Windsurf). Uses Gemini 3 Pro as its AI engine.

**Key features**:
- Built on VS Code foundation
- Deep Gemini integration throughout the IDE
- Agentic coding: AI can autonomously plan and execute multi-file changes
- "Vibe coding" support: describe what you want, AI builds it
- Generative UI interfaces: AI creates UI components from descriptions
- Built-in terminal with Gemini CLI
- Real-time collaboration features

**Target users**: Developers who want an AI-native IDE experience comparable to Cursor but powered by Gemini.

## Chrome DevTools MCP

Model Context Protocol server that connects AI coding tools to Chrome browser for real-time testing and debugging.

**What it enables**:
- AI can open browser, navigate to pages, verify code changes visually
- Read console logs, check for errors automatically
- Run performance tests (LCP, FID, CLS metrics)
- Inspect DOM, analyze CSS
- Test user flows (click through apps, fill forms, submit data)
- Debug live pages

**Setup**:
1. Use an AI coding tool that supports MCP (Gemini CLI, Cline, etc.)
2. Add Chrome DevTools MCP server to your MCP config
3. AI automatically uses browser tools after writing front-end code

**Recommended with**: Gemini CLI or any MCP-compatible AI coding tool

**Best practice**: Create a rules file telling your AI to always use Chrome DevTools MCP after writing front-end code for automatic testing.

## Firebase Genkit

Google's open-source framework for building AI-powered applications. "Firebase for AI."

**Core concepts**:
- **Flows**: AI workflows (chains of operations with inputs/outputs)
- **Evaluators**: Test if AI outputs meet quality criteria
- **Traces**: Debugging tool showing execution path and intermediate results
- **Plugins**: Extend with different models, vector stores, tools

**Quick start**:
```bash
npm init genkit@latest
```

**Language support**: JavaScript/TypeScript (stable), Go (1.0 stable), Python (Alpha)

**Key features**:
- Model-agnostic (works with Gemini, OpenAI, Anthropic, etc.)
- Built-in evaluation framework
- Trace-based debugging with local CLI and Developer UI
- Type-safe flows with schema validation
- Plugin ecosystem (Firebase, Vertex AI, Pinecone, Chroma, etc.)
- RAG, structured outputs, tool calling, agentic workflows
- Deploy to Firebase, Cloud Run, or third-party platforms

**Note**: "Vertex AI in Firebase" was rebranded to **Firebase AI Logic** at I/O 2025, adding direct Gemini Developer API access alongside Vertex AI Gemini API.

**Genkit + Gemini CLI extension**:
- Install: `gemini extensions install https://github.com/gemini-cli-extensions/genkit`
- AI understands Genkit patterns, scaffolds flows, generates evaluators, debugs from traces
- Production-ready code generation

**Use cases**: RAG pipelines, chatbots, content moderation systems, data extraction workflows, AI-powered APIs

## Jules

Google's autonomous, asynchronous AI coding agent (cloud-based). Clones repos into secure Google Cloud VMs. Powered by Gemini 2.5 Pro.

**Timeline**: Revealed Dec 2024, public beta May 2025 (I/O), exited beta Aug 2025, Jules Tools CLI + public API Oct 2025.

**Capabilities**:
- Generates code, fixes bugs, writes tests, improves performance
- Understands full project context
- Operates on GitHub repositories
- Creates branches, writes code, opens PRs
- Works asynchronously (assign task, come back to review results)

**Developer tools**:
- **Jules Tools CLI**: Brings Jules directly into the terminal (no web-to-GitHub context switching)
- **Jules API**: Public API for integrating Jules into existing workflows

**How to use**:
1. Connect GitHub repository
2. Describe the task
3. Jules creates a plan (review/approve)
4. Jules executes: writes code, creates PR
5. Review and merge

**Editions**: Free and paid plans available.

**Best for**: Delegating routine coding tasks, bug fixes, test writing, code migrations

## Project IDX

Google's cloud-based development environment.

- Full IDE in the browser
- Pre-configured templates for various frameworks
- Gemini AI assistance built-in
- Collaborative editing
- Integrated deployment to Firebase/Cloud Run
- Supports: React, Angular, Vue, Flutter, Python, Go, Node.js, and more

## Agent Development Kit (ADK)

Open-source, code-first framework for building custom AI agents. Designed to make agent development feel like traditional software development.

**Language support**: TypeScript/JavaScript (primary), Python, Java, Go

**Key features**:
- Modular: compose specialized agents into multi-agent systems with strong typing
- Deployment-agnostic: run locally, in containers, or serverless (Cloud Run)
- Model-agnostic: works with Gemini 3 Pro, Flash, and third-party models
- Multimodal streaming: bidirectional audio and video for natural interactions
- **ADK Web**: Built-in dev UI (Node.js Angular app at localhost:4200) for testing, debugging, event/trace inspection
- **Agent2Agent Protocol (A2A)**: Enables agent interoperability and task delegation between agents
- **Interactions API**: Native interface for complex state management in agentic loops

**Use cases**: Customer service bots, voice assistants, task automation agents, research agents, workflow orchestration

## Google Colab AI

Google Colab redesigned as an AI-first platform powered by Gemini 2.5 Flash.

**Key features**:
- **Data Science Agent** (Mar 2025): Fully integrated for exploring data and uncovering insights
- Code generation: short functions, boilerplate, or whole-notebook refactors
- Intelligent error fixing with diff view suggestions
- Conversational interface for code explanations and library help
- Free access to Gemini 2.5 Flash and Flash-Lite models via `google.colab.ai` Python library
- Greater than 2x efficiency improvements demonstrated

**Best for**: Data analysis, ML experimentation, collaborative notebooks with AI assistance
