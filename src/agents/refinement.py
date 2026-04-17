import os
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from .models import RefinementResult

# Use LiteLLM-compatible model setup
# You can set OPENAI_API_BASE to point to Ollama/vLLM
model_name = os.getenv("BRAIN_MODEL", "gpt-4o-mini")
model = OpenAIModel(model_name)

refinement_agent = Agent(
    model,
    result_type=RefinementResult,
    system_prompt=(
        "You are the 'AtomicBrain' Refinement Agent. Your goal is to distill raw, "
        "often messy document conversions into atomic, high-quality knowledge 'Concepts'.\n\n"
        "1. Extract a clear, concise title.\n"
        "2. Provide a one-sentence summary.\n"
        "3. Identify key points and entities.\n"
        "4. Clean up the Markdown content: fix formatting errors, remove noise (headers/footers), "
        "and ensure it is atomic (one core idea).\n"
        "5. Suggest semantic tags."
    ),
)

async def refine_concept(content: str) -> RefinementResult:
    """Runs the refinement agent on raw content."""
    result = await refinement_agent.run(content)
    return result.data
