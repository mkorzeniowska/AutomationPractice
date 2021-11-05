from pytest import mark
import json
from selenium.webdriver.common.by import By
from pages.women_page import WomenPage


@mark.womenpage
class WomenPageTests:

    def test_get_list_view(self, get_women_page):
        """ Test a list view works as expected. Assert with local storage. """
        expected_view = 'list'
        women_page = get_women_page
        women_page.view_list_icon.click()
        view_in_storage = women_page.driver.execute_script('return localStorage.getItem("display")')
        assert json.loads(view_in_storage) == expected_view

    def test_get_grid_view(self, get_women_page):
        """ Test a grid view works as expected. Assert with local storage. """
        expected_view = 'grid'
        women_page = get_women_page
        women_page.view_grid_icon.click()
        view_in_storage = women_page.driver.execute_script('return localStorage.getItem("display")')
        assert json.loads(view_in_storage) == expected_view

    def test_add_product_to_cart(self, get_women_page):
        expected_result = 'Product successfully added to your shopping cart'
        women_page = get_women_page
        women_page.add_product_to_cart('Printed Dress', '3')
        result = women_page.success_message.text
        assert result == expected_result
