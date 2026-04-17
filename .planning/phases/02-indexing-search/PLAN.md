# Phase 2: Indexing & Search - Plan

## Objective
Enable hybrid semantic and keyword search across ingested concepts by integrating LanceDB and FastEmbed into the pipeline.

## Success Criteria
1.  LanceDB initialized in `.lancedb/` with a schema compatible with `ConceptMetadata`.
2.  FastEmbed integrated for automated embedding generation.
3.  Ingestion pipeline automatically indexes new Concepts in LanceDB.
4.  CLI entry point `atomic-brain search <query>` provides hybrid results.
5.  Search results include the original source path and concept title.

## Waves & Tasks

### Wave 1: LanceDB & FastEmbed Setup
- [ ] **Task 1.1**: Create `src/database.py` to manage LanceDB connections and table initialization.
- [ ] **Task 1.2**: Define the LanceDB schema for Concepts (vector, id, content, metadata).
- [ ] **Task 1.3**: Implement `EmbeddingGenerator` using `FastEmbed`.

### Wave 2: Automated Indexing
- [ ] **Task 2.1**: Update `src/cli.py` to trigger indexing after successful ingestion.
- [ ] **Task 2.2**: Implement `src/indexer.py` to handle the LanceDB insertion logic.
- [ ] **Task 2.3**: Create a `reindex` CLI command to build the index from existing vault files.

### Wave 3: Hybrid Search Implementation
- [ ] **Task 3.1**: Implement hybrid search logic (Vector + FTS) in `src/searcher.py`.
- [ ] **Task 3.2**: Add the `search` command to `src/cli.py` with result formatting.
- [ ] **Task 3.3**: Verify search quality with sample queries against ingested data.

## Verification Strategy
- **Unit Tests**: Test the `EmbeddingGenerator` and `indexer` logic.
- **Integration Tests**: Ingest a new document and immediately verify it is discoverable via `search`.
- **Quality Audit**: Test both semantic (natural language) and keyword (exact match) queries.
