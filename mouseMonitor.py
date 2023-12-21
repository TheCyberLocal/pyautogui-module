"""
This Python script creates a GUI application using Tkinter to continuously
display the current mouse position and the color of the pixel under the mouse cursor.
It's designed to float above all other windows, providing real-time data as you navigate your computer.
This is particularly useful when requiring colors and coordinates of screen objects when programming hotkeys and macros.
"""

import pyautogui  # Imports the pyautogui module for GUI automation.
import tkinter as tk  # Imports the tkinter module for creating GUI applications.

def update_info():
    x, y = pyautogui.position()  # Gets the current mouse X and Y position.
    r, g, b = pyautogui.pixel(x, y)  # Gets the RGB color of the pixel at the current mouse position.
    label.config(text=f'X: {x} Y: {y}\nRGB: {r}, {g}, {b}')  # Updates the label with the mouse position and pixel color.
    root.after(750, update_info)  # Schedules the function to run again after 750 milliseconds.

root = tk.Tk()  # Creates the main window.
root.title("Mouse Tracker")  # Sets the title of the window.
root.attributes('-topmost', True)  # Ensures the window stays on top of other windows.

label = tk.Label(root, font=('Helvetica', 12))  # Creates a label to display the information.
label.pack()  # Packs the label into the window.

update_info()  # Calls the function to start updating the label.
root.mainloop()  # Starts the Tkinter event loop.

