# Architecture Patterns: AtomicBrain

**Domain:** Local-first, AI-powered Knowledge Management
**Researched:** May 22, 2024

## Recommended Architecture

AtomicBrain follows a **Modular Data Pipeline** architecture, separating raw file ingestion from semantic organization and multi-modal serving.

### Component Boundaries

| Component | Responsibility | Communicates With |
|-----------|---------------|-------------------|
| **Ingestion Engine** | Scans the File System, detects new/changed files, and extracts text. | File System, Extraction Layer |
| **Extraction Layer** | Converts PDFs, Office Docs, and Audio into a clean internal Markdown format. | Ingestion Engine, Distillation Engine |
| **Distillation Engine** | Uses LLMs to refine raw text into atomic "Concepts" with metadata. | Extraction Layer, Indexing Service |
| **Indexing Service** | Generates embeddings and stores vectors/metadata for fast retrieval. | Distillation Engine, Search/MCP Layer |
| **Organization Brain** | Clusters concepts and generates a hierarchical folder/file structure. | Indexing Service, File System |
| **Serving Layer (MCP)** | Exposes the brain to AI agents via the Model Context Protocol. | Indexing Service, Organization Brain |
| **Serving Layer (Web)** | Visual explorer for humans to browse the fractal hierarchy. | Organization Brain, Indexing Service |

### Data Flow

1. **Ingest:** Raw file (e.g., `paper.pdf`) enters the system.
2. **Extract:** `Docling` extracts structured text and tables.
3. **Distill:** LLM summarizes and "atomizes" the text into several `Concept` files (e.g., `Concept_A.md`, `Concept_B.md`).
4. **Index:** Concepts are vectorized (LanceDB) and tagged with "Concept Types" (SQLite).
5. **Organize:** Clustering logic assigns Concepts to folders based on semantic proximity (e.g., `/Research/AI/Pipelines/`).
6. **Serve:** Other agents query via `mcp`, or the user views in the Web UI / Obsidian.

## Patterns to Follow

### Pattern 1: Sidecar Indexing
**What:** The "Source of Truth" is the File System (Markdown). The Index (LanceDB/SQLite) is a "Sidecar" that can be rebuilt at any time.
**When:** To maintain Obsidian compatibility and local-first data ownership.
**Example:**
```python
# Pseudo-code for Sidecar Sync
def sync_concept(concept_path):
    checksum = calculate_md5(concept_path)
    if not index.has_changed(concept_path, checksum):
        return
    content = read_file(concept_path)
    vector = embed_model.encode(content)
    index.upsert(concept_path, vector, checksum)
```

### Pattern 2: Hierarchical Agglomerative Clustering (HAC)
**What:** Use HAC to build the fractal hierarchy from the bottom up.
**When:** To ensure the organization is always balanced and logically nested.
**Implementation:** Use `scikit-learn` or `FastCluster` for the math; use LLM to "Label" the resulting clusters.

## Anti-Patterns to Avoid

### Anti-Pattern 1: "The Monolith Index"
**What:** Storing all concept content only in a database and generating files as a "secondary" export.
**Why bad:** If the database corrupts, the knowledge base is lost. It also breaks the Obsidian plugin ecosystem.
**Instead:** Write the file *first*, then index it.

### Anti-Pattern 2: Real-time LLM Processing
**What:** Running the LLM on every single keystroke or file change.
**Why bad:** High cost (for cloud) or system lag (for local).
**Instead:** Use a "Processing Queue" with batching.

## Scalability Considerations

| Concern | At 100 concepts | At 10K concepts | At 100K concepts |
|---------|--------------|--------------|-------------|
| **Search Speed** | In-memory scan | LanceDB Flat Index | LanceDB IVP/PQ Index |
| **Clustering** | Instant | 10-30 seconds | Incremental Clustering (MinHash) |
| **Disk Usage** | <100 MB | 1-5 GB | 10-50 GB (mostly assets) |

## Sources

- [LanceDB Architecture](https://lancedb.github.io/lancedb/architecture/)
- [Hierarchical Clustering Guide](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)
