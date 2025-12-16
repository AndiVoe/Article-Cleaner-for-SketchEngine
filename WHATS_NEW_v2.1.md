# PDF CLEANER v2.1 - IMPROVED OUTPUT ORGANIZATION ✨

## 🎉 What's New

The tool now **automatically creates a separate `cleaned_articles` folder** to keep your PDFs and cleaned Word files organized!

---

## 📂 New Output Structure

### Before (v2.0):
```
D:\Research\
├── paper1.pdf
├── paper1_cleaned.docx         (mixed with PDF)
├── paper2.pdf
└── paper2_cleaned.docx         (mixed with PDF)
```

### After (v2.1):
```
D:\Research\
├── paper1.pdf
├── paper2.pdf
└── cleaned_articles\           ← NEW FOLDER!
    ├── paper1_cleaned.docx     (organized!)
    └── paper2_cleaned.docx     (organized!)
```

---

## ✨ Benefits

✅ **Organized** - PDFs and cleaned files separated  
✅ **Clean** - Original files stay pure  
✅ **Easy to find** - All cleaned files in one place  
✅ **Easy to upload** - Open `cleaned_articles/` → Select all → Upload to Sketch Engine  

---

## 🚀 How to Use (Same as Before!)

### Method 1: GUI (Easiest)
```
Double-click: run_pdf_cleaner.bat
```
1. Click "📁 Select PDF Files" or "📂 Select Folder"
2. Choose your PDFs
3. Done! ✨

Cleaned files automatically go to `cleaned_articles/` subfolder

### Method 2: Command Line
```powershell
python pdf_cleaner.py --folder "D:\My Papers"
```

Cleaned files automatically go to `D:\My Papers\cleaned_articles\`

---

## 📊 Real-World Example

### Scenario: Clean 3 Papers

**Before:**
```
C:\Users\MyName\Research\
├── study_2024.pdf
├── paper_2023.pdf
└── review_2022.pdf
```

**After running tool:**
```
C:\Users\MyName\Research\
├── study_2024.pdf
├── paper_2023.pdf
├── review_2022.pdf
└── cleaned_articles\              ← Created automatically!
    ├── study_2024_cleaned.docx
    ├── paper_2023_cleaned.docx
    └── review_2022_cleaned.docx
```

All cleaned files are in one convenient folder!

---

## 🎯 For Sketch Engine Users

Perfect workflow:

1. **Clean your PDFs:**
   ```
   Double-click: run_pdf_cleaner.bat
   Select PDFs → Done!
   ```

2. **Open cleaned_articles folder:**
   ```
   D:\Research\cleaned_articles\
   ```

3. **Select all cleaned files:**
   ```
   Ctrl+A → All .docx files selected
   ```

4. **Upload to Sketch Engine:**
   ```
   Sketch Engine Upload → Select folder → Upload all
   ```

Much cleaner than before! 📦✨

---

## 🔍 What Happens

### When you select a PDF from:
```
D:\Research\paper.pdf
```

### The tool creates:
```
D:\Research\cleaned_articles\
```

### And saves there:
```
D:\Research\cleaned_articles\paper_cleaned.docx
```

**Automatic!** No extra steps needed.

---

## ✅ Features Unchanged

Everything else works exactly the same:

✅ GUI interface  
✅ Batch processing  
✅ Error handling  
✅ Command line support  
✅ Customizable keywords  
✅ All documentation  

---

## 📋 File Organization Tips

### Tip 1: Research Folder Structure
```
MyResearch\
├── Literature\
│   ├── papers_collected\      (your PDFs)
│   │   ├── paper1.pdf
│   │   ├── paper2.pdf
│   │   └── cleaned_articles\  (cleaned versions)
│   │       ├── paper1_cleaned.docx
│   │       └── paper2_cleaned.docx
│   │
│   └── corpus\                (for Sketch Engine)
│       ├── paper1_cleaned.docx
│       └── paper2_cleaned.docx
```

### Tip 2: Quick Upload to Sketch Engine
1. Open: `cleaned_articles/` folder
2. Select all `.docx` files
3. Right-click → Copy
4. Paste to Sketch Engine upload area

---

## 🎯 Common Scenarios

### Scenario 1: Single Paper
```
1. Run tool
2. Select: myresearch.pdf
3. Result: myresearch_cleaned.docx in cleaned_articles/
```

### Scenario 2: Whole Folder
```
1. Run tool
2. Select: C:\Papers\ (10 PDFs)
3. Result: All 10 cleaned files in C:\Papers\cleaned_articles\
```

### Scenario 3: Multiple Folders
```
1. Run tool
2. Select: paper1.pdf (from C:\Papers1\)
3. Select: paper2.pdf (from C:\Papers2\)
4. Result: 
   - C:\Papers1\cleaned_articles\paper1_cleaned.docx
   - C:\Papers2\cleaned_articles\paper2_cleaned.docx
```

Each folder gets its own `cleaned_articles/` subfolder!

---

## 🔧 Command Line Examples

### Process folder
```powershell
python pdf_cleaner.py --folder "D:\My Papers"
# Creates: D:\My Papers\cleaned_articles\
```

### Process files
```powershell
python pdf_cleaner.py "D:\file1.pdf" "D:\file2.pdf"
# Creates: D:\cleaned_articles\
```

---

## ❓ FAQ

**Q: Where do cleaned files go?**
A: In a `cleaned_articles/` folder in the same directory as your PDFs!

**Q: Is this automatic?**
A: Yes! The folder is created automatically.

**Q: Can I change the folder name?**
A: You can edit `pdf_cleaner.py` and change `"cleaned_articles"` to whatever you want!

**Q: What about PDFs with special characters?**
A: Works fine! The cleaned file name matches the original PDF name.

**Q: Can I delete the cleaned_articles folder?**
A: Yes, but then run the tool again to recreate cleaned files.

**Q: Does this work with command line?**
A: Yes! Both GUI and command line create `cleaned_articles/` folder.

---

## 🚀 You're Ready!

Everything is updated and tested.

**Just use it as before:**
```
Double-click: run_pdf_cleaner.bat
```

And enjoy the organized output! 🎉

---

## 📞 Need Help?

Check these files:
- `START_HERE.md` - Quick start
- `QUICK_REFERENCE.md` - Quick lookup
- `PDF_CLEANER_USER_GUIDE.md` - Detailed guide

---

**PDF Cleaner v2.1**  
**With Better Organization!** ✨  
**December 2025**
