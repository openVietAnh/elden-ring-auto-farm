import threading
import time
import pydirectinput
from pynput import keyboard

running = False
listener = None

def execute_actions():
    global running
    pydirectinput.keyDown('w')
    time.sleep(4)
    pydirectinput.keyUp('w')
    while running:
        pydirectinput.press('e')
        time.sleep(3)
        pydirectinput.press('q')
        time.sleep(2)

        pydirectinput.keyDown('s')
        time.sleep(4)
        pydirectinput.keyUp('s')

        pydirectinput.press('ctrl')
        time.sleep(4)

        pydirectinput.press('w')
        pydirectinput.press('q')
        pydirectinput.keyDown('w')
        time.sleep(4.3)
        pydirectinput.keyUp('w')

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
