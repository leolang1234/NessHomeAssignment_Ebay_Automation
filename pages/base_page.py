import logging
import os
from datetime import datetime
from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(type(self).__name__)

    def navigate(self, url: str) -> None:
        self.logger.debug("Navigating to: %s", url)
        self.page.goto(url)

    def click(self, locator: Locator) -> None:
        self.logger.debug("Clicking: %s", locator)
        locator.click()

    def fill(self, locator: Locator, text: str) -> None:
        self.logger.debug("Filling element with: %s", text)
        locator.fill(text)

    def get_text(self, locator: Locator, timeout: int = 5000) -> str:
        return locator.inner_text(timeout=timeout)

    def wait_for_element(self, locator: Locator, state: str = "visible", timeout: int = 10000) -> None:
        self.logger.debug("Waiting for element (state=%s)", state)
        locator.wait_for(state=state, timeout=timeout)

    def take_screenshot(self, path: str) -> None:
        """Save a screenshot to an explicit path."""
        dir_part = os.path.dirname(path)
        if dir_part:
            os.makedirs(dir_part, exist_ok=True)
        self.logger.debug("Screenshot saved: %s", path)
        self.page.screenshot(path=path)

    def get_screenshot(self, name: str = "", output_dir: str = "reports/screenshots") -> str:
        """Save a timestamped screenshot and return its path."""
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png" if name else f"screenshot_{timestamp}.png"
        path = os.path.join(output_dir, filename)
        self.logger.info("Screenshot saved: %s", path)
        self.page.screenshot(path=path)
        return path
