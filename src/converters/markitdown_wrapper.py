from pathlib import Path
from markitdown import MarkItDown

class MarkItDownWrapper:
    """Wrapper for document conversion using MarkItDown."""
    
    def __init__(self):
        self.md = MarkItDown()

    def convert(self, file_path: Path) -> str:
        """Converts a file to Markdown content."""
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        result = self.md.convert(str(file_path))
        return result.text_content
