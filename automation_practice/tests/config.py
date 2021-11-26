from selenium import webdriver


class Config:
    def __init__(self, env):
        self.driver = {
            'chrome': webdriver.Chrome,
            'firefox': webdriver.Firefox,
            'edge': webdriver.Edge
        }[env]
        if env == 'chrome':
            self.driver = self.driver(options=webdriver.ChromeOptions().add_experimental_option('excludeSwitches',
                                                                                                ['enable-logging']))
        else:
            self.driver = self.driver()





