from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/text-box"
        self.full_name = (By.ID, "userName")
        self.email = (By.ID, "userEmail")
        self.current_address = (By.ID, "currentAddress")
        self.permanent_address = (By.ID, "permanentAddress")
        self.submit_btn = (By.ID, "submit")
        self.output_name = (By.ID, "name")

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, name, email, current_addr, permanent_addr):
        self.driver.find_element(*self.full_name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.current_address).send_keys(current_addr)
        self.driver.find_element(*self.permanent_address).send_keys(permanent_addr)

    def submit(self):
        self.driver.find_element(*self.submit_btn).click()

    def get_output_name(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.output_name)
        ).text
