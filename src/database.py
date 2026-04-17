import lancedb
import numpy as np
from pathlib import Path
from lancedb.pydantic import LanceModel, Vector

class ConceptRecord(LanceModel):
    """LanceDB schema for AtomicBrain Concepts."""
    id: str
    title: str
    content: str
    vector: Vector(384) # BGE-small-en-v1.5 dimension
    source: str
    timestamp: str
    tags: str

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
