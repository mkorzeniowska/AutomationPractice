from .base_page import BasePage
from .base_element import BaseElement
from .registration_page import RegistrationPage
from .elements_locators import AuthenticationPageLocators as AP


class AuthenticationPage(BasePage):

    url = 'http://automationpractice.com/index.php?controller=authentication'

# Sign in form:
    @property
    def sign_in_email(self):
        return BaseElement(driver=self.driver, locator=AP.REGISTERED_INPUT_EMAIL_ID)

    @property
    def sign_in_password(self):
        return BaseElement(driver=self.driver, locator=AP.REGISTERED_INPUT_PASS_ID)

    @property
    def sign_in_button(self):
        return BaseElement(driver=self.driver, locator=AP.SIGN_IN_BUTTON_CSS)

    @property
    def forgot_password(self):
        return BaseElement(driver=self.driver, locator=AP.FORGOT_PASSWORD_CSS)

    @property
    def retrieve_password_email(self):
        return BaseElement(driver=self.driver, locator=AP.RETRIEVE_PASSWORD_EMAIL)

    @property
    def retrieve_password_button(self):
        return BaseElement(driver=self.driver, locator=AP.RETRIEVE_PASSWORD_BUTTON)

    @property
    def authentication_header(self):
        return BaseElement(driver=self.driver, locator=AP.AUTHENTICATION_PAGE_HEADING_CSS)

    def login(self, email, password):
        """ Function for login to the page"""
        self.sign_in_email.input_text(email)
        self.sign_in_password.input_text(password)
        self.sign_in_button.click()
        return None

    def restore_password(self, email):
        """ Function for retrieve a password to account """
        self.forgot_password.click()
        self.retrieve_password_email.input_text(email)
        self.retrieve_password_button.click()
        return None

    # create an account form:
    @property
    def create_email(self):
        return BaseElement(driver=self.driver, locator=AP.CREATE_ACCOUNT_INPUT_EMAIL_ID)

    @property
    def create_account_button(self):
        return BaseElement(driver=self.driver, locator=AP.CREATE_ACCOUNT_BUTTON_CSS)

    def create_account(self, data):
        """ Function for creating an account """
        self.create_email.input_text(data['email'])
        self.create_account_button.click()
        return None


