import sys
print("Starting simple test", flush=True)
print(f"Python: {sys.version}", flush=True)
print(f"Executable: {sys.executable}", flush=True)

print("Importing tkinter...", flush=True)
import tkinter as tk
print("tkinter imported", flush=True)

print("Creating root...", flush=True)
root = tk.Tk()
print("Root created", flush=True)

print("Test complete!", flush=True)
