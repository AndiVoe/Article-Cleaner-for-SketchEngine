# PDF CLEANER v2.0 - VISUAL QUICK START GUIDE

## 🎯 The Absolute Easiest Way

### Step 1: Open File Explorer
Press `Windows Key + E` or click the folder icon

### Step 2: Navigate Here
```
C:\Users\AVoelser\
```

### Step 3: Find This File
```
run_pdf_cleaner.bat
```

### Step 4: Double-Click It
```
[run_pdf_cleaner.bat] 👈 DOUBLE-CLICK
```

### Step 5: A Window Opens!
```
┌─────────────────────────────────────────┐
│ PDF Research Article Cleaner            │
│                                          │
│ Select PDF files to clean...            │
│                                          │
│ [📁 Select PDF Files]                  │
│ [📂 Select Folder]                     │
│                                          │
└─────────────────────────────────────────┘
```

### Step 6: Pick Your PDFs
**Option A:** Click `📁 Select PDF Files`
- Choose individual PDF files
- Can hold Ctrl to select multiple

**Option B:** Click `📂 Select Folder`
- Choose a folder with PDFs
- All PDFs in that folder are processed

### Step 7: Wait
Files are being cleaned...
```
[1/5] Processing: paper1...
[2/5] Processing: paper2...
...
```

### Step 8: Done!
Check your folder for new `_cleaned.docx` files!

```
Before:
  research.pdf

After:
  research.pdf                    (original - unchanged)
  research_cleaned.docx           (cleaned - ready!)
```

---

## 📊 Visual File Structure

### Your PDFs Before:
```
C:\Users\MyName\Articles\
├── study_2024.pdf
├── research_2023.pdf
└── review_2022.pdf
```

### Your PDFs After:
```
C:\Users\MyName\Articles\
├── study_2024.pdf              ← original (unchanged)
├── study_2024_cleaned.docx     ← cleaned (NEW!)
├── research_2023.pdf           ← original (unchanged)
├── research_2023_cleaned.docx  ← cleaned (NEW!)
├── review_2022.pdf             ← original (unchanged)
└── review_2022_cleaned.docx    ← cleaned (NEW!)
```

---

## 🎨 What The GUI Looks Like

```
╔════════════════════════════════════════════╗
║                                             ║
║   PDF Research Article Cleaner             ║
║                                             ║
║   Select PDF files to clean for Sketch Engine
║   Cleaned files will be saved in the same  ║
║   directory.                                ║
║                                             ║
║   ┌──────────────────────────────────────┐ ║
║   │ 📁 Select PDF Files                 │ ║
║   │                                       │ ║
║   │ 📂 Select Folder                    │ ║
║   └──────────────────────────────────────┘ ║
║                                             ║
║   Selected Files:                           ║
║   ┌──────────────────────────────────────┐ ║
║   │ • paper1.pdf                        │ ║
║   │ • paper2.pdf                        │ ║
║   │ • paper3.pdf                        │ ║
║   │ ✓ paper1_cleaned.docx (DONE)       │ ║
║   │ ✓ paper2_cleaned.docx (DONE)       │ ║
║   │ Processing: 3/3                     │ ║
║   └──────────────────────────────────────┘ ║
║                                             ║
║   Cleaned files: [filename]_cleaned.docx  ║
║                                             ║
╚════════════════════════════════════════════╝
```

---

## ⚡ Three Quick Commands

### Command 1: GUI (Easiest)
```powershell
cd C:\Users\AVoelser
python pdf_cleaner.py
```

### Command 2: Process Folder
```powershell
python C:\Users\AVoelser\pdf_cleaner.py --folder "D:\My Papers"
```

### Command 3: Process Files
```powershell
python C:\Users\AVoelser\pdf_cleaner.py paper1.pdf paper2.pdf
```

---

## 🎯 Two Quick Paths

### Path A: Never Used Before
```
1. Double-click: C:\Users\AVoelser\run_pdf_cleaner.bat
2. Click: 📁 or 📂 button
3. Select files
4. Done!
```

### Path B: Command Line User
```
1. Open PowerShell/CMD
2. Type: python C:\Users\AVoelser\pdf_cleaner.py --folder "C:\path"
3. Done!
```

---

## 📱 GUI Buttons Explained

