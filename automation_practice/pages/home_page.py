from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from .elements_locators import HomePageLocators as HP

class HomePage(BasePage):

    url = 'http://automationpractice.com'

    @property
    def signature_text(self):
        locator = Locator(by=By.XPATH, value=HP.signature_text_css)
        return BaseElement(driver=self.driver,locator=locator)

    @property
    def search_input(self):
        locator = Locator(by=By.ID, value=HP.search_input_id)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def search_button(self):
        locator = Locator(by=By.NAME, value=HP.search_button_css)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def contact_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HP.contact_button_css)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sign_in_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HP.sign_in_button_css)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def shopping_cart_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HP.shopping_cart_button_css)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def shopping_cart_quantity(self):
        locator = Locator(by=By.XPATH, value=HP.shopping_cart_empty_xpath)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def menu_women_tab(self):
        locator = Locator(by=By.CSS_SELECTOR, value=HP.menu_women_tab_css)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def menu_dresses_tab(self):
        locator = Locator(by=By.XPATH, value=HP.menu_dresses_tab_xpath)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def menu_tshirts_tab(self):
        locator = Locator(by=By.XPATH, value=HP.menu_tshirts_tab_xpath)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def popular_tab(self):
        locator = Locator(by=By.XPATH, value=HP.popular_tab_xpath)
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def bestsellers_tab(self):
        locator = Locator(by=By.XPATH, value=HP.bestsellers_tab_xpath)
        return BaseElement(driver=self.driver, locator=locator)

