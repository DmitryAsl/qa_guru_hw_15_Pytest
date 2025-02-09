import pytest
from selenium import webdriver
from selene import browser
#
@pytest.fixture(params=[(1920, 1080), (1366, 768), (390, 844), (360 ,800)], ids=['Full HD', 'HD', 'iPhone 13/14/15', 'Samsung Galaxy S21'])
def browser_config(request):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument("--no-sandbox")
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()

@pytest.fixture(params=[(390, 844), (360 ,800)], ids=['iPhone 13/14/15', 'Samsung Galaxy S21'])
def browser_config_mobile(request):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument("--no-sandbox")
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()

@pytest.fixture(params=[(1920, 1080), (1366, 768)], ids=['Full HD', 'HD'])
def browser_config_desktop(request):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument("--no-sandbox")
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.config.base_url = 'https://github.com'

    yield

    browser.quit()
