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


class ContactPage:

    NAVIGATION_TAB_CSS = Locator(by=By.CSS_SELECTOR, value='.navigation_page')
    NAVIGATION_PAGE_HEADING_CSS = Locator(by=By.CSS_SELECTOR, value='.page-heading.bottom-indent')
    PAGE_SUBHEADING_TEXT = Locator(by=By.CSS_SELECTOR, value='.page-subheading')
    SELECT_SUBJECT_HEADING = Locator(by=By.ID, value='#id_contact')
    # select options :
    INPUT_EMAIL_CSS = Locator(by=By.ID, value='#email')
    INPUT_ORDER_REFERENCE_CSS = Locator(by=By.CSS_SELECTOR, value='#id_order')
    INPUT_FILE_XPATH = Locator(by=By.XPATH, value='//*[text()="No file selected"]')
    CHOOSE_FILE_BUTTON_XPATH = Locator(by=By.XPATH, value='//*[text()="Choose File"]')
    SEND_BUTTON_XPATH = Locator(by=By.XPATH, value='//*[text()="Send"]')
    MESSAGE_TEXTAREA_CSS = Locator(by=By.ID, value='#message')


class AuthenticationPageLocators:
    AUTHENTICATION_TAB_CSS = Locator(by=By.CSS_SELECTOR, value='.navigation_page')
    AUTHENTICATION_PAGE_HEADING_CSS = Locator(by=By.CSS_SELECTOR, value='.page-heading')

    CREATE_ACCOUNT_FORM_CSS = Locator(by=By.CSS_SELECTOR,
                                      value='form[id="create-account_form"] h3[class="page-subheading"]')
    CREATE_ACCOUNT_INPUT_EMAIL_CSS = Locator(by=By.ID, value='#email_create')
    CREATE_ACCOUNT_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='button[id="SubmitCreate"] span')

    REGISTERED_FORM_CSS = Locator(by=By.CSS_SELECTOR, value='form[id="login_form"] h3[class="page-subheading"]')
    REGISTERED_INPUT_EMAIL_CSS = Locator(by=By.ID, value='#email')
    REGISTERED_INPUT_PASS_CSS = Locator(by=By.ID, value='#passwd')
    FORGOT_PASSWORD_CSS = Locator(by=By.CSS_SELECTOR, value='a[title="Recover your forgotten password"]')
    SIGN_IN_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='button[id="SubmitLogin"] span')


