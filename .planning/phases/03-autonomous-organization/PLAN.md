# Phase 3: Autonomous Organization - Plan

## Objective
Implement "The Brain": an AI-driven system that extracts deep concepts and autonomously organizes the vault into a semantically meaningful hierarchy using Pydantic AI.

## Success Criteria
1.  Pydantic AI agents implemented for concept refinement and organization.
2.  Concepts are successfully distilled into atomic units with enhanced metadata.
3.  An autonomous organization logic moves files into a hierarchical folder structure based on semantic relevance.
4.  File system moves are correctly synchronized with the LanceDB index.
5.  A CLI entry point `atomic-brain organize` exists and works.

## Waves & Tasks

### Wave 1: Concept Refinement Agent
- [ ] **Task 1.1**: Set up Pydantic AI agent configuration with LiteLLM.
- [ ] **Task 1.2**: Define `RefinementResult` Pydantic model for structured agent output.
- [ ] **Task 1.3**: Implement the `RefinementAgent` to distill raw ingestion content into atomic concepts.

### Wave 2: Organization & Hierarchical Move
- [ ] **Task 2.1**: Implement the `OrganizationAgent` to suggest folder paths for concepts.
- [ ] **Task 2.2**: Create a `VaultManager` to handle physical file moves and folder creation.
- [ ] **Task 2.3**: Implement index synchronization logic to update LanceDB when files are moved.

### Wave 3: Integration & CLI
- [ ] **Task 3.1**: Integrate the refinement and organization agents into a unified workflow.
- [ ] **Task 3.2**: Add the `organize` command to `src/cli.py`.
- [ ] **Task 3.3**: Verify end-to-end organization with a sample set of ingested files.

## Verification Strategy
- **Agent Testing**: Test agents with diverse content to ensure reliable extraction and categorization.
- **FS Consistency**: Verify that the file system structure matches the agent's suggestions.
- **Index Integrity**: Ensure `atomic-brain search` still returns correct paths after organization.
