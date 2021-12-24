from playwright.sync_api import sync_playwright
from time import sleep
with sync_playwright() as p:
    user_data_dir = 'directory'

    page = p.chromium.launch_persistent_context(user_data_dir, headless=False )

    page = page.new_page()
        # page.goto('https://playwright.dev/python/docs/trace-viewer')

    page.goto('http://127.0.0.1:8000/login/')
    # login = page.query_selector('[href="/login"]')          # Using CSS Selector
    # login.click()
    sleep(1)

    # page.query_selector(p)
    # page.query_selector_all(p)
    user_input = page.query_selector("[id= 'username']")    
    user_input.click()          #Using ID 
    user_input.type("admin")
    sleep(1)

    pass_input = page.query_selector("[id= 'password']")

    # pass_input = page.query_selector('//*[text()="Password"]/following-sibling::*')
    pass_input.type("admin")
    
    sleep(1)
    page.query_selector('[type ="submit"]').click()

    # Execute login steps manually in the browser window
    sleep(4)
