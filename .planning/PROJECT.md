# PROJECT.md — AtomicBrain

## What This Is

AtomicBrain is a local-first, LLM-agnostic knowledge management application. It autonomously processes heterogeneous raw files into "Concepts", vectorizes them, and dynamically organizes them into a fractal, hierarchical Obsidian Markdown vault. It serves this knowledge both to humans (via Web UI/Obsidian) and to other AI agents (via an MCP Server).

## Core Value

Create a wiki that is a perfect representation of the data ingested.

## Context

* **Files:** Support for docs, pdf, mails, text files, and other formats convertible to markdown.
* **Organization:** Semantics-driven organization using embeddings, LLM reasoning, and clustering.
* **Storage:** Pure File System for direct compatibility with Obsidian.
* **Tech Stack:** Python, uv, FastAPI.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Autonomous file processing into Concepts.
- [ ] Semantic organization in a fractal, hierarchical vault (Obsidian compatible).
- [ ] Vector search and retrieval across the knowledge base.
- [ ] MCP Server for interaction with other AI agents.
- [ ] Web UI for human-friendly knowledge exploration.

### Out of Scope

- (To be defined)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Pure File System | Seamless integration with Obsidian and other file-based tools. | — Pending |
| Python/FastAPI/uv | Standard and efficient backend for AI/LLM applications. | — Pending |
| MCP Server Integration | Enable seamless knowledge sharing with AI agents via the Model Context Protocol. | — Pending |

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
*Last updated: April 15, 2026 after initialization*
