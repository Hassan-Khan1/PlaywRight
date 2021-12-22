from playwright.sync_api import sync_playwright
from time import sleep
def main(url):
    with sync_playwright() as p:
        browser = p.chromium .launch(headless=True)
        
        page = browser.new_page()

        page.goto(url)
        quotes = page.query_selector_all('.postbox')
        # quotes = page.waitForSelector(.col-md-9)
        print(quotes)
        # print(quotes.inner_html())

        for quote in quotes:
                # s = quote.innerHTML()
                SS = quote.query_selector('.text-dark')
                print("SS :s",SS)

        #       print(quote.query_selector('.text').inner_text())

        #       print(quotes)

if __name__ == '__main__':
    main('https://www.techjuice.pk/')