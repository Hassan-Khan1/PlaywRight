from typing import List
from playwright.sync_api import sync_playwright,TimeoutError
from time import sleep
import csv

def main(url):
  with sync_playwright() as p:
    
    browser = p.chromium .launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.close()
    page1  = browser.new_page()

    page1.goto(url)

    # with page.expect_page() as tab:
    #         page.click('.newTabByLink')
    #     # do some steps
      
    # tab.close()
    
    # browser.close()
if __name__ == '__main__':

  main('https://www.techjuice.pk/')
