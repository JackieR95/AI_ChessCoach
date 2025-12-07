#!/usr/bin/env python3
import subprocess
import sys
import os

# Change to the GUI directory
os.chdir(r'C:\Users\Jacki\College\Fall_2025\CS_210_Intro_AI_Programming\Final_Project\AI_ChessCoach\Python-Easy-Chess-GUI-master')

print("Launching Chess GUI in subprocess...", flush=True)

# Try to run with subprocess to isolate the import
try:
    proc = subprocess.Popen(
        [sys.executable, 'python_easy_chess_gui.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    print("Process started with PID:", proc.pid, flush=True)
    
    # Give it 5 seconds to initialize
    try:
        stdout, _ = proc.communicate(timeout=5)
        print("Process output:")
        print(stdout)
    except subprocess.TimeoutExpired:
        print("Process is still running (which is good for a GUI)", flush=True)
        proc.terminate()
        
except Exception as e:
    print(f"Error: {e}", flush=True)
    import traceback
    traceback.print_exc()
