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
    r'Â©\s*\d{4}',  # Copyright
    r'vol\.?\s*\d+',  # Volume numbers
    r'pp\.?\s*\d+',  # Page ranges
    r'^(received|revised|accepted|available online)[\s\S]*?$',  # Article history
]

# Regex patterns to remove article history entries
ARTICLE_HISTORY_PATTERNS = [
    r'article\s+history[\s\S]*?(?=^[A-Z\d]{3,}[\s]|introduction|^[A-Za-z]{3,}\s|$)',
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


def remove_invalid_chars(text: str) -> str:
    """
    Remove invalid XML characters from text (control characters, NULL bytes, etc).
    These cause issues when saving to .docx format.

    Args:
        text: Text possibly containing invalid characters

    Returns:
        Text with invalid characters removed
    """
    # Remove NULL bytes and other control characters (except tab, newline, carriage return)
    text = ''.join(char for char in text if ord(char) >= 32 or char in '\t\n\r')
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
    for pattern in ARTICLE_HISTORY_PATTERNS:
        text = re.sub(pattern, '', text, flags=re.MULTILINE | re.IGNORECASE | re.DOTALL)

    lines = text.split('\n')
    cleaned_lines = []

    for line in lines:
        # Skip page breaks
        if '---PAGE_BREAK---' in line:
            continue

        # Skip empty lines
        if not line.strip():
            cleaned_lines.append('')
            continue

        # Remove footer patterns
        if any(re.match(pattern, line.strip(), re.IGNORECASE) for pattern in FOOTER_PATTERNS):
            continue

        # Skip very short lines (likely headers/footers)
        if len(line.strip()) < MIN_BODY_LINE_LENGTH and line.strip() and not line.strip()[0].isupper():
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
        # Sanitize text to remove invalid XML characters
        text = remove_invalid_chars(text)

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
        logger.error(f"Failed to extract text from {pdf_path}")
        return False

    # Clean text
    try:
        cleaned_text = clean_text(text)
    except Exception as e:
        logger.error(f"Cleaning failed for {pdf_name}: {str(e)}")
        return False

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save to docx
    output_path = output_dir / f"{pdf_name}.docx"
    success = save_to_docx(cleaned_text, str(output_path))

    if success:
        logger.info(f"Successfully processed: {pdf_name}")
        return True
    else:
        logger.error(f"Failed to save: {pdf_name}")
        return False


def process_folder(folder_path: str) -> Tuple[int, int]:
    """
    Process all PDFs in a folder recursively.

    Args:
        folder_path: Path to folder containing PDFs

    Returns:
        Tuple of (successful_count, failed_count)
    """
    folder = Path(folder_path)
    output_dir = folder / "cleaned_articles"

    # Find all PDFs
    pdf_files = list(folder.glob("**/*.pdf"))

    if not pdf_files:
        logger.warning(f"No PDF files found in {folder_path}")
        return 0, 0

    success_count = 0
    failed_count = 0

    for pdf_file in pdf_files:
        if process_pdf(str(pdf_file), output_dir):
            success_count += 1
        else:
            failed_count += 1

    # Log completion summary
    total = success_count + failed_count
    logger.info("=" * 70)
    logger.info("✅ FOLDER PROCESSING COMPLETE!")
    logger.info("=" * 70)
    logger.info(f"Total files processed: {total}")
    logger.info(f"✅ Successfully cleaned: {success_count}")
    logger.info(f"❌ Failed: {failed_count}")
    logger.info(f"📁 Output folder: {output_dir}")
    logger.info("=" * 70)

    return success_count, failed_count


def process_files(file_paths: List[str]) -> Tuple[int, int]:
    """
    Process specific PDF files.
    Each file's cleaned output is saved in a 'cleaned_articles' subfolder
    in the SAME directory as the source PDF.

    Args:
        file_paths: List of PDF file paths

    Returns:
        Tuple of (successful_count, failed_count)
    """
    success_count = 0
    failed_count = 0

    for file_path in file_paths:
        # Get the directory of the source PDF
        pdf_dir = Path(file_path).parent
        output_dir = pdf_dir / "cleaned_articles"
        
        if process_pdf(file_path, output_dir):
            success_count += 1
        else:
            failed_count += 1

    # Log completion summary
    total = success_count + failed_count
    logger.info("=" * 70)
    logger.info("✅ FILE PROCESSING COMPLETE!")
    logger.info("=" * 70)
    logger.info(f"Total files processed: {total}")
    logger.info(f"✅ Successfully cleaned: {success_count}")
    logger.info(f"❌ Failed: {failed_count}")
    logger.info(f"📁 Files saved in 'cleaned_articles/' folders in each PDF's directory")
    logger.info("=" * 70)

    return success_count, failed_count


# ============================================================================
# GUI
# ============================================================================

class PDFCleanerGUI:
    """GUI for PDF Cleaner using tkinter."""

    def __init__(self, root):
        self.root = root
        self.root.title("PDF Cleaner for Sketch Engine")
        self.root.geometry("600x400")

        # Title
        title = tk.Label(root, text="PDF Cleaner for Sketch Engine", font=("Arial", 16, "bold"))
        title.pack(pady=20)

        # Description
        desc = tk.Label(root, text="Remove headers, footers, and metadata from research PDFs", 
                       font=("Arial", 10), fg="gray")
        desc.pack()

        # Buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        self.select_pdfs_btn = tk.Button(button_frame, text="Select PDFs", 
                                        command=self.select_pdfs, width=20, height=2)
        self.select_pdfs_btn.pack(side=tk.LEFT, padx=10)

        self.select_folder_btn = tk.Button(button_frame, text="Select Folder", 
                                          command=self.select_folder, width=20, height=2)
        self.select_folder_btn.pack(side=tk.LEFT, padx=10)

        # Progress text
        self.progress_text = tk.Text(root, height=15, width=70, state=tk.DISABLED)
        self.progress_text.pack(pady=10, padx=10)

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(root, textvariable=self.status_var, fg="blue")
        status_bar.pack(pady=10)

    def log_message(self, message: str):
        """Add message to progress text."""
        self.progress_text.config(state=tk.NORMAL)
        self.progress_text.insert(tk.END, message + "\n")
        self.progress_text.see(tk.END)
        self.progress_text.config(state=tk.DISABLED)
        self.root.update()

    def select_pdfs(self):
        """Select individual PDF files."""
        file_paths = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )

        if file_paths:
            self.log_message(f"Processing {len(file_paths)} files...")
            self.log_message("-" * 70)
            success, failed = process_files(list(file_paths))
            self.log_message("-" * 70)
            self.log_message(f"✅ PROCESSING COMPLETE!")
            self.log_message(f"Total files: {success + failed}")
            self.log_message(f"✅ Successfully cleaned: {success}")
            self.log_message(f"❌ Failed: {failed}")
            self.log_message("-" * 70)
            self.status_var.set(f"✅ Done! Success: {success}, Failed: {failed}")

    def select_folder(self):
        """Select a folder of PDFs."""
        folder_path = filedialog.askdirectory(title="Select folder with PDFs")

        if folder_path:
            self.log_message(f"Processing folder: {folder_path}")
            self.log_message("-" * 70)
            success, failed = process_folder(folder_path)
            self.log_message("-" * 70)
            self.log_message(f"✅ PROCESSING COMPLETE!")
            self.log_message(f"Total files: {success + failed}")
            self.log_message(f"✅ Successfully cleaned: {success}")
            self.log_message(f"❌ Failed: {failed}")
            self.log_message("-" * 70)
            self.status_var.set(f"✅ Done! Success: {success}, Failed: {failed}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Clean research PDFs by removing headers, footers, abstracts, and references."
    )

    input_group = parser.add_mutually_exclusive_group(required=False)
    input_group.add_argument("files", nargs="*", help="PDF file paths to process")
    input_group.add_argument("--folder", "-f", help="Process all PDFs in a folder (recursive)")
    input_group.add_argument("--gui", "-g", action="store_true", help="Launch GUI mode")

    args = parser.parse_args()

    # If no arguments provided, launch GUI
    if not args.files and not args.folder and not args.gui:
        args.gui = True

    if args.gui:
        # Launch GUI
        root = tk.Tk()
        app = PDFCleanerGUI(root)
        root.mainloop()

    elif args.folder:
        # Process folder
        print(f"Processing folder: {args.folder}")
        success, failed = process_folder(args.folder)
        print(f"\n✅ Success: {success} | ❌ Failed: {failed}")

    elif args.files:
        # Process files
        print(f"Processing {len(args.files)} files...")
        success, failed = process_files(args.files)
        print(f"\nSuccess: {success} | Failed: {failed}")


if __name__ == "__main__":
    main()
