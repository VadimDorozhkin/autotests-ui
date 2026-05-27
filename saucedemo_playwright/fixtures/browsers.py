import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

@pytest.fixture(scope="function")
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    yield browser.new_page()
