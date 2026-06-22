import logging
import allure
from playwright.sync_api import Page
from pages.cart_page import CartPage

logger = logging.getLogger(__name__)


def assert_cart_total_not_exceeds(page: Page, budget_per_item: float, items_count: int) -> None:
    budget = budget_per_item * items_count
    logger.info("Verifying cart total (budget: $%.2f × %d = $%.2f)", budget_per_item, items_count, budget)
    cart = CartPage(page)
    cart.open()

    total = cart.get_total_amount()
    logger.info("Cart total: $%.2f | budget: $%.2f", total, budget)

    allure.attach(page.screenshot(full_page=True), name="cart_summary", attachment_type=allure.attachment_type.PNG)

    assert total <= budget, f"Cart total {total} exceeds limit {budget}"
    logger.info("Cart total assertion passed")
