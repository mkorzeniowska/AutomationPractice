from .base_element import BaseElement
from .base_page import BasePage
from .authentication_page import AuthenticationPage
from .contact_page import ContactPage
from .elements_locators import HomePageLocators as HP


class HomePage(BasePage):

    url = 'http://automationpractice.com'

    @property
    def signature_text(self):
        return BaseElement(driver=self.driver, locator=HP.SIGNATURE_TEXT_XPATH)

    @property
    def search_input(self):
        return BaseElement(driver=self.driver, locator=HP.SEARCH_INPUT_CSS)

    @property
    def search_button(self):
        return BaseElement(driver=self.driver, locator=HP.SEARCH_BUTTON_CSS)

    @property
    def contact_button(self):
        return BaseElement(driver=self.driver, locator=HP.CONTACT_BUTTON_CSS)

    @property
    def sign_in_button(self):
        return BaseElement(driver=self.driver, locator=HP.SIGN_IN_BUTTON_CSS)

    @property
    def shopping_cart_button(self):
        return BaseElement(driver=self.driver, locator=HP.CART_BUTTON_CSS)

    @property
    def shopping_cart_quantity(self):
        return BaseElement(driver=self.driver, locator=HP.CART_EMPTY_XPATH)

    @property
    def menu_women_tab(self):
        return BaseElement(driver=self.driver, locator=HP.MENU_WOMEN_TAB_CSS)

    @property
    def menu_dresses_tab(self):
        return BaseElement(driver=self.driver, locator=HP.MENU_DRESSES_TAB_XPATH)

    @property
    def menu_tshirts_tab(self):
        return BaseElement(driver=self.driver, locator=HP.MENU_TSHIRTS_TAB_XPATH)

    @property
    def popular_tab(self):
        return BaseElement(driver=self.driver, locator=HP.POPULAR_TAB_XPATH)

    @property
    def bestsellers_tab(self):
        return BaseElement(driver=self.driver, locator=HP.BESTSELLERS_TAB_XPATH)

    @property
    def my_account_button(self):
        return BaseElement(driver=self.driver, locator=HP.MY_ACCOUNT_BUTTON_ID)

# redirect to authentication page
    def click_sign_in_button(self):
        """ Function for clicking the "Sign in" button to redirect to the authentication page. """
        self.sign_in_button.click()
        authentication_page = AuthenticationPage(self.driver)
        self.driver.implicitly_wait(10)
        return authentication_page

# redirect to contact us page
    def click_contact_button(self):
        """ Function for clicking the "Contact Us" button to redirect to the contact page."""
        self.contact_button.click()
        contact_page = ContactPage(self.driver)
        self.driver.implicitly_wait(10)
        return contact_page
