# PDF CLEANER - QUICK REFERENCE

## 🚀 Launch Methods

### **Method 1: Double-Click (Easiest!)**
```
C:\Users\AVoelser\run_pdf_cleaner.bat
```
Double-click this file to open the GUI

### **Method 2: PowerShell**
```powershell
cd C:\Users\AVoelser
python pdf_cleaner.py
```

### **Method 3: Command Prompt**
```cmd
cd C:\Users\AVoelser
python pdf_cleaner.py
```

---

## 📂 File Locations

| What | Where |
|------|-------|
| **Main Tool** | `C:\Users\AVoelser\pdf_cleaner.py` |
| **Launcher** | `C:\Users\AVoelser\run_pdf_cleaner.bat` |
| **User Guide** | `C:\Users\AVoelser\PDF_CLEANER_USER_GUIDE.md` |
| **Full Docs** | `C:\Users\AVoelser\PDF_CLEANER_README.md` |

---

## 📋 GUI Usage

```
1. Click "📁 Select PDF Files"     → Pick PDFs
   OR
   Click "📂 Select Folder"         → Pick folder with PDFs

2. Review selected files

3. Click to process

4. Check folder for "_cleaned.docx" files
```

---

## 💻 Command Line Usage

**Process folder:**
```powershell
python C:\Users\AVoelser\pdf_cleaner.py --folder "D:\My Papers"
```

**Process individual files:**
```powershell
python C:\Users\AVoelser\pdf_cleaner.py "D:\file1.pdf" "D:\file2.pdf"
```

**Get help:**
```powershell
python C:\Users\AVoelser\pdf_cleaner.py --help
```

---

## ✨ Key Features

✅ GUI - No command line needed  
✅ Output in **same directory** as input  
✅ Batch processing  
✅ Removes abstracts, references, headers, footers  
✅ Generates `.docx` files for Sketch Engine  
✅ Error handling - skips bad PDFs  

---

## 📊 Output Naming

```
Input:  research_article.pdf
Output: research_article_cleaned.docx
```

Output appears in the **same folder** as the input PDF.

---

## 🎯 Quick Examples

### Clean 1 PDF
1. Run: `C:\Users\AVoelser\run_pdf_cleaner.bat`
2. Click: "📁 Select PDF Files"
3. Pick: `MyPaper.pdf`
4. Done! Check folder for `MyPaper_cleaned.docx`

### Clean Whole Folder
1. Run: `C:\Users\AVoelser\run_pdf_cleaner.bat`
2. Click: "📂 Select Folder"
3. Pick: `C:\Users\MyName\Articles`
4. Done! All PDFs cleaned in same folder

### Command Line
```powershell
python C:\Users\AVoelser\pdf_cleaner.py --folder "C:\Users\MyName\Articles"
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| GUI won't open | Make sure Python is installed |
| "No PDFs found" | Check folder contains `.pdf` files |
| Empty output | PDF might be scanned/image-based |
| Slow processing | Large PDFs take longer - be patient |

---

## 📱 Where Files End Up

```
Before:
C:\Research\
├── paper1.pdf
└── paper2.pdf

After:
C:\Research\
├── paper1.pdf
├── paper1_cleaned.docx      ← HERE
├── paper2.pdf
└── paper2_cleaned.docx      ← HERE
```

**No separate folder created!** Everything stays organized in your original directories.

---

**Version:** 2.0 (User-Friendly GUI)  
**Status:** Ready to Use ✅
