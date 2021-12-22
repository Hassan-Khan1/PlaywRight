from playwright.sync_api import sync_playwright

path_to_extension = "./my-extension"
user_data_dir = "/tmp/test-user-data-dir"


def run(playwright):
    context = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,
        args=[
            f"--disable-extensions-except={path_to_extension}",
            f"--load-extension={path_to_extension}",
        ],
    )
    background_page = context.background_pages[0]
    # Test the background page as you would any other page.
    context.close()


with sync_playwright() as playwright:
    run(playwright)