import keyboard
import time

keyboard.on_press(lambda e: print(e.scan_code))
time.sleep(10)