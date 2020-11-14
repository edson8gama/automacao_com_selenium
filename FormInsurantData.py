from selenium.webdriver.common.by import By
from sampleTricentisCadastro import SampleTricentisCadastro


class FrmInsurantData(SampleTricentisCadastro):
    def __init__(self, teste):
        self.driver = teste.driver

    def viewfrm_enterinsurantdata(self):
        self.driver.find_element(By.ID, "enterinsurantdata").click()

    def firstname(self, firstname=''):
        self.driver.find_element(By.ID, "firstname").send_keys(firstname)

    def lastname(self, lastname=''):
        self.driver.find_element(By.ID, "lastname").send_keys(lastname)

    def birthdate(self, birthdate=''):
        self.driver.find_element(By.ID, "birthdate").send_keys(birthdate)

    def gender(self, gender_cod):
        self.driver.find_element(By.CSS_SELECTOR,
                                 f".group:nth-child(2) > .ideal-radiocheck-label:nth-child({gender_cod})"
                                 + "> .ideal-radio").click()

    def streetaddress(self, streetaddress=''):
        self.driver.find_element(By.ID, "streetaddress").send_keys(streetaddress)

    def country(self, country=''):
        self.driver.find_element(By.ID, "country").click()
        dropdown = self.driver.find_element(By.ID, "country")
        dropdown.find_element(By.XPATH, f"//option[. = '{country}']").click()

    def zipcode(self, zipcode=''):
        self.driver.find_element(By.ID, "zipcode").send_keys(zipcode)

    def city(self, city=''):
        self.driver.find_element(By.ID, "city").send_keys(city)

    def occupation(self, occupation=''):
        self.driver.find_element(By.ID, "occupation").click()
        dropdown = self.driver.find_element(By.ID, "occupation")
        dropdown.find_element(By.XPATH, f"//option[. = '{occupation}']").click()

    def hobbies(self, hobbies_cod):
        self.driver.find_element(By.CSS_SELECTOR,
                                 f".ideal-radiocheck-label:nth-child({hobbies_cod}) > .ideal-check").click()

    def website(self, website=''):
        self.driver.find_element(By.ID, "website").send_keys(website)

    def picture(self, path=''):
        self.driver.find_element(By.ID, "picturecontainer").send_keys(path)

    def nextenterproductdata(self):
        self.driver.find_element(By.ID, "nextenterproductdata").click()
