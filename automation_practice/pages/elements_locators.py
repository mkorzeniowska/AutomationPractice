from selenium.webdriver.common.by import By
from .locator import Locator
# Locators for all critical elements used in tests
# Home page


class HomePageLocators:

    SIGNATURE_TEXT_XPATH = Locator(by=By.XPATH, value='//div/h1')
    CONTACT_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='div#contact-link')
    SIGN_IN_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='a[title="Log in to your customer account"]')
    SEARCH_INPUT_CSS = Locator(by=By.CSS_SELECTOR, value='#search_query_top')
    SEARCH_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='button[name="submit_search"]')
    CART_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='a[title="View my shopping cart"] b')

# shopping cart value text xpath - when empty
    CART_EMPTY_XPATH = Locator(by=By.XPATH, value='//span[@class="ajax_cart_no_product"]')
    CART_QUANTITY_XPATH = Locator(by=By.XPATH, value='//span[@class="ajax_cart_quantity unvisible"]')
# shopping cart value text when 1 product
    CART_QUANTITY_TEXT_XPATH = Locator(by=By.XPATH, value='//span[@class="ajax_cart_product_txt unvisible"]')
# shopping cart value text when > 1 product
    CART_QUANTITY_TEXT_S = Locator(by=By.XPATH, value='//span[@class="ajax_cart_product_txt_s unvisible"]')

    MENU_WOMEN_TAB_CSS = Locator(by=By.CSS_SELECTOR, value='a[title="Women"]')
    MENU_DRESSES_TAB_XPATH = Locator(by=By.XPATH, value='//*[@id="block_top_menu"]/ul/li[2]/a')
    MENU_TSHIRTS_TAB_XPATH = Locator(by=By.XPATH, value='//*[@id="block_top_menu"]/ul/li[3]/a')
    POPULAR_TAB_XPATH = Locator(by=By.XPATH, value='//a[@class="homefeatured"]')
    BESTSELLERS_TAB_XPATH = Locator(by=By.XPATH, value='//a[@class="blockbestsellers"]')


class AuthenticationPageLocators:
    pass
