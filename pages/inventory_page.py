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

    def is_menu_visible(self) -> bool:
        """Return True if the left-side menu button is visible."""
        return self.menu_button.is_visible()

    def is_on_inventory_page(self) -> bool:
        """Check whether the current URL is the inventory page."""
        return "/inventory.html" in self.page.url

    def open_menu(self):
        """Open the left-side menu by clicking the hamburger button."""
        self.menu_button.click()
