# Phase 4: Agent Bridge (MCP) - Plan

## Objective
Implement a Model Context Protocol (MCP) server that allows external AI agents (like Claude Desktop) to query and interact with the AtomicBrain knowledge base.

## Success Criteria
1.  MCP server implemented using the `mcp` Python SDK.
2.  Standard tools (`search_concepts`, `get_concept_details`) are available and functional.
3.  Specialized tools are dynamically registered based on the vault's folder structure.
4.  The server can be successfully connected to an MCP host (e.g., Claude Desktop).
5.  A CLI entry point `atomic-brain mcp` exists to start the server.

## Waves & Tasks

### Wave 1: Core MCP Server
- [ ] **Task 1.1**: Set up `src/mcp_server.py` with basic MCP server boilerplate.
- [ ] **Task 1.2**: Implement the `search_concepts` tool using `Searcher`.
- [ ] **Task 1.3**: Implement the `get_concept_details` tool to retrieve full content and metadata.

### Wave 2: Dynamic Tool Registration
- [ ] **Task 2.1**: Implement logic to scan top-level vault folders.
- [ ] **Task 2.2**: Dynamically register `query_<category>` tools for each major folder.
- [ ] **Task 2.3**: Ensure dynamic tools use scoped search (filtering by folder path).

### Wave 3: Integration & Deployment
- [ ] **Task 3.1**: Add the `mcp` command to `src/cli.py` to launch the server.
- [ ] **Task 3.2**: Provide instructions/helper for configuring the MCP host (e.g., `config.json` for Claude).
- [ ] **Task 3.3**: Verify end-to-end integration with a real MCP host.

## Verification Strategy
- **MCP Inspector**: Use the `mcp-inspector` to test tool registration and execution.
- **Host Integration**: Connect to Claude Desktop and verify that the agent can use AtomicBrain tools.
- **Dynamic Scoping**: Verify that `query_<category>` tools correctly limit results to the specified folder.
