import pytest
from playwright.sync_api import sync_playwright
from utils.logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def logger():
    return setup_logger()


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
