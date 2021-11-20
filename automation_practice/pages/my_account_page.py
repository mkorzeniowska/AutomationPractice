from .elements_locators import MyAccountPageLocators as MA
from .base_element import BaseElement
from .base_page import BasePage


class MyAccountPage(BasePage):

    @property
    def sign_out_button(self):
        return BaseElement(driver=self.driver, locator=MA.SIGN_OUT_BUTTON)
