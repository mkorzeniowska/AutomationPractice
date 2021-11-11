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
        """ Test of adding a product to the cart. """
        expected_result = 'Product successfully added to your shopping cart'
        women_page = get_women_page
        women_page.add_product_to_cart('Printed Dress', '3')
        result = women_page.success_message.text
        women_page.driver.find_element(by=By.CSS_SELECTOR, value='span[title="Close window"]').click()
        assert result == expected_result

    def test_len_product_list(self, get_women_page):
        """ Test for length of the product list. """
        women_page = get_women_page
        product_list = women_page.create_product_list()
        assert (len(product_list)) == 7

    def test_page_heading_counter(self, get_women_page):
        """ Test for check a product counter on page heading. """
        women_page = get_women_page
        product_list = women_page.create_product_list()
        expected_result = women_page.get_page_heading_counter_text(product_list)
        assert women_page.page_heading_counter.text == expected_result

    def test_quick_view(self, get_women_page):
        """ Test a quick view for selected product. """
        women_page = get_women_page
        women_page.get_quick_view('Blouse', '2')
        iframe = women_page.driver.find_element(by=By.CSS_SELECTOR, value='iframe')
        women_page.driver.switch_to.frame(iframe)
        product_name = women_page.driver.find_element(by=By.CSS_SELECTOR, value='h1[itemprop="name"]')
        assert product_name.text == 'Blouse'
        women_page.driver.switch_to.default_content()
        women_page.driver.find_element(by=By.XPATH, value='//a[@title="Close"]').click()

    def test_subcategories_tops(self, get_women_page):
        """ Test tab for subcategories tops. """
        women_page = get_women_page
        women_page.click_subcategories_tops()
        assert women_page.title == 'Tops - My Store'
        women_page.go()

    def test_subcategories_dresses(self, get_women_page):
        """ Test tab for subcategories dresses. """
        women_page = get_women_page
        women_page.click_subcategories_dresses()
        assert women_page.title == 'Dresses - My Store'
        women_page.go()

