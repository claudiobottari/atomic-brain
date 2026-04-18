from datetime import datetime
from src.models import Concept, ConceptMetadata

def test_concept_metadata_creation():
    now = datetime.utcnow()
    metadata = ConceptMetadata(
        source="test.pdf",
        id="123",
        title="Test Title",
        tags=["tag1", "tag2"],
        timestamp=now
    )
    assert metadata.source == "test.pdf"
    assert metadata.id == "123"
    assert metadata.title == "Test Title"
    assert metadata.tags == ["tag1", "tag2"]
    assert metadata.timestamp == now

def test_concept_to_obsidian_markdown():
    now = datetime(2026, 4, 17, 12, 0, 0)
    metadata = ConceptMetadata(
        source="test.pdf",
        id="123",
        title="Test Title",
        tags=["tag1", "tag2"],
        timestamp=now
    )
    concept = Concept(metadata=metadata, content="Hello World")
    
    markdown = concept.to_obsidian_markdown()
    
    expected_frontmatter = """---
source: test.pdf
id: '123'
type: concept
timestamp: '2026-04-17T12:00:00'
title: Test Title
tags:
- tag1
- tag2
version: '1.0'
---"""
    
    assert markdown.startswith(expected_frontmatter)
    assert "Hello World" in markdown
