from pytest import mark
from selenium.webdriver.common.by import By

@mark.cart
class CartPageTests:

    def test_cart_page_title(self, setup_for_cart):
        cart_page = setup_for_cart
        assert cart_page.title == 'Order - My Store'

    def test_check_total_price(self, get_cart_page):
        cart_page = get_cart_page
        assert cart_page.check_total_price() == '$28.00'

    def test_remove_product_from_cart(self, get_cart_page):
        expected_result = 'Your shopping cart is empty.'
        cart_page = get_cart_page
        cart_page.delete_button.click()
        result = cart_page.empty_alert.text
        assert result == expected_result
