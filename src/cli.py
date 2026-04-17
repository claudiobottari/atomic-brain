import typer
import uuid
import logging
import asyncio
import yaml
from pathlib import Path
from datetime import datetime
from typing import Optional

from .models import Concept, ConceptMetadata
from .converters.orchestrator import ConverterOrchestrator
from .indexer import Indexer
from .searcher import Searcher
from .vault_manager import VaultManager
from .agents.refinement import refine_concept
from .agents.organization import suggest_organization

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

app = typer.Typer(help="AtomicBrain: Local-first, LLM-agnostic knowledge management.")
orchestrator = ConverterOrchestrator()
indexer = Indexer()
searcher = Searcher()
vault_manager = VaultManager()

@app.command()
def ingest(
    file_path: Path = typer.Argument(..., help="Path to the file to ingest."),
    vault_path: Path = typer.Option(Path("vault/Concepts"), help="Directory where ingested Concepts are stored."),
    title: Optional[str] = typer.Option(None, help="Custom title for the concept."),
    tags: Optional[str] = typer.Option(None, help="Comma-separated tags."),
):
    """Convert a file into an Obsidian-compatible Concept and index it."""
    if not file_path.exists():
        typer.echo(f"Error: File not found at {file_path}", err=True)
        raise typer.Exit(code=1)
    
    # Ensure vault path exists
    vault_path.mkdir(parents=True, exist_ok=True)
    
    try:
        # Step 1: Convert to Markdown content
        typer.echo(f"Ingesting: {file_path}")
        content = orchestrator.convert(file_path)
        
        # Step 2: Generate Metadata
        concept_id = str(uuid.uuid4())
        final_title = title if title else file_path.stem
        tag_list = [t.strip() for t in tags.split(",")] if tags else []
        
        metadata = ConceptMetadata(
            source=str(file_path.absolute()),
            id=concept_id,
            title=final_title,
            tags=tag_list,
            timestamp=datetime.utcnow()
        )
        
        # Step 3: Create Concept and format as Obsidian Markdown
        concept = Concept(metadata=metadata, content=content)
        obsidian_md = concept.to_obsidian_markdown()
        
        # Step 4: Save to Vault
        output_filename = f"{final_title}.md"
        output_path = vault_path / output_filename
        
        if output_path.exists():
            output_filename = f"{final_title}_{concept_id[:8]}.md"
            output_path = vault_path / output_filename
            
        output_path.write_text(obsidian_md, encoding="utf-8")
        typer.echo(f"Saved to vault: {output_path}")
        
        # Step 5: Index in LanceDB
        typer.echo("Indexing concept...")
        indexer.index(concept)
        typer.echo("Successfully indexed.")
        
    except Exception as e:
        logger.error(f"Failed to ingest {file_path}: {e}")
        raise typer.Exit(code=1)

@app.command()
def search(
    query: str = typer.Argument(..., help="Search query (natural language or keywords)."),
    limit: int = typer.Option(5, help="Maximum number of results to return.")
):
    """Perform hybrid search across ingested concepts."""
    typer.echo(f"Searching for: {query}...")
    results = searcher.search(query, limit=limit)
    
    if not results:
        typer.echo("No results found.")
        return

    typer.echo(f"\nFound {len(results)} results:\n")
    for i, res in enumerate(results, 1):
        typer.echo(f"{i}. {res.title}")
        typer.echo(f"   Source: {res.source}")
        typer.echo(f"   ID: {res.id}")
        # Show a snippet of content
        snippet = res.content[:150].replace("\n", " ") + "..."
        typer.echo(f"   Snippet: {snippet}")
        typer.echo("-" * 40)

@app.command()
def reindex(
    vault_path: Path = typer.Option(Path("vault/Concepts"), help="Directory to scan for concepts.")
):
    """Rebuild the index from existing files in the vault."""
    if not vault_path.exists():
        typer.echo(f"Vault path not found: {vault_path}", err=True)
        return

    import yaml
    typer.echo(f"Re-indexing files from {vault_path}...")
    
    files = list(vault_path.glob("*.md"))
    for file in files:
        try:
            raw_text = file.read_text(encoding="utf-8")
            if not raw_text.startswith("---"):
                continue
                
            parts = raw_text.split("---", 2)
            if len(parts) < 3:
                continue
                
            meta_raw = yaml.safe_load(parts[1])
            content = parts[2].strip()
            
            # Reconstruct metadata and concept
            metadata = ConceptMetadata(**meta_raw)
            concept = Concept(metadata=metadata, content=content)
            
            indexer.index(concept)
            typer.echo(f"Indexed: {file.name}")
        except Exception as e:
            logger.warning(f"Skipping {file.name}: {e}")

@app.command()
def organize(
    refine: bool = typer.Option(False, "--refine", help="Refine concept content using AI before organizing."),
    all_files: bool = typer.Option(False, "--all", help="Organize all concepts in the vault."),
    vault_path: Path = typer.Option(Path("vault/Concepts"), help="Vault path.")
):
    """Autonomously organize and optionally refine concepts."""
    if not vault_path.exists():
        typer.echo(f"Vault path not found: {vault_path}", err=True)
        return

    async def _run_organize():
        typer.echo("Starting autonomous organization...")
        files = list(vault_path.glob("*.md"))
        if not all_files:
            typer.echo("Hint: Use --all to process the entire vault.")
            files = files[:5] # Limit to 5 for non-all
            
        existing_folders = vault_manager.get_existing_folders()
        
        for file in files:
            try:
                typer.echo(f"\nProcessing: {file.name}")
                raw_text = file.read_text(encoding="utf-8")
                if not raw_text.startswith("---"): continue
                
                parts = raw_text.split("---", 2)
                if len(parts) < 3: continue
                
                meta_raw = yaml.safe_load(parts[1])
                content = parts[2].strip()
                concept_id = meta_raw.get("id")
                
                # 1. Refinement (Optional)
                if refine:
                    typer.echo("Refining concept content...")
                    refinement = await refine_concept(content)
                    content = refinement.refined_content
                    meta_raw["title"] = refinement.title
                    meta_raw["tags"] = list(set(meta_raw.get("tags", []) + refinement.suggested_tags))
                    
                    # Update the file content immediately
                    new_concept = Concept(metadata=ConceptMetadata(**meta_raw), content=content)
                    file.write_text(new_concept.to_obsidian_markdown(), encoding="utf-8")
                    # Update index with refined content
                    indexer.index(new_concept)

                # 2. Suggest Organization
                typer.echo("Categorizing...")
                summary = content[:200]
                org = await suggest_organization(summary, existing_folders)
                
                typer.echo(f"Moving to: {org.folder_path}")
                vault_manager.move_concept(file.name, org.folder_path, concept_id)
                
            except Exception as e:
                typer.echo(f"Error organizing {file.name}: {e}", err=True)

    asyncio.run(_run_organize())
    typer.echo("\nOrganization complete.")

if __name__ == "__main__":
    app()
