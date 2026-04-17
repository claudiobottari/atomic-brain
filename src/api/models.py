from pydantic import BaseModel
from typing import List, Dict
from ..database import ConceptRecord

class SystemStatus(BaseModel):
    status: str
    version: str
    database_connected: bool

class VaultStats(BaseModel):
    total_concepts: int
    categories: Dict[str, int]

class SearchResponse(BaseModel):
    query: str
    results: List[ConceptRecord]
