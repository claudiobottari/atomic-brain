import logging
from typing import List
from .database import get_concepts_table, ConceptRecord
from .embeddings import FastEmbedGenerator

logger = logging.getLogger(__name__)

class Searcher:
    """Handles hybrid search across Concepts in LanceDB."""
    
    def __init__(self):
        self.table = get_concepts_table()
        self.embedder = FastEmbedGenerator()

    def search(self, query: str, limit: int = 5) -> List[ConceptRecord]:
        """Performs hybrid search (vector + FTS) and returns results."""
        try:
            # Generate embedding for the query
            query_vector = self.embedder.embed_query(query)
            
            # Perform hybrid search using vector() and text()
            results = (
                self.table.search(query_vector)
                .text(query)
                .limit(limit)
                .to_pydantic(ConceptRecord)
            )
            return results
        except Exception as e:
            # Fallback to vector search if hybrid fails
            logger.warning(f"Hybrid search failed, falling back to vector: {e}")
            return self.table.search(query_vector).limit(limit).to_pydantic(ConceptRecord)
