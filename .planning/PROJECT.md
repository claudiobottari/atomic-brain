# PROJECT.md — AtomicBrain

## What This Is

AtomicBrain is a local-first, LLM-agnostic knowledge management application. It autonomously ingests heterogeneous raw files, extracts atomic "Concepts" via AI, organizes them into a fractal hierarchical Obsidian Markdown vault, exposes the knowledge base to external AI agents via MCP, and serves a web dashboard for human exploration.

## Core Value

Create a wiki that is a perfect representation of the data ingested.

## Context

**Shipped v1.0 — 2026-04-17**

- **~47,395 LOC** — Python backend + React/TypeScript frontend
- **Tech stack:** Python 3.12, uv, FastAPI, LanceDB, Pydantic AI, Docling, MarkItDown, FastEmbed, LiteLLM, mcp[cli], React, Vite, Typer
- **Architecture:** CLI-first (`atomic-brain ingest/search/organize/mcp/dashboard`), pure file-system vault for Obsidian compatibility, LanceDB embedded vector store, MCP stdio server
- **Known gaps:** Integration tests against real LanceDB not written; frontend has no tests; Ollama/local LLM not yet wired (requires `OPENAI_API_KEY` for organization agents)

## Requirements

### Validated

- ✓ Autonomous file processing into Concepts — v1.0 (Docling + MarkItDown + ConverterOrchestrator)
- ✓ Semantic organization in a fractal, hierarchical vault (Obsidian compatible) — v1.0 (OrganizationAgent + VaultManager)
- ✓ Vector search and retrieval across the knowledge base — v1.0 (LanceDB + FastEmbed hybrid search)
- ✓ MCP Server for interaction with other AI agents — v1.0 (mcp.server.fastmcp, dynamic tool registration)
- ✓ Web UI for human-friendly knowledge exploration — v1.0 (React/Vite + FastAPI)

### Active

- [ ] Email ingestion (.eml/.msg) — ING-03, carried from v1 deferred
- [ ] Fractal clustering for 100K+ concepts — ORG-03, needed at scale
- [ ] Agent write access via MCP — MCP-03, enables agents to create/edit concepts
- [ ] Interactive graph visualization — UI-03, visual knowledge structure explorer
- [ ] Local LLM support — wire LiteLLM to Ollama so organization works without cloud API key

### Out of Scope

- **Cloud Sync** — AtomicBrain is strictly local-first for privacy and zero latency. Still valid.
- **Social/collaborative features** — Personal brain, not a shared wiki. Still valid.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Pure File System vault | Seamless Obsidian integration, no proprietary locking | ✓ Good — zero friction, files open directly in Obsidian |
| Python/FastAPI/uv | Standard and efficient for AI/LLM applications | ✓ Good — fast setup, uv lockfile reproducible |
| MCP Server Integration | Standardized agent access via Model Context Protocol | ✓ Good — stdio transport, zero config for Claude Desktop |
| Manual FastEmbedGenerator wrapper | Avoid ONNX version conflicts with LanceDB's built-in embedding | ✓ Good — stable, predictable embedding behavior |
| Lazy agent imports in CLI | Allow `mcp` and `search` to work without `OPENAI_API_KEY` | ✓ Good — improves UX for users without cloud keys configured |
| FastAPI serves static frontend | Single `dashboard` command, no separate dev server needed | ✓ Good — simple deployment, one port |
| MarkItDown primary + Docling fallback | Avoid heavy OCR for simple file types | — Pending validation at scale |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-17 after v1.0 milestone*
