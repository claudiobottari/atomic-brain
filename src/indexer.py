import logging
from .models import Concept
from .database import get_concepts_table, ConceptRecord

logger = logging.getLogger(__name__)

class Indexer:
    """Handles indexing of Concepts into LanceDB."""
    
    def __init__(self):
        self.table = get_concepts_table()

    def index(self, concept: Concept):
        """Adds or updates a Concept in the index."""
        try:
            record = ConceptRecord(
                id=concept.metadata.id,
                title=concept.metadata.title or "Untitled",
                content=concept.content,
                source=concept.metadata.source,
                timestamp=concept.metadata.timestamp.isoformat(),
                tags=",".join(concept.metadata.tags)
            )
            
            # Use merge/upsert if possible, or simple add for now
            # LanceDB 'add' handles embedding automatically via the schema definition
            self.table.add([record])
            logger.info(f"Indexed concept: {record.title} (ID: {record.id})")
            
            # Create/Update FTS index after adding
            self.table.create_fts_index("content", replace=True)
            
        except Exception as e:
            logger.error(f"Failed to index concept {concept.metadata.id}: {e}")
            raise
