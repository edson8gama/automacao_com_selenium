from selenium.webdriver.common.by import By
from sampleTricentisCadastro import SampleTricentisCadastro


class FrmVehicleData(object):
    def __init__(self, teste):
        self.driver = teste.driver
        self.VehicleType = teste.VehicleType

    def viewfrm_entervehicledata(self):
        self.driver.find_element(By.ID, "entervehicledata").click()

    def make(self, make=''):
        self.driver.find_element(By.ID, "make").click()
        dropdown = self.driver.find_element(By.ID, "make")
        dropdown.find_element(By.XPATH, f"//option[. = '{make}']").click()

    def model(self, model=''):
        try:
            self.driver.find_element(By.ID, "model").is_displayed()
        except Exception:
            pass
        else:
            self.driver.find_element(By.ID, "model").click()
            dropdown = self.driver.find_element(By.ID, "model")
            dropdown.find_element(By.XPATH, f"//option[. = '{model}']").click()

    def cylindercapacity(self, cylindercapacity=''):
        try:
            self.driver.find_element(By.ID, "cylindercapacity").is_displayed()
        except Exception:
            pass
        else:
            self.driver.find_element(By.ID, "cylindercapacity").send_keys(cylindercapacity)

    def engineperformance(self, engineperformance=''):
        self.driver.find_element(By.ID, "engineperformance").send_keys(engineperformance)

    def dateofmanufacture(self, dateofmanufacture=''):
        self.driver.find_element(By.ID, "dateofmanufacture").send_keys(dateofmanufacture)

    # Falta Number of Seats, se for Motorcycle (id="numberofseatsmotorcycle")

    # Falta Right Hand drive

    def numberofseats(self, numberofseats=''):
        if 'auto' in self.VehicleType:
            self.driver.find_element(By.ID, "numberofseats").click()
            dropdown = self.driver.find_element(By.ID, "numberofseats")
            dropdown.find_element(By.XPATH, f"//option[. = '{numberofseats}']").click()
        else:
            self.driver.find_element(By.ID, "numberofseatsmotorcycle").click()
            dropdown = self.driver.find_element(By.ID, "numberofseatsmotorcycle")
            dropdown.find_element(By.XPATH, f"//option[. = '{numberofseats}']").click()

    def fuel(self, fuel=''):
        self.driver.find_element(By.ID, "fuel").click()
        dropdown = self.driver.find_element(By.ID, "fuel")
        dropdown.find_element(By.XPATH, f"//option[. = '{fuel}']").click()

    # Falta Payload

    # Falta Total Weight

    def listprice(self, listprice=''):
        self.driver.find_element(By.ID, "listprice").send_keys(listprice)

    def licenseplatenumber(self, licenseplatenumber=''):
        self.driver.find_element(By.ID, "licenseplatenumber").send_keys(licenseplatenumber)

    def annualmileage(self, annualmileage=''):
        self.driver.find_element(By.ID, "annualmileage").send_keys(annualmileage)

    def nextenterinsurantdata(self):
        self.driver.find_element(By.ID, "nextenterinsurantdata").click()
