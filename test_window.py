import PySimpleGUI as sg

# Create a simple window
layout = [[sg.Text('Hello from PySimpleGUI!')], [sg.Button('OK')]]
window = sg.Window('Test', layout)

# Read one event
button, values = window.read(timeout=2000)
window.close()

print(f"Window worked! Button pressed: {button}")
