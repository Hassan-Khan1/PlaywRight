from playwright.sync_api import sync_playwright
from time import sleep
def main():
    with sync_playwright() as p:
        browser = p.chromium .launch(headless=False)
        
        page = browser.new_page()
        # page.goto('https://playwright.dev/python/docs/trace-viewer')

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
        
        sleep(2)

        pass_input = page.query_selector('//*[text()="Password"]/following-sibling::*')
        pass_input.type("text")
        
        sleep(2)

        page.query_selector('[type ="submit"]').click()
        sleep(2)

        logout_selector = '//*[@href= "/logout"]'
        try:
            logout = page.wait_for_selector(logout_selector,timeout=2000)
            print("Login SuccessFully")
        except:
            print("Login Failed")
            exit()
        
        sleep(2)

        quotes = page.query_selector_all('[class="excerpt"]')
        for quote in quotes:
            print(quote.query_selector('.text').inner_text())

        

       

        page.wait_for_timeout(5000)
        # time.sleep(5) 
        print("Run SuccessFUlly")

        browser.close()





if __name__ == '__main__':
    main()