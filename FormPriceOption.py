from selenium.webdriver.common.by import By
from sampleTricentisCadastro import SampleTricentisCadastro


class FrmPriceOption(SampleTricentisCadastro):
    def __init__(self, teste):
        self.driver = teste.driver

    def viewfrm_selectpriceoption(self):
        self.driver.find_element(By.ID, "selectpriceoption").click()

    def cod(self, price_option_cod):
        self.driver.find_element(By.CSS_SELECTOR, f".choosePrice:nth-child({price_option_cod}) > .ideal-radio").click()

    def nextsendquote(self):
        self.driver.find_element(By.ID, "nextsendquote").click()
