import re
from selenium.webdriver.common.by import By
from pytest import mark


@mark.loginpage
class AuthenticationPageTests:

    @mark.smoke
    @mark.signin
    def test_redirect_from_home_page(self, get_home_page):
        home_page = get_home_page
        authentication_page = home_page.click_sign_in_button()
        assert authentication_page.authentication_header.text == 'AUTHENTICATION'

    @mark.signin
    def test_authentication_page_title(self, get_authentication_page):
        login_page = get_authentication_page
        assert login_page.title == 'Login - My Store'

    @mark.smoke
    @mark.signin
    def test_sign_in_with_valid_credentials(self, get_authentication_page, user_test_data):
        authentication_page = get_authentication_page
        test_data = user_test_data
        authentication_page.login(email=test_data['valid_credentials']['email'],
                                  password=test_data['valid_credentials']['password'])
        expected_result = test_data['valid_credentials']['expected_result']
        result = re.search(expected_result, authentication_page.page_source)
        assert result is not None

    # warning, test dependency, do after sign in:
    @mark.smoke
    @mark.signout
    def test_sign_out(self, get_authentication_page):
        authentication_page = get_authentication_page
        authentication_page.driver.find_element(by=By.CSS_SELECTOR, value='a[title="Log me out"]').click()
        # TO DO: change assertion, test false positive
        assert authentication_page.title == 'Login - My Store'
        assert authentication_page.authentication_header.text == 'AUTHENTICATION'

    @mark.signin
    def test_sign_in_with_invalid_email(self, get_authentication_page, user_test_data):
        authentication_page = get_authentication_page
        test_data = user_test_data
        authentication_page.login(email=test_data['invalid_email']['email'],
                                  password=test_data['invalid_email']['password'])
        expected_result = test_data['invalid_email']['expected_result']
        result = authentication_page.driver.find_element(by=By.CSS_SELECTOR,
                                                         value='div[class="alert alert-danger"] ol li')
        assert result.text == expected_result

    def test_sign_in_with_invalid_password(self, get_authentication_page, user_test_data):
        authentication_page = get_authentication_page
        test_data = user_test_data
        authentication_page.login(email=test_data['invalid_password']['email'],
                                  password=test_data['invalid_password']['password'])
        expected_result = test_data['invalid_password']['expected_result']
        result = authentication_page.driver.find_element(by=By.CSS_SELECTOR,
                                                         value='div[class="alert alert-danger"] ol li')
        assert result.text == expected_result

    @mark.smoke
    def test_restore_password(self, get_authentication_page, user_test_data):
        authentication_page = get_authentication_page
        test_data = user_test_data
        authentication_page.restore_password(test_data['restore_password']['email'])
        expected_result = test_data['restore_password']['confirmation'] + test_data['restore_password']['email']
        result = authentication_page.driver.find_element(by=By.CSS_SELECTOR,
                                                         value='.alert.alert-success')
        assert result.text == expected_result




