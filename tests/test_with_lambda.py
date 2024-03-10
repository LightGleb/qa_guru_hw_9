import allure
from selene import browser, have, by


def test_dynamic_steps():
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
