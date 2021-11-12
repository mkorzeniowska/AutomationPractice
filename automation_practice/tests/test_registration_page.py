from pytest import mark
from selenium.webdriver.common.by import By


@mark.registrationpage
class RegistrationPageTests:

    def test_account_registration(self, get_registration_page, user_test_data):
        # expected_result = 'Welcome to your account. Here you can manage all of your personal information and orders.'
        registration_page = get_registration_page
        data = user_test_data
        registration_page.register_account(data)
        assert registration_page.title == 'My account - My Store'

    def test_account_registration_with_used_email(self, get_authentication_page, user_test_data):
        expected_result = 'An account using this email address has already been registered. Please enter a valid password or request a new one.'
        registration_page = get_authentication_page
        data = user_test_data
        registration_page.create_account(data)
        registration_page.driver.implicitly_wait(10)
        result = registration_page.driver.find_element(by=By.CSS_SELECTOR, value='div[id="create_account_error"] ol li')
        assert result.text == expected_result
