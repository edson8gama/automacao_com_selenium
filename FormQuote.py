from selenium.webdriver.common.by import By
from sampleTricentisCadastro import SampleTricentisCadastro


class FrmQuote(SampleTricentisCadastro):
    def __init__(self, teste):
        self.driver = teste.driver

    def viewfrm_sendquote(self):
        self.driver.find_element(By.ID, "sendquote").click()

    def email(self, email=''):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def phone(self, phone=''):
        self.driver.find_element(By.ID, "phone").send_keys(phone)

    def username(self, username=''):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def password(self, password=''):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def confirm_password(self, confirm_password=''):
        self.driver.find_element(By.ID, "confirmpassword").send_keys(confirm_password)

    def send_email(self):
        self.driver.find_element(By.ID, "sendemail").click()

    def confirm(self):
        from time import sleep

        id_janela = self.driver.current_window_handle
        self.driver.switch_to_window(id_janela)
        sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".confirm").click()
