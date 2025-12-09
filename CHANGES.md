# Written by Jacqueline Rael and Copilot Agent
# Date: 12/09/2025
# Lab: Final Project

## Changes Made to AI_ChessCoach Project

### Files Created/Modified:

#### 1. **ai_chess_mentor.py** (CREATED)
   - Custom AI Chess Mentor module
   - Provides AI coaching and analysis features for the chess GUI
   - Original creation by Jacqueline Rael and Copilot Agent

#### 2. **python_easy_chess_gui.py** (MODIFIED)
   - **Line ~2531-2537**: Fixed PySimpleGUI compatibility issues
     - Updated `sg.theme()` and `sg.set_options()` calls to handle AttributeError exceptions
     - Removed deprecated `sg.ChangeLookAndFeel()` and `sg.SetOptions()` calls

   - **Line ~1505**: Replaced deprecated `sg.RButton()` with `sg.Button()`
     - Updated the `render_square()` method to use the modern Button API

   - **Line ~2638-2642**: Increased window size
     - Added `size=(1400, 900)` parameter to make the game window larger and more usable
   
   - **Line ~2544-2590**: Scaled up UI elements with larger window
     - Increased font sizes from 10 to 12 (multilines to 11)
     - Expanded text box widths and multiline sizes
     - Move list: 52x8 → 65x12
     - AI Coach: 52x3 → 65x5
   
   - **Line ~1683-1714**: Added game difficulty selection (NEW FEATURE)
     - Created `select_difficulty()` method with three difficulty levels
     - Easy: depth 3 (shallow, fastest)
     - Medium: depth 8 (balanced)
     - Hard: depth 18 (deep, most challenging)
     - Displays selected difficulty in the game status bar
   
   - **Line ~3675-3683**: Integrated difficulty selection into game flow
     - Shows difficulty dialog when user clicks "Play"
     - Passes selected difficulty to `play_game()` method
     - Sets engine search depth based on difficulty level

#### 3. **SETUP_REQUIREMENTS.txt** (MODIFIED)
   - **Line 3**: Updated PySimpleGUI version from 5.0.10 to 5.0.8.3
   - Later upgraded to PySimpleGUI 5.0.10 from the official private PyPI server
   - Added header with project information

### Files Created:
#### 1. **Engines/** (CREATED - Directory)
   - Directory for storing chess engine executables
   - Required for the application to function properly

### Issues Fixed & Features Added:

1. **PySimpleGUI Compatibility**: 
   - Original code had compatibility issues with PySimpleGUI 5.0.8.3
   - Fixed deprecated API calls and attribute errors
   - Upgraded to PySimpleGUI 5.0.10 from private PyPI server

2. **Window Size & UI Scaling**:
   - Increased default window size from auto to 1400x900 pixels for better usability
   - Scaled all UI elements (text sizes, multiline widths/heights, fonts) to match larger window

3. **Missing Directories**:
   - Created the `Engines/` directory required by the application

4. **Game Difficulty Selection** (NEW FEATURE):
   - Added interactive difficulty selection dialog when starting a game
   - Three difficulty levels with different AI search depths:
     - **Easy**: Depth 3 (quick moves, beginner-friendly)
     - **Medium**: Depth 8 (balanced gameplay)
     - **Hard**: Depth 18 (challenging, deep analysis)
   - Difficulty level displayed in the game status bar### Python Environment:

- **Python Version**: 3.12.10 (virtual environment in `venv/`)
- **Virtual Environment**: Located at root of AI_ChessCoach project
- **Installation Command**:
  ```
  pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
  ```

### How to Run:

```powershell
cd "c:\Users\Jacki\College\Fall_2025\CS_210_Intro_AI_Programming\Final_Project\AI_ChessCoach"
. .\venv\Scripts\Activate.ps1
cd Python-Easy-Chess-GUI-master
python python_easy_chess_gui.py
```

### Project Structure:

```
AI_ChessCoach/
├── venv/                              # Python 3.12 virtual environment
├── SETUP_REQUIREMENTS.txt             # Dependencies (modified)
├── SETUP_INSTRUCTIONS.md              # Setup guide
├── CHANGES.md                         # This file
└── Python-Easy-Chess-GUI-master/
    ├── python_easy_chess_gui.py       # Main GUI (modified)
    ├── ai_chess_mentor.py             # AI Coach module (created)
    ├── Engines/                       # Chess engine directory (created)
    ├── Images/                        # Chess piece images
    └── Icon/                          # Application icons
```

---

**Summary**: All modifications ensure compatibility with Python 3.12, fix deprecated PySimpleGUI API calls, increase the game window size for better user experience, and integrate the custom AI Chess Mentor module created by Jacqueline Rael and Copilot Agent.
