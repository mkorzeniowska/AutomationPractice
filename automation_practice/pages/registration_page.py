from .base_page import BasePage
from .base_element import BaseElement
from .elements_locators import RegistrationPageLocators as RP
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):

    @property
    def customer_firstname(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_CUSTOMER_FIRSTNAME_ID)

    @property
    def customer_lastname(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_CUSTOMER_LASTNAME_ID)

    @property
    def input_email(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_EMAIL_ID)

    @property
    def input_password(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_PASSWORD_ID)

    @property
    def select_days(self):
        # return BaseElement(driver=self.driver, locator=RP.SELECT_DAYS_ID)
        return self.driver.find_element(by=By.ID, value='days')

    @property
    def select_months(self):
        # return BaseElement(driver=self.driver, locator=RP.SELECT_MONTHS_ID)
        return self.driver.find_element(by=By.ID, value='months')

    @property
    def select_years(self):
        # return BaseElement(driver=self.driver, locator=RP.SELECT_YEARS_ID)
        return self.driver.find_element(by=By.ID, value='years')

    @property
    def newsletter_checkbox(self):
        return BaseElement(driver=self.driver, locator=RP.NEWSLETTER_CHECKBOX_ID)

    @property
    def special_offers_checkbox(self):
        return BaseElement(driver=self.driver, locator=RP.SPECIAL_OFFERS_CHECKBOX_ID)

    @property
    def input_firstname(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_FIRSTNAME_ID)

    @property
    def input_lastname(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_LASTNAME_ID)

    @property
    def input_address(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_ADDRESS1_ID)

    @property
    def input_city(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_CITY_ID)

    @property
    def select_state(self):
        # return BaseElement(driver=self.driver, locator=RP.SELECT_STATE_ID)
        return self.driver.find_element(by=By.ID, value='id_state')

    @property
    def input_zipcode(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_ZIPCODE_ID)

    @property
    def select_country(self):
        # return BaseElement(driver=self.driver, locator=RP.SELECT_COUNTRY_ID)
        return self.driver.find_element(by=By.ID, value='id_country')

    @property
    def input_mobile_phone(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_MOBILE_PHONE_ID)

    @property
    def input_alias_address(self):
        return BaseElement(driver=self.driver, locator=RP.INPUT_ALIAS_ADDRESS_ID)

    @property
    def register_button(self):
        return BaseElement(driver=self.driver, locator=RP.REGISTER_BUTTON_ID)

    @property
    def alert(self):
        return BaseElement(driver=self.driver, locator=RP.ALERT_CSS)

    def select_title_button(self, title):
        """ Function to select a title. Values: Mr. or Mrs."""
        if title == 'Mr':
            BaseElement(driver=self.driver, locator=RP.TITLE_MR_ID).click()
        else:
            BaseElement(driver=self.driver, locator=RP.TITLE_MRS_ID).click()

    def fill_registration_form(self, data):
        """ Function to fill a registration form. """
        self.select_title_button(data['title'])
        self.customer_firstname.input_text(data['firstname'])
        self.customer_lastname.input_text(data['lastname'])
        self.input_password.input_text(data['password'])
        self.driver.implicitly_wait(10)
        Select(self.select_days).select_by_value(data['day_of_birth'])
        Select(self.select_months).select_by_value(data['month_of_birth'])
        Select(self.select_years).select_by_value(data['year_of_birth'])
        self.input_address.input_text(data['address'])
        self.input_city.input_text(data['city'])
        Select(self.select_state).select_by_visible_text(data['state'])
        self.input_zipcode.input_text(data['zipcode'])
        Select(self.select_country).select_by_visible_text(data['country'])
        self.input_mobile_phone.input_text(data['phone'])
        self.input_alias_address.input_text(data['email'])

    def register_account(self, data):
        """ Function to register an account. """
        self.fill_registration_form(data)
        self.register_button.click()



