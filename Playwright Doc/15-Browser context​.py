from os import wait
from playwright.sync_api import sync_playwright
from time import sleep
def main():
  with sync_playwright() as p:
    browser = p.chromium .launch(headless=False)
    
    page = browser.new_page()
    page.goto('https://playwright.dev/python/docs/trace-viewer')
    

    def print_request_sent(request):
      print("Request sent: " + request.url)

    def print_request_finished(request):
      print("Request finished: " + request.url)

    page.on("request", print_request_sent)
    page.on("requestfinished", print_request_finished)
    page.goto("https://wikipedia.org")

    page.remove_listener("requestfinished", print_request_finished)
    page.goto("http://example.com/")

    # page.goto("https://www.openstreetmap.org/")
    page.on("requestfinished", print_request_finished)
    page.wait_for_timeout(5000)

    
if __name__ == '__main__':
    main()