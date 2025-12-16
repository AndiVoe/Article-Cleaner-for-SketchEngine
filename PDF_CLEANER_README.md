# PDF Research Article Cleaner

A Python command-line tool that extracts and cleans text from research article PDFs for use with **Sketch Engine** and other corpus analysis tools.

## Features

✅ **Automatic Section Removal**
- Abstracts and keywords
- References and bibliography
- Acknowledgments
- Author information and affiliations
- Conflicts of interest declarations
- Copyright and publication information
- Headers, footers, and page numbers

✅ **Batch Processing**
- Process entire folders recursively
- Or process specific PDF files
- Progress indicators for each file

✅ **Robust Error Handling**
- Skips corrupted PDFs gracefully
- Continues processing remaining files
- Detailed logging of all operations

✅ **Clean Output**
- Generates `.docx` files (Word format) for Sketch Engine compatibility
- Automatically creates `cleaned_articles/` subfolder
- Preserves main article body text (introduction, methods, results, discussion, conclusion)
- Files named as `[original_name]_cleaned.docx`

## Requirements

```
PyMuPDF==1.24.12
python-docx==1.1.2
```

## Installation

### 1. Install Dependencies

```bash
pip install PyMuPDF python-docx
```

Or using requirements file:

```bash
pip install -r requirements.txt
```

### 2. Download the Script

Place `pdf_cleaner.py` in your working directory.

## Usage

### Process All PDFs in a Folder

```bash
python pdf_cleaner.py --folder /path/to/articles
```

**Subfolder example:**
```bash
python pdf_cleaner.py --folder ./my_research_papers
```

This will:
1. Find all `.pdf` files recursively
2. Extract and clean each one
3. Save cleaned versions to `./my_research_papers/cleaned_articles/`

### Process Specific PDF Files

```bash
python pdf_cleaner.py paper1.pdf paper2.pdf paper3.pdf
```

Or mix paths:
```bash
python pdf_cleaner.py ./folder/paper1.pdf paper2.pdf
```

This will:
1. Process each specified file
2. Save cleaned versions to `./cleaned_articles/` (in current directory)

### View Help

```bash
python pdf_cleaner.py --help
```

## Output

### Naming Convention
- Input: `research_article.pdf`
- Output: `research_article_cleaned.docx`

### Location
- **Folder processing:** `<input_folder>/cleaned_articles/`
- **Individual files:** `./cleaned_articles/`

### Content
The cleaned file contains only:
- Introduction
- Methods
- Results
- Discussion
- Conclusion
- Main body text

Removed sections:
- ❌ Title page
- ❌ Abstract
- ❌ Keywords
- ❌ References
- ❌ Acknowledgments
- ❌ Author information
- ❌ Headers/Footers
- ❌ Page numbers

## Logging

The script provides detailed logging:

```
2025-12-16 10:30:45,123 - INFO - Processing: paper1...
2025-12-16 10:30:47,456 - INFO - ✓ Saved: ./cleaned_articles/paper1_cleaned.docx
2025-12-16 10:30:48,789 - WARNING - Skipping paper2 (insufficient content after cleaning)
2025-12-16 10:30:50,012 - INFO - Processing complete!
2025-12-16 10:30:50,012 - INFO - Successful: 4 | Failed: 1 | Total: 5
```

## Configuration

### Customizing Section Keywords

Edit the `SECTION_KEYWORDS` dictionary in `pdf_cleaner.py`:

```python
SECTION_KEYWORDS = {
    'abstract': ['abstract', 'summary'],
    'keywords': ['keywords', 'key words', 'index terms'],
    'acknowledgments': ['acknowledgments', 'acknowledgements', 'funding'],
    # Add custom keywords:
    'custom': ['your_keyword', 'another_keyword'],
}
```

### Adjusting Cleaning Sensitivity

**Footer patterns** (line 30-37):
```python
FOOTER_PATTERNS = [
    r'^page \d+[\s\S]*?$',
    r'^https?://[\S]+',
    # Add more regex patterns for your PDFs
]
```

