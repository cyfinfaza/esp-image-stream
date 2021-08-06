import time
from pyppeteer import launch
import asyncio
from sendImageTCP import send

loop = asyncio.get_event_loop()

async def main():
	browser = await launch(
		headless=False,
		args=['-size=320,240']
	)
	page = await browser.newPage()
	await page.goto('https://www.google.com')
	while True:
		start = time.time()
		await page.screenshot({'path': 'browserImage.jpg', 'quality':1, 'width':320, 'height':240})
		print(f"Screenshot {(time.time()-start)}s")
		send('browserImage.jpg', 0, 0, 16, 12, progressCounter=False)
		# input()
loop.run_until_complete(main())