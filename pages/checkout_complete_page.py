"""Page object for the checkout complete / confirmation page."""


class CheckoutCompletePage:
    """Represents the final confirmation page after finishing checkout."""

    def __init__(self, page):
        self.page = page
        self.complete_header = page.locator('.complete-header')
        self.complete_text = page.locator('.complete-text')
        self.back_home = page.locator('#back-to-products')

    def get_header_text(self) -> str:
        """Return the confirmation header text on the completion page."""
        return self.complete_header.text_content()

    def get_complete_text(self) -> str:
        """Return the completion message/body text on the completion page."""
        return self.complete_text.text_content()

    def back_to_products(self):
        """Click the control that returns the user back to the products page."""
        self.back_home.click()
