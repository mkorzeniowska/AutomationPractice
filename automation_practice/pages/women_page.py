from .base_page import BasePage
from .base_element import BaseElement
from .elements_locators import WomenPageLocators as WP
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class WomenPage(BasePage):

    url = 'http://automationpractice.com/index.php?id_category=3&controller=category'

    @property
    def page_heading_counter(self):
        return BaseElement(driver=self.driver, locator=WP.PAGE_HEADING_COUNTER_CSS)

    @property
    def subcategories_tops(self):
        return BaseElement(driver=self.driver, locator=WP.SUBCATEGORIES_TOPS_XPATH)

    @property
    def subcategories_dresses(self):
        return BaseElement(driver=self.driver, locator=WP.SUBCATEGORIES_DRESSES_XPATH)

    @property
    def product_container(self):
        return self.driver.find_elements(by=By.XPATH, value='//div[@class="product-container"]')

    @property
    def sort_dropbox(self):
        return BaseElement(driver=self.driver, locator=WP.SELECT_SORT_ID)

    @property
    def view_grid_icon(self):
        return BaseElement(driver=self.driver, locator=WP.VIEW_GRID_CSS)

    @property
    def view_list_icon(self):
        return BaseElement(driver=self.driver, locator=WP.VIEW_LIST_CSS)

    @property
    def success_message(self):
        return BaseElement(driver=self.driver, locator=WP.ADDED_MESSAGE_SUCCESS_XPATH)

    def create_product_list(self):
        """ Function to create a list of all products for the Women category. """
        product_list = []
        for product in self.product_container:
            product_list.append(product)
        return product_list

    def add_product_to_cart(self, selected_product, product_id):
        """ Function for add product to the cart. """
        hover = ActionChains(self.driver)
        products = self.driver.find_elements(by=By.XPATH, value='//div[@class="product-container"]')
        for product in products:
            if selected_product in product.text:
                print(product.text)
                hover.move_to_element(product).perform()
                add_to_cart = self.driver.find_element(by=By.CSS_SELECTOR,
                                                       value='[data-id-product="' + product_id + '"].btn')
                hover.move_to_element(add_to_cart).click().perform()
                break
        # self.driver.implicitly_wait(10)

    def get_page_heading_counter_text(self, product_list):
        """ Function to get product counter from page heading. """
        products = len(product_list)
        if products == 1:
            message = 'There is 1 product.'
        else:
            message = 'There are ' + str(products) + ' products.'
        return message

    def get_product_quantity_in_cart(self):
        """ Function to get the quantity of products in the cart. """
        number_of_products = self.driver.find_element(by=By.XPATH,
                                                      value='//span[@class="ajax_cart_quantity unvisible"]')
        if number_of_products.text == '1':
            product = self.driver.find_element(by=By.XPATH,
                                               value='//span[@class="ajax_cart_product_txt unvisible"]')
            result = number_of_products.text + ' ' + product.text
        else:
            products = self.driver.find_element(by=By.XPATH, value='//span[@class="ajax_cart_product_txt_s unvisible"]')
            result = number_of_products.text + ' ' + products.text
        return result

    def get_quick_view(self, selected_product, product_id):
        """ Function to get quick view of the selected product. """
        hover = ActionChains(self.driver)
        products = self.driver.find_elements(by=By.XPATH, value='//div[@class="product-container"]')
        for product in products:
            if selected_product in product.text:
                hover.move_to_element(product).perform()
                quick_view = self.driver.find_element(
                        by=By.XPATH,
                        value='//a[@class="quick-view"][@href="http://automationpractice.com/index.php?id_product='
                              + product_id + '&controller=product"]/span')
                hover.move_to_element(quick_view).click().perform()
                break
        self.driver.implicitly_wait(10)

    def click_subcategories_tops(self):
        self.subcategories_tops.click()

    def click_subcategories_dresses(self):
        self.subcategories_dresses.click()



