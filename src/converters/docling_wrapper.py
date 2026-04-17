from pathlib import Path
from docling.document_converter import DocumentConverter

class DoclingWrapper:
    """Wrapper for high-fidelity document conversion using Docling."""
    
    def __init__(self):
        self.converter = DocumentConverter()

    def convert(self, file_path: Path) -> str:
        """Converts a file (PDF, DOCX) to Markdown content."""
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        result = self.converter.convert(str(file_path))
        return result.document.export_to_markdown()
