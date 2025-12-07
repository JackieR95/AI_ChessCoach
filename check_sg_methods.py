import PySimpleGUI as sg

print("Theme methods:", [x for x in dir(sg) if 'theme' in x.lower()])
print("Set methods:", [x for x in dir(sg) if 'set' in x.lower()])
