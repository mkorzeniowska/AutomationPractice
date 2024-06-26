from pytest import mark


@mark.homepage
class HomePageTests:

    @mark.browsertest
    def test_env(self, env):
        assert env == 'firefox'

    @mark.browsertest
    def test_browser(self, get_home_page):
        home = get_home_page
        assert home.title == 'My Store'

    @mark.smoke
    def test_loading_home_page(self, get_home_page):
        """ Home page loading test. Check for correct title. """
        home_page = get_home_page
        assert home_page.title == 'My Store'

    def test_contact_button_is_displayed(self, get_home_page):
        """ Check if contact button is displayed. """
        home_page = get_home_page
        assert home_page.contact_button.text == 'Contact us'

    def test_sign_in_button_is_displayed(self, get_home_page):
        """ Check if sign in button is displayed. """
        home_page = get_home_page
        assert home_page.sign_in_button.text == 'Sign in'

    def test_menu_women_tab_is_displayed(self, get_home_page):
        """ Check if Women tab is displayed. """
        home_page = get_home_page
        assert home_page.menu_women_tab.text == 'WOMEN'

    def test_menu_dresses_tab_is_displayed(self, get_home_page):
        """ Check if Dresses tab is displayed. """
        home_page = get_home_page
        assert home_page.menu_dresses_tab.text == 'DRESSES'

    def test_menu_tshirts_tab_is_displayed(self, get_home_page):
        """ Check if T-Shirts tab is displayed. """
        home_page = get_home_page
        assert home_page.menu_tshirts_tab.text == 'T-SHIRTS'

    def test_popular_tab_is_displayed(self, get_home_page):
        """ Check if Popular tab is displayed. """
        home_page = get_home_page
        assert home_page.popular_tab.text == 'POPULAR'

    def test_bestsellers_tab_is_displayed(self, get_home_page):
        """ Check if Bestsellers tab is displayed. """
        home_page = get_home_page
        assert home_page.bestsellers_tab.text == 'BEST SELLERS'

    def test_signature_text_is_displayed(self, get_home_page):
        """ Check if text on the bottom of page is displayed. """
        home_page = get_home_page
        assert home_page.signature_text.text == 'Automation Practice Website'




