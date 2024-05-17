import pytest
from playwright.sync_api import Page

from pages.grade_page import GradePage


@pytest.mark.parametrize('email', ['abc', 'abc@.com', 'aaa.aaa.aa'])
def test_user_cannot_provide_wrong_email(page: Page, open_start_page, email):
    grade_page = GradePage(page)
    grade_page.select_grade('Grade 3')
    grade_page.click_subject_card('The Arts')

    grade_page.fill_email_field(email)
    grade_page.click_subscribe_button()
    grade_page.assert_inline_error_message('Please enter a valid email address.')


def test_user_cannot_provide_fake_email(page: Page, open_start_page):
    grade_page = GradePage(page)
    grade_page.select_grade('Grade 6')
    grade_page.click_subject_card('Social Studies')

    grade_page.fill_email_field('test123@mailinator.com')
    grade_page.click_subscribe_button()
    grade_page.assert_inline_error_message('This email address looks fake or invalid. Please enter a real email address.')


def test_user_successfully_subscribed(page: Page, open_start_page):
    grade_page = GradePage(page)
    grade_page.select_grade('Grade 6')
    grade_page.click_subject_card('Social Studies')

    # TODO verify that user with correct email can subscribe and check against database that user appears in the backend
