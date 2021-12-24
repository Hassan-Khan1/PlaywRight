from typing import List
from playwright.sync_api import sync_playwright,TimeoutError
from time import sleep
import csv


def main(url):

  with sync_playwright() as p:

    # with open('Tech-Juice.csv', 'w', newline='') as outcsv:
    #     writer = csv.writer(outcsv)
    #     writer.writerow(['Title', 'URL', 'Description'])

    browser = p.chromium .launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    # blog = page.  query_selector_all('.site-content > .row > div:first-child .col-md-9')
    # blog =  page.query_selector_all('xpath= //html/body/div/div[1]/div/div')  


    # blog_title11 =  page.query_selector('xpath= //html/body/div/div/div/div/div/div/p')  
    # print(blog_title11.inner_html())

    # Article_Heading =  page.query_selector('xpath= //html/body/div/div/div/div/div/div/h1')  
    # print(Article_Heading.inner_html())

    # written_by =  page.query_selector('xpath= //html/body/div/div/div/div/div/div/div/small/a/span')  
    # print(written_by.inner_html())

    Article_des =  page.query_selector('xpath= //html/body/div/div/div[2]/div/div/div/article/p/span')  
    print(Article_des.inner_html())

# /html/body/div[1]/div[1]/div[1]/div/div/div[1]/h1
    # page.goto(url)
# /html/body/div[1]/div[1]/div[2]/div/div/div[1]/article/p[1]
    # blog = page.query_selector_all('site-content')
    # blog = page.query_selector_all('.col-md-9')
    # print(blog)
    # print(blog.inner_html())
    # list_dic = []
# /html/body/div[1]/div/main/div[1]/div[2]/div/div[1]/div[2]/section/h1
    # dic = {}

    # list_dic = []

    # article_url = []

    # for quote in blog:
    #   # # t = quote.query_selector('xpath=div/h2/a[href].href')
    #   # t = quote.eval_on_selector_all(".text-dark", "elements => elements.map(element => element.href)")
      
    #   try:
    #     Title = quote.query_selector('xpath=div/h2/a').inner_text()
    #     print('Title : ', Title )

    #     Description = quote.query_selector('xpath=div/p').inner_text()
    #     print('Description : ', Description )

    #     hrefs_of_page = quote.eval_on_selector_all(".text-dark", "elements => elements.map(element => element.href)")
    #     str=""
    #     string_format_href = str.join(hrefs_of_page)
    #     article_url.append(string_format_href)
    #     print('hrefs_of_page : ', string_format_href )

    #     dic = {}
    #     dic['Title','Description','Url'] = Title,Description,string_format_href

    #     list_dic.append(dic)

    #     print("\n")

    #   except:
    #     Title = "Not Found"
    #     print('Title : ', Title )
    #     print('Description : ', Description )
    #     print('hrefs_of_page : ', hrefs_of_page )

      
      
 

if __name__ == '__main__':

    main('https://www.techjuice.pk/eu-ranks-huawei-as-the-worlds-2nd-highest-investor-in-rd/')

            
