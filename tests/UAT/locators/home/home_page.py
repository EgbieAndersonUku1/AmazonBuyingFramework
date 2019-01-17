from selenium.webdriver.common.by import By
from tests.UAT.locators.home import constants


class HomePageLocator(object):
    """The page locators for the home page"""

    ORDERS_LINK = By.CLASS_NAME, constants.ORDERS_TEXT_LINK_ID