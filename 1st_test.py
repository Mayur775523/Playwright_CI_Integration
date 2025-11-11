from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # set True for headless (hidden) mode
    page = browser.new_page()
    page.goto("https://example.com")
    print(f"Loaded page title: {page.title()}")
    browser.close()
