from pytest import fixture
from config import Config


@fixture(scope="session")
def browser(request):
    cfg = Config()
    driver = cfg.driver
    return driver
