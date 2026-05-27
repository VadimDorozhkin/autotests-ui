import pytest
from saucedemo_playwright.pages.login_page import LoginPage
from saucedemo_playwright.pages.inventory_page import InventoryPage
from saucedemo_playwright.pages.cart_page import CartPage
from saucedemo_playwright.pages.checkout_page import CheckoutPage

@pytest.mark.regression
@pytest.mark.smoke
def test_successful_purchase_flow(login_page: LoginPage, inventory_page: InventoryPage, cart_page: CartPage, checkout_page: CheckoutPage):
    login_page.visit("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.check_page_title("Products")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.check_cart_badge_value("1")
    
    inventory_page.go_to_cart()
    cart_page.check_item_in_cart("Sauce Labs Backpack")
    cart_page.click_checkout()
    
    checkout_page.fill_checkout_info("Ivan", "Petrov", "123456")
    checkout_page.click_continue()
    
    checkout_page.check_summary_details("Total: $32.39")
    checkout_page.click_finish()
    
    checkout_page.check_order_completed()


@pytest.mark.regression
@pytest.mark.auth
def test_locked_out_user_login(login_page: LoginPage):
    login_page.visit("https://www.saucedemo.com/")
    login_page.login("locked_out_user", "secret_sauce")
    login_page.check_error_message("Epic sadface: Sorry, this user has been locked out.")


@pytest.mark.regression
@pytest.mark.cart
def test_cart_persistence_after_relogin(login_page: LoginPage, inventory_page: InventoryPage):
    login_page.visit("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.check_cart_badge_value("1")
    
    inventory_page.logout()
    
    login_page.login("standard_user", "secret_sauce")
    inventory_page.check_cart_badge_value("1")


@pytest.mark.regression
@pytest.mark.checkout
@pytest.mark.parametrize("first_name, last_name, postal_code, expected_error", [
    ("", "Petrov", "123456", "Error: First Name is required"),
    ("Ivan", "", "123456", "Error: Last Name is required"),
    ("Ivan", "Petrov", "", "Error: Postal Code is required")
], ids=["empty_firstname", "empty_lastname", "empty_zip"])
def test_checkout_fields_validation(login_page: LoginPage, inventory_page: InventoryPage, cart_page: CartPage, checkout_page: CheckoutPage, first_name, last_name, postal_code, expected_error):
    login_page.visit("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    cart_page.click_checkout()
    
    checkout_page.fill_checkout_info(first_name, last_name, postal_code)
    checkout_page.click_continue()
    
    checkout_page.check_validation_error(expected_error)


@pytest.mark.regression
@pytest.mark.inventory
@pytest.mark.parametrize("sort_value, first_product_name, first_product_price", [
    ("lohi", "Sauce Labs Onesie", "$7.99"),
    ("hilo", "Sauce Labs Fleece Jacket", "$49.99")
], ids=["sort_low_to_high", "sort_high_to_low"])
def test_product_sorting(login_page: LoginPage, inventory_page: InventoryPage, sort_value, first_product_name, first_product_price):
    login_page.visit("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.change_sort_order(sort_value)
    name, price = inventory_page.get_first_product_name_and_price()
    
    assert name == first_product_name, f"Expected {first_product_name}, but got {name}"
    assert price == first_product_price, f"Expected {first_product_price}, but got {price}"
