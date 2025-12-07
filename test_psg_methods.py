import PySimpleGUI as sg

try:
    # Try the new method names (5.x)
    sg.theme('Reddit')
    print("sg.theme() works!")
except AttributeError as e:
    print(f"sg.theme() failed: {e}")
    try:
        # Try the old method name (4.x)
        sg.ChangeLookAndFeel('Reddit')
        print("sg.ChangeLookAndFeel() works!")
    except AttributeError as e2:
        print(f"sg.ChangeLookAndFeel() also failed: {e2}")

try:
    # Try new method name
    sg.set_options(margins=(0, 3), border_width=1)
    print("sg.set_options() works!")
except AttributeError as e:
    print(f"sg.set_options() failed: {e}")
    try:
        # Try old method name
        sg.SetOptions(margins=(0, 3), border_width=1)
        print("sg.SetOptions() works!")
    except AttributeError as e2:
        print(f"sg.SetOptions() also failed: {e2}")
