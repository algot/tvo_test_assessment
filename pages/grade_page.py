from playwright.sync_api import Page, Locator, expect
from pages.main_page import MainPage


class GradePage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)

    def click_subject_card(self, subject_name: str) -> None:
        self._get_subject_locator(subject_name).click()

    def assert_breadcrumb(self, expected_text: str) -> None:
        expect(self._get_breadcrumb_current_element()).to_have_text(expected_text)

    def assert_grade_header(self, expected_grade: str) -> None:
        expect(self._get_grade_header()).to_have_text(expected_grade)

    def assert_subject(self, expected_subject: str) -> None:
        expect(self._get_subject()).to_have_text(expected_subject)

    def _get_subject_locator(self, subject_name: str) -> Locator:
        return self.page.locator('div.button-subject').get_by_text(subject_name)

    def _get_breadcrumb_current_element(self) -> Locator:
        return self.page.locator('ol.cd-breadcrumb li.current')

    def _get_subject_banner_div(self) -> Locator:
        return self.page.locator('div.subject-banner')

    def _get_grade_header(self) -> Locator:
        return self._get_subject_banner_div().locator('div h1')

    def _get_subject(self) -> Locator:
        return self._get_subject_banner_div().locator('div h2')
