import allure
from selene import browser, have, by


def test_decorator_steps():
    open_main_page()
    search_for_repository('LightGleb/qa_guru_hw_9')
    go_to_repository('LightGleb/qa_guru_hw_9')
    open_issue_tab()
    should_see_issue_name('Test1')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('/')


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверяем имя {name} Issue")
def should_see_issue_name(name):
    browser.element('#issue_1_link').should(have.text(name))
