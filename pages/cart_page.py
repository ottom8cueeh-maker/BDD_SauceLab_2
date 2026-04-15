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
        self.remove_buttons.nth(index).click()

    def get_cart_items_count(self) -> int:
        return self.cart_items.count()

    def proceed_to_checkout(self):
        self.checkout_button.click()
