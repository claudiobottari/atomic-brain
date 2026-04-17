import lancedb
from pathlib import Path
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

# Initialize embedding model from registry (defaulting to bge-small-en-v1.5 via FastEmbed)
registry = get_registry().get("fastembed")
embedding_model = registry.create()

class ConceptRecord(LanceModel):
    """LanceDB schema for AtomicBrain Concepts."""
    id: str
    title: str
    content: str = embedding_model.SourceField()  # Field to be embedded
    vector: Vector(embedding_model.ndims()) = embedding_model.VectorField()
    source: str
    timestamp: str
    tags: str  # Stored as comma-separated string for easier FTS

DB_PATH = Path(".lancedb")

def get_db():
    """Connects to the local LanceDB instance."""
    DB_PATH.mkdir(exist_ok=True)
    return lancedb.connect(str(DB_PATH))

def get_concepts_table():
    """Returns the Concepts table, creating it if necessary."""
    db = get_db()
    table_name = "concepts"
    
    if table_name in db.table_names():
        return db.open_table(table_name)
    
    return db.create_table(table_name, schema=ConceptRecord)
