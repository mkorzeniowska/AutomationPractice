import json
from pytest import fixture
from config import Config
from pages.home_page import HomePage
from pages.authentication_page import AuthenticationPage
from pages.registration_page import RegistrationPage
from pages.contact_page import ContactPage
from pages.women_page import WomenPage
from pages.cart_page import CartPage

# TO DO: parametrize data_path
# data for registration tests
data_path = 'data/test_registration.json'
# data for login tests
data_path2 = 'data/test_login.json'


def load_test_data(path):
    """ Function to load test data from json file to dict. """
    with open(path) as test_data:
        data = json.load(test_data)
        yield data


def pytest_addoption(parser):
    """ Function to add option from command line. """
    parser.addoption(
        "--env",
        action="store",
        help="Browser to run tests"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption('env')


@fixture(scope='session')
def browser(request, env):
    """ Function to initialize the browser."""
    cfg = Config(env)
    driver = cfg.driver
    driver.maximize_window()
    yield driver
    driver.quit()


@fixture(scope='class')
def get_home_page(request, browser):
    home_page = HomePage(driver=browser)
    home_page.go()
    yield home_page


@fixture(scope='class')
def get_authentication_page(request, browser):
    authentication_page = AuthenticationPage(driver=browser)
    authentication_page.go()
    yield authentication_page


@fixture(scope='function')
def get_registration_page(request, browser, get_authentication_page, user_test_data):
    test_data = user_test_data
    auth_page = get_authentication_page
    auth_page.create_account(test_data['New_email'])
    registration_page = RegistrationPage(driver=browser)
    yield registration_page


@fixture(scope='function')
def get_contact_page(request, browser):
    contact_page = ContactPage(driver=browser)
    contact_page.go()
    yield contact_page


@fixture(scope='class')
def get_women_page(request, browser):
    women_page = WomenPage(driver=browser)
    women_page.go()
    yield women_page


@fixture(scope='class')
def get_cart_page(request, browser):
    cart_page = CartPage(driver=browser)
    cart_page.go()
    yield cart_page


@fixture(scope='function')
def setup_for_cart(request, browser, get_women_page):
    """ Setup for test the product cart. """
    women_page = get_women_page
    women_page.add_product_to_cart('Printed Dress', '3')
    women_page.close_button.click()
    women_page.click_cart_button()
    cart_page = CartPage(driver=browser)
    yield cart_page


@fixture(params=load_test_data(data_path2), scope='function')
def user_test_data(request):
    data = request.param
    yield data

