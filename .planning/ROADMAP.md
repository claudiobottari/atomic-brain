# ROADMAP — AtomicBrain

## Phases

- [x] **Phase 1: Foundation & Ingestion** - Convert raw files to Obsidian-compatible Markdown concepts.
- [ ] **Phase 2: Indexing & Search** - Enable hybrid semantic and keyword search across ingested concepts.
- [ ] **Phase 3: Autonomous Organization (The Brain)** - AI-driven concept extraction and hierarchical vault structuring.
- [ ] **Phase 4: Agent Bridge (MCP)** - Connect knowledge base to external AI agents via MCP.
- [ ] **Phase 5: Human Dashboard (Web UI)** - Web interface for monitoring and exploration.

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
  1. Search returns relevant concepts for natural language queries (vector search).
  2. Search returns exact matches for specific keywords (BM25 search).
  3. Search results include citations or direct links to the original source files.
**Plans**: TBD

### Phase 3: Autonomous Organization (The Brain)
**Goal**: Use AI to autonomously extract concepts and organize them into a hierarchical vault.
**Depends on**: Phase 2
**Requirements**: ORG-01, ORG-02
**Success Criteria** (what must be TRUE):
  1. LLM reasoning automatically identifies core ideas and relationships from raw text.
  2. Concepts are automatically organized into a multi-level folder hierarchy without user intervention.
  3. The hierarchical organization is reflected in the file system and compatible with Obsidian.
**Plans**: TBD

### Phase 4: Agent Bridge (MCP)
**Goal**: Provide a standardized interface for external AI agents to access the knowledge base.
**Depends on**: Phase 3
**Requirements**: MCP-01, MCP-02
**Success Criteria** (what must be TRUE):
  1. External agents can query the knowledge base using the Model Context Protocol.
  2. The MCP server provides specialized tools based on the vault's category structure.
  3. Agent responses are grounded in the user's local vault data.
**Plans**: TBD

### Phase 5: Human Dashboard (Web UI)
**Goal**: Provide a centralized web interface for system monitoring and knowledge exploration.
**Depends on**: Phase 4
**Requirements**: UI-01
**Success Criteria** (what must be TRUE):
  1. User can monitor ingestion progress and system health via a local web dashboard.
  2. User can perform searches and view results directly in the web browser.
  3. Dashboard provides a high-level overview of the knowledge base structure and content.
**Plans**: TBD
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
