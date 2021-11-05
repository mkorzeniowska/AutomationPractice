from pytest import fixture
from config import Config
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage
from pages.registration_page import RegistrationPage
from pages.contact_page import ContactPage
from pages.women_page import WomenPage


@fixture(scope="session")
def browser(request):
    cfg = Config()
    driver = cfg.driver
    driver.maximize_window()
    yield driver
    driver.close()


@fixture(scope='class')
def get_home_page(request, browser):
    home_page = HomePage(driver=browser)
    home_page.go()
    title = home_page.title
    yield home_page


@fixture(scope='class')
def get_authentication_page(request, browser):
    authentication_page = AuthenticationPage(driver=browser)
    authentication_page.go()
    title = authentication_page.title
    yield authentication_page


@fixture(scope='class')
def get_registration_page(request, browser):
    get_authentication_page.create_account_button.click()
    registration_page = RegistrationPage(driver=browser)
    title = registration_page.title
    yield registration_page


@fixture(scope='function')
def get_contact_page(request, browser):
    contact_page = ContactPage(driver=browser)
    contact_page.go()
    title = contact_page.title
    yield contact_page


@fixture(scope='class')
def get_women_page(request, browser):
    women_page = WomenPage(driver=browser)
    women_page.go()
    title = women_page.title
    yield women_page
