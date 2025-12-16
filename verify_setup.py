#!/usr/bin/env python3
"""
QUICK START GUIDE for PDF Cleaner
Run this to verify installation and test the tool
"""

import subprocess
import sys
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed."""
    print("Checking dependencies...\n")
    
    deps = ['fitz', 'docx']
    missing = []
    
    for dep in deps:
        try:
            if dep == 'fitz':
                import fitz
                print(f"✓ PyMuPDF (fitz) - {fitz.version}")
            elif dep == 'docx':
                from docx import Document
                print(f"✓ python-docx")
        except ImportError:
            missing.append(dep)
            print(f"✗ Missing: {dep}")
    
    if missing:
        print("\n❌ Missing dependencies detected!")
        print("\nInstall with:")
        print("  pip install -r pdf_cleaner_requirements.txt")
        return False
    
    print("\n✅ All dependencies installed!")
    return True


def show_usage():
    """Display usage examples."""
    print("\n" + "="*70)
    print("USAGE EXAMPLES")
    print("="*70 + "\n")
    
    print("1. Process all PDFs in a folder:")
    print("   python pdf_cleaner.py --folder ./my_papers\n")
    
    print("2. Process specific PDF files:")
    print("   python pdf_cleaner.py paper1.pdf paper2.pdf paper3.pdf\n")
    
    print("3. Get help:")
    print("   python pdf_cleaner.py --help\n")
    
    print("="*70 + "\n")


def verify_script():
    """Verify pdf_cleaner.py exists and is executable."""
    script_path = Path('pdf_cleaner.py')
    
    if not script_path.exists():
        print("❌ pdf_cleaner.py not found in current directory!")
        print(f"Current directory: {Path.cwd()}")
        return False
    
    print(f"✓ Found pdf_cleaner.py in {Path.cwd()}")
    return True


def main():
    """Main setup verification."""
    print("\n" + "="*70)
    print("PDF RESEARCH ARTICLE CLEANER - Setup Verification")
    print("="*70 + "\n")
    
    # Check script exists
    if not verify_script():
        sys.exit(1)
    
    print()
    
    # Check dependencies
    if not check_dependencies():
        print("\nTo install missing packages, run:")
        print("  pip install -r pdf_cleaner_requirements.txt")
        sys.exit(1)
    
    # Show usage
    show_usage()
    
    print("✅ Setup verified! You're ready to use PDF Cleaner.\n")
    print("Next steps:")
    print("1. Place your PDF files in a folder")
    print("2. Run: python pdf_cleaner.py --folder /path/to/pdfs")
    print("3. Find cleaned .docx files in cleaned_articles/ folder")
    print("\nFor more information, see PDF_CLEANER_README.md\n")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
