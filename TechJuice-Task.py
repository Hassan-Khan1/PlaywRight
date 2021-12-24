from typing import List
from playwright.sync_api import sync_playwright,TimeoutError
from time import sleep
import csv


def main(url):

  with sync_playwright() as p:

    with open('Tech-Juice.csv', 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Title', 'URL', 'Description'])

    browser = p.chromium .launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    blog = page.  query_selector_all('.site-content > .row > div:first-child .col-md-9')
    # blog = page.query_selector_all('site-content')
    # blog = page.query_selector_all('.col-md-9')
    print(blog)
    list_dic = []

    for quote in blog:
      Title = quote.query_selector('.text-dark').inner_text()
      # print('Title : ', Title )
      hrefs_of_page = quote.eval_on_selector_all(".text-dark", "elements => elements.map(element => element.href)")
      # hrefs_of_page = quote.eval_on_selector_all("a[href]", "elements => elements.map(element => element.href)")
      # print("Link : ",hrefs_of_page)
      Description = quote.query_selector('.excerpt').inner_text()
      # print('Description : ',Description ,'\n')
      dic = {}
      dic['Title','Url','Description'] = Title,hrefs_of_page,Description
      list_dic.append(dic)
      
      with open('Tech-Juice.csv', 'a', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow([Title,hrefs_of_page,Description])
    # print("Dic ; ",dic ,'\n')   
    print('List ; ',list_dic)

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