from selenium.webdriver.common.by import By
from tests.UAT.locators.login import constants


class LoginPageLocators(object):
    """The locator for login web locators"""

    EMAIL = By.ID, constants.EMAIL_ID
    PASSWORD = By.ID, constants.PASSWORD_ID
    LOGIN_BUTTON = By.ID, constants.LOGIN_BUTTON_ID




