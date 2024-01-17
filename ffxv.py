from simple_term_menu import TerminalMenu
import math
import random
import time
import os 
import subprocess

name = "Noctis"
hp = 0
damage = 0 

#print("Вы знакомы с сериями игр Final fantasy? \ от вашего выбора зависит сложность игры")
#ch = input("1: \ 2:")\

#if ch == "1":

def main():
    options = ["New game", "about game", "about author"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"selected {options[menu_entry_index]}!")
    
def text_cent(txt):
    term_width = os.get_terminal_size().columns
    padding = (term_width - len(txt)) // 2
    print(" " * padding + txt)



text_cent("Square Enix")
time.sleep(2)
text_cent("Final Fantasy CLI Remake")
time.sleep(2)

if __name__ == "__main__":
    main()
