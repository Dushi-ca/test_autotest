from locators import LoginPageLocators
from config import URL, CREDENTIALS
import pytest
from main_actions import MainActions

@pytest.mark.parametrize("username, password", CREDENTIALS)
def test_auth(browser, username, password):

    actions = MainActions(browser, base_url=URL)
    browser.get(actions._base_url)

    actions.enter_text_to_field(LoginPageLocators.USERNAME_INPUT, username)
    actions.enter_text_to_field(LoginPageLocators.PASSWORD_INPUT, password)

    actions.click_button(LoginPageLocators.LOGIN_BUTTON)

    result = actions.check_internal_error_message()
    if result:
        pytest.fail(result)


    result = actions.check_error_message()
    if result:
        print(result)
        return

    result = actions.check_is_displayed()
    if result:
        print(result)
        return
    pytest.fail("No button is displayed")
