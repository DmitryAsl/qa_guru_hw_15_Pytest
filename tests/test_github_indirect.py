import pytest
from selene import browser, be, have

web_only = pytest.mark.parametrize('browser_config', [(1920, 1080), (1366, 768)], indirect=True, ids=['Full HD', 'HD'])
mobile_only = pytest.mark.parametrize('browser_config', [(390, 844), (360, 800)], indirect=True,
                                      ids=['iPhone 13/14/15', 'Samsung Galaxy S21'])

text_sign_in = 'Sign in to GitHub'


@web_only
def test_open_auth_desktop_with_indirect(browser_config):
    browser.open('/')
    browser.element('[class*="HeaderMenu-link--sign-in HeaderMenu-button"]').should(be.visible).click()
    browser.element('[class*="auth-form-header"]').should(have.text(text_sign_in))


@mobile_only
def test_open_auth_mobile_with_indirect(browser_config):
    browser.open('/')
    browser.element('[class*="HeaderMenu-link HeaderMenu-button"]').should(be.visible).click()
    browser.element('[class*="auth-form-header"]').should(have.text(text_sign_in))
