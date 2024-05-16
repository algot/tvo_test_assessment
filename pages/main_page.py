from playwright.sync_api import Page, Locator, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def select_grade(self, grade_name: str) -> None:
        self.dropdown_learning_resources.click()
        self._get_grade_locator(grade_name).click()

    def assert_title(self, expected_title: str) -> None:
        expect(self.page).to_have_title(expected_title)

    @property
    def dropdown_learning_resources(self) -> Locator:
        return self.page.get_by_role('button', name='Learning Resources (K-12)')

    def _get_grade_locator(self, grade_name: str) -> Locator:
        return self.page.get_by_role('link', name=grade_name, exact=True)
