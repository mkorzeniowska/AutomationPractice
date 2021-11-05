from pytest import mark
from selenium.webdriver.support.select import Select


@mark.contactpage
class ContactPageTests:

    def test_contact_us_button_click(self, get_home_page):
        """ Test redirect from home page by clicking the "Contact us" button. """
        home_page = get_home_page
        contact_page = home_page.click_contact_button()
        assert contact_page.title == 'Contact us - My Store'

    def test_select_subject_heading(self, get_contact_page):
        """ Message subject header selection test: Webmaster or Customer service. """
        texts = ['Webmaster', 'Customer service']
        contact_page = get_contact_page
        for text in texts:
            heading = contact_page.select_subject_heading(text)
            assert heading.first_selected_option.text == text

    @mark.smoke
    def test_send_message_without_attachment(self, get_contact_page):
        """ Test sending a message without attaching a file. """
        contact_page = get_contact_page
        contact_page.select_subject_heading('Customer service')
        contact_page.contact_email.input_text('testing@o2.pl')
        contact_page.order_reference.input_text('123456')
        contact_page.message_text_area.input_text('This is test message')
        contact_page.send_message_button.click()
        expected_result = 'Your message has been successfully sent to our team.'
        assert contact_page.success_message.text == expected_result

    def test_send_message_without_subject_and_attachment(self, get_contact_page):
        """ Test sending a message without a selected subject and attaching a file. """
        contact_page = get_contact_page
        contact_page.contact_email.input_text('testing@o2.pl')
        contact_page.order_reference.input_text('123456')
        contact_page.message_text_area.input_text('This is test message')
        contact_page.send_message_button.click()
        expected_result = 'Please select a subject from the list provided.'
        assert contact_page.failure_message.text == expected_result

    def test_send_empty_message(self, get_contact_page):
        """ Test sending a message without any text. """
        contact_page = get_contact_page
        contact_page.contact_email.input_text('testing@o2.pl')
        contact_page.order_reference.input_text('123456')
        contact_page.send_message_button.click()
        expected_result = 'The message cannot be blank.'
        assert contact_page.failure_message.text == expected_result

    def test_send_message_without_email_address(self, get_contact_page):
        """ Test sending a message without contact email address. """
        contact_page = get_contact_page
        contact_page.order_reference.input_text('123456')
        contact_page.message_text_area.input_text('This is test message')
        contact_page.send_message_button.click()
        expected_result = 'Invalid email address.'
        assert contact_page.failure_message.text == expected_result





