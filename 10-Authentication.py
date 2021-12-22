from playwright.sync_api import sync_playwright



# Automate logging in​

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=50)
    # page = browser.new_page()
    # page.goto("http://whatsmyuseragent.org/")
    # page.screenshot(path="example.png")
    context = browser.new_context()

    page = browser.new_page()
    page.goto('https://github.com/login')

    page.click("input[name=\"login\"]")

    page.fill('input[name="login"]', "Hassan-Khan")

    # page.click("input[name=\"username\"]")
    # page.fill("input[name=\"login\"]", "Hassan Khan")
    # page.fill('input[name=\"login\"]', "asd")
    page.fill('input[name="password"]', "Hassan12")
    
    page.click('[type ="submit"]')

    
# Verify app is logged in

