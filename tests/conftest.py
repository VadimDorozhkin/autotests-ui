import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright, context) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context.storage_state(path='browser-state.json')

@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)




