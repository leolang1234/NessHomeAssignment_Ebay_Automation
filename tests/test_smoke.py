from utils.data_utils import load_test_data
from flows.login_flow import login_and_verify
from flows.search_flow import search_items_by_name_under_price
from flows.add_to_cart_flow import add_items_to_cart
from flows.cart_flow import assert_cart_total_not_exceeds
from pages.cart_page import CartPage


def test_smoke(page):
    data = load_test_data()

    login_and_verify(page, username=data["user_name"], password=data["password"])

    CartPage(page).clear()

    urls = search_items_by_name_under_price(
        page=page,
        query=data["query"],
        max_price=data["max_price"],
        limit=data["limit"],
    )

    added_count = add_items_to_cart(page, urls, max_price=data["max_price"])

    assert_cart_total_not_exceeds(
        page=page,
        budget_per_item=data["max_price"],
        items_count=added_count,
    )
