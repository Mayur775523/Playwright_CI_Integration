import os
import pytest
from playwright.sync_api import sync_playwright

# ---------------- Browser Fixture ----------------
@pytest.fixture(scope="session")
def browser():
    """Launch Chromium browser once per test session."""
    with sync_playwright() as p:
        # Detect CI environment
        is_ci = os.getenv("GITHUB_ACTIONS") == "true"

        browser = p.chromium.launch(
            headless=is_ci,  # ✅ Headless in CI, headed locally
            slow_mo=200
        )
        yield browser
        browser.close()


# ---------------- Page Fixture ----------------
@pytest.fixture(scope="function")
def page(browser):
    """Creates a new browser context and page for each test."""
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    yield page
    # Take screenshot after each test
    page.screenshot(
        path=f"screenshots/{page.title() or 'test_page'}.png", full_page=True
    )
    context.close()
