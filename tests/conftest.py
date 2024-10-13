import pytest
from selene import browser
from selenium.webdriver import FirefoxOptions


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_name = 'firefox'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 7.0
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.timeouts = {'pageLoad': 3000}
    options.page_load_strategy = 'none'
    browser.config.driver_options = options

    yield

    browser.quit()