from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from locators import LoginPageLocators
from config import URL, CREDENTIALS
import pytest




@pytest.mark.parametrize("username, password", CREDENTIALS)
def test_auth(browser, username, password):

    url = URL
    browser.get(url)

    username_input = browser.find_element(*LoginPageLocators.USERNAME_INPUT)
    password_input = browser.find_element(*LoginPageLocators.PASSWORD_INPUT)

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    try:
        logout_button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located(LoginPageLocators.LOGOUT_BUTTON)
        )
        assert logout_button.is_displayed(), "Login failed, 'Log Out' button not found"
        print(f"Login successful for {username}.")

    except TimeoutException:
        try:
            error_message = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located(LoginPageLocators.ERROR_MESSAGE)
            )
            if error_message.is_displayed() and error_message.text == "The username and password could not be verified.":
                print(f"Login failed for {username}: Incorrect username or password.")
            else:
                pytest.fail(f"Unexpected error message: {error_message.text}")
        except TimeoutException:
            pytest.fail("Timeout: Unable to detect error message or logout button.")

    except WebDriverException as e:
        pytest.fail(f"WebDriver error: {e}")



