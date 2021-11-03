from pytest import mark
from selenium.webdriver.support.select import Select
from pages.contact_page import ContactPage


@mark.contactpage
class ContactPageTests:

    def test_select_subject_heading(self, get_contact_page):
        texts = ['Webmaster', 'Customer service']
        contact_page = get_contact_page
        for text in texts:
            heading = contact_page.select_subject_heading(text)
            assert heading.first_selected_option.text == text




