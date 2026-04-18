import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from typer.testing import CliRunner
from pathlib import Path

from src.cli import app

runner = CliRunner()


@patch('src.cli.orchestrator')
@patch('src.cli.indexer')
def test_ingest_file_not_found(mock_indexer, mock_orchestrator):
    """Tests that ingest exits with code 1 when the file does not exist."""
    result = runner.invoke(app, ["ingest", "nonexistent_file.pdf"])
    assert result.exit_code == 1


@patch('src.cli.orchestrator')
@patch('src.cli.indexer')
def test_ingest_success(mock_indexer, mock_orchestrator, tmp_path):
    """Tests that ingest converts a file, saves it to the vault, and indexes it."""
    src_file = tmp_path / "test.md"
    src_file.write_text("# Hello World")
    vault_dir = tmp_path / "Concepts"

    mock_orchestrator.convert.return_value = "# Converted Content"

    result = runner.invoke(app, [
        "ingest", str(src_file),
        "--vault-path", str(vault_dir),
    ])

    assert result.exit_code == 0
    mock_orchestrator.convert.assert_called_once_with(src_file)
    mock_indexer.index.assert_called_once()
    md_files = list(vault_dir.glob("*.md"))
    assert len(md_files) == 1


@patch('src.cli.searcher')
def test_search_no_results(mock_searcher):
    """Tests that search prints 'No results found' when nothing matches."""
    mock_searcher.search.return_value = []

    result = runner.invoke(app, ["search", "unknown query"])

    assert result.exit_code == 0
    assert "No results found" in result.output


@patch('src.cli.searcher')
def test_search_with_results(mock_searcher):
    """Tests that search prints results when matches are found."""
    mock_result = MagicMock()
    mock_result.title = "Test Concept"
    mock_result.source = "/path/to/source.md"
    mock_result.id = "abc-123"
    mock_result.content = "Some content here"
    mock_searcher.search.return_value = [mock_result]

    result = runner.invoke(app, ["search", "test query"])

    assert result.exit_code == 0
    assert "Test Concept" in result.output
    mock_searcher.search.assert_called_once_with("test query", limit=5)


@patch('src.cli.asyncio')
@patch('src.cli.vault_manager')
@patch('src.cli.indexer')
def test_organize_vault_not_found(mock_indexer, mock_vault_manager, mock_asyncio, tmp_path):
    """Tests that organize exits cleanly when vault path does not exist."""
    result = runner.invoke(app, ["organize", "--vault-path", str(tmp_path / "nonexistent")])
    assert result.exit_code == 0
    assert "not found" in result.output


def test_mcp_command():
    """Tests that the mcp command starts the MCP server."""
    mock_mcp = MagicMock()
    with patch('src.mcp_server.mcp', mock_mcp):
        result = runner.invoke(app, ["mcp"])
    assert result.exit_code == 0
    assert "MCP server" in result.output


def test_dashboard_no_frontend(tmp_path):
    """Tests that dashboard exits with code 1 when ui/dist is missing."""
    with patch('src.cli.Path') as mock_path_cls:
        mock_dist = MagicMock()
        mock_dist.exists.return_value = False
        mock_path_cls.return_value = mock_dist
        result = runner.invoke(app, ["dashboard"])
    assert result.exit_code == 1
