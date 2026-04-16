# Phase 1: Foundation & Ingestion - Context

## Domain Boundary
This phase converts raw files (PDF, DOCX, Markdown) into standardized, Obsidian-compatible Markdown \"Concepts\".

## Implementation Decisions

### File Ingestion Strategy
- **ING-01**: Use Docling for high-fidelity extraction of PDF and Office formats.
- **ING-02**: Use MarkItDown for secondary format support (e.g., mail).

### Concept Metadata Schema
- All Concepts must include YAML frontmatter with:
  - `source`: path to original file.
  - `id`: unique identifier.
  - `type`: document type (concept, resource, etc.).
  - `timestamp`: date of ingestion.

### Initial Vault Structure
- Concepts stored in a flat hierarchy initially, with final organization handled by the \"Organization Brain\" in Phase 3.

## Canonical References
- `https://lancedb.github.io/lancedb/architecture/`
- `https://modelcontextprotocol.io`
