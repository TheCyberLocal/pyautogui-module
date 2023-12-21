"""
This Python script serves as a comprehensive reference guide to the `pyautogui` module,
designed for educational purposes. It showcases various functions and capabilities of `pyautogui`,
such as screen analysis, mouse automation, and GUI interaction.
The script provides examples of each function in action,
making it a valuable resource for learning and understanding how to automate GUI operations in Python.
It's a perfect starting point for those looking to explore GUI automation and enhance their Python scripting skills.
"""

import pyautogui  # Imports the pyautogui module for GUI automation.

x, y = 20, 50  # Sets variables x and y to 20 and 50, respectively.

screenWidth, screenHeight = pyautogui.size()  # Retrieves the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position()  # Gets the current mouse X and Y position.

x_width, y_width = (100, 100)  # Sets the size of the search region.

# Searches for 'picture.png' on screen in the specified region, using grayscale and a confidence level.
pyautogui.locateOnScreen('picture.png', region=(screenWidth, screenHeight, x_width, y_width), grayscale=True, confidence=0.9)

# Locates the center of 'picture.png' on screen in the specified region.
pyautogui.locateCenterOnScreen('picture.png', region=(screenWidth, screenHeight, x_width, y_width), grayscale=True, confidence=0.9)

r1, g1, b1 = pyautogui.pixel(x, y)  # Gets the RGB color of the pixel at (x, y).

# Takes a screenshot of the specified region.
pic = pyautogui.screenshot(region=(screenWidth, screenHeight, x_width, y_width))

r2, g2, b2 = pic.getpixel(x, y)  # Gets the RGB color of the pixel at (x, y) in the screenshot.

pyautogui.click()  # Performs a mouse click at the current mouse location.
pyautogui.click(100, 200)  # Moves the mouse to (100, 200) and clicks.
pyautogui.click('button.png')  # Finds 'button.png' on the screen and clicks it.

pyautogui.move(0, 10)  # Moves the mouse cursor 10 pixels down.
pyautogui.moveTo(100, 150)  # Moves the mouse cursor to the coordinates (100, 150).
pyautogui.doubleClick()  # Double clicks at the current mouse location.

# Moves the mouse to (500, 500) over 2 seconds with an ease-in-out quad tween.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

pyautogui.click(clicks=2)  # Performs a double click.
# Double clicks with a quarter-second interval between clicks.
pyautogui.click(clicks=2, interval=0.25)
# Triple right-clicks with a quarter-second interval between clicks.
pyautogui.click(button='right', clicks=3, interval=0.25)

# Drags the mouse to (100, 200) while holding the left mouse button.
pyautogui.dragTo(100, 200, button='left')
# Drags the mouse to (300, 400) over 2 seconds while holding the left mouse button.
pyautogui.dragTo(300, 400, 2, button='left')
# Drags the mouse left 30 pixels over 2 seconds while holding the right mouse button.
pyautogui.drag(30, 0, 2, button='right')

# This line scrolls the mouse wheel up by a small amount (10 clicks).
pyautogui.scroll(10)
# This line scrolls the mouse wheel down by a small amount (10 clicks).
pyautogui.scroll(-10)

# Types 'Hello world!' with a quarter-second pause between each key press.
pyautogui.write('Hello world!', interval=0.25)
pyautogui.press('esc')  # Presses the Esc key.
pyautogui.press('left', presses=3)  # Presses the left arrow key three times.

pyautogui.keyDown('shift')  # Holds down the Shift key.
pyautogui.press(['left', 'left', 'left', 'left'])  # Presses the left arrow key four times.
pyautogui.keyUp('shift')  # Releases the Shift key.

pyautogui.hotkey('ctrl', 'shift', 'esc')  # Presses Ctrl+Shift+Esc keys together.
pyautogui.hotkey('ctrl', 'c')  # Presses Ctrl+C keys together.

# The following are functions to create different types of alert and prompt windows.
pyautogui.alert(text='', title='', button='OK')
pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])
pyautogui.prompt(text='', title='' , default='')
pyautogui.password(text='', title='', default='', mask='*')

# The commented section below lists all the key names that can be used with pyautogui's typing and pressing functions.
'''
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
'''
