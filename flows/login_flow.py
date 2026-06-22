import logging
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def login_and_verify(page: Page, username: str, password: str) -> None:
    logger.info("Logging in as %s", username)
    login = LoginPage(page)
    login.open()
    login.login(username, password)

    assert login.is_logged_in(), "Login failed: user greeting not found after sign-in"
    logger.info("Login successful")

    allure.attach(
        page.screenshot(),
        name="login_success",
        attachment_type=allure.attachment_type.PNG,
    )
