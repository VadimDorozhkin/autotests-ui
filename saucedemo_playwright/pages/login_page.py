from playwright.sync_api import Page, expect
from saucedemo_playwright.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_container = page.locator(".error-message-container")

    def fill_login_form(self, username: str, password: str):
        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)
        
        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.fill_login_form(username, password)
        self.click_login_button()

    def check_error_message(self, expected_text: str):
        expect(self.error_container).to_be_visible()
        expect(self.error_container).to_contain_text(expected_text)
