from selenium import webdriver


class WebDriver(object):
    def setup_method(self, url):
        # self.driver = webdriver.Edge('C:\\Temp\\EdgeWeDriver\\msedgedriver.exe')
        self.driver = webdriver.Chrome('C:\\Temp\\ChromeDriver\\chromedriver.exe')
        # self.vars = {}
        self.driver.get(url)

    def teardown_method(self):
        self.driver.quit()
