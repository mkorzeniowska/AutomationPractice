from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.find()

    def find(self):
        """ Finding element on the page using visibility as expected conditions """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        self.web_element = element
        return None

    def input_text(self, txt):
        """ Function to enter text into input fields """
        self.web_element.clear()
        self.web_element.send_keys(txt)
        return None

    def click(self):
        """ Function to click elements using expected conditions """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click()
        return None

    def attribute(self, attr_name):
        """ Function to get the attribute of an element """
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        """ Function to retrieve text from an element. Set as @property """
        text = self.web_element.text
        return text
