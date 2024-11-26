import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    option = Options()
    option.add_argument('--headless')
    option.add_argument("--incognito")
    option.add_argument("--ignore-certificate-errors")
    option.add_argument("--disable-cache")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-popup-blocking")
    option.add_argument("--window-size=1980,1080")

    driver_instance = webdriver.Chrome(options=option)
    yield driver_instance
    driver_instance .quit()

