from selenium.webdriver.common.by import By
from tests.UAT.locators.navigation import constants


class SearchPageLocator(object):
    """The search page contains the locator which is needed by the framework to
       navigate the pages to retrieve various items, etc.
    """
    SEARCH_BAR = By.ID, constants.SEARCH_BAR_ID
    SEARCH_BUTTON = By.CLASS_NAME, constants.SEARCH_BUTTON
    SEARCH_PATH_BOOK_LINK = By.CSS_SELECTOR, constants.BOOK_LINK_CSS_SELECTOR
    PAPER_BACK_TAB_CSS_SELECTOR = By.CSS_SELECTOR, constants.PAPER_BACK_TAB_CSS_SELECTOR
    PAPER_BACK_BUTTON_TAB_ID = By.ID, constants.PAPER_BACK_TAB_BUTTON_ID