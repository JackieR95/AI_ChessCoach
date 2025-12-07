#!/usr/bin/env python3
import sys
import threading

print("Test 1: Direct import", flush=True)

def import_psg():
    try:
        print("Thread: Importing PySimpleGUI...", flush=True)
        import PySimpleGUI as sg
        print("Thread: PySimpleGUI imported!", flush=True)
        sg.popup("Hello from PySimpleGUI!")
        print("Thread: Popup shown!", flush=True)
    except Exception as e:
        print(f"Thread error: {e}", flush=True)
        import traceback
        traceback.print_exc()

t = threading.Thread(target=import_psg, daemon=False)
t.start()
t.join(timeout=5)

if t.is_alive():
    print("ERROR: PySimpleGUI import timed out!", flush=True)
    sys.exit(1)
else:
    print("SUCCESS: PySimpleGUI worked!", flush=True)