### 📁 Select PDF Files
- Click to choose individual PDF files
- Can select from any folders
- Hold Ctrl to pick multiple files from different places
- Each file's cleaned version goes in its own folder

### 📂 Select Folder  
- Click to choose a whole folder
- Finds all PDFs in that folder
- Cleans all at once
- All cleaned versions stay in same folder

---

## 🔄 The Process

```
Select PDFs
    ↓
[Processing...]
    ↓
PDF Text Extracted
    ↓
Text Cleaned (abstracts, references removed)
    ↓
Word Document (.docx) Created
    ↓
Saved in Same Folder
    ↓
✓ Done! Ready for Sketch Engine
```

---

## ✨ What Gets Cleaned

```
BEFORE (Original PDF):
┌─────────────────────┐
│ Title Page          │ ❌ REMOVED
├─────────────────────┤
│ Abstract            │ ❌ REMOVED
├─────────────────────┤
│ Introduction        │ ✅ KEPT
│ Methods             │ ✅ KEPT
│ Results             │ ✅ KEPT
│ Discussion          │ ✅ KEPT
│ Conclusion          │ ✅ KEPT
├─────────────────────┤
│ References          │ ❌ REMOVED
│ Acknowledgments     │ ❌ REMOVED
│ Author Info         │ ❌ REMOVED
└─────────────────────┘

AFTER (Cleaned .docx):
┌─────────────────────┐
│ Introduction        │
│ Methods             │
│ Results             │
│ Discussion          │
│ Conclusion          │
│                     │
│ (Clean body text)   │
└─────────────────────┘
```

---

## 📍 File Locations

### Everything is here:
```
C:\Users\AVoelser\
```

### Most important file:
```
C:\Users\AVoelser\run_pdf_cleaner.bat  ← DOUBLE-CLICK THIS!
```

### Other helpful files:
```
C:\Users\AVoelser\START_HERE.md        ← Quick guide
C:\Users\AVoelser\QUICK_REFERENCE.md   ← Reference
C:\Users\AVoelser\PDF_CLEANER_USER_GUIDE.md ← Detailed
```

---

## 🎓 For Sketch Engine

### Workflow:
```
1. Clean your PDFs
   └─ Double-click: run_pdf_cleaner.bat
   └─ Select PDFs
   └─ Wait for completion

2. Find cleaned files
   └─ They're in same folder as PDFs
   └─ Names: [original]_cleaned.docx

3. Upload to Sketch Engine
   └─ Use Sketch Engine's upload feature
   └─ Select all _cleaned.docx files
   └─ Upload!

4. Analyze in Sketch Engine
   └─ Corpus is ready!
```

---

## 🆘 If Something Goes Wrong

### "Window won't open"
- Make sure you're double-clicking: `run_pdf_cleaner.bat`
- Check it's in: `C:\Users\AVoelser\`

### "No PDFs found"
- Make sure folder has `.pdf` files
- Try selecting individual files instead

### "Processing is slow"
- Large PDFs take longer
- Wait for it to finish
- Usually 1-3 seconds per PDF

### "Files are empty"
- PDF might be scanned (image-based)
- Try opening PDF in another app to test

### "Want to see full guide?"
- Read: `PDF_CLEANER_USER_GUIDE.md`
- Run: `verify_setup.py`

---

## ✅ Checklist Before You Start

```
☑ PDF Cleaner installed?              YES ✓
☑ All files in C:\Users\AVoelser\?    YES ✓
☑ Python installed?                    YES ✓
☑ run_pdf_cleaner.bat exists?         YES ✓
☑ Ready to go?                         YES ✓
```

---

## 🚀 You're Ready!

### Next Step:
```
1. Open File Explorer
2. Go to: C:\Users\AVoelser\
3. Double-click: run_pdf_cleaner.bat
4. Click: 📁 or 📂
5. Select: Your PDFs
6. Done! 🎉
```

---

## 📞 Quick Help

**Quick reference?**
→ See: `QUICK_REFERENCE.md`

**Detailed guide?**
→ See: `PDF_CLEANER_USER_GUIDE.md`

**File list?**
→ See: `FILE_INDEX.md`

**What's new in v2?**
→ See: `WHATS_NEW_v2.0.md`

---

**PDF Cleaner v2.0**  
**Ready to Use!** ✨  
**December 2025**
