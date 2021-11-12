from selenium.webdriver.common.by import By
from .locator import Locator
# Locators for all key components used in testing


class HomePageLocators:

    SIGNATURE_TEXT_XPATH = Locator(by=By.XPATH, value='//div/h1')
    CONTACT_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='div#contact-link')
    SIGN_IN_BUTTON_CSS = Locator(by=By.LINK_TEXT, value='Sign in')
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

# my account button
    MY_ACCOUNT_BUTTON_ID = '//a[@ title = "View my customer account"]'


class ContactPageLocators:

    NAVIGATION_TAB_CSS = Locator(by=By.CSS_SELECTOR, value='.navigation_page')
    NAVIGATION_PAGE_HEADING_CSS = Locator(by=By.CSS_SELECTOR, value='.page-heading.bottom-indent')
    PAGE_SUBHEADING_TEXT = Locator(by=By.CSS_SELECTOR, value='.page-subheading')
    # send message form :
    SELECT_SUBJECT_HEADING_ID = Locator(by=By.ID, value='id_contact')
    INPUT_EMAIL_ID = Locator(by=By.ID, value='email')
    INPUT_ORDER_REFERENCE_CSS = Locator(by=By.CSS_SELECTOR, value='#id_order')
    INPUT_FILE_XPATH = Locator(by=By.XPATH, value='//*[text()="No file selected"]')
    CHOOSE_FILE_BUTTON_XPATH = Locator(by=By.XPATH, value='//*[text()="Choose File"]')
    SEND_BUTTON_XPATH = Locator(by=By.XPATH, value='//*[text()="Send"]')
    MESSAGE_TEXTAREA_ID = Locator(by=By.ID, value='message')
    # alert text:
    SUCCESS_MESSAGE_CSS = Locator(by=By.CSS_SELECTOR, value='.alert.alert-success')
    FAILURE_MESSAGE_CSS = Locator(by=By.CSS_SELECTOR, value='div[class="alert alert-danger"] ol li')


class AuthenticationPageLocators:
    AUTHENTICATION_TAB_CSS = Locator(by=By.CSS_SELECTOR, value='.navigation_page')
    AUTHENTICATION_PAGE_HEADING_CSS = Locator(by=By.CSS_SELECTOR, value='.page-heading')

    CREATE_ACCOUNT_FORM_CSS = Locator(by=By.CSS_SELECTOR,
                                      value='form[id="create-account_form"] h3[class="page-subheading"]')
    CREATE_ACCOUNT_INPUT_EMAIL_ID = Locator(by=By.ID, value='email_create')
    CREATE_ACCOUNT_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='button[id="SubmitCreate"] span')
    CREATE_ACCOUNT_ALERT_ID = Locator(by=By.ID, value='create_account_error')

    REGISTERED_FORM_CSS = Locator(by=By.CSS_SELECTOR, value='form[id="login_form"] h3[class="page-subheading"]')
    REGISTERED_INPUT_EMAIL_ID = Locator(by=By.ID, value='email')
    REGISTERED_INPUT_PASS_ID = Locator(by=By.ID, value='passwd')
    FORGOT_PASSWORD_CSS = Locator(by=By.CSS_SELECTOR, value='a[title="Recover your forgotten password"]')
    SIGN_IN_BUTTON_CSS = Locator(by=By.CSS_SELECTOR, value='button[id="SubmitLogin"] span')


class RegistrationPageLocators:

    # Your personal information:
    TITLE_MR_ID = Locator(by=By.ID, value='id_gender1')
    TITLE_MRS_ID = Locator(by=By.ID, value='id_gender2')
    INPUT_CUSTOMER_FIRSTNAME_ID= Locator(by=By.ID, value='customer_firstname')
    INPUT_CUSTOMER_LASTNAME_ID = Locator(by=By.ID, value='customer_lastname')
    INPUT_EMAIL_ID = Locator(by=By.ID, value='email')
    INPUT_PASSWORD_ID = Locator(by=By.ID, value='passwd')
    #date of birth:
    SELECT_DAYS_ID = Locator(by=By.ID, value='days')
    SELECT_MONTHS_ID = Locator(by=By.ID, value='months')
    SELECT_YEARS_ID = Locator(by=By.ID, value='years')
    NEWSLETTER_CHECKBOX_ID = Locator(by=By.ID, value='newsletter')
    SPECIAL_OFFERS_CHECKBOX_ID = Locator(by=By.ID, value='optin')
    #Your address:
    INPUT_FIRSTNAME_ID = Locator(by=By.ID, value='firstname')
    INPUT_LASTNAME_ID = Locator(by=By.ID, value='lastname')
    # INPUT_COMPANY_ID = Locator(by=By.ID, value='company')
    INPUT_ADDRESS1_ID = Locator(by=By.ID, value='address1')
    # INPUT_ADDRESS2_ID = Locator(by=By.ID, value='address2')
    INPUT_CITY_ID = Locator(by=By.ID, value='city')
    SELECT_STATE_ID = Locator(by=By.ID, value='id_state')
    INPUT_ZIPCODE_ID = Locator(by=By.ID, value='postcode')
    SELECT_COUNTRY_ID = Locator(by=By.ID, value='id_country')
    # INPUT_OTHER_INFO_ID = Locator(by=By.ID, value='other')
    # INPUT_HOME_PHONE_ID = Locator(by=By.ID, value='phone')
    INPUT_MOBILE_PHONE_ID = Locator(by=By.ID, value='phone_mobile')
    INPUT_ALIAS_ADDRESS_ID = Locator(by=By.ID, value='alias')
    REGISTER_BUTTON_ID = Locator(by=By.ID, value='submitAccount')
    ALERT_CSS = Locator(by=By.CSS_SELECTOR, value='.alert.alert-danger')


class WomenPageLocators:

    WOMEN_PAGE_HEADING = Locator(by=By.CSS_SELECTOR, value='span[class="cat-name"]')
    # Product counter:
    PAGE_HEADING_COUNTER_CSS = Locator(by=By.CSS_SELECTOR, value='span[class="heading-counter"]')
    SUBCATEGORIES_TOPS_XPATH = Locator(by=By.XPATH, value='//a[@title="Tops"]//img[@class="replace-2x"]')
    SUBCATEGORIES_DRESSES_XPATH = Locator(by=By.XPATH, value='//a[@title="Dresses"]//img[@class="replace-2x"]')
    PRODUCT_CONTAINER_XPATH = Locator(by=By.XPATH, value='//div[@class="product-container"]')
    # Sort by: Price: Lowest first, Price: Highest first, Product name: A to Z, Product name: Z to A, In Stock,
    # Reference: Lowest first, Reference: Highest first,
    SELECT_SORT_ID = Locator(by=By.ID, value='selectProductSort')
    # Message:
    ADDED_MESSAGE_SUCCESS_XPATH = Locator(by=By.XPATH,
                                          value='//h2[normalize-space()="Product successfully added to your shopping cart"]')
    # View
    VIEW_GRID_CSS = Locator(by=By.CSS_SELECTOR, value='.icon-th-large')
    VIEW_LIST_CSS = Locator(by=By.CSS_SELECTOR, value='.icon-th-list')
