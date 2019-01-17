from selenium.webdriver.common.by import By
from tests.UAT.locators.sign_in_page import constants


class SignInPageLocators(object):
    """This class contains the locator which is needed by the framework to
       log the user into the application.
    """
    SIGN_IN_TO_ACCOUNT_LINK = By.XPATH, constants.SIGN_INTO_ACCOUNT_XPATH

