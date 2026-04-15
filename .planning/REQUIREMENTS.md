# REQUIREMENTS.md — AtomicBrain

## v1 Requirements (MVP)

These features constitute the core value of AtomicBrain: a local-first, autonomous, agent-ready "wiki" that represents ingested data.

### Ingestion & Processing
- [ ] **ING-01**: High-fidelity ingestion of text, Markdown, PDF, and DOCX using **MarkItDown** for conversion.
- [ ] **ING-02**: Atomic extraction of content into "Concepts" with standardized Markdown metadata.

### Search & Retrieval
- [ ] **SRCH-01**: Hybrid search functionality combining **Vector Search** (LanceDB/FastEmbed) and **Keyword Search** (BM25 or similar).
- [ ] **SRCH-02**: Semantic retrieval that grounds search results in the original source documents.

### The Brain: Organization
- [ ] **ORG-01**: **Autonomous Concept Extraction**: AI identifies core ideas and relationships in raw text using LLM reasoning (Pydantic AI).
- [ ] **ORG-02**: **Hierarchical Vault**: Organization of Concepts into a multi-level folder structure compatible with Obsidian.

### Agent Bridge: MCP
- [ ] **MCP-01**: **Read-only MCP Server**: Standardized retrieval tools (`query_general`, `query_topic`) for external AI agents.
- [ ] **MCP-02**: **Dynamic Tool Registration**: Server automatically registers specialized tools based on major vault categories (e.g., `get_finance()`).

### Human Interface
- [ ] **UI-01**: **Web UI Dashboard**: Local dashboard for monitoring system status, ingestion progress, and basic search.
- [ ] **UI-02**: **Obsidian Native**: Direct file system storage ensuring the vault is immediately usable in Obsidian with no proprietary locking.

## v2 Requirements (Deferred)

- [ ] **ING-03**: Support for complex formats: Emails (.eml/.msg), OCR for images, and audio transcription.
- [ ] **ORG-03**: **Fractal Clustering**: Deep recursive organization that handles 100K+ concepts with nested sub-topics.
- [ ] **MCP-03**: **Agent Write Access**: Authorization flow for external agents to create new concepts or edit existing ones.
- [ ] **UI-03**: **Interactive Graph Explorer**: Visual representation of the hierarchical knowledge structure.

## Out of Scope

- **Cloud Sync**: AtomicBrain is strictly local-first to ensure maximum privacy and zero latency.
- **Social Features**: This is a personal "brain", not a collaborative wiki platform.

## Traceability

| Requirement | Phase | Success Criterion | Status |
|-------------|-------|------------------|--------|
| ING-01      | Phase 1 | User can ingest PDF, DOCX, and Markdown files. | Pending |
| ING-02      | Phase 1 | Each ingested file is converted to a Markdown "Concept" with metadata. | Pending |
| SRCH-01     | Phase 2 | Search returns relevant concepts for natural language queries and keyword matches. | Pending |
| SRCH-02     | Phase 2 | Search results include citations or direct links to original source files. | Pending |
| ORG-01      | Phase 3 | LLM reasoning identifies core ideas and relationships from raw text. | Pending |
| ORG-02      | Phase 3 | Concepts are organized into a multi-level folder hierarchy in the FS. | Pending |
| MCP-01      | Phase 4 | External agents can query the knowledge base using MCP. | Pending |
| MCP-02      | Phase 4 | MCP server provides specialized tools based on vault categories. | Pending |
| UI-01       | Phase 5 | User can monitor status and search via a local web dashboard. | Pending |
| UI-02       | Phase 1 | Vault is immediately usable in Obsidian. | Pending |

---
*Last updated: April 15, 2026 after roadmap creation*
