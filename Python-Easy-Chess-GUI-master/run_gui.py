#!/usr/bin/env python3
import sys
import traceback

try:
    print("Starting Chess GUI...", flush=True)
    sys.path.insert(0, '.')
    from python_easy_chess_gui import main
    print("Main function imported successfully", flush=True)
    main()
    print("Main function completed", flush=True)
except Exception as e:
    print(f"ERROR: {e}", flush=True)
    traceback.print_exc()
    sys.exit(1)
