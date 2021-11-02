import re

from pages.authentication_page import AuthenticationPage
from pages.home_page import HomePage
from pytest import mark


@mark.loginpage
class AuthenticationPageTests:

    @mark.smoke
    @mark.signin
    def test_redirect_from_home_page(self, browser, get_home_page):
        home_page = get_home_page
        authentication_page = home_page.click_sign_in_button()
        assert authentication_page.authentication_header.text == 'AUTHENTICATION'

    @mark.signin
    def test_sign_in_page_title(self, get_authentication_page):
        login_page = get_authentication_page
        assert login_page.title == 'Login - My Store'

    @mark.signin
    def test_sign_in(self, get_authentication_page):
        authentication_page = get_authentication_page
        authentication_page.login(email='kotytrzy@o2.pl', password='5fEb.5aBbmKN3RK')
        expected_result = 'Welcome to your account.'
        result = re.search(expected_result, authentication_page.page_source)
        assert result is not None









