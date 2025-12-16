@echo off
REM PDF Research Article Cleaner - Windows Launcher
REM Just double-click this file to open the cleaner!

cd /d "%~dp0"
python pdf_cleaner.py %*
pause
