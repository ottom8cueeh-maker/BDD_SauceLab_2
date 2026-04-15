"""Page object for the checkout step one (your information) page."""


class CheckoutStepOnePage:
    """Represents the first checkout form (name / postal code)."""

    def __init__(self, page):
        self.page = page
        self.first_name = page.locator('#first-name')
        self.last_name = page.locator('#last-name')
        self.postal_code = page.locator('#postal-code')
        self.continue_button = page.locator('#continue')
        self.cancel_button = page.locator('#cancel')

    def fill_information(self, first: str, last: str, postal: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def continue_checkout(self):
        self.continue_button.click()
