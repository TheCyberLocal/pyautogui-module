import pyautogui
import time

time.sleep(5)

wait = 0.1
distance = 1000

pyautogui.move(-(distance/2), -(distance/2))

while distance > 0:
    pyautogui.drag(distance, 0, duration=wait)  # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=wait)  # move down
    pyautogui.drag(-distance, 0, duration=wait)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=wait)  # move up
