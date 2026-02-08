#!/usr/bin/env python3
"""
BookTradutor - A learning project to translate books, comics, and other text documents
"""

import argparse
import sys
from pathlib import Path
from translator import BookTranslator


def main():
    parser = argparse.ArgumentParser(
        description='BookTradutor - Translate books, comics, and other documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Translate a text file from English to Portuguese
  python main.py input.txt -s en -t pt -o output.txt
  
  # Translate a PDF from English to Spanish
  python main.py book.pdf -s en -t es -o book_es.pdf
  
  # Auto-detect source language
  python main.py document.txt -t fr
        '''
    )
    
    parser.add_argument('input', type=str, help='Input file to translate')
    parser.add_argument('-s', '--source', type=str, default='auto',
                        help='Source language code (default: auto-detect)')
    parser.add_argument('-t', '--target', type=str, required=True,
                        help='Target language code (e.g., pt, en, es, fr)')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='Output file path (default: translated_<input_file>)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Verbose output')
    
    args = parser.parse_args()
    
    # Check if input file exists
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{args.input}' does not exist")
        sys.exit(1)
    
    # Determine output path
    if args.output is None:
        output_path = input_path.parent / f"translated_{input_path.name}"
    else:
        output_path = Path(args.output)
    
    # Create translator instance
    translator = BookTranslator(verbose=args.verbose)
    
    try:
        # Translate the file
        actual_output_path = translator.translate_file(
            input_path=input_path,
            output_path=output_path,
            source_lang=args.source,
            target_lang=args.target
        )
        
        print(f"\n✓ Translation completed successfully!")
        print(f"  Output saved to: {actual_output_path}")
        
    except Exception as e:
        print(f"\n✗ Error during translation: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
