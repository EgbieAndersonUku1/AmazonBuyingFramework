from tests.UAT.locators.sign_in_page.sign_in import SignInPageLocators
from tests.UAT.page_models.base_page import BaseModel
from tests.UAT.page_models import constants


class SignInModel(BaseModel):

    @property
    def url(self):
        """Returns the URL for the site being tested"""
        return constants.URL

    def sign_in_page(self):
        """When clicked this takes to the user to sign in page"""

        sign_in_elem = self.find_locator_by_element(locator=SignInPageLocators.SIGN_IN_TO_ACCOUNT_LINK)
        sign_in_elem.click()
