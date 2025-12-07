#!/usr/bin/env python3
print("Starting tkinter test...", flush=True)
try:
    import tkinter as tk
    print("tkinter imported", flush=True)
    root = tk.Tk()
    print("tkinter Tk() created", flush=True)
    root.title("Test")
    root.geometry("200x100")
    label = tk.Label(root, text="Hello")
    label.pack()
    print("About to show window...", flush=True)
    root.after(1000, root.quit)
    root.mainloop()
    print("Done", flush=True)
except Exception as e:
    print(f"Error: {e}", flush=True)
    import traceback
    traceback.print_exc()
