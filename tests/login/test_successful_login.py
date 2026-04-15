"""End-to-end login tests for Sauce Demo.

These tests implement the scenarios described in `features/login.feature` and
exercise the login flow using Playwright's `page` fixture and simple page
objects (`LoginPage`, `InventoryPage`).
"""
import logging
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(page, base_url):
    """Scenario: Successful login with valid credentials.

    Verifies that a standard user can log in and reach the inventory page where
    the main menu is visible.
    """
    logging.info("Starting test: test_successful_login...")

    login = LoginPage(page, base_url)
    login.goto()
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    inventory = InventoryPage(page)
    assert inventory.is_on_inventory_page()
    assert inventory.is_menu_visible()
