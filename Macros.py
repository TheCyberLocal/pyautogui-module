from pynput import keyboard as key
from pyautogui import click
import sys


def close_hotkeys():
    sys.exit(0)


def clicker():
    click(clicks=15)


def click_power_1():
    click(876, 90)


def click_power_2():
    click(960, 140)


def click_power_3():
    click(1056, 86)


with key.GlobalHotKeys({

    '<ctrl>': close_hotkeys,

    '<alt>': clicker,

    'q': click_power_1,
    'w': click_power_2,
    'e': click_power_3,

}) as h:
    h.join()
