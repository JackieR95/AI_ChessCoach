#!/usr/bin/env python3
import sys

print("1. Starting...", flush=True)

try:
    print("2. Importing modules...", flush=True)
    import PySimpleGUI as sg
    print("3. PySimpleGUI imported", flush=True)
    
    import os
    import chess
    import chess.pgn
    import chess.engine
    print("4. Chess modules imported", flush=True)
    
    print("5. All imports successful", flush=True)
except Exception as e:
    print(f"ERROR during import: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("6. Attempting to import main...", flush=True)

try:
    from python_easy_chess_gui import main
    print("7. Main imported", flush=True)
except Exception as e:
    print(f"ERROR importing main: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("8. Calling main()...", flush=True)
try:
    main()
    print("9. Main completed", flush=True)
except Exception as e:
    print(f"ERROR in main: {e}", flush=True)
    import traceback
    traceback.print_exc()
    sys.exit(1)
