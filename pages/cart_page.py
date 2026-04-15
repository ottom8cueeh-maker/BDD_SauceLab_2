"""Page object for the shopping cart page."""


class CartPage:
    """Simple cart page object: inspect items, remove items, checkout."""

    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator('.cart_item')
        self.item_names = page.locator('.inventory_item_name')
        self.remove_buttons = page.locator('button.cart_button')
        self.checkout_button = page.locator('#checkout')
        self.continue_shopping = page.locator('#continue-shopping')

    def remove_item_by_index(self, index: int = 0):
        """Remove the cart item at `index` by clicking its remove button."""
        self.remove_buttons.nth(index).click()

    def get_cart_items_count(self) -> int:
        """Return the number of items currently listed in the cart."""
        return self.cart_items.count()

    def proceed_to_checkout(self):
        """Click the checkout button to begin the checkout flow."""
        self.checkout_button.click()
