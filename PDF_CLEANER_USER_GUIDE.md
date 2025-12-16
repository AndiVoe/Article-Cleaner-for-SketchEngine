# PDF Research Article Cleaner - User Guide

A simple, user-friendly tool that cleans research PDFs for use with Sketch Engine.

## ✨ Key Feature: Cleaned files are saved **in the same directory** as your original PDFs!

---

## 🚀 Quick Start (3 Steps)

### **Step 1: Run the Program**
```powershell
python C:\Users\AVoelser\pdf_cleaner.py
```

### **Step 2: Select Your PDFs**
- Click **"📁 Select PDF Files"** to choose individual PDFs, or
- Click **"📂 Select Folder"** to process all PDFs in a folder

### **Step 3: Done!**
Cleaned files automatically appear in the same directory with `_cleaned.docx` naming:
- Input: `research_article.pdf`
- Output: `research_article_cleaned.docx` (in the **same folder**)

---

## 📱 User Interface

When you run the program without arguments, you'll see a clean window with:

```
┌─────────────────────────────────────────────┐
│  PDF Research Article Cleaner              │
│                                              │
│  Select PDF files to clean for Sketch Engine│
│  Cleaned files will be saved in the same    │
│  directory.                                  │
│                                              │
│  [📁 Select PDF Files]                     │
│  [📂 Select Folder]                        │
│                                              │
│  Selected Files:                            │
│  ┌──────────────────────────────────────┐  │
│  │ • paper1.pdf                        │  │
│  │ • paper2.pdf                        │  │
│  │ ✓ paper1_cleaned.docx               │  │
│  │ Processing: 2/2                     │  │
│  └──────────────────────────────────────┘  │
│                                              │
│  Cleaned files: [filename]_cleaned.docx    │
└─────────────────────────────────────────────┘
```

---

## 🎯 Two Ways to Use

### **Option 1: GUI Mode (Default - Easy!)**

Just run the script with no arguments:
```powershell
python C:\Users\AVoelser\pdf_cleaner.py
```

Then use the buttons to select files or folders.

### **Option 2: Command Line Mode (Advanced)**

Process a folder (all PDFs saved there):
```powershell
python C:\Users\AVoelser\pdf_cleaner.py --folder "D:\My Papers"
```

Process specific files:
```powershell
python C:\Users\AVoelser\pdf_cleaner.py "D:\My Papers\study1.pdf" "D:\My Papers\study2.pdf"
```

Get help:
```powershell
python C:\Users\AVoelser\pdf_cleaner.py --help
```

---

## 📂 How Output Works

### **Example 1: Select Individual Files**

```
Before:
D:\Research\
├── paper1.pdf
├── paper2.pdf
└── paper3.pdf

After running tool and selecting files:
D:\Research\
├── paper1.pdf
├── paper1_cleaned.docx    ← OUTPUT (ready for Sketch Engine)
├── paper2.pdf
├── paper2_cleaned.docx    ← OUTPUT
├── paper3.pdf
└── paper3_cleaned.docx    ← OUTPUT
```

### **Example 2: Select Entire Folder**

```
Before:
C:\Users\MyName\Documents\Articles\
├── study_2024.pdf
├── research_2023.pdf
└── review_2022.pdf

After running tool and selecting folder:
C:\Users\MyName\Documents\Articles\
├── study_2024.pdf
├── study_2024_cleaned.docx        ← OUTPUT
├── research_2023.pdf
├── research_2023_cleaned.docx      ← OUTPUT
├── review_2022.pdf
└── review_2022_cleaned.docx        ← OUTPUT
```

---

## 🔧 What Gets Cleaned

### ✅ Kept:
- Introduction
- Methods
- Results
- Discussion
- Conclusion
- Main body text

### ❌ Removed:
- Title pages
- Abstracts
- Keywords
- References
- Acknowledgments
- Author information
- Headers and footers
- Page numbers
- Copyright info

---

## 📊 Using with Sketch Engine

### **Step 1: Clean Your PDFs**
```powershell
python C:\Users\AVoelser\pdf_cleaner.py
```
Select your PDF files or folder → Files are cleaned

