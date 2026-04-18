# Project Retrospective

*A living document updated after each milestone. Lessons feed forward into future planning.*

---

## Milestone: v1.0 — MVP

**Shipped:** 2026-04-17
**Phases:** 5 | **Plans:** 5

### What Was Built

1. Complete file ingestion pipeline (Docling + MarkItDown) → Obsidian YAML Markdown concepts
2. LanceDB + FastEmbed hybrid vector/FTS search with auto-indexing on ingest
3. Pydantic AI agents for concept refinement and hierarchical vault organization
4. MCP server with dynamic tool registration for external agent access via stdio
5. React/Vite frontend + FastAPI backend with Obsidian-like dashboard UI

### What Worked

- **CLI-first architecture** — Typer-based CLI made it easy to test each phase independently before wiring them together
- **`uv` for dependency management** — Fast lockfile resolution, no environment drift across sessions
- **Pydantic models as the backbone** — `ConceptRecord` and `ConceptMetadata` as shared types prevented divergence between DB schema, API, and vault format
- **Lazy imports in CLI** — Allowing `search` and `mcp` to run without `OPENAI_API_KEY` was a small change with big UX impact
- **FastAPI static file serving** — Eliminating a separate frontend server simplified the deployment story significantly

### What Was Inefficient

- **Requirements traceability not updated during execution** — All 10 requirements were implemented but REQUIREMENTS.md stayed "Pending" throughout. Future milestones should mark requirements complete as each phase ships.
- **No integration tests written** — Unit tests with mocks were written but real LanceDB integration tests were deferred. This is tech debt that could hide regressions.
- **LiteLLM/Ollama not wired** — The stack was chosen to be LLM-agnostic but organization agents still require `OPENAI_API_KEY`. Local LLM support should be a v2.0 phase 1 priority.

### Patterns Established

- **ConverterOrchestrator pattern** — Routing file types to the best available tool (Docling vs MarkItDown) is reusable for any multi-backend conversion need
- **VaultManager as the single write path** — All file-system mutations go through VaultManager which also syncs LanceDB. This prevents index drift.
- **Lazy agent import pattern** — `from src.agents import ...` inside the function body prevents import-time failures for non-AI CLI commands

### Key Lessons

1. Always mark requirements complete as phases ship — retroactive marking is error-prone
2. Write one integration test per phase before moving on — mocks give false confidence on embedded DB interactions
3. Local LLM support should be designed in from the start, not retrofitted — the LiteLLM abstraction was chosen but never exercised
4. Five phases in three days is fast; slow down for v2 to write proper tests

### Cost Observations

- Model mix: ~100% sonnet (no opus or haiku in logs)
- Sessions: 1 primary implementation session
- Notable: Entire MVP shipped in a single focused session — context efficiency was high

---

## Cross-Milestone Trends

| Metric | v1.0 |
|--------|------|
| Phases | 5 |
| Days | 3 |
| LOC | ~47,395 |
| Test coverage | Partial (unit only) |
| Requirements hit rate | 10/10 (100%) |
