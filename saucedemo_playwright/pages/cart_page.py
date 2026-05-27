from playwright.sync_api import Page, expect
from saucedemo_playwright.pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def check_item_in_cart(self, item_name: str):
        expect(self.cart_items.filter(has_text=item_name)).to_be_visible()

    def click_checkout(self):
        self.checkout_button.click()
