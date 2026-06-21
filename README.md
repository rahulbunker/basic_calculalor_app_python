# 🧮 Calculator App — Python

Ek modern dark-theme calculator jo Python aur Tkinter se bani hai.

---

## 📁 Files

| File | Kaam |
|---|---|
| `calculator_final.py` | Main Python source code |
| `calculator.ico` | App icon (Windows .exe ke liye) |
| `calculator_icon.png` | App icon (PNG format) |
| `WINDOWS_BUILD.bat` | Windows pe .exe banane ka script |
| `README.md` | Yeh file |

---

## ⚙️ Requirements

- Python 3.8 ya usse naya
- pip (Python package manager)

---

## 🚀 Installation & Setup

### Step 1 — Python Install Karo
[python.org/downloads](https://www.python.org/downloads/) se download karo.
> ⚠️ Install karte waqt **"Add Python to PATH"** zaroor tick karo!

### Step 2 — Dependencies Install Karo
Terminal (CMD ya VS Code terminal) mein:
```
pip install pyinstaller pillow
```

### Step 3 — Direct Chalao (bina build ke)
```
python calculator_final.py
```

---

## 🏗️ .EXE App Banao (Windows)

### Method 1 — BAT File se (Aasaan)
`WINDOWS_BUILD.bat` pe **double-click** karo — automatically build ho jayega.

### Method 2 — Terminal se (VS Code)
```
pyinstaller --onefile --windowed --icon=calculator.ico --name="Calculator" calculator_final.py
```

Build hone ke baad:
```
dist\Calculator.exe
```
Yahan milegi aapki app! ✅

---

## 🖥️ Desktop Shortcut Kaise Lagayen

1. `dist\Calculator.exe` pe **Right Click** karo
2. **"Send to" → "Desktop (create shortcut)"** select karo
3. Ab desktop pe directly open ho sakti hai app!

---

## ✨ Features

| Feature | Detail |
|---|---|
| Basic Operations | Jodna (+), Ghatana (−), Guna (×), Bhag (÷) |
| AC Button | Sab kuch clear karo |
| ⌫ Button | Last digit delete karo |
| % Button | Percentage nikalo |
| ± Button | Positive/Negative toggle karo |
| Decimal | Dashamlav (.) support |
| Dark Theme | Modern purple/green UI |
| Error Handling | Zero se bhag karne pe error message |

---

## 🐛 Common Errors aur Fix

### ❌ `pip` not found
```
python -m pip install pyinstaller pillow
```

### ❌ `pyinstaller` not found
```
python -m PyInstaller --onefile --windowed --icon=calculator.ico --name="Calculator" calculator_final.py
```

### ❌ ICO file error
ICO aur Python file **same folder** mein honi chahiye. Agar phir bhi error aaye toh:
```
pyinstaller --onefile --windowed --name="Calculator" calculator_final.py
```
(icon ke bina build karo)

### ❌ `dist` folder nahi mila
Matlab build abhi hua nahi. Pehle upar wali build command chalao.

---

## 📱 Mobile App Banana Chahte Ho?

Yeh app sirf **Windows/Mac/Linux** pe chalti hai (Desktop only).

Mobile ke liye options:
- **Android APK** → Kivy (Python) use karo
- **Android + iOS** → Flutter use karo
- **Browser mein** → HTML/JavaScript use karo

---

## 👨‍💻 Developer Notes

- Language: Python 3
- GUI Library: Tkinter (built-in)
- Packaging: PyInstaller
- Icon: Pillow se banaya gaya

---

*Calculator App — Python + Tkinter*