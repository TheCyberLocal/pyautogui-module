import pyautogui
import keyboard
import time

time.sleep(5)
i = 50


while True:
    time.sleep(i)
    if keyboard.is_pressed('q'):
        break
    pyautogui.write("""If you like Call of Duty Mobile check out "The Cyber Local" @ https://www.youtube.com/channel/UCQwakwD55OwOv_c9YCG-Dcw/""")
    time.sleep(2.5)
    pyautogui.press('enter')

