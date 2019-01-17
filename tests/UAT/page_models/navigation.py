from time import sleep

from tests.UAT.locators.navigation.navigate import SearchPageLocator
from tests.UAT.page_models.base_page import BaseModel


class SearchPage(BaseModel):
    """The search page model allows the application to search for any item on Amazon page"""

    def search_books(self, book_name):
        """search_books(str) -> return None

           Takes a book name and returns the page associated with that name

           :param
                book_name: The book name will be used by the method to navigate
                           to the item's page.
        """

        search_bar_elem = self.find_locator_by_element(locator=SearchPageLocator.SEARCH_BAR)
        search_bar_elem.send_keys(book_name)

        search_button_elem = self.find_locator_by_element(locator=SearchPageLocator.SEARCH_BUTTON)
        search_button_elem.click()

        book_link_elem = self.find_locator_by_element(locator=SearchPageLocator.SEARCH_PATH_BOOK_LINK)
        book_link_elem.click()

    def click_paper_back_tab(self):
        """For each item page there is a table that contains three headings Kindle,
           Paperback and Other Sellers. This method allows the selenium application to
           click on the paper back tab which then allows the user to add the entry to
           their shopping cart if they want to.
        """
        sleep(1)
        elem = self.find_locator_by_element(SearchPageLocator.PAPER_BACK_TAB_CSS_SELECTOR)
        elem.click()

    def click_paper_back_button_tab(self):
        """ For some item page there is a two button tabs these are the kindle and paperback
            tab. This method allows the selenium application to
            click on the paper back tab which then allows the user to add the entry to
            their shopping cart if they want to.
        """
        elem = self.find_locator_by_element(locator=SearchPageLocator.PAPER_BACK_BUTTON_TAB_ID)
        elem.click()