from playwright.sync_api import Page, expect

class HomePageOrangeHRM:

    def __init__(self, page: Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")

    def is_upgrade_button_visible(self):
        expect(self.upgrade_button.is_visible() )

    def navigate_to_performance(self):
        self.performance_link.click()

    def navigate_to_dashboard(self):
        self.dashboard_link.click()