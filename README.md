# 📚 PDF Cleaner - Research Article Text Extractor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A powerful Python tool for extracting and cleaning text from academic research PDFs. Removes metadata, headers, footers, and non-body content to create clean text corpora suitable for linguistic analysis with [Sketch Engine](https://www.sketchengine.eu/).

## 🎯 Features

- **Intelligent Text Extraction**: Uses PyMuPDF for accurate PDF text extraction
- **Comprehensive Content Removal**:
    - ✅ Keywords, Index Terms
  - ✅ Article history (Received, Revised, Accepted dates)
  - ✅ Conflict of interest statements
  - ✅ Funding statements
  - ✅ Supplementary material references
  - ✅ Abbreviations lists
  - ✅ Headers, footers, and page numbers
  - ✅ Copyright information
  
- **Multiple Interfaces**:
  - 🖱️ **GUI** - User-friendly graphical interface with file selection
  - 💻 **CLI** - Command-line interface for batch processing
  - 📦 **Python API** - Use as a library in your own scripts

- **Batch Processing**: Process multiple PDFs at once
- **Smart Output Organization**: Cleaned files automatically saved to `cleaned_articles/` subfolder
- **Professional Output**: Generates clean .docx files with preserved formatting
- **Error Handling**: Robust error handling with detailed logging

## 📋 What Gets Removed

### Metadata & Administrative Content
- Abstract, Summary
- Keywords, Index Terms
- Author Information, Affiliations
- Conflict of Interest Statements
- Funding Statements
- Article History (dates)
- Correspondence Information

### Supplementary Content
- References, Bibliography
- Acknowledgments
- Supplementary Material References
- Appendices
- List of Abbreviations

### Structural Elements
- Page headers and footers
- Page numbers
- Copyright information
- Volume/Issue information
- Running titles
- DOI/URLs

### What Stays
✅ Introduction, Methods, Results, Discussion, Conclusion  
✅ Main article body text  
✅ Figures and table descriptions (optional)  
✅ All relevant academic content

## 🚀 Quick Start

### Requirements
- Python 3.7+
- PyMuPDF (`fitz`)
- python-docx

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/pdf-cleaner.git
cd pdf-cleaner
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Usage

#### GUI Mode (Easiest) 🖱️
```bash
python pdf_cleaner.py --gui
# or double-click: run_pdf_cleaner.bat
```

Then:
1. Click "Select PDFs" or "Select Folder"
2. Choose your files
3. Click "Process"
4. Find cleaned files in `cleaned_articles/` folder

#### Command Line 💻

Process single PDF:
```bash
python pdf_cleaner.py --input article.pdf --output cleaned.docx
```

Process entire folder:
```bash
python pdf_cleaner.py --folder "C:\My Papers"
```

Get help:
```bash
python pdf_cleaner.py --help
```

#### Python API 📦

```python
from pdf_cleaner import process_pdf

# Process single PDF
success = process_pdf('article.pdf', output_folder='cleaned_articles/')

# Get cleaned text directly
from pdf_cleaner import extract_text_from_pdf, clean_text

text, success = extract_text_from_pdf('article.pdf')
cleaned = clean_text(text)
print(cleaned)
```

## 📦 Output Structure

```
C:\Path\To\PDFs\
├── article1.pdf
├── article2.pdf
└── cleaned_articles/           ← Cleaned output folder (auto-created)
    ├── article1.docx
    └── article2.docx
```

## ⚙️ Configuration

Edit `SECTION_KEYWORDS` in `pdf_cleaner.py` to customize what gets removed:

```python
SECTION_KEYWORDS = {
    'abstract': ['abstract', 'summary'],
    'keywords': ['keywords', 'key words'],
    'funding': ['funding statement', 'financial disclosure'],
    'conflict': ['conflict of interest'],
    # Add or modify as needed
}
```

## 🔧 Customization

### Adjust Section Keywords
```python
SECTION_KEYWORDS = {
    'your_section': ['keyword1', 'keyword2', 'keyword3'],
}
```

### Modify Pattern Matching
```python
METADATA_PATTERNS = [
    r'your_pattern_here',
]
```

### Change Output Format
```python
from pdf_cleaner import save_to_docx, extract_text_from_pdf, clean_text

text, _ = extract_text_from_pdf('article.pdf')
cleaned = clean_text(text)
# Use cleaned text however you want
```

## 📊 Version History

### v2.3 (Current)
- ✨ Added Conflict of Interest statement removal
- ✨ Added Funding statement removal
- ✨ Added Supplementary Material reference removal
- 🐛 Improved pattern matching accuracy
- 📦 Released on GitHub

### v2.2
- ✨ Enhanced article history removal
- ✨ Improved header/footer detection

### v2.1
- ✨ Added cleaned_articles/ subfolder output
- 🔧 Batch processing improvements

### v2.0
- 🚀 Initial release
- ✨ GUI and CLI interfaces
- ✨ Basic section removal

## 🧪 Testing

Test the tool with sample PDFs:

```bash
# Test single PDF
python pdf_cleaner.py --input sample.pdf --output test_output.docx

# Test folder processing
python pdf_cleaner.py --folder ./sample_pdfs

# Test GUI
python pdf_cleaner.py --gui
```

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'fitz'"
```bash
pip install PyMuPDF
```

### "ModuleNotFoundError: No module named 'docx'"
```bash
pip install python-docx
```

### PDF extraction fails
- Ensure PDF is not corrupted
- Try a different PDF
- Check file permissions
- Review logs for detailed error messages

### Cleaned text looks wrong
- Review SECTION_KEYWORDS in the code
- Adjust keyword matching patterns
- Check if article uses non-standard section naming

## 📖 Documentation

- **START_HERE.md** - Quickest introduction
- **PDF_CLEANER_USER_GUIDE.md** - Comprehensive manual
- **QUICK_REFERENCE.md** - One-page cheat sheet

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution:
- Additional section keyword patterns
- Support for more document types (ePub, HTML, etc.)
- Improved OCR support for scanned PDFs
- Performance optimizations
- Translation support
- Additional language patterns

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✨ Acknowledgments

- Built with [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- Output generation with [python-docx](https://python-docx.readthedocs.io/)
- Designed for [Sketch Engine](https://www.sketchengine.eu/) corpus creation

## 📬 Support

For issues and questions:
- 📋 Open an [Issue](https://github.com/yourusername/pdf-cleaner/issues)
- 💬 Start a [Discussion](https://github.com/yourusername/pdf-cleaner/discussions)
- 📧 Email or contact

## 🗺️ Roadmap

- [ ] Support for more PDF formats
- [ ] OCR integration for scanned PDFs
- [ ] Web interface
- [ ] Docker containerization
- [ ] Configuration file support (.yaml)
- [ ] Support for other output formats (TXT, PDF)
- [ ] Advanced filtering options (by language, date range, etc.)
- [ ] Duplicate detection and removal
- [ ] Metadata preservation option

---

**Made with ❤️ for researchers and corpus linguists**

*Last Updated: December 2025*
