from pages.start_page import StartPage


class StartPageTests:

    def test_loading_start_page(self, browser):
        start_page = StartPage(driver=browser)
        start_page.go()
        assert start_page.signature_text.text == 'Automation Practice Website'

