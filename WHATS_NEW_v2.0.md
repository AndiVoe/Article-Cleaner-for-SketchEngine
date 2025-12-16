# PDF CLEANER v2.0 - USER-FRIENDLY EDITION ✨

## What's New

### 🎯 **MAJOR IMPROVEMENT: Output Files Save in Same Directory as PDFs!**

No more confusing `cleaned_articles/` subfolders. Files save exactly where you want them.

**Before:**
```
C:\Research\
├── papers\
│   ├── paper1.pdf
│   ├── paper2.pdf
│   └── cleaned_articles\        ← Had to look here
│       ├── paper1_cleaned.docx
│       └── paper2_cleaned.docx
```

**After:**
```
C:\Research\
├── paper1.pdf
├── paper1_cleaned.docx         ← Right there!
├── paper2.pdf
└── paper2_cleaned.docx         ← Right there!
```

---

## 🎨 **NEW: Graphical User Interface (GUI)**

No more command line! Just:
1. **Run:** `C:\Users\AVoelser\run_pdf_cleaner.bat` (double-click!)
2. **Click:** "📁 Select PDF Files" or "📂 Select Folder"
3. **Done!** Files are cleaned and saved

### GUI Features:
- ✅ Visual file selection (no typing paths!)
- ✅ See selected files before processing
- ✅ Real-time progress indicator
- ✅ Clean, professional interface
- ✅ Success/error notifications
- ✅ Scrollable file list

---

## 📂 **How It Works Now**

### **Scenario 1: Single PDF**
```
1. Open GUI
2. Click "📁 Select PDF Files"
3. Choose: D:\Articles\myresearch.pdf
4. ✓ Done!
   → D:\Articles\myresearch_cleaned.docx appears
```

### **Scenario 2: Whole Folder**
```
1. Open GUI
2. Click "📂 Select Folder"
3. Choose: D:\Articles\
4. ✓ Done!
   → All PDFs cleaned and saved in D:\Articles\
   → All _cleaned.docx files appear there
```

### **Scenario 3: Multiple Files from Different Folders**
```
1. Open GUI
2. Click "📁 Select PDF Files"
3. Hold Ctrl and select:
   - D:\Research\paper1.pdf
   - D:\Articles\paper2.pdf
   - D:\Documents\paper3.pdf
4. ✓ Done!
   → paper1_cleaned.docx → D:\Research\
   → paper2_cleaned.docx → D:\Articles\
   → paper3_cleaned.docx → D:\Documents\
```

---

## 📋 **Files Included**

```
C:\Users\AVoelser\
├── pdf_cleaner.py                      ← Main tool (DO NOT MOVE)
├── run_pdf_cleaner.bat                 ← Launcher (double-click this!)
├── PDF_CLEANER_USER_GUIDE.md          ← Easy-to-read guide
├── QUICK_REFERENCE.md                  ← This file
├── PDF_CLEANER_README.md               ← Technical docs
├── SETUP_COMPLETE.md                   ← Setup info
└── verify_setup.py                     ← Verification script
```

---

## 🚀 **Quick Start**

### **Easiest Way: Double-Click**
```
C:\Users\AVoelser\run_pdf_cleaner.bat
```
A window opens → Select files → Done!

### **Alternative: PowerShell**
```powershell
cd C:\Users\AVoelser
python pdf_cleaner.py
```

### **Command Line (Advanced)**
```powershell
# Process folder
python C:\Users\AVoelser\pdf_cleaner.py --folder "D:\My Papers"

# Process files
python C:\Users\AVoelser\pdf_cleaner.py file1.pdf file2.pdf
```

---

## ✨ **Features Remain**

All original features still work:

✅ Removes abstracts  
✅ Removes references  
✅ Removes headers/footers  
✅ Removes author info  
✅ Removes acknowledgments  
✅ Batch processing  
✅ Error handling  
✅ Logging  
✅ Customizable keywords  

---

## 🎯 **The Best Part**

**No more confusion about where files go!**

When you select a PDF from:
- `D:\Research\Paper1.pdf`

The output goes to:
- `D:\Research\Paper1_cleaned.docx`

Same folder. Easy. Clean. Organized.

---

## 📊 **Workflow**

```
Traditional (Old):
Select PDFs → Process → Find output in subfolder

New & Easy:
Select PDFs → Process → Output in same folder ✓
```

---

## 🔧 **Settings**

Still customizable! Edit `pdf_cleaner.py`:

```python
SECTION_KEYWORDS = {
    'abstract': ['abstract', 'summary'],
    'keywords': ['keywords', 'key words'],
    # Add custom keywords as needed
}
```

---

## 💡 **Pro Tips**

1. **Multi-select files:**
   - Hold Ctrl while clicking to select multiple PDFs
   - All are processed in one go

2. **Different folders:**
   - Select files from multiple folders
   - Each saves to its own original folder

3. **Organize first:**
   - Put related PDFs in one folder
   - Run tool on that folder
   - Everything stays organized

4. **Safe to reprocess:**
   - Running tool again is safe
   - Creates fresh cleaned versions

---

## 🆚 **What Changed**

| Feature | Old | New |
|---------|-----|-----|
| **Output Location** | `folder/cleaned_articles/` | `same folder as PDF` |
| **How to Launch** | Command line only | GUI + CLI |
| **Select Files** | Type paths | Visual dialog |
| **User Experience** | Beginner-unfriendly | Beginner-friendly |
| **File Organization** | Scattered | Clean & organized |

---

## ✅ **Everything Still Works**

- Command line mode: `python pdf_cleaner.py --folder path`
- Single file processing: `python pdf_cleaner.py file.pdf`
- Help: `python pdf_cleaner.py --help`
- Custom keywords: Edit section_keywords
- Error handling: Same as before
- Logging: Same as before

---

## 🎓 **For Sketch Engine Users**

Workflow is now even simpler:

1. Clean your PDFs using the GUI
2. All `_cleaned.docx` files stay in their folders
3. Upload directly from those folders to Sketch Engine
4. No "cleaned_articles" subfolder to manage

---

## 📞 **Getting Help**

See these files:
- **Quick start?** → `QUICK_REFERENCE.md`
- **How to use?** → `PDF_CLEANER_USER_GUIDE.md`
- **Technical details?** → `PDF_CLEANER_README.md`
- **Issues?** → `verify_setup.py`

---

## 🎉 **Summary**

**Version 2.0 = Smarter + Simpler + Better Organized**

- GUI for easy file selection
- Output in same folder (no subfolder)
- Better user experience
- All old features work
- Ready to go!

---

**Status: Ready to Use** ✅  
**Last Updated: December 2025**  
**Version: 2.0 - User-Friendly Edition**
