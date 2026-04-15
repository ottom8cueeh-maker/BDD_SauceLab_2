"""Page object for the checkout overview / step two page."""


class CheckoutStepTwoPage:
    """Order overview: review items and finish checkout."""

    def __init__(self, page):
        self.page = page
        self.summary_info = page.locator('.summary_info')
        self.finish_button = page.locator('#finish')
        self.cancel_button = page.locator('#cancel')

    def finish(self):
        """Finish the checkout and submit the order."""
        self.finish_button.click()

    def get_summary_text(self) -> str:
        """Return the order summary text shown on the overview page."""
        return self.summary_info.text_content()
