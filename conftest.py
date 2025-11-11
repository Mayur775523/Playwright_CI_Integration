import pytest
from playwright.sync_api import sync_playwright

# ---------------- Browser Fixture ----------------
@pytest.fixture(scope="session")
def browser():
    """Launches Chromium browser once per test session (headed)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        yield browser
        browser.close()

# ---------------- Page Fixture ----------------
@pytest.fixture(scope="function")
def page(browser):
    """Creates a new browser context and page for each test."""
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    yield page
    # Take screenshot after each test (for tracking or debugging)
    page.screenshot(path=f"screenshots/{page.title() or 'test_page'}.png", full_page=True)
    context.close()

# ---------------- Notes ----------------
# A fixture = reusable setup & teardown code for tests.

# browser fixture:
# 1. Launches Chromium browser once for all tests.
# 2. `yield` gives control to the test.
# 3. Closes the browser after session ends.

# page fixture:
# 1. Uses browser fixture to create isolated context per test.
# 2. Opens a fresh page (tab) for every test.
# 3. Records video to /videos folder.
# 4. After test, takes screenshot & closes the context.

# Example usage:
# def test_google_search(page):
#     page.goto("https://www.google.com")
#     assert "Google" in page.title()
