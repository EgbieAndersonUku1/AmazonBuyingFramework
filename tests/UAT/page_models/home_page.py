from tests.UAT.locators.home.home_page import HomePageLocator
from tests.UAT.page_models.base_page import BaseModel


class HomeModel(BaseModel):
    """The model for the home page"""

    @property
    def orders_link_text(self):
        return self.find_locator_by_element(locator=HomePageLocator.ORDERS_LINK)


