import re
from playwright.sync_api import Page, expect
from pages.login_orangehrm import LoginPage
from pages.homepage_orangehrm import HomePageOrangeHRM


def test_example(page: Page) -> None:
    loginpage = LoginPage(page)
    homepage = HomePageOrangeHRM(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    loginpage.enter_username("Admin")
    loginpage.enter_password("admin123")
    loginpage.click_login()

    expect(homepage.upgrade_button).to_be_visible()
    homepage.navigate_to_performance()
    homepage.navigate_to_dashboard()
