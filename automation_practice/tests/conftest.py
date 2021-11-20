import json
from pytest import fixture
from config import Config
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage
from pages.registration_page import RegistrationPage
from pages.contact_page import ContactPage
from pages.women_page import WomenPage

# data for registration tests
data_path = 'data/test_registration.json'
# data for login tests
data_path2 = 'data/test_login.json'


def load_test_data(path):
    """ Function to load test dana from json file to dict. """
    with open(path) as test_data:
        data = json.load(test_data)
        yield data


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


@fixture(scope='function')
def get_authentication_page(request, browser):
    authentication_page = AuthenticationPage(driver=browser)
    authentication_page.go()
    title = authentication_page.title
    driver = authentication_page.driver
    yield authentication_page


@fixture(scope='function')
def get_registration_page(request, browser, get_authentication_page, user_test_data):
    test_data = user_test_data
    auth_page = get_authentication_page
    auth_page.create_account(test_data['New_email'])
    registration_page = RegistrationPage(driver=browser)
    title = registration_page.title
    driver = registration_page.driver
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
    driver = women_page.driver
    yield women_page


@fixture(params=load_test_data(data_path2), scope='function')
def user_test_data(request):
    data = request.param
    yield data

