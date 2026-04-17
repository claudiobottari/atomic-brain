# Phase 5: Human Dashboard (Web UI) - Plan

## Objective
Implement a local web dashboard for monitoring system status, ingestion progress, and basic search/exploration.

## Success Criteria
1.  FastAPI backend implemented with endpoints for status, search, and stats.
2.  React/Vite frontend scaffolded and built with modern Vanilla CSS.
3.  Frontend components for Search results, Concept view, and Status dashboard functional.
4.  CLI entry point `atomic-brain dashboard` launches the server.
5.  Verification of end-to-end flow: search concept in UI and see results.

## Waves & Tasks

### Wave 1: Backend API (FastAPI)
- [ ] **Task 1.1**: Create `src/api/main.py` with FastAPI boilerplate.
- [ ] **Task 1.2**: Implement endpoints for `/api/status`, `/api/search`, and `/api/stats`.
- [ ] **Task 1.3**: Add Pydantic models for API responses.

### Wave 2: Frontend (React + Vite)
- [ ] **Task 2.1**: Scaffold React/Vite app in `ui/`.
- [ ] **Task 2.2**: Build Dashboard layout and "Obsidian-like" styling.
- [ ] **Task 2.3**: Implement Search component and Concept Detail viewer.

### Wave 3: Integration & CLI
- [ ] **Task 3.1**: Build frontend for production and configure FastAPI to serve static files.
- [ ] **Task 3.2**: Add the `dashboard` command to `src/cli.py`.
- [ ] **Task 3.3**: Verify end-to-end dashboard functionality in a browser.

## Verification Strategy
- **API Tests**: Use `pytest` and `httpx` to test backend endpoints.
- **UI Tests**: Manually verify responsiveness and functionality across search/view flows.
- **CLI Test**: Run `atomic-brain dashboard` and confirm it loads in `localhost:8000`.
