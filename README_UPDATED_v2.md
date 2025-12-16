# PDF CLEANER v2.0 - NOW EVEN MORE USER-FRIENDLY! ✨

## 🎉 What You Got

A **super easy, user-friendly PDF cleaner** with:
- ✅ **GUI Interface** (no command line needed!)
- ✅ **Smart Output Location** (files save in same folder as PDFs)
- ✅ **Batch Processing** (clean one or 100 PDFs)
- ✅ **Visual File Selection** (nice dialog, not typing paths)
- ✅ **Perfect for Sketch Engine** (.docx format)

---

## 🚀 HOW TO USE (Super Simple!)

### **Method 1: Double-Click (EASIEST)**
```
C:\Users\AVoelser\run_pdf_cleaner.bat
```
Double-click this file → A window opens → Select files → Done!

### **Method 2: Command Line (Still Works)**
```powershell
python C:\Users\AVoelser\pdf_cleaner.py
```

---

## 📂 WHERE YOUR CLEANED FILES GO

**Simple: SAME FOLDER AS YOUR PDFs!**

```
Your Folder:
  paper1.pdf                 (original - unchanged)
  paper1_cleaned.docx        (cleaned - ready to use!)
  paper2.pdf                 (original - unchanged)
  paper2_cleaned.docx        (cleaned - ready to use!)
```

No confusing subfolders. No hunting for files. **Everything stays organized!**

---

## 📋 ALL YOUR FILES

Located in: `C:\Users\AVoelser\`

| File | What It Does |
|------|-------------|
| `run_pdf_cleaner.bat` | **👈 Click this to start!** |
| `pdf_cleaner.py` | The actual cleaning tool |
| `START_HERE.md` | Quick start guide |
| `QUICK_REFERENCE.md` | Fast reference card |
| `PDF_CLEANER_USER_GUIDE.md` | Detailed user guide |
| `WHATS_NEW_v2.0.md` | What changed from v1 |
| `PDF_CLEANER_README.md` | Technical documentation |

---

## ✨ KEY IMPROVEMENTS FROM v1.0

| What | v1.0 | v2.0 |
|-----|------|------|
| **How to launch** | Command line only | GUI + Command line |
| **Select files** | Type file paths | Visual dialog |
| **Output location** | `folder/cleaned_articles/` | **Same folder as PDF** |
| **Friendly for beginners** | ❌ Not really | ✅ Very friendly! |
| **Organization** | Scattered | **Clean & organized** |

---

## 🎯 3-STEP QUICK START

### Step 1: Run
```
Double-click: C:\Users\AVoelser\run_pdf_cleaner.bat
```

### Step 2: Select
Click "📁 Select PDF Files" or "📂 Select Folder"

### Step 3: Done
Find `_cleaned.docx` files in the same folder as your PDFs!

---

## 💡 USE CASES

### "Clean 1 Research Paper"
1. Open GUI
2. Click: 📁 Select PDF Files
3. Pick: myresearch.pdf
4. ✓ Find: myresearch_cleaned.docx in same folder

### "Batch Clean 50 Papers"
1. Open GUI
2. Click: 📂 Select Folder
3. Pick: C:\Users\MyName\AllPapers\
4. ✓ Find: All 50 papers cleaned, in same folder

### "Clean Papers from Multiple Places"
1. Open GUI
2. Click: 📁 Select PDF Files
3. Hold Ctrl, click papers from different folders
4. ✓ Each paper's cleaned version appears in its original folder

---

## 🎓 FOR SKETCH ENGINE USERS

Perfect workflow now:

1. **Clean PDFs:**
   - Open GUI
   - Select PDFs
   - Done!

2. **Upload to Sketch Engine:**
   - Find `_cleaned.docx` files in same folders
   - Upload to Sketch Engine
   - No subfolder hunting!

---

## 🔧 STILL CUSTOMIZABLE

Want to change what gets removed?

Edit `pdf_cleaner.py` and customize:

```python
SECTION_KEYWORDS = {
    'abstract': ['abstract', 'summary'],
    'references': ['references', 'bibliography'],
    # Add your custom keywords
}
```

Then use the GUI or command line as usual!

---

## ⚡ FEATURES

✅ **GUI Interface** - No command line!  
✅ **Smart Output** - Same folder as input  
✅ **Batch Processing** - One or many PDFs  
✅ **Multi-select** - Hold Ctrl for multiple files  
✅ **Error Handling** - Skips bad PDFs, continues  
✅ **Logging** - See what's happening  
✅ **Fast** - 1-3 seconds per paper  
✅ **Safe** - Never changes original PDFs  
✅ **Organized** - No confusing subfolders  
✅ **Customizable** - Adjust keywords  

---

## 📊 WHAT GETS CLEANED

### Removed:
- ❌ Abstracts
- ❌ Keywords
- ❌ References/Bibliography
- ❌ Acknowledgments
- ❌ Author info
- ❌ Conflicts of interest
- ❌ Headers/Footers
- ❌ Page numbers
- ❌ Copyright info

### Kept:
- ✅ Introduction
- ✅ Methods
- ✅ Results
- ✅ Discussion
- ✅ Conclusion
- ✅ Main body text

---

## 🆘 QUICK HELP

| Issue | Solution |
|-------|----------|
| "GUI won't open" | Make sure you're in `C:\Users\AVoelser\` |
| "No PDFs found" | Check folder actually has `.pdf` files |
| "Output is empty" | PDF might be scanned (image-based) |
| "Processing is slow" | Large PDFs take longer - be patient |
| "Want command line?" | Run: `python pdf_cleaner.py --help` |

---

## 📖 DOCUMENTATION

**Just starting?** → Read `START_HERE.md`

**Quick reference?** → Read `QUICK_REFERENCE.md`

**Detailed guide?** → Read `PDF_CLEANER_USER_GUIDE.md`

**Want technical info?** → Read `PDF_CLEANER_README.md`

**Curious about changes?** → Read `WHATS_NEW_v2.0.md`

---

## 🎉 YOU'RE ALL SET!

Everything is ready to use. No more setup needed.

### **Just:**
```
1. Open: C:\Users\AVoelser\run_pdf_cleaner.bat
2. Click: Select your PDFs
3. Wait: Processing happens
4. Find: Cleaned files in same folder
5. Upload: To Sketch Engine (or wherever)
```

**That's it! Enjoy your cleaned PDFs!** 🚀

---

**Version:** 2.0 - User-Friendly Edition  
**Status:** ✅ Ready to Use  
**Last Updated:** December 2025

---

### Need help? 
Start with: `C:\Users\AVoelser\START_HERE.md`
