from selenium.webdriver.common.by import By
from sampleTricentisCadastro import SampleTricentisCadastro


class FrmProductData(SampleTricentisCadastro):
    def __init__(self, teste):
        self.driver = teste.driver

    def viewfrm_enterproductdata(self):
        self.driver.find_element(By.ID, "enterproductdata").click()

    def startdate(self, startdate=''):
        self.driver.find_element(By.ID, "startdate").send_keys(startdate)

    def insurancesum(self, insurancesum_cod):
        """
        - Soma do segurao.
        :param insurancesum_cod: Codigo dos valores, inteiro, 1 é reservado, primeiro valor começa no 2.
        :return:
        """
        self.driver.find_element(By.ID, "insurancesum").click()
        dropdown = self.driver.find_element(By.ID, "insurancesum")
        dropdown.find_element(By.XPATH, f'//*[@id="insurancesum"]/option[{insurancesum_cod}]').click()

    def merit_rating(self, merit_rating=''):
        self.driver.find_element(By.ID, "meritrating").click()
        dropdown = self.driver.find_element(By.ID, "meritrating")
        dropdown.find_element(By.XPATH, f"//option[. = '{merit_rating}']").click()

    def damage_insurance(self, damageinsurance=''):
        self.driver.find_element(By.ID, "damageinsurance").click()
        dropdown = self.driver.find_element(By.ID, "damageinsurance")
        dropdown.find_element(By.XPATH, f"//option[. = '{damageinsurance}']").click()

    def optional_products(self, optional_products_cod):
        self.driver.find_element(By.XPATH,
                                 '//*[@id="insurance-form"]'
                                 + f'/div/section[3]/div[5]/p/label[{optional_products_cod}]').click()

    def courtsy_car(self, courtsy_car_cod):
        self.driver.find_element(By.ID, "courtesycar").click()
        dropdown = self.driver.find_element(By.ID, "courtesycar")
        dropdown.find_element(By.XPATH, f'//*[@id="courtesycar"]/option[{courtsy_car_cod}]').click()

    def nextselectpriceoption(self):
        self.driver.find_element(By.ID, "nextselectpriceoption").click()
