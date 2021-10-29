from .base_page import BasePage
from .base_element import BaseElement
from .elements_locators import AuthenticationPageLocators as AP


class AuthenticationPage(BasePage):

    url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

# Sign in form:
    @property
    def sign_in_email(self):
        return BaseElement(driver=self.driver, locator=AP.REGISTERED_INPUT_EMAIL_CSS)

    @property
    def sign_in_password(self):
        return BaseElement(driver=self.driver, locator=AP.REGISTERED_INPUT_PASS_CSS)

    @property
    def sign_in_button(self):
        return BaseElement(driver=self.driver, locator=AP.SIGN_IN_BUTTON_CSS)

    @property
    def forgot_password(self):
        return BaseElement(driver=self.driver, locator=AP.FORGOT_PASSWORD_CSS)

    def login(self, email, password):
        self.sign_in_email.input_text(email)
        self.sign_in_password.input_text(password)
        self.sign_in_button.click()
        return None

    def restore_password(self, email):
        self.forgot_password.click()
        return None

