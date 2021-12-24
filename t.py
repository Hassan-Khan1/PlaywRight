from playwright.sync_api import sync_playwright,TimeoutError

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('https://example.com')
        element = page.querySelector('xpath=//html/body')
        
        
        print(element)
