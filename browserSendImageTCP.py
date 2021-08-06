from pyppeteer import launch
import asyncio
from sendImageTCP import send

loop = asyncio.get_event_loop()

async def main():
	browser = await launch(
		headless=False,
		args=['--size=320,240']
	)
	page = await browser.newPage()
	while True:
		await page.screenshot({'path': 'browserImage.png'})
		send('browserImage.png')
		# input()
loop.run_until_complete(main())