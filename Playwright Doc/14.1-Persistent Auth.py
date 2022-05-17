from playwright.sync_api import sync_playwright
from time import sleep
import os

with sync_playwright() as p:

  username = "hassan86"
  user_data_dir = os.path.join("basepath", username)

  browser = p.chromium.launch_persistent_context(user_data_dir, headless=False ,slow_mo=50)
  # browser = p.chromium.launch(headless=False,)

  page = browser.new_page()
  # page.goto("http://whatsmyuseragent.org/")
  page.goto('https://github.com/login')

  page.click("input[name=\"login\"]")
  page.wait_for_timeout(5000)

  # page.fill('input[name="login"]', "hassan.jamal@mobylogix.com")
  page.fill('input[name="login"]', "hj4684976@gmail.com")
  page.wait_for_timeout(5000)
  # page.fill('input[name="password"]', "hassanmobylogix")
  page.fill('input[name="password"]', "hassan1213khan")
  page.wait_for_timeout(5000)
  
  page.click('[type ="submit"]')
  page.wait_for_timeout(5000)

  page.screenshot(path="Git Hub.png")

  browser.close()


     