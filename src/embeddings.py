import numpy as np
from typing import List
from fastembed import TextEmbedding

class FastEmbedGenerator:
    """Manual embedding generator using FastEmbed."""
    
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model = TextEmbedding(model_name)

    def embed_documents(self, texts: List[str]) -> List[np.ndarray]:
        """Generates embeddings for a list of documents."""
        return list(self.model.embed(texts))

    def embed_query(self, query: str) -> np.ndarray:
        """Generates an embedding for a single query."""
        # FastEmbed's embed() returns an iterator, we take the first result
        return next(self.model.embed([query]))
