import pyautogui
import time

start = time.time()
myScreenshot = pyautogui.screenshot()
myScreenshot.save('desktopImage.jpg')
print(f"Screenshot {time.time()-start}s")