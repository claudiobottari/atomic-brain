# Phase 1: Foundation & Ingestion - Plan

## Objective
Establish the project foundation with `uv` and implement the core ingestion pipeline to convert PDF, DOCX, and Markdown files into Obsidian-compatible "Concepts" with standardized metadata.

## Success Criteria
1.  Python environment initialized with `uv` and all dependencies (`Docling`, `MarkItDown`, `FastAPI`, `Pydantic AI`).
2.  Metadata schema for "Concepts" defined and validated via Pydantic.
3.  Ingestion pipeline correctly converts PDF and DOCX to Markdown.
4.  Ingested files are stored in a designated "Vault" directory with appropriate YAML frontmatter.
5.  A CLI entry point `atomic-brain ingest <path>` exists and works.

## Waves & Tasks

### Wave 1: Project Scaffolding & Schema
- [ ] **Task 1.1**: Initialize Python environment with `uv` and install core dependencies.
- [ ] **Task 1.2**: Define `Concept` metadata schema (YAML frontmatter) and Pydantic models.
- [ ] **Task 1.3**: Set up the basic directory structure for the local Obsidian vault.

### Wave 2: Ingestion Pipeline (Docling + MarkItDown)
- [ ] **Task 2.1**: Implement `Docling` wrapper for high-fidelity PDF/DOCX to Markdown conversion.
- [ ] **Task 2.2**: Implement `MarkItDown` as a secondary/fallback converter for common formats.
- [ ] **Task 2.3**: Create a `Converter` orchestrator that selects the appropriate tool based on file extension.

### Wave 3: CLI & Vault Integration
- [ ] **Task 3.1**: Create a basic CLI using `Typer` or `argparse` for the `ingest` command.
- [ ] **Task 3.2**: Implement the `ingest` logic: convert file, generate metadata, and save to vault.
- [ ] **Task 3.3**: Verify that ingested files are readable and valid in a standard Markdown/Obsidian viewer.

## Verification Strategy
- **Unit Tests**: Test the `Converter` orchestrator with various file types.
- **Integration Tests**: Run the `ingest` CLI command on a sample set of PDF, DOCX, and MD files and verify the output vault structure and metadata.
