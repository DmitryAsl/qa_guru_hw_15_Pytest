from selene import browser, be, have

text_sign_in = 'Sign in to GitHub'


def test_open_auth_desktop(browser_config_desktop):
    browser.open('/')
    browser.element('[class*="HeaderMenu-link--sign-in HeaderMenu-button"]').should(be.visible).click()
    browser.element('[class*="auth-form-header"]').should(have.text(text_sign_in))


def test_open_auth_mobile(browser_config_mobile):
    browser.open('/')
    browser.element('[class*="HeaderMenu-link HeaderMenu-button"]').should(be.visible).click()
    browser.element('[class*="auth-form-header"]').should(have.text(text_sign_in))
