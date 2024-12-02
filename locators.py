from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGOUT_BUTTON = (By.LINK_TEXT, 'Log Out')
    LOGIN_BUTTON= (By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input')

    ERROR_MESSAGE = (By.XPATH, '//p[@class="error" and contains(text(), "The username and password could not be verified")]')
    INTERNAL_ERROR = (By.XPATH, '//p[@class="error" and contains(text(), "An internal error has occurred")]')