# Graph Report - .  (2026-04-18)

## Corpus Check
- Corpus is ~9,273 words - fits in a single context window. You may not need a graph.

## Summary
- 233 nodes · 416 edges · 18 communities detected
- Extraction: 53% EXTRACTED · 47% INFERRED · 0% AMBIGUOUS · INFERRED: 197 edges (avg confidence: 0.63)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Tech Stack & Architecture|Tech Stack & Architecture]]
- [[_COMMUNITY_Data Models & API|Data Models & API]]
- [[_COMMUNITY_CLI Commands & Workflows|CLI Commands & Workflows]]
- [[_COMMUNITY_Database & Embeddings|Database & Embeddings]]
- [[_COMMUNITY_Vault Manager & Tests|Vault Manager & Tests]]
- [[_COMMUNITY_Document Converters|Document Converters]]
- [[_COMMUNITY_UI Brand & Assets|UI Brand & Assets]]
- [[_COMMUNITY_AI Agents|AI Agents]]
- [[_COMMUNITY_CLI Tests|CLI Tests]]
- [[_COMMUNITY_Frontend App|Frontend App]]
- [[_COMMUNITY_Vite Build Plugins|Vite Build Plugins]]
- [[_COMMUNITY_ESLint & React|ESLint & React]]
- [[_COMMUNITY_Package Init|Package Init]]
- [[_COMMUNITY_ESLint Config|ESLint Config]]
- [[_COMMUNITY_Vite Config|Vite Config]]
- [[_COMMUNITY_Ruff Linter|Ruff Linter]]
- [[_COMMUNITY_Pytest|Pytest]]
- [[_COMMUNITY_TypeScript|TypeScript]]

## God Nodes (most connected - your core abstractions)
1. `ConceptRecord` - 30 edges
2. `Searcher` - 25 edges
3. `VaultManager` - 24 edges
4. `Concept` - 20 edges
5. `FastEmbedGenerator` - 19 edges
6. `Indexer` - 17 edges
7. `ConceptMetadata` - 17 edges
8. `AtomicBrain` - 17 edges
9. `ConverterOrchestrator` - 14 edges
10. `get_concepts_table()` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Tests that get_db creates the DB_PATH if it doesn't exist.` --uses--> `ConceptRecord`  [INFERRED]
  tests\test_database.py → src\database.py
- `Tests that get_db connects to the path if it already exists.` --uses--> `ConceptRecord`  [INFERRED]
  tests\test_database.py → src\database.py
- `Tests that get_concepts_table opens an existing table.` --uses--> `ConceptRecord`  [INFERRED]
  tests\test_database.py → src\database.py
- `Tests that get_concepts_table creates a new table if it doesn't exist.` --uses--> `ConceptRecord`  [INFERRED]
  tests\test_database.py → src\database.py
- `Tests the structure of the ConceptRecord schema.` --uses--> `ConceptRecord`  [INFERRED]
  tests\test_database.py → src\database.py

## Hyperedges (group relationships)
- **AtomicBrain Core Technology Stack** — claude_atomicbrain, claude_python, claude_fastapi, claude_lancedb, claude_pydanticai, claude_uv [EXTRACTED 1.00]
- **AtomicBrain Supporting Libraries** — claude_atomicbrain, claude_docling, claude_markitdown, claude_fastembed, claude_litellm, claude_mcpcli, claude_logfire [EXTRACTED 1.00]
- **UI Frontend Stack** — ui_indexhtml, ui_react, ui_typescript, ui_vite, ui_maintsx [INFERRED 0.90]
- **LLM Agnostic Bridge via LiteLLM** — claude_litellm, claude_ollama, claude_llamacpp, claude_llmagnostic [EXTRACTED 1.00]
- **UI Public Static Assets** — favicon_atomicbrain_logo, icons_svg_sprite [INFERRED 0.90]
- **UI Source Brand and Tech Assets** — hero_layered_illustration, react_logo, vite_logo [INFERRED 0.85]
- **Social Media Icon Set** — icons_bluesky_icon, icons_discord_icon, icons_x_icon, icons_github_icon, icons_social_icon [INFERRED 0.88]
- **React and Vite Frontend Stack** — react_logo, vite_logo, concept_ui_tech_stack [INFERRED 0.88]

## Communities

### Community 0 - "Tech Stack & Architecture"
Cohesion: 0.06
Nodes (39): AtomicBrain, ChromaDB (Alternative), Concepts (Knowledge Units), Docling, FAISS (Avoided), FastAPI, FastEmbed, LanceDB (+31 more)

### Community 1 - "Data Models & API"
Cohesion: 0.13
Nodes (29): BaseModel, ConceptRecord, LanceDB schema for AtomicBrain Concepts., LanceModel, get_concept(), get_stats(), get_status(), Returns the system health and status. (+21 more)

### Community 2 - "CLI Commands & Workflows"
Cohesion: 0.14
Nodes (26): dashboard(), ingest(), mcp(), organize(), Rebuild the index from existing files in the vault., Autonomously organize and optionally refine concepts., Start the Model Context Protocol (MCP) server., Launch the Human Dashboard (Web UI). (+18 more)

