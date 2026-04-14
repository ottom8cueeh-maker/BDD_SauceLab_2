"""Page objects for the Sauce Demo login view.

This module provides `LoginPage`, a small page-object wrapper around
Playwright's `page` scoped to the login screen. It encapsulates common
interactions used by tests (navigating to the page, filling credentials,
and reading error messages).
"""


class LoginPage:
    """Page object for the Sauce Demo login page.

    Args:
        page: Playwright `Page` instance (from pytest-playwright fixture).
        base_url: Base URL for the application under test (from fixture).
    """

    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error = page.locator('[data-test="error"]')

    def goto(self):
        """Navigate the browser to the login page (base_url)."""
        self.page.goto(self.base_url)

    def login(self, username: str, password: str):
        """Fill username/password and submit the login form."""
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def click_login(self):
        """Click the login button without changing input fields."""
        self.login_button.click()

    def get_error_text(self):
        """Return the text content of the error message element (or None)."""
        return self.error.text_content()

    def is_error_visible(self) -> bool:
        """Return True if an error message element is visible on the page."""
        return self.error.is_visible()
