import logging
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

logger = logging.getLogger(__name__)


def search_items_by_name_under_price(page: Page, query: str, max_price: float, limit: int = 5) -> list[str]:
    logger.info("Searching for '%s' (max price: $%.2f, limit: %d)", query, max_price, limit)
    home = HomePage(page)
    home.open()
    home.set_ship_to_us()
    home.search(query)

    results = SearchResultsPage(page)
    results.filter_max_price(max_price)
    urls = results.get_item_urls(limit)
    logger.info("Found %d item URLs", len(urls))
    return urls
