"""
PDF Processing and Text Utilities
Helper functions for PDF parsing, text cleaning, and preprocessing.
"""

import re
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional

try:
    import pdfplumber
except ImportError:
    raise ImportError(
        "pdfplumber is required. Install it with: pip install pdfplumber"
    )


class PDFProcessor:
    """Handles PDF text extraction and metadata parsing."""
    
    def __init__(self):
        self.supported_extensions = ['.pdf']
    
    def extract_text(self, pdf_path: Path) -> str:
        """
        Extract text content from a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text as a string
            
        Raises:
            Exception: If PDF cannot be processed
        """
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text_content = []
                
                for page_num, page in enumerate(pdf.pages, 1):
                    try:
                        page_text = page.extract_text()
                        if page_text:
                            text_content.append(page_text)
                    except Exception as e:
                        print(f"Warning: Could not extract text from page {page_num}: {e}")
                        continue
                
                if not text_content:
                    raise Exception("No text could be extracted from any page")
                
                return "\n\n".join(text_content)
                
        except Exception as e:
            raise Exception(f"Failed to process PDF '{pdf_path}': {e}")
    
    def extract_metadata(self, pdf_path: Path) -> Dict:
        """
        Extract metadata from PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Dictionary containing PDF metadata
        """
        try:
            with pdfplumber.open(pdf_path) as pdf:
                metadata = pdf.metadata or {}
                
                return {
                    "title": metadata.get("Title", ""),
                    "author": metadata.get("Author", ""),
                    "subject": metadata.get("Subject", ""),
                    "creator": metadata.get("Creator", ""),
                    "producer": metadata.get("Producer", ""),
                    "creation_date": metadata.get("CreationDate", ""),
                    "modification_date": metadata.get("ModDate", ""),
                    "page_count": len(pdf.pages),
                    "file_size": pdf_path.stat().st_size
                }
        except Exception as e:
            return {"error": f"Could not extract metadata: {e}"}
    
    def extract_tables(self, pdf_path: Path) -> List[List[List]]:
        """
        Extract tables from PDF if present.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            List of tables, where each table is a list of rows
        """
        tables = []
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_tables = page.extract_tables()
                    if page_tables:
                        tables.extend(page_tables)
        except Exception as e:
            print(f"Warning: Could not extract tables: {e}")
        
        return tables


class TextCleaner:
    """Handles text cleaning and preprocessing operations."""
    
    def __init__(self):
        # Common patterns for cleaning
        self.patterns = {
            'extra_whitespace': re.compile(r'\s+'),
            'page_breaks': re.compile(r'\f'),
            'bullet_points': re.compile(r'^[•\-\*\+]\s*', re.MULTILINE),
            'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'phone': re.compile(r'\b(?:\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})\b'),
            'date': re.compile(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b'),
            'currency': re.compile(r'\$[\d,]+\.?\d*|\b\d+\.?\d*\s*(?:USD|EUR|GBP|dollars?|euros?|pounds?)\b', re.IGNORECASE),
        }
    
    def clean_text(self, text: str) -> str:
        """
        Clean and normalize text content.
        
        Args:
            text: Raw text to clean
            
        Returns:
            Cleaned and normalized text
        """
        if not text:
            return ""
        
        # Normalize unicode characters
        text = unicodedata.normalize('NFKD', text)
        
        # Remove page breaks
        text = self.patterns['page_breaks'].sub(' ', text)
        
        # Normalize whitespace
        text = self.patterns['extra_whitespace'].sub(' ', text)
        
        # Remove excessive line breaks
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        
        # Strip leading/trailing whitespace
        text = text.strip()
        
        return text
    
    def extract_structured_data(self, text: str) -> Dict:
        """
        Extract structured data like emails, phone numbers, dates, etc.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary containing extracted structured data
        """
        structured_data = {}
        
        # Extract emails
        emails = self.patterns['email'].findall(text)
        if emails:
            structured_data['emails'] = list(set(emails))
        
        # Extract phone numbers
        phones = self.patterns['phone'].findall(text)
        if phones:
            structured_data['phone_numbers'] = ['-'.join(phone) for phone in phones]
        
        # Extract dates
        dates = self.patterns['date'].findall(text)
        if dates:
            structured_data['dates'] = list(set(dates))
        
        # Extract currency amounts
        currency = self.patterns['currency'].findall(text)
        if currency:
            structured_data['currency_amounts'] = list(set(currency))
        
        return structured_data
    
    def get_text_statistics(self, text: str) -> Dict:
        """
        Calculate basic text statistics.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary containing text statistics
        """
        if not text:
            return {}
        
        words = text.split()
        sentences = re.split(r'[.!?]+', text)
        paragraphs = text.split('\n\n')
        
        return {
            'character_count': len(text),
            'word_count': len(words),
            'sentence_count': len([s for s in sentences if s.strip()]),
            'paragraph_count': len([p for p in paragraphs if p.strip()]),
            'average_words_per_sentence': len(words) / max(len(sentences), 1),
            'reading_time_minutes': len(words) / 200  # Assuming 200 words per minute
        }
    
    def extract_keywords(self, text: str, top_n: int = 10) -> List[str]:
        """
        Extract potential keywords from text using simple frequency analysis.
        
        Args:
            text: Text to analyze
            top_n: Number of top keywords to return
            
        Returns:
            List of potential keywords
        """
        # Simple keyword extraction - in production, consider using libraries like NLTK or spaCy
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        
        # Common stop words to filter out
        stop_words = {
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'who', 'boy', 'did', 'she', 'use', 'way', 'been', 'call', 'came', 'each', 'find', 'have', 'here', 'just', 'like', 'long', 'look', 'made', 'make', 'many', 'more', 'most', 'move', 'much', 'must', 'name', 'need', 'only', 'over', 'said', 'same', 'some', 'take', 'than', 'that', 'this', 'time', 'very', 'well', 'were', 'what', 'when', 'will', 'with', 'word', 'work', 'your'
        }
        
        # Filter stop words and count frequency
        filtered_words = [word for word in words if word not in stop_words and len(word) > 3]
        word_freq = {}
        for word in filtered_words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Return top keywords
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:top_n]]
