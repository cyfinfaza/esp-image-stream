import pyautogui
import time
from sendImageTCP import send

while True:
	start = time.time()
	pyautogui.screenshot('desktopImage.jpg')
	print(f"Screenshot {(time.time()-start)}s")
	send('desktopImage.jpg', 0, 30, 320, 180, progressCounter=False)