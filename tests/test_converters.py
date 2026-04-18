from unittest.mock import MagicMock, patch
from pathlib import Path
from src.converters.orchestrator import ConverterOrchestrator

def test_orchestrator_selects_docling_for_pdf():
    with patch('src.converters.orchestrator.DoclingWrapper') as mock_docling, \
         patch('src.converters.orchestrator.MarkItDownWrapper') as mock_markitdown:
        
        orchestrator = ConverterOrchestrator()
        orchestrator.docling.convert = MagicMock(return_value="# PDF Content")
        
        result = orchestrator.convert(Path("test.pdf"))
        
        assert result == "# PDF Content"
        orchestrator.docling.convert.assert_called_once()
        orchestrator.markitdown.convert.assert_not_called()

def test_orchestrator_selects_markitdown_for_md():
    with patch('src.converters.orchestrator.DoclingWrapper') as mock_docling, \
         patch('src.converters.orchestrator.MarkItDownWrapper') as mock_markitdown:
        
        orchestrator = ConverterOrchestrator()
        orchestrator.markitdown.convert = MagicMock(return_value="# MD Content")
        
        result = orchestrator.convert(Path("test.md"))
        
        assert result == "# MD Content"
        orchestrator.markitdown.convert.assert_called_once()
        orchestrator.docling.convert.assert_not_called()
