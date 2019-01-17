from selenium.webdriver.common.by import By
from tests.UAT.locators.cart import constants


class _ItemLocation(object):
    """The section is where the item CSS selectors can be found."""

    SAVE_FOR_LATER_SECTION = "save_item_for_later"
    DELETE_SECTION = "delete_from_cart"


class CartPageLocator(object):
    """The class object is for the various web elements locator found inside
       and associated with the Cart page.
    """

    ADD_TO_CART_ID = By.ID, constants.ADD_TO_CART_BUTTON_ID
    CART_ICON_ID = By.ID, constants.CART_ICON_ID
    CART_QUANTITY_DROP_DOWN = By.CSS_SELECTOR, constants.SHOPPING_CART_QUANTITY_DROPDOWN_CLASS_NAME
    CART_HEADING_TAG = By.TAG_NAME, constants.CART_H2_TAG
    SUB_TOTAL_CART_ID = By.ID, constants.SUB_TOTAL_CART_ID
    FIRST_ITEM_IN_CART_CSS_SELECTOR = By.CSS_SELECTOR, constants.FIRST_ITEM_NAME_IN_CART_CSS_SELECTOR
    SAVE_AS_GIFT_CSS_SELECTOR = By.CSS_SELECTOR, constants.GIFT_CHECKBOX_CSS_SELECTOR
    SAVE_FOR_LATER_TITLE_CSS_SELECTOR = By.CSS_SELECTOR, constants.SAVE_FOR_LATER_HEADING_CSS_SELECTOR
    ITEM_LOCATION = _ItemLocation()

    @classmethod
    def get_css_selector_by_item_name(cls, item_name, loc):
        """get_css_selector_by_item_name(str, str) -> Web element

           This methods takes in a name of item and the location
           needed to look for the item's CSS selector and returns
           a locator element.

           :param
                item_name: The name of the item whose css selector will be returned
                loc: The location to look for the CSS selector
        """
        return By.CSS_SELECTOR, constants.data[loc].get(item_name)

