# Phase 2: Indexing & Search - Context

## Domain Boundary
Enable hybrid (semantic + keyword) search across ingested concepts using LanceDB and FastEmbed.

## Implementation Decisions

### Vector Database & Embeddings
- **LanceDB**: Local, serverless vector database stored in `.lancedb/`.
- **FastEmbed**: Local embeddings generation (default: `BAAI/bge-small-en-v1.5`).

### Search Strategy (Hybrid)
- **Vector Search**: Natural language similarity search for semantic relevance.
- **Full-Text Search (FTS)**: BM25-based keyword matching for exact terms.
- **Reranking/Combination**: Basic linear combination of results for the MVP.

### Indexing Trigger
- Automatic indexing of newly ingested concepts during the `ingest` command.
- Background "re-index all" command for maintenance.

## Canonical References
- `https://lancedb.github.io/lancedb/hybrid_search/`
- `https://qdrant.github.io/fastembed/`
