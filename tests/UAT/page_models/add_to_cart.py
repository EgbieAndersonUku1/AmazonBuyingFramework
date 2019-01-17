from time import sleep

from selenium.webdriver.support.select import Select

from tests.UAT.utils.wait import WebElemWait
from tests.UAT.page_models.base_page import BaseModel
from tests.UAT.locators.cart.cart_page import CartPageLocator


class Cart(object):
    """A model representation for the cart found in the Amazon website"""

    def __init__(self, driver):
        self._base_driver = BaseModel(driver)
        self.search = _CartSearch(driver)
        self.item_quantity = _Quantity()

    def increase_item_content(self, number_by):
        """increase_item_content(int) -> return str

           Takes a number as a parameter via the parameter number_by and increase
           or decrease an item content by that number via the dropdown menu associated
           by that item.

           :param
                number_by: The parameter allow the framework to increase or decrease the item quantity
        """

        elem = WebElemWait.retry_to_find_elem(self._base_driver.driver,
                                              elem_to_locate=CartPageLocator.CART_QUANTITY_DROP_DOWN)

        assert elem, 'NO WEB ELEMENT FOUND!!'

        select = Select(elem)
        select.select_by_value(number_by)

        option = select.first_selected_option
        return str(option.text.strip())  # return the current selection in dropdown menu

    def get_number_of_items_in_cart(self):
        """Returns the current number of items in the cart"""

        sleep(3)
        elem = WebElemWait.wait_for_elem(self._base_driver.driver, elem_to_locate=CartPageLocator.SUB_TOTAL_CART_ID)
        return str(elem.text.split(":")[0])

    def is_cart_empty(self):
        """This checks whether the shopping cart is empty.
           If the cart is empty returns True or False if it
           is not.
        """

        cart_message = "Your Shopping Cart is empty."
        self._base_driver.driver.refresh()

        sleep(3)

        elems = self._base_driver.get_all_elements(CartPageLocator.CART_HEADING_TAG)

        sleep(6)

        for elem in elems:
            if str(elem.text.strip()) == cart_message:
                return True
        return False

    def add_to_cart(self):
        """This methods allows items to be added to the cart"""

        elem = WebElemWait.wait_for_elem(self._base_driver.driver, elem_to_locate=CartPageLocator.ADD_TO_CART_ID)
        elem.click()

    def delete_item_from_cart(self, item_name):
        """delete_item_from_cart(str) -> return None

           This method by takes an item by name and deletes that item from that cart

           :param
                item_name: The name of the item that will be deleted from the cart
        """

        sleep(6)
        css_selector = CartPageLocator.get_css_selector_by_item_name(item_name,
                                                                     loc=CartPageLocator.ITEM_LOCATION.DELETE_SECTION)

        WebElemWait.wait_for_elem(self._base_driver.driver, elem_to_locate=css_selector).click()

    def mark_first_item_as_gift(self):
        """Takes the first item in the cart and marks it as a gift"""

        sleep(3)
        check_box_elem = WebElemWait.wait_for_presence_of_elem(self._base_driver.driver,
                                                               elem_to_locate=CartPageLocator.SAVE_AS_GIFT_CSS_SELECTOR)
        check_box_elem[0].click()
        return check_box_elem[0].is_selected()

    def save_item_for_later(self, item_name):
        """save_item_for_later(str) -> return None

           Takes the name of a given item and saves the item for later.

           :param
               item_name: The name of the items that will be saved for later.
        """
        css_selector = CartPageLocator.get_css_selector_by_item_name(item_name,
                                                                     loc=CartPageLocator.ITEM_LOCATION.SAVE_FOR_LATER_SECTION)
        elem = self._base_driver.find_locator_by_element(locator=css_selector)
        elem.click()

    @property
    def get_save_for_later_heading_text(self):
        """Retrieves the banner for the save for later text. If it is found meaning
           an item has been saved for later, then it returns that banner heading.
        """
        seconds_to_wait = 20
        elem = WebElemWait.wait_for_elem(self._base_driver.driver, seconds_to_wait,
                                         elem_to_locate=CartPageLocator.SAVE_FOR_LATER_TITLE_CSS_SELECTOR)
        return str(elem.text).strip()


class _Quantity(object):
    """Allows the user to control the number of items they want
       to increase or decrease the item in dropdown box
    """

    class Number(object):
        one = "1"
        two = "2"
        three = "3"
        four = "4"
        five = "5"


class _CartSearch(object):
    """Allows the user to retrieve information from cart such as the name of the first item, etc"""

    def __init__(self, driver):
        self.driver = BaseModel(driver)
        self._web_driver = self.driver.driver

    @property
    def get_first_item_from_cart(self):
        """Returns the name of the first item found in the cart"""

        self._goto_cart()

        return self._get_elem_helper(elem_to_locate=CartPageLocator.FIRST_ITEM_IN_CART_CSS_SELECTOR).text

    def _goto_cart(self):
        """Allows the application to go inside the cart. The application can then
           navigate inside the cart.
        """
        return self._get_elem_helper(elem_to_locate=CartPageLocator.CART_ICON_ID).click()

    def _get_elem_helper(self, elem_to_locate):
        """_get_elem_helper(web elem locator) -> selenium web element obj

           A helper function that takes a web elem locator such as a tag, xpath, etc and
           uses it to return the Selenium web element object associated with that
           web locator.

           elem_to_locate: The web element locator that will be used by Selenium in order
                           to find Selenium web element object associated with it
        """
        return WebElemWait.wait_for_elem(self._web_driver, elem_to_locate=elem_to_locate)
