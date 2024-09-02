import threading
import time
import pydirectinput
from pynput import keyboard

running = False
listener = None

def execute_actions():
    global running
    while running:
        # Press W for 2.5 seconds
        pydirectinput.keyDown('w')
        time.sleep(4)
        pydirectinput.keyUp('w')

        # Press E, delay 3 seconds, press Q
        pydirectinput.press('e')
        time.sleep(3)
        pydirectinput.press('q')

        # Move mouse to the left
        pydirectinput.moveRel(-100, 0, duration=0.5)

        # Press W for 2.5 seconds
        pydirectinput.keyDown('w')
        time.sleep(4)
        pydirectinput.keyUp('w')

        # Press Ctrl
        pydirectinput.press('ctrl')

        # Move mouse to the left again
        pydirectinput.moveRel(-100, 0, duration=0.5)

def on_press(key):
    global running, listener
    try:
        if key.char == 'c':
            if running:
                running = False
                listener.stop()
            else:
                running = True
                threading.Thread(target=execute_actions).start()
    except AttributeError:
        pass

def main():
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
