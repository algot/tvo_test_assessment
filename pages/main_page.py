from playwright.sync_api import Page, Locator, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def select_grade(self, grade_name: str) -> None:
        self._dropdown_learning_resources_locator().click()
        self._get_grade_locator(grade_name).click()

    def assert_title(self, expected_title: str) -> None:
        expect(self.page).to_have_title(expected_title)

    def fill_email_field(self, email_address: str) -> None:
        self._get_email_field_locator().fill(email_address)

    def click_subscribe_button(self) -> None:
        self._get_subscribe_button().click()

    def assert_inline_error_message(self, expected_error_message: str) -> None:
        expect(self._get_inline_error_locator()).to_have_text(expected_error_message)

    def _dropdown_learning_resources_locator(self) -> Locator:
        return self.page.get_by_role('button', name='Learning Resources (K-12)')

    def _get_grade_locator(self, grade_name: str) -> Locator:
        return self.page.get_by_role('link', name=grade_name, exact=True)

    def _get_email_field_locator(self) -> Locator:
        return self.page.locator('#mce-EMAIL')

    def _get_inline_error_locator(self) -> Locator:
        return self.page.locator('div.mce_inline_error')

    def _get_subscribe_button(self) -> Locator:
        return self.page.get_by_role('button', name='Subscribe')
