from tests.UAT.page_models.book import Book

# The Cart constant page contains all the web locator for the cart page

# The ID for add to cart button
ADD_TO_CART_BUTTON_ID = "add-to-cart-button"

# The id for the cart icon picture located on the top of the page
CART_ICON_ID = "nav-cart"

# The dropdown ID for quantity needed to increment or decrement the items in the cart
CART_QUANTITY_DROP_DOWN_ID = "item_quantity"

# The CSS selector for the first item in the cart
FIRST_ITEM_NAME_IN_CART_CSS_SELECTOR = ".sc-product-title"

# The CSS SELECTION link for turning an item into a gift
GIFT_CHECKBOX_CSS_SELECTOR = ".sc-gift-option > label:nth-child(1) > input:nth-child(1)"

# The CSS Selector to the heading that displayed just above the item when it is saved e.g. 'saved item (1 item)'
SAVE_FOR_LATER_HEADING_CSS_SELECTOR = ".sc-list-caption"

# The cart id for the sub total number of items displayed for the cart e.g 'subtotal (1 items): $5.99'
SUB_TOTAL_CART_ID = "sc-subtotal-label-activecart"


# The dropdown class name for needed to increment or decrement the items in the cart
SHOPPING_CART_QUANTITY_DROPDOWN_CLASS_NAME = "select.a-native-dropdown"


# The cart heading tag that displayed above the cart
CART_H2_TAG = "h2"


# Book titles needed for testing
_TEST_AUTOMATION = Book.Title.TEST_AUTOMATION
_AGILE_TESTING = Book.Title.AGILE_TESTING
_SELENIUM_WEBDRIVER = Book.Title.SELENIUM_WEB_DRIVER


# The CSS SELECTOR for the 'save later link' for the items for the Selenium webdriver, Agile Testing and testing automation
_AGILE_TESTING_SAVE_FOR_LATER_CSS_SELECTOR = NotImplemented
_SELENIUM_WEB_DRIVER_SAVE_FOR_LATER_CSS_SELECTOR = NotImplemented
_TEST_AUTOMATION_SAVE_FOR_LATER_CSS_SELECTOR = "div.sc-list-item:nth-child(3) > div:nth-child(4) > " \
                                              "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) " \
                                              "> div:nth-child(1) > div:nth-child(2) > div:nth-child(2)" \
                                              " > span:nth-child(3) > span:nth-child(1) > input:nth-child(1)"


#  The CSS SELECTOR for the delete link for the items for the Selenium webdriver, Agile Testing and testing automation
_SELENIUM_WEB_DRIVER_DELETE_LINK_CSS_SELECTOR = ".sc-action-delete > span:nth-child(1) > input:nth-child(1)"
_TEST_AUTOMATION_DELETE_LINK_CSS_SELECTOR = NotImplemented

_AGILE_TESTING_DELETE_LINK_CSS_SELECTOR = "div.sc-list-item:nth-child(2) > div:nth-child(4) > div:nth-child(1) >" \
                                          " div:nth-child(1) > div:nth-child(1) > div:nth-child(1) >" \
                                          " div:nth-child(2) > div:nth-child(2) > span:nth-child(1) > " \
                                          "span:nth-child(1) > input:nth-child(1)"





data = {
        "save_item_for_later": {_TEST_AUTOMATION: _TEST_AUTOMATION_SAVE_FOR_LATER_CSS_SELECTOR,
                           _AGILE_TESTING: _SELENIUM_WEB_DRIVER_SAVE_FOR_LATER_CSS_SELECTOR,
                           _SELENIUM_WEBDRIVER: _SELENIUM_WEB_DRIVER_SAVE_FOR_LATER_CSS_SELECTOR

        },

        "delete_from_cart": {_TEST_AUTOMATION: _TEST_AUTOMATION_DELETE_LINK_CSS_SELECTOR,
                             _AGILE_TESTING: _AGILE_TESTING_DELETE_LINK_CSS_SELECTOR,
                             _SELENIUM_WEBDRIVER: _SELENIUM_WEB_DRIVER_DELETE_LINK_CSS_SELECTOR
    }

}