import pytest
from playwright.sync_api import sync_playwright
from utils.logger import setup_logger


def pytest_addoption(parser):
    parser.addoption("--username", action="store", required=True, help="eBay login email")
    parser.addoption("--password", action="store", required=True, help="eBay login password")


@pytest.fixture(scope="session", autouse=True)
def logger():
    return setup_logger()


@pytest.fixture(scope="session")
def username(request):
    value = request.config.getoption("--username")
    if not value or not value.strip():
        pytest.exit("--username must be provided and cannot be empty", returncode=1)
    return value


@pytest.fixture(scope="session")
def password(request):
    value = request.config.getoption("--password")
    if not value or not value.strip():
        pytest.exit("--password must be provided and cannot be empty", returncode=1)
    return value


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
