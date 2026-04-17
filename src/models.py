from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl

class ConceptMetadata(BaseModel):
    """Standardized metadata for an AtomicBrain Concept."""
    source: str = Field(..., description="Path to the original source file.")
    id: str = Field(..., description="Unique identifier for the concept (e.g., UUID or slug).")
    type: str = Field(default="concept", description="Document type (e.g., concept, resource, person).")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Time of ingestion.")
    title: Optional[str] = Field(None, description="Extracted or manually provided title.")
    tags: List[str] = Field(default_factory=list, description="Associated tags or categories.")
    version: str = Field(default="1.0", description="Schema version.")

class Concept(BaseModel):
    """A single knowledge unit in AtomicBrain."""
    metadata: ConceptMetadata
    content: str = Field(..., description="The Markdown content of the concept.")

    def to_obsidian_markdown(self) -> str:
        """Converts the concept to an Obsidian-compatible Markdown string with YAML frontmatter."""
        import yaml
        
        # Convert metadata to dict and handle datetime
        meta_dict = self.metadata.model_dump()
        meta_dict['timestamp'] = meta_dict['timestamp'].isoformat()
        
        yaml_frontmatter = yaml.dump(meta_dict, sort_keys=False).strip()
        return f"---\n{yaml_frontmatter}\n---\n\n{self.content}"
