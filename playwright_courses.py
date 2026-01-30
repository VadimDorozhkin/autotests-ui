from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='chrome-state.json')

    page.wait_for_timeout(5000)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='chrome-state.json')
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    text_Courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(text_Courses).to_be_visible()
    expect(text_Courses).to_have_text('Courses')

    text_Result = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_Result).to_be_visible()
    expect(text_Result).to_have_text('There is no results')

    icon_view = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_view).to_be_visible()

    text_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(text_description).to_be_visible()
    expect(text_description).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)











