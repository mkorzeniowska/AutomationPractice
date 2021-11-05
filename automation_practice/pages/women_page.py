from .base_page import BasePage
from .base_element import BaseElement
from .elements_locators import WomenPageLocators as WP
from .elements_locators import HomePageLocators as HP
from .locator import Locator
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
        return BaseElement(driver=self.driver, locator=WP.SUBCATEGORIES_DRESSES_CSS)

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
    def quick_view(self):
        return BaseElement(driver=self.driver, locator=WP.QUICK_VIEW_XPATH)

    @property
    def add_to_cart_button(self):
        return self.driver.find_element(by=By.XPATH, value='//span[contains(text(), "Add to cart")]')

    @property
    def success_message(self):
        return BaseElement(driver=self.driver, locator=WP.ADDED_MESSAGE_SUCCESS_XPATH)

    @property
    def cart_empty(self):
        return BaseElement(driver=self.driver, locator=HP.CART_EMPTY_XPATH)



    def create_product_list(self):
        """ Function to create a list of all products for the Women category. """
        product_list = []
        for product in self.product_container:
            product_list.append(product)
        return product_list

    def add_product_to_cart(self, selected_product, product_id):
        hover = ActionChains(self.driver)
        products = self.driver.find_elements(by=By.XPATH, value='//div[@class="product-container"]')
        for product in products:
            if selected_product in product.text:
                print(product.text)
                hover.move_to_element(product).perform()
                # add_to_cart = self.driver.find_element(by=By.XPATH, value='//a[@title="' + selected_product + '"]/../../div[2]/a[1]')
                add_to_cart = self.driver.find_element(by=By.CSS_SELECTOR, value='[data-id-product="' + product_id + '"].btn')
                hover.move_to_element(add_to_cart).click().perform()
                break
        # self.driver.implicitly_wait(10)
