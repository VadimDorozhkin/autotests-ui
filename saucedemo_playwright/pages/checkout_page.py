from playwright.sync_api import Page, expect
from saucedemo_playwright.pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.error_container = page.locator(".error-message-container")

        self.finish_button = page.locator("#finish")
        self.payment_info = page.locator(".summary_value_label").first
        self.total_label = page.locator(".summary_total_label")

        self.complete_header = page.locator(".complete-header")
        self.back_home_button = page.locator("#back-to-products")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        if first_name:
            self.first_name_input.fill(first_name)
        if last_name:
            self.last_name_input.fill(last_name)
        if postal_code:
            self.postal_code_input.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()

    def check_validation_error(self, expected_text: str):
        expect(self.error_container).to_be_visible()
        expect(self.error_container).to_contain_text(expected_text)

    def check_summary_details(self, expected_total: str):
        expect(self.total_label).to_contain_text(expected_total)

    def click_finish(self):
        self.finish_button.click()

    def check_order_completed(self, expected_msg: str = "Thank you for your order!"):
        expect(self.complete_header).to_be_visible()
        expect(self.complete_header).to_have_text(expected_msg)
