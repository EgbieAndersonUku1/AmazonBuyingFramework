from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class WebElemWait(object):

    @classmethod
    def retry_to_find_elem(cls, driver, wait_for=30, elem_to_locate=None, num_of_times_retry=20):
        """"""
        for i in range(num_of_times_retry):
            try:
                return cls.wait_for_elem(driver, wait_for, elem_to_locate)
            except:
                pass

    @classmethod
    def wait_for_elem(cls, driver, secs_to_wait=30, elem_to_locate=None):
        return cls._wait_for_elem_helper(driver, secs_to_wait, ec.visibility_of_element_located, elem_to_locate)

    @classmethod
    def wait_for_presence_of_elem(cls, driver, secs_to_wait=30, elem_to_locate=None):
        return cls._wait_for_elem_helper(driver, secs_to_wait, ec.presence_of_all_elements_located, elem_to_locate)

    @classmethod
    def _wait_for_elem_helper(cls, driver, secs_to_wait, func, elem_to_locate):
        """"""
        return WebDriverWait(driver, secs_to_wait).until(func(elem_to_locate))


