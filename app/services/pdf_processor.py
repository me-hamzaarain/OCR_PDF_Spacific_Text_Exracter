"""PDF processing service module"""
import pdfplumber
from pathlib import Path
from typing import Dict, List, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PDFProcessor:
    """Service class for processing PDF files"""
    
    def __init__(self):
        """Initialize the PDF processor"""
        pass
    
    def extract_text_from_pdf(self, pdf_path: str) -> Dict[str, any]:
        """
        Extract raw text from a single PDF file
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Dictionary containing filename, status, text content, and page count
        """
        result = {
            'filename': Path(pdf_path).name,
            'status': 'success',
            'text': '',
            'pages': 0,
            'error': None
        }
        
        try:
            with pdfplumber.open(pdf_path) as pdf:
                result['pages'] = len(pdf.pages)
                
                # Extract text from all pages
                text_content = []
                for page_num, page in enumerate(pdf.pages, start=1):
                    page_text = page.extract_text()
                    if page_text:
                        text_content.append(f"--- Page {page_num} ---\n{page_text}")
                    else:
                        text_content.append(f"--- Page {page_num} ---\n[No text found on this page]")
                
                result['text'] = '\n\n'.join(text_content)
                
                logger.info(f"Successfully extracted text from {result['filename']} ({result['pages']} pages)")
                
        except Exception as e:
            result['status'] = 'error'
            result['error'] = str(e)
            logger.error(f"Error processing {pdf_path}: {str(e)}")
        
        return result
    
    def process_multiple_pdfs(self, pdf_paths: List[str]) -> List[Dict[str, any]]:
        """
        Process multiple PDF files
        
        Args:
            pdf_paths: List of paths to PDF files
            
        Returns:
            List of dictionaries containing extraction results for each PDF
        """
        results = []
        
        for pdf_path in pdf_paths:
            result = self.extract_text_from_pdf(pdf_path)
            results.append(result)
        
        logger.info(f"Processed {len(results)} PDF file(s)")
        return results
    
    def get_summary(self, results: List[Dict[str, any]]) -> Dict[str, any]:
        """
        Generate a summary of processing results
        
        Args:
            results: List of processing results
            
        Returns:
            Summary dictionary with statistics
        """
        total_files = len(results)
        successful = sum(1 for r in results if r['status'] == 'success')
        failed = total_files - successful
        total_pages = sum(r['pages'] for r in results if r['status'] == 'success')
        
        return {
            'total_files': total_files,
            'successful': successful,
            'failed': failed,
            'total_pages': total_pages
        }
