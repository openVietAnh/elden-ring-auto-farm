import threading
import time
import pyautogui
from pynput import keyboard

running = False
listener = None

def execute_actions():
    global running
    while running:
        # Press W for 2.5 seconds
        pyautogui.keyDown('w')
        time.sleep(2.5)
        pyautogui.keyUp('w')

        # Press E, delay 3 seconds, press Q
        pyautogui.press('e')
        time.sleep(3)
        pyautogui.press('q')

        # Move mouse to the left
        pyautogui.moveRel(-100, 0, duration=0.5)

        # Press W for 2.5 seconds
        pyautogui.keyDown('w')
        time.sleep(2.5)
        pyautogui.keyUp('w')

        # Press Ctrl
        pyautogui.press('ctrl')

        # Move mouse to the left again
        pyautogui.moveRel(-100, 0, duration=0.5)

def on_press(key):
    global running, listener
    try:
        if key == keyboard.Key.f12:
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
