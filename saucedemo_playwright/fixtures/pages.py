import pytest
from playwright.sync_api import Page

from saucedemo_playwright.pages.login_page import LoginPage
from saucedemo_playwright.pages.inventory_page import InventoryPage
from saucedemo_playwright.pages.cart_page import CartPage
from saucedemo_playwright.pages.checkout_page import CheckoutPage

@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)

@pytest.fixture
def inventory_page(chromium_page: Page) -> InventoryPage:
    return InventoryPage(page=chromium_page)

@pytest.fixture
def cart_page(chromium_page: Page) -> CartPage:
    return CartPage(page=chromium_page)

@pytest.fixture
def checkout_page(chromium_page: Page) -> CheckoutPage:
    return CheckoutPage(page=chromium_page)
