# Written using python 3.64
# Author EgbieAndersonUku1

from time import sleep
from pathlib import Path
from selenium import webdriver
from behave import given, when, then

import sys

# main path to the director "C:\some\\path\to\this\directory\AmazonBuyingTest"
parent_directory = str(Path().resolve().parents[2])  # needed to run otherwise behave cannot see the tests imports
sys.path.append(parent_directory)


from tests.UAT.page_models.sign_in_page import SignInModel
from tests.UAT.page_models.login_page import LoginModel
from tests.UAT.page_models.home_page import HomeModel
from tests.UAT.page_models.book import Book
from tests.UAT.page_models.navigation import SearchPage
from tests.UAT.page_models.add_to_cart import Cart
from tests.UAT.page_models import errors


# Add the path to the downloaded chromedriver here. Check the README.md or readme.txt for more information
chrome_driver_address ="C:\\Users\\<username here>\\Downloads\\chromedriver_win32\\chromedriver.exe" # for windows only

# Add your Amazon credentials here
_USERNAME = 'AMAZON USERNAME HERE'
_PASSWORD = 'AMAZON PASSWORD'


@given('the user has the correct credentials and successfully logs in')
def step_impl(context):

    context.driver = webdriver.Chrome(chrome_driver_address)
    context.driver.maximize_window()

    context.cart = Cart(context.driver)
    context.sign_in_page = SignInModel(context.driver)
    context.login_page = LoginModel(context.driver)
    context.home_page = HomeModel(context.driver)

    context.driver.get(context.sign_in_page.url)

    context.sign_in_page.sign_in_page()
    context.login_page.login(username=_USERNAME, password=_PASSWORD)

    try:
        assert context.home_page.orders_link_text.is_displayed(), errors.SIGN_IN_ERROR
    except:
        raise Exception('Invalid username or password')


@when("the users adds book to 'Experiences of Test Automation: Case Studies of Software Test Automation' to cart")
def step_impl(context):

    cart = _add_item_to_cart_helper(context.driver, item_name=Book.Title.TEST_AUTOMATION, click_table_tab=True)
    item_name = cart.search.get_first_item_from_cart

    assert item_name == Book.Title.TEST_AUTOMATION, errors.FIRST_ITEM_ERROR.format(Book.Title.TEST_AUTOMATION, item_name)


@when("the users adds book to 'Agile Testing: A Practical Guide for Testers and Agile Teams' to cart")
def step_impl(context):

    cart = _add_item_to_cart_helper(context.driver, item_name=Book.Title.AGILE_TESTING)
    item_name = cart.search.get_first_item_from_cart
    assert item_name == Book.Title.AGILE_TESTING, errors.FIRST_ITEM_ERROR.format(Book.Title.AGILE_TESTING, item_name)


@when("the users adds book to 'Selenium WebDriver 3 Practical Guide' to the cart")
def step_impl(context):

    cart = _add_item_to_cart_helper(context.driver, item_name=Book.Title.SELENIUM_WEB_DRIVER, click_tab_button=True)
    name = cart.search.get_first_item_from_cart

    assert name == Book.Title.SELENIUM_WEB_DRIVER, errors.FIRST_ITEM_ERROR.format(Book.Title.SELENIUM_WEB_DRIVER, name)


@when("the users selects the 'Save For Later' option for 'Experiences of Test Automation'")
def step_impl(context):

    expected_text = "Saved for later (1 item)"

    context.cart.save_item_for_later(item_name=Book.Title.TEST_AUTOMATION)
    returned_value = context.cart.get_save_for_later_heading_text

    assert returned_value == expected_text, errors.SAVE_FOR_LATER_ERROR.format(expected_text, returned_value)


@when("the users selects the 'Delete' option for 'Agile Testing'")
def step_impl(context):

    expected_text_before_deletion = "Subtotal (2 items)"
    expected_text_after_deletion = "Subtotal (1 item)"

    no_of_items_in_cart = context.cart.get_number_of_items_in_cart() # get number of items before deletion

    assert no_of_items_in_cart == expected_text_before_deletion, \
                                   errors.QUANTITY_ERROR.format(expected_text_before_deletion, no_of_items_in_cart)

    context.cart.delete_item_from_cart(item_name=Book.Title.AGILE_TESTING)
    no_of_items_in_cart = context.cart.get_number_of_items_in_cart()

    assert no_of_items_in_cart == expected_text_after_deletion, \
                                  errors.DELETION_QUANTITY_ERROR.format(expected_text_after_deletion, no_of_items_in_cart)

@when("""then increases the quantity of the basket for 'Selenium WebDriver 3 Practical Guide' by 3 copies""")
def step_impl(context):

    expected_item_quantity = "3"
    item_quantity = context.cart.increase_item_content(number_by=context.cart.item_quantity.Number.three)

    assert item_quantity == expected_item_quantity, errors.ITEM_INCREMENT_ERROR.format(expected_item_quantity, item_quantity)


@when("""the user marks 'Selenium WebDriver 3' as a gift""")
def step_impl(context):
    assert context.cart.mark_first_item_as_gift()


@then("the user deletes all copies of 'Selenium WebDriver 3' from the cart")
def step_impl(context):

    sleep(2)
    context.cart.delete_item_from_cart(item_name=Book.Title.SELENIUM_WEB_DRIVER)
    assert context.cart.is_cart_empty(), errors.EMPTY_CART_ERROR


def _add_item_to_cart_helper(driver, item_name, click_table_tab=False, click_tab_button=False):
    """_add_item_to_cart_helper(obj driver, str, optional boolean, optional boolean) -> cart obj

       A helper function that adds additional help to function by adding items to the cart.

       :param
            driver: The web driver need to run the application
            item_name: The item name to search for
            click_table_tab: This will tell the framework whether or not to click the table
                             for the paperback when the item page is found. Default False
            click_tab_button: This will tell the framework to click on the tab button
                              containing kindle or paperback tab if no table tab is found.
                              Default False.
    """
    search = SearchPage(driver)
    search.search_books(book_name=item_name)

    if click_table_tab:
        search.click_paper_back_tab()
    elif click_tab_button:
        search.click_paper_back_button_tab()

    cart = Cart(driver=driver)
    cart.add_to_cart()

    return cart

