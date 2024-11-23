from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import pytest
import conftest


@pytest.fixture(scope="function")
def browser():
    option = Options()
    option.add_argument("--incognito")
    option.add_argument("--ignore-certificate-errors")
    option.add_argument("--disable-cache")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-popup-blocking")
    option.add_argument("--window-size=1980,1080")

    driver_instance = webdriver.Chrome(options=option)
    yield driver_instance
    driver_instance .quit()


@pytest.mark.parametrize("username, password", conftest.CREDENTIALS)
def test_auth(browser, username, password):

    url = conftest.URL
    browser.get(url)

    username_input = browser.find_element(By.NAME, 'username')
    password_input = browser.find_element(By.NAME, 'password')

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    try:

        error_message = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'error'))
        )
        if error_message.is_displayed():
            pytest.fail(
                "Internal server error occurred after login: 'An internal error has occurred and has been logged.'")

    except TimeoutException:

        try:
            logout_button = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Log Out'))
            )
            assert logout_button.is_displayed(), "Login failed, 'Log Out' button not found"

        except NoSuchElementException as e:
                pytest.fail(f"Test failed due to missing element: {e}")

    except WebDriverException as e:
        pytest.fail(f"WebDriver error: {e}")





