import pytest
from selene import browser, be, have

text_sign_in = 'Sign in to GitHub'


def test_open_auth_desktop(browser_config):
    if browser.config.window_width < browser.config.window_height:
        pytest.skip(reason='Для мобильной версии отдельный тест')

    browser.open('/')
    browser.element('[class*="HeaderMenu-link--sign-in HeaderMenu-button"]').should(be.visible).click()
    browser.element('[class*="auth-form-header"]').should(have.text(text_sign_in))


def test_open_auth_mobile(browser_config):
    if browser.config.window_width > browser.config.window_height:
        pytest.skip(reason='Для мобильной версии отдельный тест')

    browser.open('/')
    browser.element('[class*="HeaderMenu-link HeaderMenu-button"]').should(be.visible).click()
    browser.element('[class*="auth-form-header"]').should(have.text(text_sign_in))
