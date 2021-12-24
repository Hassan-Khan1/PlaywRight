from playwright.sync_api import Playwright, sync_playwright


# Run CMd For inspector playwright codegen http://quotes.toscrape.com/

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://quotes.toscrape.com/
    page.goto("http://quotes.toscrape.com/")

    # Click text=Login
    page.click("text=Login")
    # assert page.url == "http://quotes.toscrape.com/login"

    # Click input[name="username"]
    page.click("input[name=\"username\"]")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Click input[name="username"]
    page.click("input[name=\"username\"]")

    # Fill input[name="username"]
    page.fill("input[name=\"username\"]", "FDFD")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "FDFD")

    # Click input:has-text("Login")
    page.click("input:has-text(\"Login\")")
    # assert page.url == "http://quotes.toscrape.com/"

    # Click text=“The world as we have created it is a process of our thinking. It cannot be chan
    page.click("text=“The world as we have created it is a process of our thinking. It cannot be chan")

    # Click :nth-match(div:has-text("“The world as we have created it is a process of our thinking. It cannot be chan"), 4)
    page.click(":nth-match(div:has-text(\"“The world as we have created it is a process of our thinking. It cannot be chan\"), 4)")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
