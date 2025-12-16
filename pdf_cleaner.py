#!/usr/bin/env python3
"""
PDF Research Article Cleaner
Extracts and cleans text from academic PDFs for use with Sketch Engine.
Removes headers, footers, abstracts, references, and other non-body content.
"""

import argparse
import logging
import re
import sys
import tkinter as tk
from pathlib import Path
from typing import List, Tuple, Optional
from tkinter import filedialog, messagebox
from tkinter import ttk

import fitz  # PyMuPDF
from docx import Document
from docx.shared import Pt, RGBColor


# ============================================================================
# CONFIGURATION
# ============================================================================

# Keywords to identify and remove sections (case-insensitive)
SECTION_KEYWORDS = {
    'abstract': ['abstract', 'summary'],
    'keywords': ['keywords', 'key words', 'index terms'],
    'acknowledgments': ['acknowledgments', 'acknowledgements'],
    'funding': ['funding statement', 'financial disclosure', 'grant', 'supported by'],
    'conflict': ['conflict of interest', 'declaration of interest', 'competing interests'],
    'supplementary': ['supplementary material', 'supplementary information', 'supporting information', 'appendix'],
    'author_info': ['author information', 'correspondence', 'author details', 'affiliation'],
    'references': ['references', 'bibliography', 'citations', 'works cited'],
    'abbreviations': ['list of abbreviations', 'abbreviations', 'list of acronyms'],
    'article_history': ['article history', 'received', 'revised', 'accepted', 'available online'],
}

# Regex patterns to remove common academic footer/header patterns
FOOTER_PATTERNS = [
    r'^page \d+[\s\S]*?$',  # Page X
    r'^\d+[\s\S]*?$',  # Just page numbers
    r'^https?://[\S]+',  # URLs
    r'©\s*\d{4}',  # Copyright
    r'vol\.?\s*\d+',  # Volume numbers
    r'pp\.?\s*\d+',  # Page ranges
    r'^(received|revised|accepted|available online)[\s\S]*?$',  # Article history
]

# Regex patterns to remove article history entries
ARTICLE_HISTORY_PATTERNS = [
    r'article\s+history[\s\S]*?(?=^[A-Z\d]{{3,}}[\s]|introduction|^[A-Za-z]{3,}\s|$)',
    r'(received|revised|accepted|available online)\s+\d+\s+(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{4}',
]
# Regex patterns for conflict of interest, funding, and supplementary materials
METADATA_PATTERNS = [
    r'conflict\s+of\s+interest[\s\S]{0,500}?(?=\n\n|introduction|acknowledgments|$)',  # Conflict statements
    r'funding\s+(statement|disclosure|information)[\s\S]{0,300}?(?=\n\n|conflict|acknowledgments|$)',  # Funding statements
    r'supplementary\s+(material|information|data)[\s\S]{0,200}?(?=\n\n|appendix|references|$)',  # Supplementary refs
    r'this\s+work\s+was\s+(supported|funded)\s+by[\s\S]{0,200}?(?=\.|\n)',  # Inline funding
    r'grant\s+number[\s\S]{0,150}?(?=\n|\.)',  # Grant numbers
]
# Lines shorter than this are likely headers/footers
MIN_BODY_LINE_LENGTH = 20

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ============================================================================
# CORE FUNCTIONS
# ============================================================================

