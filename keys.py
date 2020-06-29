# DOCS: https://pynput.readthedocs.io/en/latest/

from pynput.mouse import Button, Controller as MController
from pynput.keyboard import Key, Controller as KController
import time

mouse = MController()
keyboard = KController()

def press_and_release(k):
    if type(k) is Key:
        keyboard.press(k)
        keyboard.release(k)
    elif type(k) is Button:
        mouse.press(k)
        mouse.release(k)

# Start chrome and search for the weather
press_and_release(Key.cmd)
time.sleep(0.1)

keyboard.type('Google Chrome')
time.sleep(0.1)

press_and_release(Key.enter)
time.sleep(1)

keyboard.type('What is the weather today')
press_and_release(Key.enter)