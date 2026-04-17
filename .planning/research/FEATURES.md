# Feature Landscape: AtomicBrain

**Domain:** Local-first Knowledge Management / AI Agent Memory
**Researched:** April 15, 2026

## Table Stakes

Features users expect in a modern KM application. Missing these = product feels incomplete.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Multi-format Support** | Knowledge comes in PDF, Word, Email, and Text. | MEDIUM | Use **Docling** for most formats; **MarkItDown** for Mail/Office. |
| **Vector Search** | Semantic retrieval (finding by "meaning") is the new standard. | LOW | Handled by **LanceDB** + **FastEmbed**. |
| **Markdown Export** | Users want to own their data and use it in tools like Obsidian. | LOW | Standard output for ingestion. |
| **Local-First Privacy** | KM often contains sensitive or private thoughts/data. | MEDIUM | Entire stack (LanceDB, FastEmbed, Ollama) must be local. |

## Differentiators

Features that set AtomicBrain apart. These provide the core value proposition.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| **Autonomous "Concept" Extraction** | No more manual tagging; AI identifies the core ideas in a document automatically. | HIGH | Use **Pydantic AI** for structured extraction. |
| **Fractal, Hierarchical Vault** | Not just a flat list of notes, but a structured hierarchy that reflects the "shape" of the knowledge. | HIGH | Requires a sophisticated clustering/reasoning algorithm. |
| **MCP Server Integration** | Enables other AI agents (like Claude Desktop) to "browse" the brain's knowledge. | MEDIUM | Standard protocol for agent-to-agent communication. |
| **Obsidian Native Compatibility** | The primary storage *is* an Obsidian vault, making it instantly usable in human-facing tools. | LOW | Just a file-system structure convention. |

## Anti-Features

Features to explicitly NOT build to maintain focus and local-first value.

| Anti-Feature | Why Avoid | What to Do Instead |
|--------------|-----------|-------------------|
| **Cloud-only Database** | Violates privacy; adds latency and cost. | Use **LanceDB** (embedded). |
| **Proprietary File Formats** | Locks users in; limits interoperability. | Use **Obsidian-compatible Markdown**. |
| **Manual Categorization UI** | The "Brain" should handle the heavy lifting autonomously. | Use AI-driven organization with human overrides. |

## Feature Dependencies

```
Raw File Ingestion → Markdown Conversion → Vectorization → Semantic Search
                                         ↘ Concept Extraction → Hierarchical Organization → Obsidian Vault
```

## MVP Recommendation

Prioritize:
1. **High-fidelity Ingestion:** PDF, DOCX, and EML conversion to Markdown.
2. **Local Vector Search:** Semantic retrieval using LanceDB and FastEmbed.
3. **Basic Hierarchical Organization:** Create the first-level vault structure (folder-per-concept).
4. **MCP Tooling:** Simple tool for other agents to query the brain.

Defer:
- **Advanced Fractal Clustering:** Focus on a simple hierarchy first.
- **Complex Web UI:** Focus on Obsidian compatibility as the primary human interface.

## Sources

- Obsidian community forums (Obsidian as a standard for KM).
- Model Context Protocol (MCP) specifications.
- Modern RAG architecture patterns (HuggingFace/LanceDB).
