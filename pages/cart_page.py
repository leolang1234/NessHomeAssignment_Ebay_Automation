import re
from playwright.sync_api import Page, Locator
from utils.data_utils import load_test_data
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_url = load_test_data()["cart_url"]

        self.selectors = {
            "cart_container": '[data-test-id="app-cart"]',
        }

        self.cart_container: Locator = self.page.locator(self.selectors["cart_container"])

    def open(self) -> None:
        self.logger.debug("Opening cart: %s", self.cart_url)
        self.page.goto(self.cart_url)

    def clear(self) -> None:
        self.logger.info("Clearing cart")
        self.open()
        self.cart_container.wait_for()
        removed_count = 0
        while True:
            removed = self.page.evaluate("""() => {
                const btn = document.querySelector('button[data-test-id="cart-remove-item"]');
                if (btn) { btn.click(); return true; }
                return false;
            }""")
            if not removed:
                break
            removed_count += 1
            self.page.wait_for_timeout(800)
        self.logger.info("Removed %d item(s) from cart", removed_count)

    def get_total_amount(self) -> float:
        self.cart_container.wait_for()

        # Each cart item has a div.item-price container with the USD price.
        # Using the container (not individual nested spans) ensures one read per item.
        prices = self.page.evaluate("""() => {
            const prices = [];
            document.querySelectorAll('[data-test-id="app-cart"] div.item-price').forEach(el => {
                const match = el.textContent.match(/US \\$([\\d,.]+)/);
                if (match) prices.push(parseFloat(match[1].replace(/,/g, '')));
            });
            return prices;
        }""")

        total = sum(prices)
        self.logger.debug("Cart prices: %s → total: $%.2f", prices, total)
        return total

