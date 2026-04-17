import logging
from pathlib import Path
from .docling_wrapper import DoclingWrapper
from .markitdown_wrapper import MarkItDownWrapper

logger = logging.getLogger(__name__)

class ConverterOrchestrator:
    """Orchestrates document conversion by selecting the appropriate tool."""
    
    def __init__(self):
        self.docling = DoclingWrapper()
        self.markitdown = MarkItDownWrapper()

    def convert(self, file_path: Path) -> str:
        """Determines the best converter for the given file extension and returns Markdown."""
        suffix = file_path.suffix.lower()
        
        # Prefer Docling for high-fidelity PDF/DOCX
        if suffix in {'.pdf', '.docx'}:
            logger.info(f"Using Docling for: {file_path}")
            return self.docling.convert(file_path)
        
        # Fallback to MarkItDown for others
        logger.info(f"Using MarkItDown for: {file_path}")
        return self.markitdown.convert(file_path)
