from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
      browser = p.chromium .launch(headless=False)
      context = browser.new_context()

      context.tracing.start(screenshots=True, snapshots=True)

      # page.goto('https://playwright.dev/python/docs/trace-viewer')
      page = browser.new_page()
      page.goto('https://quotes.toscrape.com')

      heading = page.query_selector('//h1/a')
      print(heading.inner_text())


      login = page.query_selector('[href="/login"]')          # Using CSS Selector
      login.click()

      sleep(2)
      # page.query_selector(p)
      # page.query_selector_all(p)
      user_input = page.query_selector("[id= 'username']")              #Using ID 
      user_input.type("user")
      


      page.wait_for_timeout(5000)
      # time.sleep(5) 
      print("Run SuccessFUlly")
      context.tracing.stop(path = "trace.zip")

      # browser.close()
