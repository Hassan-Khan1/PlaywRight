from typing import List
from playwright.sync_api import sync_playwright,TimeoutError
from time import sleep
import csv

def main(url):
  with sync_playwright() as p:
    with open('Tech-Juice-xpath.csv', 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Title', 'URL', 'Description','Written-by','Article-Heading'])
    browser = p.chromium .launch(headless=False)
    page = browser.new_page()
    page.goto(url)
  
    Homepage =  page.query_selector_all('xpath= //html/body/div/div[4]/div[1]/div')  
   
    list_dic = []
    article_url = []

    for quote in Homepage:
     
      try:
        Title = quote.query_selector('xpath=div/h2/a').inner_text()
        print('Title : ', Title )

        Description = quote.query_selector('xpath=div/p').inner_text()
        print('Description : ', Description )

        hrefs_of_page = quote.eval_on_selector_all(".text-dark", "elements => elements.map(element => element.href)")
        str=""
        string_format_href = str.join(hrefs_of_page)
        article_url.append(string_format_href)
        print('hrefs_of_page : ', string_format_href )

        dic = {}
        dic['Title','Description','Url'] = Title,Description,string_format_href
        list_dic.append(dic)

        with open('Tech-Juice-xpath.csv', 'a', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow([Title,string_format_href,Description])

        print("\n")

      except:
        Title = "Not Found"
        print('Title : ', Title )
        print('Description : ', Description )
        print('hrefs_of_page : ', hrefs_of_page )
      
    print('Article_url : ',article_url)

    page.wait_for_timeout((5000))

    for i in article_url:
      Article_page = browser.new_page()
      Article_page.goto(i)

      Article_Heading =  Article_page.query_selector('xpath= //html/body/div/div/div/div/div/div/h1').inner_html()
      print('Article_Heading : ',Article_Heading)

      written_by =  Article_page.query_selector('xpath= //html/body/div/div/div/div/div/div/div/small/a/span').inner_html()  
      print("Written By --",written_by)

      with open('Tech-Juice-xpath.csv', 'a', newline='') as outcsv:
            writer = csv.writer(outcsv)
            writer.writerow(["","","",written_by,Article_Heading])
      
      Article_page.close()

if __name__ == '__main__':

    main('https://www.techjuice.pk/')

            
# blog = page.query_selector_all('site-content')
# blog = page.query_selector_all('.col-md-9')

# blog = page.  query_selector_all('.site-content > .row > div:first-child .col-md-9')
# blog =  page.query_selector_all('xpath= //html/body/div/div[1]/div/div')  

# # t = quote.query_selector('xpath=div/h2/a[href].href')
# t = quote.eval_on_selector_all(".text-dark", "elements => elements.map(element => element.href)")