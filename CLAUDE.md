<!-- GSD:project-start source:PROJECT.md -->
## Project

**PROJECT.md — AtomicBrain**

AtomicBrain is a local-first, LLM-agnostic knowledge management application. It autonomously processes heterogeneous raw files into "Concepts", vectorizes them, and dynamically organizes them into a fractal, hierarchical Obsidian Markdown vault. It serves this knowledge both to humans (via Web UI/Obsidian) and to other AI agents (via an MCP Server).

**Core Value:** Create a wiki that is a perfect representation of the data ingested.
<!-- GSD:project-end -->

<!-- GSD:stack-start source:research/STACK.md -->
## Technology Stack

## Recommended Stack
### Core Technologies
| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| **Python** | 3.12+ | Runtime | Standard for AI/LLM ecosystems; 3.12 offers significant performance improvements and better type hinting. |
| **uv** | 0.5.13+ | Package Manager | Replaces pip/poetry/pyenv; extremely fast (written in Rust), handles virtualenvs and lockfiles efficiently. |
| **FastAPI** | 0.115.13+ | API Framework | High-performance, asynchronous, and provides automatic OpenAPI docs for the human Web UI. |
| **LanceDB** | 0.17.0+ | Vector Database | Embedded, serverless, and stores data in Apache Arrow format. Ideal for local-first apps with zero-latency overhead. |
| **Pydantic AI** | 1.0.5+ | Agent Framework | Type-safe, "FastAPI-like" experience for building agents. Ensures structured data extraction from LLMs. |
### Supporting Libraries
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| **Docling** | 2.0.1+ | Doc Conversion | Primary tool for converting complex PDFs and Office docs to LLM-ready Markdown. |
| **MarkItDown** | 0.0.1+ | Mail/Office Conversion | Secondary tool specifically for `.msg` and `.eml` files and basic office conversions. |
| **FastEmbed** | 0.4.2+ | Local Embeddings | Use for generating vector representations locally via ONNX (faster than PyTorch-based SentenceTransformers). |
| **LiteLLM** | 1.83.3+ | LLM Abstraction | Use to provide a unified OpenAI-compatible API across 100+ providers (Ollama, Anthropic, OpenAI, etc.). |
| **mcp[cli]** | 1.27.0+ | Agent Interface | To implement the Model Context Protocol server for inter-agent communication. |
| **Logfire** | Latest | Observability | Built by Pydantic; provides excellent tracing and monitoring for LLM calls and system logs. |
### Development Tools
| Tool | Purpose | Notes |
|------|---------|-------|
| **Ruff** | Linting & Formatting | Replaces Black/Flake8; extremely fast and uv-friendly. |
| **Pytest** | Testing | Standard for Python testing; use `pytest-asyncio` for FastAPI tests. |
## Installation
# Core dependencies
# Mail support for MarkItDown
# Dev dependencies
## Alternatives Considered
| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| **LanceDB** | **ChromaDB** | If you prefer a client-server architecture over an embedded file-based one. |
| **FastEmbed** | **SentenceTransformers** | If you need specific niche models not yet ported to FastEmbed's ONNX format. |
| **Docling** | **Unstructured** | If you need to handle extremely rare file formats at the cost of significantly higher weight and complexity. |
| **Pydantic AI** | **LangChain** | If you are building extremely complex multi-step chains with pre-built community integrations. |
## What NOT to Use
| Avoid | Why | Use Instead |
|-------|-----|-------------|
| **FAISS** | Purely an index, lacks metadata management and persistent table structure out of the box. | **LanceDB** |
| **Poetry** | Slower resolution and installation compared to uv; more complex workspace management. | **uv** |
| **LangChain** | Often considered "heavy" with too many abstractions; can make debugging local-first logic difficult. | **Pydantic AI** |
| **Pinecone** | Cloud-only; violates the "local-first" core value of AtomicBrain. | **LanceDB** |
## Stack Patterns by Variant
- Use **Ollama** or **Llama.cpp** via **LiteLLM**'s local endpoints.
- Ensure **FastEmbed** models are pre-downloaded.
- Use **Docling** with the `StandardPdfPipeline` and `do_ocr=True`.
- This requires more CPU/GPU resources but preserves tables perfectly.
## Version Compatibility
| Package A | Compatible With | Notes |
|-----------|-----------------|-------|
| `pydantic-ai@1.0.5` | `pydantic>=2.10.0` | Relies on latest Pydantic V2 features. |
| `lancedb@0.17.0` | `pyarrow>=16.0.0` | Optimized for latest Arrow format. |
## Sources
- `/lancedb/lancedb` — Local file-based persistence best practices.
- `/docling-project/docling` — Document to markdown conversion pipelines.
- `/pydantic/pydantic-ai` — Model agnosticism and structured data extraction.
- `/berriai/litellm` — LLM provider bridging.
- `/astral-sh/uv` — Project management and performance.
- Official PyPI/GitHub for MCP SDK v1.27.0 and LiteLLM v1.83.3.
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, or `.github/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
