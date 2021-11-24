from .elements_locators import CartPageLocators as CP
from .base_page import BasePage
from .base_element import BaseElement
from selenium.webdriver.common.by import By

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
    def proceed_address_checkout(self):
        return BaseElement(driver=self.driver, locator=CP.PROCEED_CHECKOUT_ADDRESS_BUTTON_CSS)
    
    @property
    def proceed_carrier_checkout(self):
        return BaseElement(driver=self.driver, locator=CP.PROCEED_CHECKOUT_SHIPPING_BUTTON_CSS)

    @property
    def terms_of_service_checkbox(self):
        return BaseElement(driver=self.driver, locator=CP.TERMS_OF_SERVICE_ID)

    @property
    def pay_by_bank_button(self):
        return BaseElement(driver=self.driver, locator=CP.PAY_BY_BANK_CSS)

    @property
    def confirm_order_button(self):
        return BaseElement(driver=self.driver, locator=CP.CONFIRM_ORDER_CSS)

    @property
    def empty_alert(self):
        return BaseElement(driver=self.driver, locator=CP.EMPTY_ALERT_CSS)

    def remove_product_from_cart(self, product_id):
        delete_button = self.driver.find_element(by=By.CSS_SELECTOR,
                                                 value='a[id^="' + product_id + '"]')
        delete_button.click()
        return None

    def check_total_price(self):
        total_price = self.total_price.text
        return total_price

    def purchase_product(self):
        # dodać zaznaczenie checkboxu z adresem
        self.proceed_address_checkout.click()
        self.terms_of_service_checkbox.click()
        self.proceed_carrier_checkout.click()
        self.pay_by_bank_button.click()
        self.confirm_order_button.click()
        return None