### **Step 2: Open File Explorer**
Navigate to the folder containing your cleaned `.docx` files

### **Step 3: Upload to Sketch Engine**
- Go to your Sketch Engine project
- Select **"Add corpus"** or **"Import"**
- Upload the `_cleaned.docx` files

---

## ⚙️ Settings (Advanced)

To customize what gets removed, edit the file:

`C:\Users\AVoelser\pdf_cleaner.py`

Find this section (around line 12):

```python
SECTION_KEYWORDS = {
    'abstract': ['abstract', 'summary'],
    'keywords': ['keywords', 'key words'],
    'acknowledgments': ['acknowledgments', 'funding'],
    'references': ['references', 'bibliography'],
    'conflict': ['conflict of interest'],
    'author_info': ['author information'],
}
```

Add your custom keywords:
```python
SECTION_KEYWORDS = {
    # ... existing entries ...
    'methods': ['methods', 'methodology'],  # Add to remove methods sections
    'custom': ['your_keyword'],
}
```

---

## ❓ Troubleshooting

### **GUI doesn't appear**
Make sure you're in the right directory:
```powershell
cd C:\Users\AVoelser
python pdf_cleaner.py
```

### **"No PDF files found"**
- Check the folder contains `.pdf` files
- Try selecting files individually instead of a folder

### **Output files are empty**
- The PDF might be image-based (scanned) - requires OCR
- Try opening the PDF with another app to verify it has text

### **File didn't process**
- Check the Windows notification area for error messages
- The PDF might be corrupted
- Try the file separately to see the error

### **Want to process files from different folders**
- Use "Select PDF Files" button and multi-select files from different folders
- Files will be cleaned and saved in their **original directories**

---

## 🎯 Common Tasks

### **Batch clean 50 research papers**
1. Put all PDFs in one folder: `C:\Research\Articles\`
2. Run: `python C:\Users\AVoelser\pdf_cleaner.py`
3. Click: **"📂 Select Folder"**
4. Choose: `C:\Research\Articles\`
5. Wait for completion → All `_cleaned.docx` files appear in the same folder

### **Clean just one paper**
1. Run: `python C:\Users\AVoelser\pdf_cleaner.py`
2. Click: **"📁 Select PDF Files"**
3. Choose: `myresearch.pdf`
4. Wait → `myresearch_cleaned.docx` appears in the same folder

### **Use command line**
```powershell
# Process folder
python C:\Users\AVoelser\pdf_cleaner.py --folder "C:\Research\Articles"

# Process files
python C:\Users\AVoelser\pdf_cleaner.py "C:\paper1.pdf" "C:\paper2.pdf"
```

---

## 📝 Output Quality Tips

1. **PDF must have extractable text**
   - Most PDFs are fine
   - Scanned/image-based PDFs won't work
   - Check: Open PDF in Adobe Reader → Can you select text?

2. **Academic papers work best**
   - Tool is designed for research articles
   - Works with most journal formats
   - May need tweaking for unusual layouts

3. **Processing speed**
   - Single paper: 1-3 seconds
   - Batch (10 papers): 15-30 seconds
   - Depends on paper length and your computer

---

## 🎓 For Sketch Engine Users

After cleaning your PDFs:

1. ✅ Converted to `.docx` (Word format)
2. ✅ All non-academic content removed
3. ✅ Ready for corpus analysis
4. ✅ Compatible with Sketch Engine import

Upload to Sketch Engine and enjoy cleaner, more focused text analysis!

---

## 💡 Tips & Tricks

- **Multi-select in file dialog**: Hold `Ctrl` while clicking to select multiple files
- **Different folders**: Select files from different folders at once - each saves to its own folder
- **Reprocess**: Safe to reprocess files - creates new `_cleaned.docx` files
- **Keep originals**: Original PDFs are never modified, only cleaned versions are created

---

## 📞 Need Help?

Check these files for more info:
- `PDF_CLEANER_README.md` - Detailed technical documentation
- `SETUP_COMPLETE.md` - Setup information
- `verify_setup.py` - Run to check if everything is installed

---

**Version:** 2.0 (GUI-Enhanced)  
**Last Updated:** December 2025  
**Status:** Ready to Use ✅
