# README - Python Easy Chess GUI

## Overview
A Chess GUI application built with Python, PySimpleGUI, and Python-Chess library. Play against UCI chess engines with a modern graphical interface.

## Quick Start

### Windows Users
1. Install Python 3.12 from https://www.python.org/downloads/
2. Double-click `setup.bat` to automatically set up everything
3. Navigate to `Python-Easy-Chess-GUI-master` and run `python python_easy_chess_gui.py`

### macOS/Linux Users
1. Install Python 3.12 from https://www.python.org/downloads/
2. Run: `bash setup.sh`
3. Navigate to `Python-Easy-Chess-GUI-master` and run `python python_easy_chess_gui.py`

### Manual Setup
See `SETUP_INSTRUCTIONS.md` for detailed step-by-step instructions.

## System Requirements
- Python 3.12 (NOT 3.14)
- 500MB free disk space
- Windows 10+, macOS 10.14+, or Linux

## Features
- Play against chess engines (UCI protocol)
- Save/load games in PGN format
- Opening book support
- Engine analysis and advice
- Customizable board appearance
- Multiple time controls
- Move history and annotations

## Getting an Engine
You need a UCI chess engine to play. Download Stockfish:
- https://stockfishchess.org/download/

Then place it in the `Engines` folder and install it via: Engine → Manage → Install

## Files Included
- `SETUP_REQUIREMENTS.txt` - Python package dependencies
- `SETUP_INSTRUCTIONS.md` - Detailed setup guide
- `setup.bat` - Automated setup for Windows
- `setup.sh` - Automated setup for macOS/Linux
- `Python-Easy-Chess-GUI-master/` - Main application code

## Troubleshooting

**Q: "No module named PySimpleGUI"**
A: Run the setup script again or ensure virtual environment is activated

**Q: Python version error**
A: You must use Python 3.12. Check: `python --version`

**Q: Engine not working**
A: Download Stockfish and place in `Engines` folder, then use Engine → Manage → Install

## Support
For issues, refer to `SETUP_INSTRUCTIONS.md` troubleshooting section.

## Attribution & Licensing

**Important Note**: This is an educational project for CS 210 (Intro to AI Programming) and is **not intended for publishing or commercial use**.

This project builds upon and incorporates code from:
- **Python-Easy-Chess-GUI** - Original project by the Python-Easy-Chess-GUI developers. Used as the foundation for this educational chess application.

This project also uses:
- **Stockfish** - A free and open-source UCI chess engine developed by the Stockfish community. We gratefully acknowledge the Stockfish authors and contributors for their excellent chess engine.

Both the original Python-Easy-Chess-GUI project and Stockfish are used here for educational purposes only to learn about AI, chess algorithms, and GUI development. Credit and recognition are given to the original creators and maintainers of these projects.

---
Enjoy playing chess! ♟️
