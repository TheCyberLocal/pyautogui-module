"""
This script uses pyautogui to automate mouse movements, creating a square spiral pattern on the screen.
The time.sleep(5) at the beginning provides a 5-second delay before the script starts,
which gives you time to move the cursor onto a drawing program.
The while loop decreases the distance with each iteration, causing the spiral to get smaller.
Once the cursor moves an increment of less then one pixel the program will stop.
"""

import pyautogui  # Imports the pyautogui library for GUI automation
import time  # Imports the time library for time-related functions

time.sleep(5)  # Pauses execution for 5 seconds

wait = 0.1  # Sets a wait time of 0.1 seconds for each GUI action
distance = 1000  # Sets the initial distance for movement

pyautogui.move(-(distance/2), -(distance/2))  # Moves the mouse cursor to the starting position

while distance > 0:  # Starts a loop that will run until the distance is 0
    pyautogui.drag(distance, 0, duration=wait)  # Drags the mouse right by 'distance' pixels
    distance -= 5  # Decreases the distance for the next move
    pyautogui.drag(0, distance, duration=wait)  # Drags the mouse down by 'distance' pixels
    pyautogui.drag(-distance, 0, duration=wait)  # Drags the mouse left by 'distance' pixels
    distance -= 5  # Decreases the distance again for the next move
    pyautogui.drag(0, -distance, duration=wait)  # Drags the mouse up by 'distance' pixels
