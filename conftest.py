import pytest
from playwright.sync_api import Page

BASE_URL = 'https://tvolearn.com/'


@pytest.fixture()
def open_start_page(page: Page) -> None:
    page.goto(BASE_URL)
