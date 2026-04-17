from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
import os
from typing import List

from .models import SystemStatus, VaultStats, SearchResponse
from ..searcher import Searcher
from ..database import get_concepts_table, ConceptRecord

app = FastAPI(title="AtomicBrain API")
searcher = Searcher()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Endpoints
@app.get("/api/status", response_model=SystemStatus)
async def get_status():
    """Returns the system health and status."""
    try:
        get_concepts_table()
        db_connected = True
    except Exception:
        db_connected = False
        
    return {
        "status": "online",
        "version": "1.0.0",
        "database_connected": db_connected
    }

@app.get("/api/stats", response_model=VaultStats)
async def get_stats():
    """Returns vault statistics."""
    try:
        table = get_concepts_table()
        total = table.count_rows()
        
        vault_base = Path("vault/Concepts")
        categories = {}
        if vault_base.exists():
            for p in vault_base.iterdir():
                if p.is_dir():
                    count = len(list(p.rglob("*.md")))
                    categories[p.name] = count
                    
        return {
            "total_concepts": total,
            "categories": categories
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/search", response_model=SearchResponse)
async def search(q: str, limit: int = 10):
    """Hybrid search endpoint."""
    results = searcher.search(q, limit=limit)
    return {
        "query": q,
        "results": results
    }

@app.get("/api/concepts/{concept_id}", response_model=ConceptRecord)
async def get_concept(concept_id: str):
    """Retrieve a single concept by ID."""
    table = get_concepts_table()
    results = table.search().where(f"id = '{concept_id}'").limit(1).to_pydantic(ConceptRecord)
    if not results:
        raise HTTPException(status_code=404, detail="Concept not found")
    return results[0]

# Serve Static Frontend
dist_path = Path("ui/dist")
if dist_path.exists():
    app.mount("/", StaticFiles(directory=str(dist_path), html=True), name="static")
    
    @app.exception_handler(404)
    async def static_404_handler(request, exc):
        # For SPA support: return index.html on 404
        return FileResponse(dist_path / "index.html")
else:
    @app.get("/")
    async def root():
        return {"message": "AtomicBrain API is running. UI not built."}
