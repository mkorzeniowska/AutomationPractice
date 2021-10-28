from pages.home_page import HomePage


class HomePageTests:
    def test_loading_home_page(self, load_home_page):
        home_page = load_home_page
        assert home_page.title == 'My Store'

    def test_contact_button_text_is_displayed(self, load_home_page):
        home_page = load_home_page
        assert home_page.contact_button.text == 'Contact us'

    def test_sign_in_button_text_is_displayed(self, load_home_page):
        home_page = load_home_page
        assert home_page.sign_in_button.text == 'Sign in'


    def test_menu_women_tab_text_is_displayed(self, load_home_page):
        home_page = load_home_page
        assert home_page.menu_women_tab.text == 'WOMEN'

    def test_menu_dresses_text_tab_is_displayed(self, load_home_page):
        home_page = load_home_page
        assert home_page.menu_dresses_tab.text == 'DRESSES'

    def test_menu_tshirts_tab_text_is_displayed(self, load_home_page):
        home_page = load_home_page
        assert home_page.menu_tshirts_tab.text == 'T-SHIRTS'

    def test_signature_text_is_displayed(self, load_home_page):
        home_page = load_home_page
        assert home_page.signature_text.text == 'Automation Practice Website'


