import logging
import json
from mcp.server.fastmcp import FastMCP
from .searcher import Searcher
from .database import get_concepts_table, ConceptRecord
from pathlib import Path

# Initialize FastMCP server
mcp = FastMCP("AtomicBrain")
searcher = Searcher()

@mcp.tool()
def search_concepts(query: str, limit: int = 5) -> str:
    """
    Search for knowledge concepts in AtomicBrain using hybrid semantic and keyword search.
    Returns a list of matching concepts with their titles, IDs, and snippets.
    """
    results = searcher.search(query, limit=limit)
    if not results:
        return "No matching concepts found."
    
    output = []
    for res in results:
        output.append(f"Title: {res.title}\nID: {res.id}\nSnippet: {res.content[:200]}...\n---")
    
    return "\n".join(output)

@mcp.tool()
def get_concept_details(concept_id: str) -> str:
    """
    Retrieve the full content and metadata of a specific concept by its ID.
    """
    try:
        table = get_concepts_table()
        results = table.search().where(f"id = '{concept_id}'").limit(1).to_pydantic(ConceptRecord)
        
        if not results:
            return f"Concept with ID {concept_id} not found."
        
        res = results[0]
        return f"Title: {res.title}\nSource: {res.source}\nTimestamp: {res.timestamp}\nTags: {res.tags}\n\nContent:\n{res.content}"
    except Exception as e:
        return f"Error retrieving concept: {str(e)}"

# Wave 2: Dynamic Tool Registration
def register_dynamic_tools():
    """Scans the vault and registers scoped search tools for each top-level category."""
    vault_base = Path("vault/Concepts")
    if not vault_base.exists():
        return

    categories = [p.name for p in vault_base.iterdir() if p.is_dir()]
    
    for category in categories:
        tool_name = f"query_{category.lower().replace(' ', '_')}"
        
        # We need a closure to capture the category correctly
        def create_tool(cat):
            @mcp.tool(name=f"query_{cat.lower().replace(' ', '_')}")
            def scoped_query(query: str, limit: int = 5) -> str:
                # Use FTS to filter by source path containing the category
                # Note: This is a simple implementation for MVP
                try:
                    table = get_concepts_table()
                    # We use a combined vector + text search with a where clause on the source path
                    query_vector = searcher.embedder.embed_query(query)
                    
                    # Normalize category for path matching
                    cat_path_part = cat.replace('\\', '/')
                    
                    results = (
                        table.search(query_vector)
                        .text(query)
                        .where(f"source LIKE '%/{cat_path_part}/%'")
                        .limit(limit)
                        .to_pydantic(ConceptRecord)
                    )
                    
                    if not results:
                        return f"No matching concepts found in category '{cat}'."
                    
                    output = []
                    for res in results:
                        output.append(f"Title: {res.title}\nID: {res.id}\nSnippet: {res.content[:200]}...\n---")
                    
                    return f"Results for '{query}' in {cat}:\n\n" + "\n".join(output)
                except Exception as e:
                    return f"Error searching category {cat}: {str(e)}"
            
            return scoped_query

        create_tool(category)

# Register tools on module load
register_dynamic_tools()

if __name__ == "__main__":
    mcp.run()
