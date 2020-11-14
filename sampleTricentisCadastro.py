from WebDriver import WebDriver
from selenium.webdriver.common.by import By


class SampleTricentisCadastro(WebDriver):
    def start(self, vehicle_type='nav_automobile'):
        """

        :param vehicle_type: IDs nav_automobile, nav_truck, nav_motorcycle ou nav_camper
        :return:
        """
        self.VehicleType = vehicle_type
        self.setup_method('http://sampleapp.tricentis.com/101/app.php')
        self.driver.find_element(By.ID, f'{self.VehicleType}').click()

    def resolucao(self, maximiza=True, custom=(0, 0)):
        if maximiza:
            self.driver.maximize_window()
        else:
            self.driver.set_window_size(custom[0], custom[1])
