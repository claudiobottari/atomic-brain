import pytest
from unittest.mock import MagicMock, patch
import numpy as np
from src.embeddings import FastEmbedGenerator

def test_fast_embed_generator_init():
    """Tests the initialization of FastEmbedGenerator."""
    model_name = "test-model"
    mock_embedding_model = MagicMock()
    mock_embedding_model.ndims.return_value = 384
    
    with patch('src.embeddings.TextEmbedding', return_value=mock_embedding_model) as mock_text_embedding:
        generator = FastEmbedGenerator(model_name=model_name)
        mock_text_embedding.assert_called_once_with(model_name)
        assert generator.model == mock_embedding_model

def test_fast_embed_generator_embed_documents():
    """Tests the embed_documents method of FastEmbedGenerator."""
    mock_embedding_model = MagicMock()
    mock_embedding_model.embed.return_value = iter([np.array([0.1, 0.2]), np.array([0.3, 0.4])])
    
    generator = FastEmbedGenerator()
    generator.model = mock_embedding_model
    
    texts = ["text1", "text2"]
    embeddings = generator.embed_documents(texts)
    
    mock_embedding_model.embed.assert_called_once_with(texts)
    assert len(embeddings) == 2
    assert isinstance(embeddings[0], np.ndarray)
    assert np.array_equal(embeddings[0], np.array([0.1, 0.2]))
    assert np.array_equal(embeddings[1], np.array([0.3, 0.4]))

def test_fast_embed_generator_embed_query():
    """Tests the embed_query method of FastEmbedGenerator."""
    mock_embedding_model = MagicMock()
    # .embed() returns an iterator, so we mock its behavior
    mock_embedding_model.embed.return_value = iter([np.array([0.5, 0.6])]) 
    
    generator = FastEmbedGenerator()
    generator.model = mock_embedding_model
    
    query = "sample query"
    embedding = generator.embed_query(query)
    
    mock_embedding_model.embed.assert_called_once_with([query])
    assert isinstance(embedding, np.ndarray)
    assert np.array_equal(embedding, np.array([0.5, 0.6]))
