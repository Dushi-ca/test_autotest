from selenium.common import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

class MainActions:
    def __init__(self, driver, base_url, timeout=5):
        self._driver = driver
        self._base_url = base_url
        self._timeout = timeout

    def enter_text_to_field(self, locator, text):
        try:
            input_element = WebDriverWait(self._driver, self._timeout).until(
                EC.presence_of_element_located(locator)
            )
            input_element.send_keys(text)
        except WebDriverException as e:
            assert False, e


    def click_button(self, locator):
        try:
            button = WebDriverWait(self._driver, self._timeout).until(
                EC.element_to_be_clickable(locator)
            )
            button.click()
        except WebDriverException as e:
            assert False, e

    def check_internal_error_message(self):
        try:
            internal_error_element = WebDriverWait(self._driver, self._timeout).until(
                EC.presence_of_element_located(LoginPageLocators.INTERNAL_ERROR)
            )
            internal_error = internal_error_element.text
            return internal_error

        except TimeoutException:
            return None




    def check_error_message(self):
        try:
            error_message_element = WebDriverWait(self._driver, self._timeout).until(
                EC.presence_of_element_located(LoginPageLocators.ERROR_MESSAGE)
            )

            error_message = error_message_element.text

            return error_message

        except TimeoutException:
            return None

    def check_is_displayed(self):
        try:
            logout_button = WebDriverWait(self._driver, self._timeout).until(
                EC.presence_of_element_located(LoginPageLocators.LOGOUT_BUTTON)
            )
            return "Logout button is displayed"
        except WebDriverException as e:
            assert False, e




