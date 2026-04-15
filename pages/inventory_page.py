"""Page objects for inventory-related UI on Sauce Demo.

This module exposes `InventoryPage`, a thin page-object wrapper around
Playwright's `page` scoped to the post-login inventory view.
"""


class InventoryPage:
    """Page object for the inventory (post-login) page on Sauce Demo.

    Args:
        page: Playwright `Page` instance (from pytest-playwright fixture).
    """

    def __init__(self, page):
        self.page = page
        # left-side main menu button (hamburger)
        self.menu_button = page.locator('#react-burger-menu-btn')
        # inventory container/list
        self.inventory_container = page.locator('.inventory_list')
        # product elements
        self.product_items = page.locator('.inventory_item')
        self.product_names = page.locator('.inventory_item_name')
        self.add_buttons = page.locator('button.btn_inventory')
        # cart link / badge
        self.cart_link = page.locator('.shopping_cart_link')
        self.cart_badge = page.locator('.shopping_cart_badge')

    def is_menu_visible(self) -> bool:
        """Return True if the left-side menu button is visible."""
        return self.menu_button.is_visible()

    def is_on_inventory_page(self) -> bool:
        """Check whether the current URL is the inventory page."""
        return "/inventory.html" in self.page.url

    def open_menu(self):
        """Open the left-side menu by clicking the hamburger button."""
        self.menu_button.click()

    def add_product_to_cart_by_index(self, index: int = 0):
        """Click the add-to-cart button for the product at `index`.

        Index is zero-based and will raise if out-of-range.
        """
        self.add_buttons.nth(index).click()

    def go_to_cart(self):
        """Navigate to the cart page by clicking the cart link."""
        self.cart_link.click()

    def get_cart_count(self) -> int:
        """Return the numeric cart badge count (0 if not present)."""
        if not self.cart_badge.count():
            return 0
        text = self.cart_badge.text_content() or "0"
        try:
            return int(text.strip())
        except ValueError:
            return 0

    def open_product_by_index(self, index: int = 0):
        """Open the product details page for the product at `index`."""
        self.product_names.nth(index).click()
