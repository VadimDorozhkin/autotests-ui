import pytest
from playwright.sync_api import sync_playwright, Page, expect
from pages.login_page import LoginPage


test_data = [("user.name@gmail.com", "password"),
             ("user.name@gmail.com", "  "),
             ("  ", "password")
             ]
@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password', test_data, ids=lambda data: f'email={data}, password={data}')
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):

    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()


