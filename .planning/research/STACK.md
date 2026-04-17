# Stack Research: AtomicBrain

**Domain:** Local-first Knowledge Management / AI Agent Memory
**Researched:** April 15, 2026
**Confidence:** HIGH

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

```bash
# Core dependencies
uv add fastapi lancedb pydantic-ai litellm fastembed docling mcp[cli] logfire

# Mail support for MarkItDown
uv add "markitdown[outlook]"

# Dev dependencies
uv add --dev ruff pytest pytest-asyncio
```

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

**If Running Entirely Offline:**
- Use **Ollama** or **Llama.cpp** via **LiteLLM**'s local endpoints.
- Ensure **FastEmbed** models are pre-downloaded.

**If High-Accuracy PDF Parsing is Required:**
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

---
*Stack research for: AtomicBrain*
*Researched: April 15, 2026*
