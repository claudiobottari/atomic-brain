import typer
import uuid
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional

from .models import Concept, ConceptMetadata
from .converters.orchestrator import ConverterOrchestrator

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

app = typer.Typer(help="AtomicBrain: Local-first, LLM-agnostic knowledge management.")
orchestrator = ConverterOrchestrator()

@app.command()
def ingest(
    file_path: Path = typer.Argument(..., help="Path to the file to ingest."),
    vault_path: Path = typer.Option(Path("vault/Concepts"), help="Directory where ingested Concepts are stored."),
    title: Optional[str] = typer.Option(None, help="Custom title for the concept."),
    tags: Optional[str] = typer.Option(None, help="Comma-separated tags."),
):
    """Convert a file into an Obsidian-compatible Concept."""
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
        # Use provided title or fallback to filename stem
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
        
        # Handle filename collisions (basic)
        if output_path.exists():
            output_filename = f"{final_title}_{concept_id[:8]}.md"
            output_path = vault_path / output_filename
            
        output_path.write_text(obsidian_md, encoding="utf-8")
        typer.echo(f"Successfully ingested to: {output_path}")
        
    except Exception as e:
        logger.error(f"Failed to ingest {file_path}: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
