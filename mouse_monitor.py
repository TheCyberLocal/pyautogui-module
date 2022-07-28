import pyautogui
import time
while True:
    currentMouseX, currentMouseY = pyautogui.position()
    print('X: ' + str(currentMouseX), 'Y: ' + str(currentMouseY))
    r, g, b = pyautogui.pixel(currentMouseX, currentMouseY)
    print('RGB: ' + str(r) + ', ' + str(g) + ', ' + str(b))
    time.sleep(0.75)
