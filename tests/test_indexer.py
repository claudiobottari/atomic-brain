import pytest
from unittest.mock import MagicMock, patch
from src.indexer import Indexer
from src.models import Concept, ConceptMetadata
from datetime import datetime

@patch('src.indexer.get_concepts_table')
def test_indexer_index(mock_get_concepts_table):
    """Tests the index method of the Indexer."""
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table
    
    indexer = Indexer()
    
    # Mock the concept data
    metadata = ConceptMetadata(source="doc.md", id="concept-123", title="Test Concept", timestamp=datetime.utcnow())
    concept = Concept(metadata=metadata, content="Some content here.")
    
    indexer.index(concept)
    
    # Verify that table.add was called with the correct record
    mock_table.add.assert_called_once()
    added_record = mock_table.add.call_args[0][0][0]
    
    assert added_record.id == "concept-123"
    assert added_record.title == "Test Concept"
    assert added_record.content == "Some content here."
    assert added_record.source == "doc.md"
    assert added_record.tags == "" # Empty list defaults to empty string
    
    # Verify FTS index creation
    mock_table.create_fts_index.assert_called_once_with("content", replace=True)

@patch('src.indexer.get_concepts_table')
def test_indexer_index_handles_errors(mock_get_concepts_table):
    """Tests that indexer logs errors and re-raises exceptions."""
    mock_table = MagicMock()
    mock_get_concepts_table.return_value = mock_table
    mock_table.add.side_effect = Exception("Database error")
    
    indexer = Indexer()
    
    metadata = ConceptMetadata(source="doc.md", id="concept-123", title="Test Concept")
    concept = Concept(metadata=metadata, content="Some content here.")
    
    with pytest.raises(Exception) as excinfo:
        indexer.index(concept)
        
    assert "Database error" in str(excinfo.value)
    mock_table.add.assert_called_once()
    mock_table.create_fts_index.assert_not_called() # FTS index creation should not happen if add fails
