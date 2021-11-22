from .elements_locators import CartPageLocators as CP
from .base_page import BasePage
from .base_element import BaseElement

class CartPage(BasePage):

    url = 'http://automationpractice.com/index.php?controller=order'

    @property
    def delete_button(self):
        return BaseElement(driver=self.driver, locator=CP.DELETE_BUTTON_CSS)

    @property
    def continue_shopping_button(self):
        return BaseElement(driver=self.driver, locator=CP.CONTINUE_SHOPPING_BUTTON_CSS)

    @property
    def checkout_button(self):
        return BaseElement(driver=self.driver, locator=CP.CHECKOUT_BUTTON_CSS)

    @property
    def total_price(self):
        return BaseElement(driver=self.driver, locator=CP.TOTAL_PRICE)

    @property
    def empty_alert(self):
        return BaseElement(driver=self.driver, locator=CP.EMPTY_ALERT_CSS)

    def remove_product_from_cart(self):
        self.delete_button.click()
        return None

    def check_total_price(self):
        total_price = self.total_price.text
        return total_price
