from tests.UAT.locators.login.login_page import LoginPageLocators
from tests.UAT.page_models.base_page import BaseModel


class LoginModel(BaseModel):
    """The login model for Amazon sign in page"""

    def login(self, username, password):
        """login(str, str) -> return None

           Takes two strings a username and password and provided the credentials
           are correct logs the user in.

           :param
                username: The username associated with the account
                password: The password belong to the user
        """
        self._set_username(username=username)
        self._set_password(password=password)
        self._sign_in()

    def _set_username(self, username):
        """_set_username(str) -> return None

           A private method that sets the user's username to Amazon GUI username field

           :param
                username: The username to be set to the field
        """
        self._set_fields(field_name=username, field_locator=LoginPageLocators.EMAIL)

    def _set_password(self, password):
        """_set_username(str) -> return None

           A private method that sets the user's password to Amazon GUI password field

           :param
                username: The username to be set to the field
        """
        self._set_fields(field_name=password, field_locator=LoginPageLocators.PASSWORD)

    def _set_fields(self, field_name, field_locator):
        """"""
        field = self.find_locator_by_element(locator=field_locator)
        field.send_keys(field_name)

    def _sign_in(self):
        """Clicks the button that allows the user to sign into their account"""

        sign_button = self.find_locator_by_element(locator=LoginPageLocators.LOGIN_BUTTON)
        sign_button.click()
