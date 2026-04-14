import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(page, base_url):
    login = LoginPage(page, base_url)
    login.goto()
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    inventory = InventoryPage(page)
    assert inventory.is_on_inventory_page()
    assert inventory.is_menu_visible()


def test_failed_login_invalid_password(page, base_url):
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
