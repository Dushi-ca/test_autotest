from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error')
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Log Out')