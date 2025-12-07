import PySimpleGUI as sg
print("Available popup methods:")
print([x for x in dir(sg) if 'popup' in x.lower()])
print("\nAvailable window methods:")
print([x for x in dir(sg) if 'window' in x.lower()])
print("\nAll upper methods:")
print([x for x in dir(sg) if x[0].isupper()][:20])
