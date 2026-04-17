# Phase 4: Agent Bridge (MCP) - Context

## Domain Boundary
Expose the AtomicBrain knowledge base to external AI agents using the Model Context Protocol (MCP).

## Implementation Decisions

### MCP Server Architecture
- **Protocol**: Model Context Protocol (MCP) v1.0.
- **Transport**: stdio (Standard Input/Output) for local integration.
- **SDK**: `mcp` Python SDK.

### Tooling Strategy
- **Base Tools**:
  - `search_concepts(query)`: General hybrid search tool.
  - `read_concept(id)`: Retrieve full content and metadata for a specific concept.
- **Dynamic Tools**:
  - Automatically register tools based on top-level vault categories (e.g., `query_projects`, `query_finance`).

### Grounding & Safety
- **Read-only**: The MVP bridge is read-only to ensure system integrity.
- **Context Filtering**: Ensure results are relevant and grounded in the vault data.

## Canonical References
- `https://modelcontextprotocol.io/`
- `https://github.com/modelcontextprotocol/python-sdk`
