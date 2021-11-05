from pytest import mark
from selenium.webdriver.common.by import By
from pages.women_page import WomenPage


@mark.womenpage
class WomenPageTests:

    def test_get_list_view(self, get_women_page):
        """ Test for get a list view. """
        women_page = get_women_page
        women_page.view_list_icon.click()

    def test_get_grid_view(self, get_women_page):
        """ Test for get a grid view. """
        women_page = get_women_page
        women_page.view_grid_icon.click()


    def test_add_product_to_cart(self, get_women_page):
        expected_result = 'Product successfully added to your shopping cart'
        women_page = get_women_page
        women_page.add_product_to_cart('Printed Dress', '3')
        result = women_page.success_message.text
        assert result == expected_result
