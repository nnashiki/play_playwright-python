import asyncio
from playwright.async_api import async_playwright
import uuid


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        await page.screenshot(path=f"./captcha/ {str(uuid.uuid4())}.png")
        await browser.close()

asyncio.run(main())
