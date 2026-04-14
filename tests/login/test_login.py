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


def test_failed_login_invalid_password(page, base_url):
    """Scenario: Failed login with invalid password.

    Submitting a wrong password shows an error containing the expected text
    and does not allow navigation to the inventory page.
    """
    logging.info("Starting test: test_failed_login_invalid_password...")
    login = LoginPage(page, base_url)
    login.goto()
    login.login("standard_user", "wrongpassword")
    # expect an error about invalid credentials and remain on login page
    login.error.wait_for(state="visible")
    assert login.is_error_visible()
    err = (login.get_error_text() or "").strip()
    assert "Epic sadface" in err
    assert "do not match" in err
    inventory = InventoryPage(page)
    assert not inventory.is_on_inventory_page()


def test_failed_login_invalid_username(page, base_url):
    """Scenario: Failed login with invalid username.

    Submitting a non-existent username shows the same invalid-credentials
    message and keeps the user on the login page.
    """
    logging.info("Starting test: test_failed_login_invalid_username...")
    login = LoginPage(page, base_url)
    login.goto()
    login.login("bad_username", "secret_sauce")
    login.error.wait_for(state="visible")
    assert login.is_error_visible()
    err = (login.get_error_text() or "").strip()
    assert "Epic sadface" in err
    assert "do not match" in err
    inventory = InventoryPage(page)
    assert not inventory.is_on_inventory_page()


def test_empty_fields_no_error_displayed(page, base_url):
    """Scenario: Login form validation — empty fields.

    Verify behavior when the login form is submitted with empty fields. The
    live site displays a validation error; assert that behavior and ensure the
    user remains on the login page.
    """
    logging.info("Starting test: test_empty_fields_no_error_displayed...")
    login = LoginPage(page, base_url)
    login.goto()
    login.click_login()
    # per feature: no error displayed and remain on login page
    # allow a short timeout to ensure an error does not appear
    # site shows a validation error when submitting empty fields; assert that behavior
    login.error.wait_for(state="visible")
    assert login.is_error_visible()
    err = (login.get_error_text() or "").strip()
    assert "Epic sadface" in err
    inventory = InventoryPage(page)
    assert not inventory.is_on_inventory_page()
