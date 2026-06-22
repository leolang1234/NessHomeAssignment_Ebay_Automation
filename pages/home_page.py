from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.base_url = "https://www.ebay.com"

        self.selectors = {
            "search_input": 'input[name="_nkw"]',
            "ship_to_btn": ".gh-ship-to__menu",
            "country_dropdown": ".menu-button__button",
            "country_option": ".menu-button__item",
            "ship_to_done": ".shipto__close-btn",
        }

        self.search_input: Locator = self.page.locator(self.selectors["search_input"])

    def open(self) -> None:
        self.logger.debug("Opening eBay home: %s", self.base_url)
        self.page.goto(self.base_url)

    def set_ship_to_us(self) -> None:
        self.logger.debug("Setting ship-to: United States")
        self.page.locator(self.selectors["ship_to_btn"]).click()
        self.page.locator(self.selectors["country_dropdown"]).click()
        self.page.locator(f'{self.selectors["country_option"]}:has-text("United States")').click()
        self.page.locator(self.selectors["ship_to_done"]).click()
        self.page.wait_for_timeout(1000)

    def search(self, query: str) -> None:
        self.logger.debug("Searching for '%s'", query)
        self.search_input.fill(query)
        self.search_input.press("Enter")
