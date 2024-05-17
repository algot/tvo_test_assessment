import pytest

from playwright.sync_api import Page, expect

from pages.grade_page import GradePage
from pages.main_page import MainPage

TITLE_SUFFIX = ' | TVO Learn'


@pytest.mark.parametrize('grade,subject', [('Grade 1', 'Mathematics'),
                                           ('Grade 5', 'Social Studies')])
def test_grade_subject_navigation(page: Page, open_start_page, grade: str, subject: str):
    main_page = MainPage(page)

    main_page.select_grade(grade)
    main_page.assert_title(f'{grade}{TITLE_SUFFIX}')

    grade_page = GradePage(page)

    grade_page.click_subject_card(subject)
    grade_page.assert_title(f'{grade} - {subject}{TITLE_SUFFIX}')
    grade_page.assert_breadcrumb(subject)
    grade_page.assert_grade_header(grade)
    grade_page.assert_subject(subject)


def test_jumplinks_displayed_on_grade_page(open_start_page, grade_page: GradePage):
    grade_page.select_grade('Grade 2')
    grade_page.click_subject_card('Mathematics')

    locator_jumplinks = grade_page.page.locator('.jumplinks ul>li')

    expected_jumplinks_text = ['Learning Activities',
                               'Resources for Learning',
                               'Apply the Learning',
                               'Vocabulary']
    expected_jumplinks_href = ['#jumpto-lesson-packs',
                               '#jumpto-resources',
                               '#jumpto-activities',
                               '#jumpto-vocabulary']

    expect(locator_jumplinks).to_have_count(len(expected_jumplinks_text))

    for i, locator in enumerate(locator_jumplinks.all()):
        expect(locator).to_have_text(expected_jumplinks_text[i])
        expect(locator.locator('a')).to_have_attribute('href', expected_jumplinks_href[i])