def extract_text_from_pdf(pdf_path: str) -> Tuple[str, bool]:
    """
    Extract raw text from PDF file.
    
    Args:
        pdf_path: Path to PDF file
        
    Returns:
        Tuple of (extracted_text, success_flag)
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text += page.get_text()
            text += "\n\n---PAGE_BREAK---\n\n"
        
        doc.close()
        return text, True
    
    except Exception as e:
        logger.error(f"Failed to extract text from {pdf_path}: {str(e)}")
        return "", False


def remove_section_by_keyword(text: str, keywords: List[str]) -> str:
    """
    Remove text section starting with specified keywords.
    Removes from keyword match to the next major section heading.
    
    Args:
        text: Full article text
        keywords: List of keywords to match section start
        
    Returns:
        Text with section removed
    """
    for keyword in keywords:
        # Pattern: keyword (case-insensitive) followed by optional subtitle/colon
        pattern = rf'^[\s]*{re.escape(keyword)}[\s:\-]*.*?(?=^[A-Z\d]{{3,}}[\s]|$)'
        text = re.sub(
            pattern,
            '',
            text,
            flags=re.MULTILINE | re.IGNORECASE | re.DOTALL,
            count=1
        )
    
    return text


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text by removing headers, footers, and sections.
    
    Args:
        text: Raw extracted text
        
    Returns:
        Cleaned text suitable for corpus analysis
    """
    # Remove metadata patterns first (multi-line)
    for pattern in METADATA_PATTERNS:
        text = re.sub(pattern, '', text, flags=re.MULTILINE | re.IGNORECASE | re.DOTALL)

    # Remove article history patterns (multi-line)
        
        # Skip empty lines
        if not line.strip():
            cleaned_lines.append('')
            continue
        
        # Remove footer patterns
        if any(re.match(pattern, line.strip(), re.IGNORECASE) for pattern in FOOTER_PATTERNS):
            continue
        
        # Skip very short lines (likely headers/footers)
        if len(line.strip()) < MIN_BODY_LINE_LENGTH and not line[0].isupper():
            continue
        
        # Remove common header patterns (repeated across pages)
        if re.match(r'^(Journal|Volume|Issue|Pages|DOI)', line.strip(), re.IGNORECASE):
            continue
        
        # Skip lines that are article history entries
        if re.match(r'^(received|revised|accepted|available online)', line.strip(), re.IGNORECASE):
            continue
        
        cleaned_lines.append(line)
    
    # Join lines
    text = '\n'.join(cleaned_lines)
    
    # Remove sections by keyword
    for section, keywords in SECTION_KEYWORDS.items():
        text = remove_section_by_keyword(text, keywords)
    
    # Clean up excessive whitespace
    text = re.sub(r'\n{4,}', '\n\n\n', text)  # Remove excessive blank lines
    text = re.sub(r'[ \t]{2,}', ' ', text)  # Remove excessive spaces/tabs
    text = text.strip()
    
    return text


def save_to_docx(text: str, output_path: str) -> bool:
    """
    Save cleaned text to .docx file.
    
    Args:
        text: Cleaned text to save
        output_path: Path for output .docx file
        
    Returns:
        Success flag
    """
    try:
        doc = Document()
        
        # Add text in paragraphs
        paragraphs = text.split('\n\n')
        for para_text in paragraphs:
            if para_text.strip():
                para = doc.add_paragraph(para_text.strip())
                para.style = 'Normal'
                # Set font
                for run in para.runs:
                    run.font.size = Pt(11)
                    run.font.name = 'Calibri'
        
        doc.save(output_path)
        return True
    
    except Exception as e:
        logger.error(f"Failed to save to {output_path}: {str(e)}")
        return False


def process_pdf(pdf_path: str, output_dir: Path) -> bool:
    """
    Process single PDF: extract, clean, and save.
    
    Args:
        pdf_path: Path to input PDF
        output_dir: Directory for output files
        
    Returns:
        Success flag
    """
    pdf_name = Path(pdf_path).stem
    logger.info(f"Processing: {pdf_name}...")
    
    # Extract text
    text, success = extract_text_from_pdf(pdf_path)
    if not success:
        logger.warning(f"Skipping {pdf_name} (extraction failed)")
        return False
    
    # Clean text
    try:
        cleaned_text = clean_text(text)
        
        if not cleaned_text or len(cleaned_text.strip()) < 500:
            logger.warning(f"Skipping {pdf_name} (insufficient content after cleaning)")
            return False
    
    except Exception as e:
        logger.error(f"Cleaning failed for {pdf_name}: {str(e)}")
        return False
    
    # Create cleaned_articles subfolder
    cleaned_folder = output_dir / "cleaned_articles"
    cleaned_folder.mkdir(exist_ok=True)
    
    # Save to docx in cleaned_articles subfolder
    output_path = cleaned_folder / f"{pdf_name}_cleaned.docx"
    
    if save_to_docx(cleaned_text, str(output_path)):
        logger.info(f"✓ Saved: {output_path}")
        return True
    else:
        return False


