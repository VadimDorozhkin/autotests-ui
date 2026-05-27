from playwright.sync_api import Page, expect
from saucedemo_playwright.pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page_title = page.locator(".title")
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.sort_select = page.locator(".product_sort_container")
        self.burger_menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")
        self.inventory_items = page.locator(".inventory_item")

    def check_page_title(self, expected_title: str = "Products"):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text(expected_title)

    def add_product_to_cart(self, product_name: str):
        item = self.inventory_items.filter(has_text=product_name)
        add_btn = item.locator("button:has-text('Add to cart')")
        add_btn.click()

    def remove_product_from_cart(self, product_name: str):
        item = self.inventory_items.filter(has_text=product_name)
        remove_btn = item.locator("button:has-text('Remove')")
        remove_btn.click()

    def check_cart_badge_value(self, expected_value: str):
        expect(self.shopping_cart_badge).to_have_text(expected_value)

    def check_cart_badge_empty(self):
        expect(self.shopping_cart_badge).not_to_be_visible()

    def go_to_cart(self):
        self.shopping_cart_link.click()

    def change_sort_order(self, sort_value: str):
        self.sort_select.select_option(value=sort_value)

    def get_first_product_name_and_price(self):
        first_item = self.inventory_items.first
        name = first_item.locator(".inventory_item_name").inner_text()
        price_str = first_item.locator(".inventory_item_price").inner_text()
        return name, price_str

    def logout(self):
        self.burger_menu_button.click()
        self.logout_link.wait_for(state="visible")
        self.logout_link.click()
