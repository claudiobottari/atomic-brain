from unittest.mock import MagicMock, patch
from src.searcher import Searcher
from src.database import ConceptRecord
import numpy as np


@patch('src.searcher.get_concepts_table')
@patch('src.searcher.FastEmbedGenerator')
def test_searcher_search_hybrid(mock_fastembed_cls, mock_get_concepts_table):
    """Tests the search method of the Searcher for hybrid search."""
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table

    mock_embedder = MagicMock()
    mock_embedder.embed_query.return_value = np.array([0.5] * 384)
    mock_fastembed_cls.return_value = mock_embedder

    searcher = Searcher()

    mock_results = [
        ConceptRecord(id="id1", title="Title1", content="Content1", vector=np.array([0.1]*384), source="src1", timestamp="ts1", tags="tag1"),
        ConceptRecord(id="id2", title="Title2", content="Content2", vector=np.array([0.2]*384), source="src2", timestamp="ts2", tags="tag2"),
    ]

    # Mock the full chain: search().text().limit().to_pydantic()
    mock_search_chain = MagicMock()
    mock_table.search.return_value = mock_search_chain
    mock_search_chain.text.return_value.limit.return_value.to_pydantic.return_value = mock_results

    query = "test query"
    limit = 10

    results = searcher.search(query, limit=limit)

    mock_embedder.embed_query.assert_called_once_with(query)
    mock_table.search.assert_called_once_with(mock_embedder.embed_query.return_value)
    mock_search_chain.text.assert_called_once_with(query)
    mock_search_chain.text.return_value.limit.assert_called_once_with(limit)

    assert len(results) == 2
    assert results[0].id == "id1"


@patch('src.searcher.get_concepts_table')
@patch('src.searcher.FastEmbedGenerator')
def test_searcher_search_no_results(mock_fastembed_cls, mock_get_concepts_table):
    """Tests the search method when no results are found."""
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table

    mock_embedder = MagicMock()
    mock_embedder.embed_query.return_value = np.array([0.5] * 384)
    mock_fastembed_cls.return_value = mock_embedder

    searcher = Searcher()

    mock_search_chain = MagicMock()
    mock_table.search.return_value = mock_search_chain
    mock_search_chain.text.return_value.limit.return_value.to_pydantic.return_value = []

    results = searcher.search("nonexistent query")

    assert results == []
    mock_table.search.assert_called_once()


@patch('src.searcher.get_concepts_table')
@patch('src.searcher.FastEmbedGenerator')
def test_searcher_search_handles_errors(mock_fastembed_cls, mock_get_concepts_table):
    """Tests that searcher returns empty list when both hybrid and vector search fail."""
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table

    mock_embedder = MagicMock()
    mock_embedder.embed_query.return_value = np.array([0.5] * 384)
    mock_fastembed_cls.return_value = mock_embedder

    searcher = Searcher()
    mock_table.search.side_effect = Exception("Database connection error")

    results = searcher.search("error query")

    assert results == []
    assert mock_table.search.call_count == 2  # hybrid attempt + fallback attempt