def process_folder(folder_path: str) -> None:
    """
    Process all PDFs in a folder.
    
    Args:
        folder_path: Path to folder containing PDFs
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        logger.error(f"Folder not found: {folder_path}")
        sys.exit(1)
    
    # Find all PDFs (non-recursive)
    pdf_files = list(folder.glob('*.pdf')) + list(folder.glob('*.PDF'))
    
    if not pdf_files:
        logger.warning(f"No PDF files found in {folder_path}")
        sys.exit(1)
    
    logger.info(f"Found {len(pdf_files)} PDF(s)")
    logger.info(f"Output directory: {folder_path}/cleaned_articles (will be created)")
    
    # Process each PDF
    successful = 0
    failed = 0
    
    for idx, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{idx}/{len(pdf_files)}]", end=" ")
        
        if process_pdf(str(pdf_path), folder):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "="*70)
    logger.info(f"Processing complete!")
    logger.info(f"Successful: {successful} | Failed: {failed} | Total: {len(pdf_files)}")
    print("="*70)


def process_files(file_paths: List[str]) -> None:
    """
    Process specific PDF files.
    
    Args:
        file_paths: List of paths to PDF files
    """
    successful = 0
    failed = 0
    
    for idx, pdf_path in enumerate(file_paths, 1):
        print(f"\n[{idx}/{len(file_paths)}]", end=" ")
        
        if not Path(pdf_path).exists():
            logger.error(f"File not found: {pdf_path}")
            failed += 1
            continue
        
        # Save to same directory as the PDF
        output_dir = Path(pdf_path).parent
        
        if process_pdf(pdf_path, output_dir):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "="*70)
    logger.info(f"Processing complete!")
    logger.info(f"Successful: {successful} | Failed: {failed} | Total: {len(file_paths)}")
    print("="*70)


# ============================================================================
# GUI APPLICATION
# ============================================================================

class PDFCleanerGUI:
    """User-friendly GUI for PDF Cleaner."""
    
    def __init__(self, root):
        """Initialize the GUI."""
        self.root = root
        self.root.title("PDF Research Article Cleaner")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="PDF Research Article Cleaner",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 10))
        
        # Description
        desc_label = ttk.Label(
            main_frame,
            text="Select PDF files to clean for Sketch Engine.\nCleaned files will be saved in 'cleaned_articles' folder.",
            font=("Arial", 10),
            justify=tk.CENTER
        )
        desc_label.pack(pady=(0, 20))
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        # Select files button
        select_files_btn = ttk.Button(
            button_frame,
            text="📁 Select PDF Files",
            command=self.select_files
        )
        select_files_btn.pack(pady=10, fill=tk.X)
        
        # Select folder button
        select_folder_btn = ttk.Button(
            button_frame,
            text="📂 Select Folder",
            command=self.select_folder
        )
        select_folder_btn.pack(pady=10, fill=tk.X)
        
        # Selected files text
        ttk.Label(main_frame, text="Selected Files:", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(20, 5))
        
        # Text widget for showing selected files
        self.text_widget = tk.Text(main_frame, height=10, width=70, state=tk.DISABLED)
        self.text_widget.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.text_widget, command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Progress label
        self.progress_label = ttk.Label(main_frame, text="", font=("Arial", 9))
        self.progress_label.pack(anchor=tk.W, pady=(10, 0))
        
        # Footer
        footer_label = ttk.Label(
            main_frame,
            text="Cleaned files: [filename]_cleaned.docx in 'cleaned_articles' subfolder",
            font=("Arial", 9, "italic"),
            foreground="gray"
        )
        footer_label.pack(side=tk.BOTTOM, pady=(10, 0))
        
        self.selected_files = []
    
    def add_text(self, text):
        """Add text to the text widget."""
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, text + "\n")
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)
        self.root.update()
    
    def clear_text(self):
        """Clear text widget."""
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.config(state=tk.DISABLED)
    
    def select_files(self):
        """Open file dialog to select PDF files."""
        files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if files:
            self.selected_files = list(files)
            self.clear_text()
            self.add_text(f"Selected {len(self.selected_files)} file(s):\n")
            for f in self.selected_files:
                self.add_text(f"  • {Path(f).name}")
            
            # Process files
            self.process_selected_files()
    
    def select_folder(self):
        """Open folder dialog to select a folder."""
        folder = filedialog.askdirectory(title="Select Folder with PDFs")
        
        if folder:
            pdf_files = list(Path(folder).glob('*.pdf')) + list(Path(folder).glob('*.PDF'))
            
            if not pdf_files:
                messagebox.showwarning("No PDFs Found", f"No PDF files found in:\n{folder}")
                return
            
            self.selected_files = [str(f) for f in pdf_files]
            self.clear_text()
            self.add_text(f"Found {len(self.selected_files)} PDF(s) in:\n{folder}\n\n")
            for f in self.selected_files:
                self.add_text(f"  • {Path(f).name}")
            
            # Process files
            self.process_selected_files()
    
    def process_selected_files(self):
        """Process the selected PDF files."""
        if not self.selected_files:
            messagebox.showwarning("No Files", "No files selected!")
            return
        
        # Determine output directories (same as input files)
        output_dirs = {}
        for pdf_path in self.selected_files:
            pdf_dir = Path(pdf_path).parent
            if pdf_dir not in output_dirs:
                output_dirs[pdf_dir] = []
            output_dirs[pdf_dir].append(pdf_path)
        
        self.add_text("\n" + "="*70)
        self.add_text("PROCESSING...\n")
        
        successful = 0
        failed = 0
        
        for idx, pdf_path in enumerate(self.selected_files, 1):
            self.progress_label.config(text=f"Processing: {idx}/{len(self.selected_files)}")
            self.root.update()
            
            pdf_dir = Path(pdf_path).parent
            
            if process_pdf(pdf_path, pdf_dir):
                successful += 1
                self.add_text(f"✓ {Path(pdf_path).name}")
            else:
                failed += 1
                self.add_text(f"✗ {Path(pdf_path).name} (failed)")
        
        self.add_text("\n" + "="*70)
        self.add_text(f"COMPLETE: {successful} successful, {failed} failed")
        self.progress_label.config(text="")
        
        messagebox.showinfo(
            "Processing Complete",
            f"Successfully cleaned: {successful}\nFailed: {failed}\n\nCheck 'cleaned_articles' folder for '_cleaned.docx' files"
        )


# ============================================================================
# CLI & MAIN
# ============================================================================

def main():
    """Main entry point - uses GUI by default, CLI if arguments provided."""
    # Check if CLI arguments provided
    if len(sys.argv) > 1:
        # Use CLI mode
        parser = argparse.ArgumentParser(
            description="Clean research PDFs by removing headers, footers, abstracts, and references.",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  # Process all PDFs in a folder
  python pdf_cleaner.py --folder /path/to/articles
  
  # Process specific PDF files
  python pdf_cleaner.py paper1.pdf paper2.pdf paper3.pdf
            """
        )
        
        # Input options (mutually exclusive)
        input_group = parser.add_mutually_exclusive_group(required=True)
        input_group.add_argument(
            '--folder', '-f',
            type=str,
            help='Process all PDFs in a folder (recursive)'
        )
        input_group.add_argument(
            'files',
            nargs='*',
            help='PDF file paths to process'
        )
        
        args = parser.parse_args()
        
        # Process based on input type
        if args.folder:
            process_folder(args.folder)
        elif args.files:
            if not args.files:
                parser.error("Please provide PDF file paths or use --folder")
            process_files(args.files)
        else:
            parser.print_help()
    else:
        # Use GUI mode
        root = tk.Tk()
        app = PDFCleanerGUI(root)
        root.mainloop()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Process interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        sys.exit(1)
