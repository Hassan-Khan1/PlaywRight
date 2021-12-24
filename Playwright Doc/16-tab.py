from typing import List
from playwright.sync_api import sync_playwright,TimeoutError
from time import sleep
import csv


def main(url):

  with sync_playwright() as p:

    # with open('Tech-Juice.csv', 'w', newline='') as outcsv:
    #     writer = csv.writer(outcsv)
    #     writer.writerow(['Title', 'URL', 'Description'])

    browser = p.chromium .launch(headless=False)
    
    page = browser.new_page()
    page.goto('https://playwright.dev/python/docs/trace-viewer')
    sleep(2)
    


    # article_url = []
    hrefs_of_page =['https://www.techjuice.pk/how-does-huawei-wifi-ax2-enable-a-better-internet-environment-for-you-when-wfh/', 'https://www.techjuice.pk/federal-minister-for-it-urges-ericsson-to-hire-pakistani-youth/', 'https://www.techjuice.pk/eu-ranks-huawei-as-the-worlds-2nd-highest-investor-in-rd/', 'https://www.techjuice.pk/ufone-launches-roaming-data-gift-facility-in-uae-saudi-arabia/', 'https://www.techjuice.pk/meezan-bank-becomes-the-first-bank-in-the-country-to-launch-state-bank-of-pakistans-i-saaf-scheme-for-small-and-medium-enterprises-smes/', 'https://www.techjuice.pk/huawei-applauds-engineers-in-ict-industry-who-focused-on-new-innovative-technologies-in-the-tiger-2021-program/', 'https://www.techjuice.pk/pitb-and-code-for-pakistan-sign-mou-to-improve-civic-engagement-master-data-management-framework-mdmf/', 'https://www.techjuice.pk/pakistani-b2b-agri-marketplace-tazahs-raises-pakistans-largest-pre-seed-round-extension/', 'https://www.techjuice.pk/supernet-pakistan-unlocks-global-service-offering-through-satadsls-nexat-platform/', 'https://www.techjuice.pk/mastercard-partners-with-ravi-urban-development-authority-to-build-cashless-economic-zone/', 'https://www.techjuice.pk/realme-announces-three-technological-world-firsts-at-realme-gt-2-series-event/', 'https://www.techjuice.pk/jiye-technologies-raises-2-5-million-in-pre-seed-funding-rolls-out-expansion-across-pakistans-major-cities/', 'https://www.techjuice.pk/realme-gave-the-entry-level-market-a-real-quality-overhaul-with-its-c-series/', '']
    # str=""
    # string_format = str.join(hrefs_of_page)
    # article_url.append(string_format)
    # print('hrefs_of_page : ', hrefs_of_page )



    for i in hrefs_of_page:
      page = browser.new_page()
      print(i)
      page.goto(i)
      page.close()
  # await page1.fill('[name="q"]', 'plop');
    # page1 = browser.new_page()
    # blog = page.  query_selector_all('.site-content > .row > div:first-child .col-md-9')
    # blog =  page.query_selector_all('xpath= //html/body/div/div[1]/div/div')  

    # def print_request_sent(request):
    #   print("Request sent: " + request.url)

    # def print_request_finished(request):
      # print("Request finished: " + request.url)

    # page.on("request", print_request_sent)
    # page.on("requestfinished", print_request_finished)

    # page1.on('https://stackoverflow.com/questions/66638076/how-do-i-switch-to-new-tab-or-window-in-playwright-java')
    
    
    
    # blog =  page.query_selector_all('xpath= //html/body/div/div[4]/div[1]/div')  

    # blog = page.query_selector_all('site-content')
    # blog = page.query_selector_all('.col-md-9')
    # print(blog)
    # print(blog.inner_html())
    # list_dic = []
# /html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/h1
    dic = {}
    list_dic = []

    article_url = []
    for quote in range:
      # # t = quote.query_selector('xpath=div/h2/a[href].href')
      # t = quote.eval_on_selector_all(".text-dark", "elements => elements.map(element => element.href)")
      
      try:
        Title = quote.query_selector('xpath=div/h2/a').inner_text()
        # print('Title : ', Title )

        Description = quote.query_selector('xpath=div/p').inner_text()
        # print('Description : ', Description )

        hrefs_of_page = quote.eval_on_selector_all(".text-dark", "elements => elements.map(element => element.href)")
        article_url.append(hrefs_of_page)
        # print('hrefs_of_page : ', hrefs_of_page )
        dic = {}
        dic['Title','Description','Url'] = Title,Description,hrefs_of_page

        list_dic.append(dic)

        print("\n")

      except:
        Title = "Not Found"
        print('Title : ', Title )
        print('Description : ', Description )
        print('hrefs_of_page : ', hrefs_of_page )

      
      
    print("<----------------> LAst")
    # print('List : ',list_dic)
    print('article_url : ',article_url)

    print("<---------------->LAst")

if __name__ == '__main__':

    main('https://www.techjuice.pk/')

            
