import numpy as np
from unittest.mock import MagicMock, patch
from pathlib import Path
from src.database import get_db, get_concepts_table, ConceptRecord
from lancedb.pydantic import Vector

# Mocking the embedding model dimension as it's hardcoded in ConceptRecord
MOCK_VECTOR_DIM = 384

@patch('src.database.Path.mkdir')
@patch('lancedb.connect')
def test_get_db_creates_path_if_not_exists(mock_connect, mock_mkdir):
    """Tests that get_db creates the DB_PATH if it doesn't exist."""
    mock_db_instance = MagicMock()
    mock_connect.return_value = mock_db_instance
    
    db = get_db()
    
    mock_mkdir.assert_called_once_with(exist_ok=True)
    mock_connect.assert_called_once_with(str(Path(".lancedb")))
    assert db == mock_db_instance

@patch('src.database.Path.mkdir')
@patch('lancedb.connect')
def test_get_db_connects_to_existing_path(mock_connect, mock_mkdir):
    """Tests that get_db connects to the path if it already exists."""
    mock_db_instance = MagicMock()
    mock_connect.return_value = mock_db_instance
    
    db = get_db()
    
    mock_mkdir.assert_called_once_with(exist_ok=True)
    mock_connect.assert_called_once_with(str(Path(".lancedb")))
    assert db == mock_db_instance

@patch('src.database.get_db')
def test_get_concepts_table_opens_existing(mock_get_db):
    """Tests that get_concepts_table opens an existing table."""
    mock_db = MagicMock()
    mock_get_db.return_value = mock_db
    mock_db.table_names.return_value = ["concepts"]
    mock_table_instance = MagicMock()
    mock_db.open_table.return_value = mock_table_instance
    
    table = get_concepts_table()
    
    mock_db.open_table.assert_called_once_with("concepts")
    mock_db.create_table.assert_not_called()
    assert table == mock_table_instance

@patch('src.database.get_db')
def test_get_concepts_table_creates_new(mock_get_db):
    """Tests that get_concepts_table creates a new table if it doesn't exist."""
    mock_db = MagicMock()
    mock_get_db.return_value = mock_db
    mock_db.table_names.return_value = [] # No existing table
    mock_table_instance = MagicMock()
    mock_db.create_table.return_value = mock_table_instance
    
    table = get_concepts_table()
    
    mock_db.create_table.assert_called_once_with("concepts", schema=ConceptRecord)
    mock_db.open_table.assert_not_called()
    assert table == mock_table_instance

def test_concept_record_schema():
    """Tests the structure of the ConceptRecord schema."""
    record = ConceptRecord(
        id="test-id",
        title="Test Title",
        content="Test content",
        vector=np.array([0.1] * MOCK_VECTOR_DIM),
        source="/path/to/source.md",
        timestamp="2026-04-17T12:00:00",
        tags="tag1,tag2"
    )
    
    assert record.id == "test-id"
    assert record.title == "Test Title"
    assert record.content == "Test content"
    assert len(record.vector) == MOCK_VECTOR_DIM
    assert record.source == "/path/to/source.md"
    assert record.timestamp == "2026-04-17T12:00:00"
    assert record.tags == "tag1,tag2"
