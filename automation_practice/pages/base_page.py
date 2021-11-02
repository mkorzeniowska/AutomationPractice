class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)
        
    @property
    def title(self):
        title = self.driver.title
        return title

    @property
    def page_source(self):
        page_source = self.driver.page_source
        return page_source
