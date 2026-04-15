"""Page object for the inventory item (product details) page."""


class InventoryItemPage:
    """Page object for a single product detail view.

    Typical locators and interactions: read name/description, add/remove
    from cart and navigate back to products.
    """

    def __init__(self, page):
        self.page = page
        self.name = page.locator('.inventory_details_name')
        self.description = page.locator('.inventory_details_desc')
        self.price = page.locator('.inventory_details_price')
        self.add_button = page.locator('button.btn_inventory')
        self.back_button = page.locator('button.inventory_details_back_button')

    def add_to_cart(self):
        """Click the add-to-cart button on the product detail page."""
        self.add_button.click()

    def remove_from_cart(self):
        """Click the remove-from-cart button on the product detail page."""
        self.add_button.click()

    def back_to_products(self):
        """Return to the inventory/product listing by clicking back."""
        self.back_button.click()

    def get_name(self) -> str:
        """Return the product name text from the details view."""
        return self.name.text_content()

    def get_description(self) -> str:
        """Return the product description text from the details view."""
        return self.description.text_content()
