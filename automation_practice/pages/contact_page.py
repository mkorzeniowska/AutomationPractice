from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .elements_locators import ContactPage as CP


class ContactPage(BasePage):

    url = 'http://automationpractice.com/index.php?controller=contact'

# send a message form:
    @property
    def subject_heading(self):
        return self.driver.find_element(By.ID, 'id_contact')

    @property
    def contact_email(self):
        return BaseElement(driver=self.driver, locator=CP.INPUT_EMAIL_ID)

    @property
    def order_reference(self):
        return BaseElement(driver=self.driver, locator=CP.INPUT_ORDER_REFERENCE_CSS)

    @property
    def attach_file_field(self):
        return BaseElement(driver=self.driver, locator=CP.INPUT_FILE_XPATH)

    @property
    def choose_file_button(self):
        return BaseElement(driver=self.driver, locator=CP.CHOOSE_FILE_BUTTON_XPATH)

    @property
    def message_text_area(self):
        return BaseElement(driver=self.driver, locator=CP.MESSAGE_TEXTAREA_ID)

    @property
    def send_message_button(self):
        return BaseElement(driver=self.driver, locator=CP.SEND_BUTTON_XPATH)

    @property
    def success_message(self):
        return BaseElement(driver=self.driver, locator=CP.SUCCESS_MESSAGE_CSS)

    @property
    def failure_message(self):
        return BaseElement(driver=self.driver, locator=CP.FAILURE_MESSAGE_CSS)

    def select_subject_heading(self, text):
        """ Function for select subject heading: Customer service or Webmaster. """
        heading = Select(self.subject_heading)
        heading.select_by_visible_text(text)
        return heading
