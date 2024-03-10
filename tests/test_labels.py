import allure
from allure_commons.types import Severity
from selene import browser, by, have


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Issues в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    with allure.step("Открываем главную страницу"):
        browser.open('/')

    with allure.step("Ищем репозиторий"):
        browser.element('.search-input-container').click()
        browser.element('#query-builder-test').send_keys('LightGleb/qa_guru_hw_9').press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("LightGleb/qa_guru_hw_9")).click()

    with allure.step("Открываем таб Issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем наличие Issue с именем Test1"):
        browser.element('#issue_1_link').should(have.text('Test1'))


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Clight")
@allure.feature("Issues в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
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
