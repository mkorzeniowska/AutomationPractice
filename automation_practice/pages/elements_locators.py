# Locators for all critical elements used in tests
# Home page
class HomePageLocators:
# signature text css
    signature_text_css = '//div/h1'
# Contact button
    contact_button_css = 'div#contact-link'
# Sign in button
    sign_in_button_css = 'a[title="Log in to your customer account"]'
# search input bar css id
    search_input_id = '#search_query_top'
# search button css name
    search_button_css = 'button[name="submit_search"]'
# shopping cart button css
    shopping_cart_button_css = 'a[title="View my shopping cart"] b'
# shopping cart value text xpath - when empty
    shopping_cart_empty_xpath = '//span[@class="ajax_cart_no_product"]'
    shopping_cart_quantity_xpath = '//span[@class="ajax_cart_quantity unvisible"]'
# shopping cart value text when 1 product
    shopping_cart_quantity_text = '//span[@class="ajax_cart_product_txt unvisible"]'
# shopping cart value text when > 1 product
    shopping_cart_quantity_text_s = '//span[@class="ajax_cart_product_txt_s unvisible"]'
# Main menu - Women tab css
    menu_women_tab_css = 'a[title="Women"]'
# Main menu - Dresses tab xpath
    menu_dresses_tab_xpath = '//*[@id="block_top_menu"]/ul/li[2]/a'
# Main menu - T-shirts tab xpath
    menu_tshirts_tab_xpath = '//*[@id="block_top_menu"]/ul/li[3]/a'
# Popular tab xpath
    popular_tab_xpath = '//a[@class="homefeatured"]'
# Bestsellers tab xpath
    bestsellers_tab_xpath = '//a[@class="blockbestsellers"]'


class AuthenticationPageLocators:
    pass
