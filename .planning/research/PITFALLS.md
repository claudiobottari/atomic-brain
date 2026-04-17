# Domain Pitfalls: AtomicBrain

**Domain:** Local-first, AI-powered Knowledge Management
**Researched:** May 22, 2024
**Confidence:** HIGH

## Critical Pitfalls

Mistakes that cause rewrites or major issues.

### Pitfall 1: The "Dual-Write" Problem (Syncing FS and Index)
**What goes wrong:** Files are added or deleted from the File System (FS), but the Vector DB/SQLite index doesn't reflect the change, leading to "ghost" search results or broken links.
**Why it happens:** Manual file operations outside the app or failures during the indexing process.
**Consequences:** Loss of trust in the "Perfect Wiki" promise; search becomes unreliable.
**Prevention:** Implement a robust file-watching system (e.g., `watchdog`) and atomic index updates. Use checksums (MD5/SHA) to verify if a file has changed before re-indexing.
**Detection:** Periodic "Self-Heal" scan that compares the index against the current FS state.

### Pitfall 2: Atomic "Concept" Granularity Issues
**What goes wrong:** The LLM distills a 50-page PDF into either one giant note (too vague) or 500 tiny sentences (too fragmented).
**Why it happens:** Poor prompting or lack of context-aware chunking strategies during extraction.
**Consequences:** Low search quality and poor "fractal" organization.
**Prevention:** Use recursive summarization and semantic chunking (e.g., LangChain's SemanticChunker). Allow users to "refine" concept boundaries.
**Detection:** High variance in concept lengths; user feedback during the extraction phase.

### Pitfall 3: Model Context Protocol (MCP) Security
**What goes wrong:** An external AI agent (e.g., Claude) is given read/write access to the brain and accidentally deletes or modifies critical notes.
**Why it happens:** Lack of granular permissions in the MCP implementation.
**Consequences:** Irreversible data loss or corrupted knowledge base.
**Prevention:** Start with a "Read-Only" MCP server. Implement "Staging" for agent writes where the user must approve changes before they hit the FS.
**Detection:** Auditing agent commands via a log file.

## Moderate Pitfalls

### Pitfall 1: Dependency Bloat
**What goes wrong:** The application's installation size exceeds 5GB and takes 10 minutes to install.
**Why it happens:** Heavy ML libraries like `docling`, `pytorch`, and `sentence-transformers`.
**Prevention:** Use `uv` for efficient management. Consider an "Optional Dependencies" approach where heavy extractors are only installed if needed.
**Detection:** CI/CD build times and user complaints about disk space.

### Pitfall 2: "The Hallucinated Hierarchy"
**What goes wrong:** The AI-generated fractal hierarchy creates folders like "Miscellaneous 1", "Miscellaneous 2", or "Cool Stuff".
**Why it happens:** LLM temperature is too high or the "Concept Types" aren't well-defined.
**Prevention:** Use constrained generation (Instructor/Pydantic) for category naming. Provide a small "Seed Hierarchy" for the AI to follow.
**Detection:** High number of single-concept folders or vague folder names.

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| **Extraction** | Hallucinations during distillation | Always include the "Source Grounding" link to the raw file. |
| **Hierarchy** | Over-nesting (too deep) | Cap the hierarchy depth to 4-5 levels; prefer "flat-ish" clusters. |
| **MCP Integration** | Protocol version mismatch | Use the official `mcp` SDK and stick to the core specification. |
| **Search** | Low relevance | Use Hybrid Search (Semantic + BM25) to ensure exact keyword matches work. |

## Sources

- [Logseq "DB Version" Transition Notes](https://blog.logseq.com)
- [Unstructured.io RAG Best Practices](https://unstructured.io/blog)
- [The Dual-Write Problem in Databases](https://wikipedia.org)
- [Obsidian Link Integrity Discussions](https://forum.obsidian.md)
