import allure


@allure.title("тестируем issue на github")
@allure.suite('issue #1')
@allure.sub_suite('5')
@allure.link("https://github.com")
@allure.epic("Супер эпик")
@allure.severity("Высокий")
@allure.parent_suite("parent-suite")
@allure.manual()
@allure.tag("web")
@allure.description("Тестирование")
@allure.description_html("<h1>Тестирование в html формате</h1>")
@allure.feature("Супер фича")
@allure.id(15)
@allure.issue("#55")
@allure.label("owner", "Глеб")
def test_dynamic_labels():
    pass
