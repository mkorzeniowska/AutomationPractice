from pytest import fixture
from config import Config
from pages.home_page import HomePage


@fixture(scope="session")
def browser(request):
    cfg = Config()
    driver = cfg.driver
    driver.maximize_window()
    yield driver
    driver.close()


@fixture(scope='class')
def load_home_page(request, browser):
        home_page = HomePage(driver=browser)
        home_page.go()
        title = home_page.title
        yield home_page


