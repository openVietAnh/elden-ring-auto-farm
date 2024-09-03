import threading
import time
import pydirectinput
import ctypes
from pynput import keyboard

running = False
listener = None

# ctypes structures and functions for mouse events
PUL = ctypes.POINTER(ctypes.c_ulong)

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL))

class INPUT_I(ctypes.Union):
    _fields_ = [("mi", MOUSEINPUT)]

class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", INPUT_I)]

def move_mouse(dx, dy):
    extra = ctypes.c_ulong(0)
    mi = MOUSEINPUT(dx, dy, 0, 0x0001, 0, ctypes.pointer(extra))
    inp = INPUT(ctypes.c_ulong(0), INPUT_I(mi))
    ctypes.windll.user32.SendInput(1, ctypes.pointer(inp), ctypes.sizeof(inp))

def execute_actions():
    global running
    while running:
        # Press W for 2.5 seconds
        pydirectinput.keyDown('w')
        time.sleep(2.5)
        pydirectinput.keyUp('w')

        # Press E, delay 3 seconds, press Q
        pydirectinput.press('e')
        time.sleep(3)
        pydirectinput.press('q')

        # Move mouse to the left
        move_mouse(-100, 0)

        # Press W for 2.5 seconds
        pydirectinput.keyDown('w')
        time.sleep(2.5)
        pydirectinput.keyUp('w')

        # Press Ctrl
        pydirectinput.press('ctrl')

        # Move mouse to the left again
        move_mouse(-100, 0)

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
