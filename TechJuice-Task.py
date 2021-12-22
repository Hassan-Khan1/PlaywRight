from playwright.sync_api import sync_playwright
from time import sleep
def main(url):

  with sync_playwright() as p:

    browser = p.chromium .launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    blog = page.query_selector_all('.col-md-9')
  
    for quote in blog:
      
      Title = quote.query_selector('.text-dark').inner_text()
      Description = quote.query_selector('.excerpt').inner_text()
      print('Title : ', Title )
      print('Description : ',Description)

if __name__ == '__main__':
    main('https://www.techjuice.pk/')

            # quotes =page.text_content("row")

# SHandle preview=JSHandle@node
 # quotes = page.query_selector_all('[class="row"]')
        # s = quotes[2].getProperty('innerHTML');
        # print(quotes)
        # print(quotes.innerHtml())

              # print(quo,te.query_selector('.text-dark')).innerHTML()
        # for quote in quotes:
        #         # s = quote.innerHTML()
        #         SS = quote.query_selector('.text-dark')
                # print("SS :s",quote)

        #       print(quote.query_selector('.text').inner_text())
        # page.wait_for_timeout(10000)
        #       print(quotes)