**Minimum line length** for body text (line 41):
```python
MIN_BODY_LINE_LENGTH = 20  # Increase to skip more short lines
```

## Examples

### Example 1: Single Folder
```bash
python pdf_cleaner.py --folder ./research_papers
```

Input structure:
```
research_papers/
├── nature_2023.pdf
├── science_2022.pdf
└── journal_2021.pdf
```

Output structure:
```
research_papers/
├── nature_2023.pdf
├── science_2022.pdf
├── journal_2021.pdf
└── cleaned_articles/
    ├── nature_2023_cleaned.docx
    ├── science_2022_cleaned.docx
    └── journal_2021_cleaned.docx
```

### Example 2: Multiple Specific Files
```bash
python pdf_cleaner.py ./papers/study1.pdf ./papers/study2.pdf ./downloaded/study3.pdf
```

Output:
```
cleaned_articles/
├── study1_cleaned.docx
├── study2_cleaned.docx
└── study3_cleaned.docx
```

## Using with Sketch Engine

1. **Process your PDFs:**
   ```bash
   python pdf_cleaner.py --folder ./articles
   ```

2. **Upload cleaned files to Sketch Engine:**
   - Navigate to `cleaned_articles/` folder
   - Select `.docx` files
   - Upload to your Sketch Engine project

3. **Or create a corpus:**
   - Combine all `.docx` files into your corpus directory
   - Use Sketch Engine's import tools

## Troubleshooting

### Issue: "No PDF files found"
- Check folder path is correct
- Ensure files have `.pdf` extension (case-sensitive on Linux)
- Try: `python pdf_cleaner.py --folder .` for current directory

### Issue: "Insufficient content after cleaning"
- PDF may have non-standard formatting
- Edit `SECTION_KEYWORDS` to better match your PDFs
- Check if PDF is image-based (requires OCR)

### Issue: Output file is empty
- Original PDF may be corrupted
- Try opening PDF with another application first
- Check logs for specific errors

### Issue: Memory error on large folders
- Process files in smaller batches
- Use individual file mode: `python pdf_cleaner.py file1.pdf file2.pdf`

## Performance

- **Single paper:** ~1-3 seconds
- **Batch (10 papers):** ~15-30 seconds
- **Large folder (100+ papers):** 2-5 minutes

Processing speed depends on:
- PDF size and complexity
- System resources (RAM, CPU)
- PDF extraction quality

## File Format Notes

### Why .docx?
- ✅ Compatible with Sketch Engine
- ✅ Preserves text formatting
- ✅ Smaller file size than PDF
- ✅ Universal compatibility
- ✅ Easy to edit if needed

## Advanced Usage

### Process with Custom Keywords

Create a modified version of `pdf_cleaner.py`:

```python
SECTION_KEYWORDS = {
    'abstract': ['abstract', 'summary', 'overview'],
    'references': ['references', 'bibliography', 'works cited', 'citations'],
    'methods': ['methods', 'methodology'],  # Add to remove methods if needed
}
```

Then run:
```bash
python pdf_cleaner.py --folder ./articles
```

## Limitations

- Requires PDFs with extractable text (not image-based scans)
- Accuracy depends on PDF structure consistency
- May need tuning for non-standard academic formats
- Very large files (>1000 pages) may be slow

## Support & Debugging

### Enable Verbose Logging

The script already provides INFO-level logging. For more details, modify the logging level:

```python
logging.basicConfig(level=logging.DEBUG)  # Change INFO to DEBUG
```

### Check a Single File

```bash
python pdf_cleaner.py problematic_paper.pdf
```

Then review the output in `cleaned_articles/` and logs.

## License & Attribution

This tool is designed for academic and research purposes. Always respect PDF copyright and terms of use when processing research papers.

## Version

**PDF Cleaner v1.0**
- Supports Python 3.8+
- Last updated: December 2025
