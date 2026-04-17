# Phase 3: Autonomous Organization - Context

## Domain Boundary
Transform a flat collection of ingested files into a structured, semantically organized knowledge base (The Brain).

## Implementation Decisions

### Concept Extraction & Refinement
- **Structured Extraction**: Use Pydantic AI to extract core ideas, entities, and relationships from raw Markdown content.
- **Refinement Agent**: An agent that takes raw ingestion output and "distills" it into a cleaner, more atomic Concept.

### Hierarchical Organization (The Brain)
- **Semantic Categorization**: Use LLM reasoning to determine the best folder path for a given Concept based on its content and the existing vault structure.
- **Dynamic Folder Creation**: The system autonomously creates and manages the folder hierarchy in the `vault/Concepts/` directory.
- **Obsidian Compatibility**: Ensure all organization is reflected in the file system to maintain native Obsidian functionality.

### Index Synchronization
- **Consistency**: Any file move or metadata update must be reflected in the LanceDB index to ensure search remains accurate.

## Canonical References
- `https://ai.pydantic.dev/`
- `https://obsidian.md/`
