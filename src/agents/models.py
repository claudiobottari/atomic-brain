from typing import List, Optional
from pydantic import BaseModel, Field

class RefinementResult(BaseModel):
    """Structured output from the Refinement Agent."""
    title: str = Field(..., description="A concise, descriptive title for the concept.")
    summary: str = Field(..., description="A one-sentence summary of the core idea.")
    key_points: List[str] = Field(..., description="List of the most important takeaways.")
    entities: List[str] = Field(..., description="Key people, places, organizations, or technical terms.")
    refined_content: str = Field(..., description="The cleaned, atomic Markdown content.")
    suggested_tags: List[str] = Field(..., description="Semantic tags derived from the content.")

class OrganizationResult(BaseModel):
    """Structured output from the Organization Agent."""
    folder_path: str = Field(..., description="The suggested hierarchical folder path (e.g., 'Finance/Invoices/2024').")
    reasoning: str = Field(..., description="Technical rationale for this placement.")
