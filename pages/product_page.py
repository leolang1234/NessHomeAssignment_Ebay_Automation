import random
import re
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.selectors = {
            "add_to_cart_button": "#atcBtn_btn_1",
            "options_container": 'div[data-testid="x-msku-evo"]',
            "option_groups": "div.x-sku",
            "open_options_button": "button.listbox-button__control",
            "clickable_option": 'div[role="option"][data-sku-value-name]:not([aria-disabled="true"])',
            "added_success": '.lightbox-dialog__window span.ux-textspans:has-text("Added to cart")',
            "price": '[data-testid="x-price-primary"]',
        }

        self.add_to_cart_button: Locator = self.page.locator(self.selectors["add_to_cart_button"])
        self.options_container: Locator = self.page.locator(self.selectors["options_container"])
        self.option_groups: Locator = self.options_container.locator(self.selectors["option_groups"])
        self.added_success: Locator = self.page.locator(self.selectors["added_success"])
        self.price_locator: Locator = self.page.locator(self.selectors["price"])

    def open(self, url: str) -> None:
        self.logger.debug("Opening product: %s", url)
        self.page.goto(url)

    def _select_variants(self) -> None:
        if self.options_container.count() == 0:
            return

        self.option_groups.first.wait_for()

        for group_index in range(self.option_groups.count()):
            group = self.option_groups.nth(group_index)

            group.locator(self.selectors["open_options_button"]).first.click()

            available_options = group.locator(self.selectors["clickable_option"])
            available_count = available_options.count()

            if available_count == 0:
                raise RuntimeError("Unable to select a variant")

            rnd_index = random.randrange(available_count)
            available_options.nth(rnd_index).click()

    def is_available(self) -> bool:
        return self.add_to_cart_button.count() > 0

    def get_price(self) -> float:
        try:
            price_text = self.price_locator.inner_text(timeout=5000)
            match = re.search(r"[\d,.]+", price_text)
            return float(match.group(0).replace(",", "")) if match else float("inf")
        except Exception:
            return float("inf")

    def add_to_cart_with_random_variants(self, max_price: float = None) -> bool:
        self._select_variants()
        if max_price is not None:
            price = self.get_price()
            if price > max_price:
                self.logger.debug("Price $%.2f exceeds max $%.2f – skipping", price, max_price)
                return False
        self.add_to_cart_button.click()
        # Logged-in users are redirected straight to cart; guests see a lightbox.
        try:
            self.page.wait_for_url(lambda url: "cart" in url, timeout=8000)
            return True
        except Exception:
            self.added_success.wait_for()
            return True

