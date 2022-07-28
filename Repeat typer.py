import pyautogui
import keyboard
import time

time.sleep(5)
i = 10

while True:
    time.sleep(i)
    if keyboard.is_pressed('q'):
        break
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'tab')

