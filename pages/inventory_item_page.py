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
        # The same button is used for both 'Add to cart' and 'Remove' states.
        # Use `toggle_button` and inspect its text to decide current state.
        self.toggle_button = page.locator('button.btn_inventory')
        self.back_button = page.locator('button.inventory_details_back_button')

    def is_in_cart(self) -> bool:
        """Return True if the product is currently in the cart.

        The product detail view uses the same button for adding and removing;
        when its visible text contains "Remove" we treat the item as in-cart.
        """
        text = (self.toggle_button.text_content() or "").strip().lower()
        return "remove" in text

    def add_to_cart(self):
        """Add the product to the cart if it is not already added.

        If the item is already in the cart this is a no-op.
        """
        if not self.is_in_cart():
            self.toggle_button.click()

    def remove_from_cart(self):
        """Remove the product from the cart if it is currently added.

        If the item is not in the cart this is a no-op.
        """
        if self.is_in_cart():
            self.toggle_button.click()

    def back_to_products(self):
        """Return to the inventory/product listing by clicking back."""
        self.back_button.click()

    def get_name(self) -> str:
        """Return the product name text from the details view."""
        return self.name.text_content()

    def get_description(self) -> str:
        """Return the product description text from the details view."""
        return self.description.text_content()
