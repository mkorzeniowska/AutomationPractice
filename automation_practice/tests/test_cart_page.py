from pytest import mark
from selenium.webdriver.common.by import By
from pages.authentication_page import AuthenticationPage


@mark.cart
class CartPageTests:

    @mark.purchase_product
    @mark.remove_product
    def test_cart_page_title(self, setup_for_cart):
        cart_page = setup_for_cart
        assert cart_page.title == 'Order - My Store'

    @mark.purchase_product
    def test_check_total_price(self, get_cart_page):
        cart_page = get_cart_page
        assert cart_page.check_total_price() == '$28.00'

    @mark.smoke
    @mark.purchase_product
    def test_purchase_product_from_cart(self, get_cart_page, user_test_data):
        cart_page = get_cart_page
        cart_page.checkout_button.click()
        login_page = AuthenticationPage(driver=cart_page.driver)
        test_data = user_test_data
        login_page.login(email=test_data['valid_credentials']['email'],
                         password=test_data['valid_credentials']['password'])
        cart_page.purchase_product()
        expected_result = 'Your order on My Store is complete.'
        result = cart_page.driver.find_element(by=By.CSS_SELECTOR, value='p[class="cheque-indent"] strong[class="dark"]')
        assert result.text == expected_result

    @mark.smoke
    @mark.remove_product
    def test_remove_product_from_cart(self, get_cart_page):
        expected_result = 'Your shopping cart is empty.'
        cart_page = get_cart_page
        cart_page.remove_product_from_cart('3')
        result = cart_page.empty_alert.text
        assert result == expected_result
