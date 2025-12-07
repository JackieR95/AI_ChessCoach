import sys
import time
sys.path.insert(0, r'C:\Users\Jacki\College\Fall_2025\CS_210_Intro_AI_Programming\Final_Project\AI_ChessCoach\Python-Easy-Chess-GUI-master')

try:
    from python_easy_chess_gui import EasyChessGui
    print("Import successful")
    
    gui = EasyChessGui(
        theme='Reddit',
        engine_config_file='pecg_engines.json',
        user_config_file='pecg_user.json',
        gui_book_file='book/gui_book.bin',
        computer_book_file='book/comp.bin',
        human_book_file='book/human.bin',
        is_use_gui_book=False,
        is_random_book=True,
        max_book_ply=16
    )
    print("GUI initialized successfully")
    gui.main_loop()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
