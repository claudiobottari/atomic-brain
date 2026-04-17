# ROADMAP — AtomicBrain

## Phases

- [x] **Phase 1: Foundation & Ingestion** - Convert raw files to Obsidian-compatible Markdown concepts.
- [x] **Phase 2: Indexing & Search** - Enable hybrid semantic and keyword search across ingested concepts.
- [x] **Phase 3: Autonomous Organization (The Brain)** - AI-driven concept extraction and hierarchical vault structuring.
- [x] **Phase 4: Agent Bridge (MCP)** - Connect knowledge base to external AI agents via MCP.
- [x] **Phase 5: Human Dashboard (Web UI)** - Web interface for monitoring and exploration.

## Phase Details

### Phase 1: Foundation & Ingestion
**Goal**: Convert raw files to standardized, Obsidian-compatible Markdown concepts.
**Depends on**: Nothing
**Requirements**: ING-01, ING-02, UI-02
**Success Criteria** (what must be TRUE):
  1. Python environment initialized with `uv` and all dependencies (`Docling`, `MarkItDown`, `FastAPI`, `Pydantic AI`).
  2. Metadata schema for "Concepts" defined and validated via Pydantic.
  3. Ingestion pipeline correctly converts PDF and DOCX to Markdown.
  4. Ingested files are stored in a designated "Vault" directory with appropriate YAML frontmatter.
  5. A CLI entry point `atomic-brain ingest <path>` exists and works.
**Plans**: 
  - [ ] Wave 1: Project Scaffolding & Schema
  - [ ] Wave 2: Ingestion Pipeline (Docling + MarkItDown)
  - [ ] Wave 3: CLI & Vault Integration
**UI hint**: yes

### Phase 2: Indexing & Search
**Goal**: Enable hybrid semantic and keyword search across all ingested concepts.
**Depends on**: Phase 1
**Requirements**: SRCH-01, SRCH-02
**Success Criteria** (what must be TRUE):
  1. LanceDB initialized in `.lancedb/` with a schema compatible with `ConceptMetadata`.
  2. FastEmbed integrated for automated embedding generation.
  3. Ingestion pipeline automatically indexes new Concepts in LanceDB.
  4. CLI entry point `atomic-brain search <query>` provides hybrid results.
  5. Search results include the original source path and concept title.
**Plans**: 
  - [ ] Wave 1: LanceDB & FastEmbed Setup
  - [ ] Wave 2: Automated Indexing
  - [ ] Wave 3: Hybrid Search Implementation
**UI hint**: no
### Phase 3: Autonomous Organization (The Brain)
**Goal**: Use AI to autonomously extract concepts and organize them into a hierarchical vault.
**Depends on**: Phase 2
**Requirements**: ORG-01, ORG-02
**Success Criteria** (what must be TRUE):
  1. Pydantic AI agents implemented for concept refinement and organization.
  2. Concepts are successfully distilled into atomic units with enhanced metadata.
  3. An autonomous organization logic moves files into a hierarchical folder structure.
  4. File system moves are correctly synchronized with the LanceDB index.
  5. A CLI entry point `atomic-brain organize` exists and works.
**Plans**: 
  - [ ] Wave 1: Concept Refinement Agent
  - [ ] Wave 2: Organization & Hierarchical Move
  - [ ] Wave 3: Integration & CLI
**UI hint**: no

### Phase 4: Agent Bridge (MCP)
**Goal**: Provide a standardized interface for external AI agents to access the knowledge base.
**Depends on**: Phase 3
**Requirements**: MCP-01, MCP-02
**Success Criteria** (what must be TRUE):
  1. MCP server implemented using the `mcp` Python SDK.
  2. Standard tools (`search_concepts`, `get_concept_details`) functional.
  3. Specialized tools dynamically registered based on vault categories.
  4. Server connects successfully to an MCP host (e.g., Claude Desktop).
  5. A CLI entry point `atomic-brain mcp` exists to start the server.
**Plans**: 
  - [ ] Wave 1: Core MCP Server
  - [ ] Wave 2: Dynamic Tool Registration
  - [ ] Wave 3: Integration & Deployment
**UI hint**: no

### Phase 5: Human Dashboard (Web UI)
**Goal**: Provide a centralized web interface for system monitoring and knowledge exploration.
**Depends on**: Phase 4
**Requirements**: UI-01
**Success Criteria** (what must be TRUE):
  1. FastAPI backend implemented with endpoints for status, search, and stats.
  2. React/Vite frontend scaffolded and built with modern Vanilla CSS.
  3. UI components for search results, concept view, and status dashboard functional.
  4. CLI entry point `atomic-brain dashboard` launches the server.
  5. End-to-end flow verified in the browser.
**Plans**: 
  - [ ] Wave 1: Backend API (FastAPI)
  - [ ] Wave 2: Frontend (React + Vite)
  - [ ] Wave 3: Integration & CLI
**UI hint**: yes

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Foundation & Ingestion | 0/1 | Not started | - |
| 2. Indexing & Search | 0/1 | Not started | - |
| 3. Autonomous Organization (The Brain) | 0/1 | Not started | - |
| 4. Agent Bridge (MCP) | 0/1 | Not started | - |
| 5. Human Dashboard (Web UI) | 0/1 | Not started | - |

---
*Last updated: April 15, 2026*
