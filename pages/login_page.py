from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.signin_url = "https://www.ebay.com/signin/"

        self.selectors = {
            "email_input": "#userid",
            "continue_button": "#signin-continue-btn",
            "password_input": "#pass",
            "sign_in_button": "#sgnBt",
            "user_greeting": ".gh-identity",
        }

        self.email_input: Locator = self.page.locator(self.selectors["email_input"])
        self.continue_button: Locator = self.page.locator(self.selectors["continue_button"])
        self.password_input: Locator = self.page.locator(self.selectors["password_input"])
        self.sign_in_button: Locator = self.page.locator(self.selectors["sign_in_button"])
        self.user_greeting: Locator = self.page.locator(self.selectors["user_greeting"])

    def open(self) -> None:
        self.logger.debug("Navigating to sign-in page")
        self.page.goto(self.signin_url)

    def login(self, username: str, password: str) -> None:
        self.logger.debug("Filling credentials for %s", username)
        self.email_input.click()
        self.email_input.fill(username)
        self.page.wait_for_timeout(500)
        self.continue_button.click()
        self.password_input.wait_for(state="visible")

        self.password_input.fill(password)
        self.sign_in_button.click()

        # Wait until we've left the sign-in domain
        self.page.wait_for_url(lambda url: "signin.ebay.com" not in url, timeout=30000)

        # eBay may redirect to a passkey registration page after login; skip it
        if "authn-register" in self.page.url:
            self.logger.debug("Passkey registration page detected – skipping to home")
            self.page.goto("https://www.ebay.com")
            self.page.wait_for_load_state("domcontentloaded")

    def is_logged_in(self) -> bool:
        try:
            self.user_greeting.wait_for(timeout=5000)
            text = self.user_greeting.inner_text(timeout=3000)
            result = text.startswith("Hi ")
            self.logger.debug("Login check: %s", "passed" if result else "failed")
            return result
        except Exception:
            self.logger.debug("Login check: greeting element not found")
            return False

