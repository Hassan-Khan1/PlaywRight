from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio


# Demo with Sync

# with sync_playwright() as p:
#     browser = p.chromium .launch(headless=False)
#     page = browser.new_page()
#     page.goto("http://playwright.dev")
#     print(page.title())
#     browser.close()


# Demo with Async 

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main())