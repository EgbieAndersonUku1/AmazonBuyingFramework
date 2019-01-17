
class BaseModel(object):

    def __init__(self, driver):
        self.driver = driver

    def find_locator_by_element(self, locator):
        """find_locator_by_element(locator) -> return Selenium object

           Takes a locator e.g xpath, tag, etc and returns
           a single selenium element objected associated with locator.
           Returns None if not found

           :param
               'locator': The locator can be in the form of xpath, tag, etc
                          for following path of a web page. This locator will be
                          used by the application to retrieve a single
                          selenium web object associated
        """
        return self.driver.find_element(*locator)

    def get_all_elements(self, locator):
        """get_all_elements(locator) -> return List of selenium object

           Takes a locator e.g xpath, tag, etc and returns a list containing
           selenium element objected associated with locator. Returns None if not found

           :param
               'locator': This locator will be used by the application to
                          retrieve a list of selenium web object
        """
        return self.driver.find_elements(*locator)