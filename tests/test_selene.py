from selene import browser, by, have


def test_check_name_issue():
    browser.open('/')
    # WHEN
    browser.element('.search-input-container').click()
    browser.element('#query-builder-test').send_keys('LightGleb/qa_guru_hw_9').press_enter()
    browser.element(by.link_text("LightGleb/qa_guru_hw_9")).click()
    browser.element('#issues-tab').click()
    # THEN
    browser.element('#issue_1_link').should(have.text('Test1'))
