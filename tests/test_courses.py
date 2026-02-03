import pytest
from playwright.sync_api import sync_playwright, expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = chromium_page_with_state.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')

        username_input = chromium_page_with_state.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = chromium_page_with_state.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        registration_button = chromium_page_with_state.get_by_test_id('registration-page-registration-button')
        registration_button.click()


        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        text_Courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(text_Courses).to_be_visible()
        expect(text_Courses).to_have_text('Courses')

        text_Result = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(text_Result).to_be_visible()
        expect(text_Result).to_have_text('There is no results')

        icon_view = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_view).to_be_visible()

        text_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(text_description).to_be_visible()
        expect(text_description).to_have_text('Results from the load test pipeline will be displayed here')

        chromium_page_with_state.wait_for_timeout(5000)