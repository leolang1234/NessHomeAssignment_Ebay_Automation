import logging
import allure
from playwright.sync_api import Page
from pages.product_page import ProductPage

logger = logging.getLogger(__name__)


def add_items_to_cart(page: Page, urls: list[str], max_price: float = None) -> int:
    product = ProductPage(page)
    added = 0

    for i, url in enumerate(urls, 1):
        logger.debug("Processing item %d/%d: %s", i, len(urls), url)
        product.open(url)
        if not product.is_available():
            logger.debug("Item %d not available – skipping", i)
            continue
        if not product.add_to_cart_with_random_variants(max_price=max_price):
            logger.debug("Item %d skipped (price exceeds limit or add failed)", i)
            continue
        added += 1
        logger.info("Item %d added to cart (total so far: %d)", i, added)
        allure.attach(page.screenshot(), name=f"item_{added}_added_to_cart", attachment_type=allure.attachment_type.PNG)

    logger.info("Finished: %d/%d items added to cart", added, len(urls))
    return added
