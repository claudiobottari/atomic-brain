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
        # Find by ID
        results = table.search().where(f"id = '{concept_id}'").limit(1).to_pydantic(ConceptRecord)
        
        if not results:
            return f"Concept with ID {concept_id} not found."
        
        res = results[0]
        return f"Title: {res.title}\nSource: {res.source}\nTimestamp: {res.timestamp}\nTags: {res.tags}\n\nContent:\n{res.content}"
    except Exception as e:
        return f"Error retrieving concept: {str(e)}"

if __name__ == "__main__":
    mcp.run()
