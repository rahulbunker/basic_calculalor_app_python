@echo off
echo ========================================
echo    Calculator App - Windows Build
echo ========================================
echo.
echo Step 1: PyInstaller install ho raha hai...
pip install pyinstaller pillow

echo.
echo Step 2: App build ho raha hai (.exe)...
pyinstaller --onefile --windowed --icon=calculator.ico --name="Calculator" calculator_final.py

echo.
echo ========================================
echo Build Complete!
echo dist\Calculator.exe file ready hai!
echo ========================================
pause