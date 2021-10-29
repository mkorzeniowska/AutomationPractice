from pages.authentication_page import AuthenticationPage
from pages.home_page import HomePage
from selenium import webdriver


class AuthenticationPageTests:

    def test_sign_in(self, browser):
        login_page = AuthenticationPage(browser)
        login_page.go()
        # login_page.login(email='kotytrzy@o2.pl', password='5fEb.5aBbmKN3RK')
        assert login_page.title == 'Login - My Store'









