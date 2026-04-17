# Research Summary: AtomicBrain

**Domain:** Local-first, AI-powered Knowledge Management
**Researched:** May 22, 2024
**Overall confidence:** HIGH

## Executive Summary

AtomicBrain aims to solve the "Knowledge Burden" of manual organization in modern PKMs like Obsidian and Logseq. By autonomously distilling raw files (PDFs, Mails, Web Clips) into atomic "Concepts" and organizing them into a fractal, hierarchical vault, it transforms a messy collection of files into a "Perfect Wiki".

Key findings suggest that while the "Table Stakes" (Markdown, Search, Backlinks) are well-defined by competitors like Obsidian, the "Differentiators" (Autonomous Extraction, Fractal Hierarchy, and MCP Server) are the true value-drivers. The Model Context Protocol (MCP) specifically positions AtomicBrain as a "Brain for Agents", allowing external AIs to use the user's personal knowledge as their own context.

The technical stack should leverage high-precision extractors like **Docling** (IBM) and **MarkItDown** (Microsoft), backed by a local-first vector store like **LanceDB**. This ensures data ownership while providing production-grade search performance.

## Key Findings

**Stack:** Python 3.12+, FastAPI, uv, LanceDB, Docling, and MCP.
**Architecture:** A "Modular Data Pipeline" with Sidecar Indexing to ensure the File System remains the source of truth for Obsidian compatibility.
**Critical Pitfall:** The "Dual-Write" sync problem between the File System and the Vector/SQLite index.

## Implications for Roadmap

Suggested phase structure for the AtomicBrain roadmap:

1. **Phase 1: Foundation (Ingest & Index)**
   - Addresses: Core Ingestion, Extraction (Docling/MarkItDown), and Indexing (LanceDB).
   - Avoids: Dependency bloat by starting with a clean `uv` environment.

2. **Phase 2: The Brain (Distill & Organize)**
   - Addresses: Autonomous Concept Extraction (LLM) and Fractal Hierarchy (HAC Clustering).
   - Rationale: This is the core differentiator; needs validation early.

3. **Phase 3: The Bridge (MCP & Export)**
   - Addresses: MCP Server (Read-only) and Obsidian-compatible Markdown export.
   - Avoids: Breaking the "Agent Context" by using standardized MCP.

4. **Phase 4: The Interface (Web UI & Assistant)**
   - Addresses: Visual explorer, Source Grounding UI, and Agent Write support.

**Phase ordering rationale:**
- Extraction and Indexing must come first to have data to organize.
- "The Brain" (Organization) is the most technically risky part, so it's prioritized for Phase 2.
- Interface (Web UI) is deferred to Phase 4 as Obsidian serves as the "Primary UI" in early stages.

**Research flags for phases:**
- Phase 2: Needs deeper research into Hierarchical Agglomerative Clustering (HAC) algorithms for semantic organization.
- Phase 3: Requires monitoring of the evolving Model Context Protocol (MCP) spec for feature parity.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Modern, well-supported libraries identified (Docling, LanceDB). |
| Features | HIGH | Clear gap identified between manual PKM and autonomous KM. |
| Architecture | MEDIUM | Sidecar indexing is a proven pattern, but sync-integrity needs careful coding. |
| Pitfalls | HIGH | Common AI/RAG pitfalls are well-documented and avoidable. |

## Gaps to Address

- **Clustering Performance:** Performance of HAC at 100K+ concepts needs benchmarking.
- **LLM Cost/Latency:** Benchmarking Ollama (local) vs Cloud for extraction tasks to optimize for different user hardware.
- **MCP Security:** Defining a granular permission model for agent "Write" access.

---
*Research synthesized for: AtomicBrain Roadmap*
*Researched: May 22, 2024*
