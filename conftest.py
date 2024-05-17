import pytest
from playwright.sync_api import Page

from pages.grade_page import GradePage

BASE_URL = 'https://tvolearn.com/'


@pytest.fixture()
def open_start_page(page: Page) -> None:
    page.goto(BASE_URL)


@pytest.fixture()
def grade_page(page: Page) -> GradePage:
    return GradePage(page)
