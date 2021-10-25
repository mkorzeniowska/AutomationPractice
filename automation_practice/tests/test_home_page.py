from pages.home_page import StartPage


class HomePageTests:

    def test_loading_home_page(self, browser):
        start_page = StartPage(driver=browser)
        start_page.go()
        assert start_page.signature_text.text == 'Automation Practice Website'

