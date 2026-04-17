# Phase 5: Human Dashboard (Web UI) - Context

## Domain Boundary
Provide a centralized web interface for system monitoring, knowledge exploration, and basic search.

## Implementation Decisions

### Frontend Stack
- **Framework**: React (TypeScript).
- **Build Tool**: Vite.
- **Styling**: Vanilla CSS (Modern, "Obsidian-like" aesthetic).

### Backend API
- **Framework**: FastAPI (extending the existing `src/` core).
- **Endpoints**:
  - `GET /api/status`: System health and ingestion metrics.
  - `GET /api/search`: Concept search (proxied to `Searcher`).
  - `GET /api/concepts/{id}`: Detailed concept view.
  - `GET /api/stats`: Vault statistics (counts by category, etc.).

### CLI Integration
- **Command**: `atomic-brain dashboard` starts the FastAPI server and optionally serves the built frontend.

## Canonical References
- `https://fastapi.tiangolo.com/`
- `https://vitejs.dev/`
