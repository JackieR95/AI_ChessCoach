# Python Easy Chess GUI - Setup Instructions

## Quick Start Guide for Other Users

This is a Chess GUI application built with Python that allows you to play against chess engines.

### System Requirements
- **Windows 10 or later** (or macOS/Linux)
- **Python 3.12 or later** (Python 3.14 is NOT compatible due to PySimpleGUI issues)
- **At least 500MB free disk space**

### Installation Steps

**If you want AI Coach explanations (Gemini):**
- Get an API key from https://aistudio.google.com/app/apikey
- Put it in `Python-Easy-Chess-GUI-master/.env` as `GOOGLE_GEMINI_API_KEY=your_key`
- Without this, the GUI still works; the AI Coach box will just show Stockfish evaluation only.

#### Step 1: Install Python 3.12
1. Download Python 3.12 from https://www.python.org/downloads/
2. During installation, **CHECK** the box "Add Python to PATH"
3. Verify installation by opening Command Prompt or PowerShell and running:
   ```
   python --version
   ```
   You should see: `Python 3.12.x`

#### Step 2: Download/Extract the Project
1. Extract the AI_ChessCoach folder to your desired location
2. Open Command Prompt or PowerShell
3. Navigate to the AI_ChessCoach folder:
   ```
   cd path\to\AI_ChessCoach
   ```

#### Step 3: Create Virtual Environment
```
python -m venv venv
```

#### Step 4: Activate Virtual Environment
**Windows (PowerShell):**
```
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```
venv\Scripts\activate.bat
```

**macOS/Linux:**
```
source venv/bin/activate
```

#### Step 5: Install Dependencies
```
pip install --upgrade pip
pip install -r SETUP_REQUIREMENTS.txt
```

#### Step 6: Run the Chess GUI
```
cd Python-Easy-Chess-GUI-master
python python_easy_chess_gui.py
```

If you want AI Coach explanations, ensure `.env` exists in this folder with `GOOGLE_GEMINI_API_KEY` set.

### First Time Setup in the GUI

When you run the program for the first time:

1. **Install a Chess Engine:**
   - Go to: **Engine → Manage → Install**
   - Click **Add** and browse to select a chess engine (e.g., Stockfish)
   - If you don't have an engine, download Stockfish from: https://stockfishchess.org/download/
   - Place it in the `Engines` folder

2. **Start Playing:**
   - Go to: **Mode → Play**
   - The engine will be your opponent
   - Make your moves on the board

### Common Issues & Solutions

**Issue: "No module named 'PySimpleGUI'"**
- **Solution:** Make sure you activated the virtual environment and ran `pip install -r SETUP_REQUIREMENTS.txt`

**Issue: "Python 3.14 or later detected"**
- **Solution:** Use Python 3.12 instead. Download from https://www.python.org/downloads/
- To check: `python --version`

**Issue: Engine not found**
- **Solution:** 
  1. Download Stockfish: https://stockfishchess.org/download/
  2. Place the executable in the `Engines` folder
  3. In GUI: Engine → Manage → Install → Add → select the engine file

**Issue: AI Coach text says analysis error or is empty**
- **Solution:**
   1. Make sure `.env` in `Python-Easy-Chess-GUI-master` has `GOOGLE_GEMINI_API_KEY=your_key`
   2. Verify internet access
   3. If still failing, AI Coach will fall back to Stockfish-only output

**Issue: Cannot activate virtual environment**
- **For PowerShell:** If you get an error, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Then try activating again

### Project Structure
```
AI_ChessCoach/
├── venv/                              # Virtual environment (created by you)
├── SETUP_REQUIREMENTS.txt             # Dependencies file
├── SETUP_INSTRUCTIONS.md              # This file
└── Python-Easy-Chess-GUI-master/      # Main application
    ├── python_easy_chess_gui.py       # Main program
    ├── Engines/                       # Place chess engines here
    ├── Book/                          # Opening book files
    ├── Images/                        # Chess piece images
    └── Icon/                          # Application icons
```

### Features

- ✅ Play chess against UCI engines (Stockfish, etc.)
- ✅ Save and load games in PGN format
- ✅ Get engine analysis and advice
- ✅ Customize board colors and themes
- ✅ Multiple time control options
- ✅ Opening book support

### Troubleshooting: Deactivate Virtual Environment

When done, deactivate the virtual environment:
```
deactivate
```

### Additional Resources

- **Python Chess Library:** https://github.com/niklasf/python-chess
- **PySimpleGUI Documentation:** https://github.com/PySimpleGUI/PySimpleGUI
- **Stockfish Chess Engine:** https://stockfishchess.org/

### Support

If you encounter any issues:
1. Check that Python 3.12 is installed (NOT 3.14)
2. Verify virtual environment is activated
3. Ensure all dependencies are installed: `pip list`
4. Delete `pecg_engines.json` and restart to reset engine configuration

---

**Enjoy playing chess!** ♟️
