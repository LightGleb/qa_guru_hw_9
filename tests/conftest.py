import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()
