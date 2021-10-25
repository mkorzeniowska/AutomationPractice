from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class StartPage(BasePage):

    url = 'http://automationpractice.com'

    @property
    def signature_text(self):
        locator = Locator(by=By.XPATH, value='//div/h1')
        return BaseElement(driver=self.driver,locator=locator)

    @property
    def search_input(self):
        locator = Locator(by=By.ID, value='search_query_top')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_button(self):
        locator = Locator(by=By.NAME, value='submit_search')
        return BaseElement(driver=self.driver, locator=locator)
