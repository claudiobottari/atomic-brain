import os
from typing import List
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from .models import OrganizationResult

model_name = os.getenv("BRAIN_MODEL", "gpt-4o-mini")
model = OpenAIModel(model_name)

organization_agent = Agent(
    model,
    result_type=OrganizationResult,
    system_prompt=(
        "You are the 'AtomicBrain' Organization Agent. Your goal is to determine the "
        "optimal hierarchical folder structure for knowledge Concepts.\n\n"
        "Rules:\n"
        "1. Create a path that is semantic and logical (e.g., 'Projects/AtomicBrain/Design').\n"
        "2. Do not include the file name in the path.\n"
        "3. Keep the hierarchy reasonably shallow (max 4 levels).\n"
        "4. Use Title Case for folder names.\n"
        "5. Consider the existing vault structure if provided."
    ),
)

async def suggest_organization(content_summary: str, existing_folders: List[str]) -> OrganizationResult:
    """Runs the organization agent to suggest a path."""
    context = f"Summary: {content_summary}\n\nExisting structure: {', '.join(existing_folders)}"
    result = await organization_agent.run(context)
    return result.data
