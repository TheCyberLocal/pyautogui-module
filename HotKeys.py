from pynput import keyboard as key  # Imports the keyboard module from pynput for hotkey functionality
from pyautogui import click  # Imports the click function from pyautogui for simulating mouse clicks
import sys  # Imports the sys module for system-specific parameters and functions

def close_hotkeys():  # Defines a function to close the program
    sys.exit(0)  # Exits the program

def clicker():  # Defines a function to simulate mouse clicks
    click(clicks=15)  # Simulates 15 mouse clicks

def click_power_1():  # Defines a function to click at a specific screen position
    click(876, 90)  # Clicks at coordinates (876, 90)

def click_power_2():  # Defines another function for clicking at a different position
    click(960, 140)  # Clicks at coordinates (960, 140)

def click_power_3():  # Defines a third function for clicking at another position
    click(1056, 86)  # Clicks at coordinates (1056, 86)

with key.GlobalHotKeys({  # Creates a context manager for global hotkeys

    '<ctrl>': close_hotkeys,  # Binds the Ctrl key to the close_hotkeys function

    '<alt>': clicker,  # Binds the Alt key to the clicker function

    'q': click_power_1,  # Binds the 'q' key to the click_power_1 function
    'w': click_power_2,  # Binds the 'w' key to the click_power_2 function
    'e': click_power_3,  # Binds the 'e' key to the click_power_3 function

}) as h:  # Opens the hotkey context manager as h
    h.join()  # Waits for the hotkey thread to terminate
