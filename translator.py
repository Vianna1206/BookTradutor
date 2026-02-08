"""
Translator module for BookTradutor
Handles translation of different file formats
"""

import os
import re
from pathlib import Path
from typing import Optional
from googletrans import Translator
from tqdm import tqdm


class BookTranslator:
    """Main translator class for handling various file formats"""
    
    def __init__(self, verbose: bool = False):
        """
        Initialize the translator
        
        Args:
            verbose: Enable verbose output
        """
        self.translator = Translator()
        self.verbose = verbose
        
    def translate_text(self, text: str, source_lang: str = 'auto', 
                      target_lang: str = 'pt') -> str:
        """
        Translate a text string
        
        Args:
            text: Text to translate
            source_lang: Source language code
            target_lang: Target language code
            
        Returns:
            Translated text
        """
        if not text or not text.strip():
            return text
            
        try:
            result = self.translator.translate(
                text, 
                src=source_lang, 
                dest=target_lang
            )
            return result.text
        except Exception as e:
            if self.verbose:
                print(f"Warning: Translation failed for text: {text[:50]}... Error: {e}")
            return text
    
    def translate_file(self, input_path: Path, output_path: Path,
                      source_lang: str = 'auto', target_lang: str = 'pt'):
        """
        Translate a file based on its format
        
        Args:
            input_path: Path to input file
            output_path: Path to output file
            source_lang: Source language code
            target_lang: Target language code
        """
        file_extension = input_path.suffix.lower()
        
        if file_extension == '.pdf':
            self._translate_pdf(input_path, output_path, source_lang, target_lang)
        elif file_extension in ['.txt', '.md', '.text']:
            self._translate_text_file(input_path, output_path, source_lang, target_lang)
        else:
            # Try as text file
            self._translate_text_file(input_path, output_path, source_lang, target_lang)
    
    def _translate_text_file(self, input_path: Path, output_path: Path,
                            source_lang: str, target_lang: str):
        """Translate a plain text file"""
        print(f"Reading file: {input_path}")
        
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            # Try with different encoding
            with open(input_path, 'r', encoding='latin-1') as f:
                content = f.read()
        
        # Split into paragraphs for better translation
        paragraphs = content.split('\n\n')
        translated_paragraphs = []
        
        print(f"Translating {len(paragraphs)} paragraphs from {source_lang} to {target_lang}...")
        
        for paragraph in tqdm(paragraphs, desc="Translation progress"):
            if paragraph.strip():
                translated = self.translate_text(paragraph, source_lang, target_lang)
                translated_paragraphs.append(translated)
            else:
                translated_paragraphs.append('')
        
        # Write translated content
        translated_content = '\n\n'.join(translated_paragraphs)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
    
    def _translate_pdf(self, input_path: Path, output_path: Path,
                      source_lang: str, target_lang: str):
        """Translate a PDF file"""
        try:
            import PyPDF2
        except ImportError:
            raise ImportError("PyPDF2 is required for PDF translation. Install it with: pip install PyPDF2")
        
        print(f"Reading PDF: {input_path}")
        
        # Read PDF
        with open(input_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            num_pages = len(pdf_reader.pages)
            
            print(f"Extracting text from {num_pages} pages...")
            
            all_text = []
            for page_num in tqdm(range(num_pages), desc="Extracting pages"):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                all_text.append(text)
        
        # Translate extracted text
        print(f"Translating content from {source_lang} to {target_lang}...")
        translated_pages = []
        
        for page_text in tqdm(all_text, desc="Translation progress"):
            if page_text.strip():
                # Split into smaller chunks for better translation
                chunks = self._split_into_chunks(page_text, max_length=5000)
                translated_chunks = []
                
                for chunk in chunks:
                    translated = self.translate_text(chunk, source_lang, target_lang)
                    translated_chunks.append(translated)
                
                translated_pages.append('\n'.join(translated_chunks))
            else:
                translated_pages.append('')
        
        # Save as text file (creating PDF requires more complex libraries)
        output_txt = output_path.with_suffix('.txt')
        with open(output_txt, 'w', encoding='utf-8') as f:
            for i, page_text in enumerate(translated_pages, 1):
                f.write(f"\n{'='*60}\n")
                f.write(f"PAGE {i}\n")
                f.write(f"{'='*60}\n\n")
                f.write(page_text)
                f.write("\n\n")
        
        print(f"Note: PDF content extracted and translated to text file: {output_txt}")
    
    def _split_into_chunks(self, text: str, max_length: int = 5000) -> list:
        """Split text into chunks for translation"""
        if len(text) <= max_length:
            return [text]
        
        chunks = []
        sentences = re.split(r'([.!?]\s+)', text)
        
        current_chunk = ""
        for sentence in sentences:
            if len(current_chunk) + len(sentence) <= max_length:
                current_chunk += sentence
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                current_chunk = sentence
        
        if current_chunk:
            chunks.append(current_chunk)
        
        return chunks
