import pyautogui

x, y = 20, 50  # setting vars


screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.


x_width, y_width = (100, 100)  # box size for search
pyautogui.locateOnScreen('picture.png',
                         region=(screenWidth, screenHeight, x_width, y_width),
                         grayscale=True,
                         confidence=0.9)

pyautogui.locateCenterOnScreen('picture.png',
                               region=(screenWidth, screenHeight, x_width, y_width),
                               grayscale=True,
                               confidence=0.9)


r1, g1, b1 = pyautogui.pixel(x, y)

pic = pyautogui.screenshot(region=(screenWidth, screenHeight, x_width, y_width))

r2, g2, b2 = pic.getpixel(x, y)


pyautogui.click()  # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
pyautogui.click('button.png')  # Find where button.png appears on the screen and click it.

pyautogui.move(0, 10)  # Move mouse 10 pixels down from its current position.
pyautogui.moveTo(100, 150)  # Move the mouse to XY coordinates.
pyautogui.doubleClick()  # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2,
                 tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

pyautogui.click(clicks=2)  # double-click the left mouse button
pyautogui.click(clicks=2,
                interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
pyautogui.click(button='right', clicks=3,
                interval=0.25)  # triple-click the right mouse button with a quarter second pause in between clicks

pyautogui.dragTo(100, 200, button='left')  # drag mouse to X of 100, Y of 200 while holding down left mouse button
pyautogui.dragTo(300, 400, 2,
                 button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
pyautogui.drag(30, 0, 2,
               button='right')  # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button


pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')  # Press the Esc key. All key names are in pyautogui.KEY_NAMES
pyautogui.press('left', presses=3)

pyautogui.keyDown('shift')  # Press the Shift key down and hold it.
pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
pyautogui.keyUp('shift')  # Let go of the Shift key.

pyautogui.hotkey('ctrl', 'shift', 'esc')
pyautogui.hotkey('ctrl', 'c')  # Press the Ctrl-C hotkey combination.


# The alert() Function
# Displays a simple message box with text and a single OK button.
# Returns the text of the button clicked on.
pyautogui.alert(text='', title='', button='OK')

# The confirm() Function
# Displays a message box with OK and Cancel buttons. Number and text of buttons can be customized.
# Returns the text of the button clicked on.
pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])

# The prompt() Function
# Displays a message box with text input, and OK & Cancel buttons.
# Returns the text entered, or None if Cancel was clicked.
pyautogui.prompt(text='', title='' , default='')

# The password() Function
# Displays a message box with text input, and OK & Cancel buttons.
# Typed characters appear as *. Returns the text entered, or None if Cancel was clicked.
pyautogui.password(text='', title='', default='', mask='*')

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