### Community 3 - "Database & Embeddings"
Cohesion: 0.08
Nodes (25): get_concepts_table(), get_db(), Connects to the local LanceDB instance., Returns the Concepts table, creating it if necessary., FastEmbedGenerator, Generates embeddings for a list of documents., Generates an embedding for a single query., Manual embedding generator using FastEmbed. (+17 more)

### Community 4 - "Vault Manager & Tests"
Cohesion: 0.16
Nodes (17): Tests moving a concept to a new folder., Tests finding the source file via rglob if not in root., Tests that move_concept still works if index update fails., Tests moving a concept when the target file already exists, creating a new name., Tests moving a concept when it's already in the target location., Tests moving a concept when the source file is not found in the root., test_vault_manager_move_concept_already_in_place(), test_vault_manager_move_concept_file_already_exists() (+9 more)

### Community 5 - "Document Converters"
Cohesion: 0.15
Nodes (11): DoclingWrapper, Converts a file (PDF, DOCX) to Markdown content., Wrapper for high-fidelity document conversion using Docling., MarkItDownWrapper, Converts a file to Markdown content., Wrapper for document conversion using MarkItDown., ConverterOrchestrator, Determines the best converter for the given file extension and returns Markdown. (+3 more)

### Community 6 - "UI Brand & Assets"
Cohesion: 0.19
Nodes (14): AtomicBrain Brand Identity, Social Media Link Set, UI Technology Stack (React + Vite), AtomicBrain Favicon / App Logo, Hero Layered Isometric Illustration, Bluesky Social Icon, Discord Icon, Documentation Icon (+6 more)

### Community 7 - "AI Agents"
Cohesion: 0.22
Nodes (8): OrganizationResult, Structured output from the Organization Agent., Structured output from the Refinement Agent., RefinementResult, Runs the organization agent to suggest a path., suggest_organization(), Runs the refinement agent on raw content., refine_concept()

### Community 8 - "CLI Tests"
Cohesion: 0.4
Nodes (4): Tests the organize command with refinement and move., Tests the mcp command., test_mcp_command(), test_organize_command_refine_and_move()

### Community 9 - "Frontend App"
Cohesion: 0.4
Nodes (0): 

### Community 10 - "Vite Build Plugins"
Cohesion: 0.67
Nodes (3): @vitejs/plugin-react, @vitejs/plugin-react-swc, Vite

### Community 11 - "ESLint & React"
Cohesion: 1.0
Nodes (2): ESLint, React

### Community 12 - "Package Init"
Cohesion: 1.0
Nodes (0): 

### Community 13 - "ESLint Config"
Cohesion: 1.0
Nodes (0): 

### Community 14 - "Vite Config"
Cohesion: 1.0
Nodes (0): 

### Community 15 - "Ruff Linter"
Cohesion: 1.0
Nodes (1): Ruff

### Community 16 - "Pytest"
Cohesion: 1.0
Nodes (1): Pytest

### Community 17 - "TypeScript"
Cohesion: 1.0
Nodes (1): TypeScript

## Knowledge Gaps
- **45 isolated node(s):** `LanceDB schema for AtomicBrain Concepts.`, `Connects to the local LanceDB instance.`, `Returns the Concepts table, creating it if necessary.`, `Manual embedding generator using FastEmbed.`, `Generates embeddings for a list of documents.` (+40 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `ESLint & React`** (2 nodes): `ESLint`, `React`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Package Init`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `ESLint Config`** (1 nodes): `eslint.config.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Vite Config`** (1 nodes): `vite.config.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Ruff Linter`** (1 nodes): `Ruff`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Pytest`** (1 nodes): `Pytest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `TypeScript`** (1 nodes): `TypeScript`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Searcher` connect `Data Models & API` to `CLI Commands & Workflows`, `Database & Embeddings`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._
- **Why does `VaultManager` connect `Vault Manager & Tests` to `CLI Commands & Workflows`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Why does `ConverterOrchestrator` connect `Document Converters` to `CLI Commands & Workflows`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `ConceptRecord` (e.g. with `Indexer` and `Handles indexing of Concepts into LanceDB.`) actually correct?**
  _`ConceptRecord` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `Searcher` (e.g. with `Convert a file into an Obsidian-compatible Concept and index it.` and `Perform hybrid search across ingested concepts.`) actually correct?**
  _`Searcher` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 18 inferred relationships involving `VaultManager` (e.g. with `Convert a file into an Obsidian-compatible Concept and index it.` and `Perform hybrid search across ingested concepts.`) actually correct?**
  _`VaultManager` has 18 INFERRED edges - model-reasoned connections that need verification._
- **Are the 16 inferred relationships involving `Concept` (e.g. with `Convert a file into an Obsidian-compatible Concept and index it.` and `Perform hybrid search across ingested concepts.`) actually correct?**
  _`Concept` has 16 INFERRED edges - model-reasoned connections that need verification._