import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class clientsP:

    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(username)

    def password(self, password):
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)

    def login_btn(self):
        self.driver.find_element(By.XPATH, "//button[@class='col-md-12 btn btn-login pt-2 mt-4']").click()

    def settings(self):
        self.driver.find_element(By.CSS_SELECTOR, ".bg-transparent > img").click()

    def add_client(self):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-plus']").click()

    def client_name(self, client_name):
        self.driver.find_element(By.XPATH, "//input[@id='txtClientName']").send_keys(client_name)

    def clientNumber(self, clientNumber):
        self.driver.find_element(By.XPATH, "//input[@id='txtClientNumber']").send_keys(clientNumber)

    def status_drop(self):
        dropdown = self.driver.find_element(By.XPATH, "//select[@id='drpStatuses']")
        select = Select(dropdown)
        select.select_by_visible_text("Active")

    def Address(self, client_address):
        self.driver.find_element(By.XPATH, "//input[@id='txtAddress']").send_keys(client_address)

    def location(self, client_location):
        self.driver.find_element(By.XPATH, "//select[@id='drpLocations']").send_keys(client_location)

    def city(self, client_city):
        self.driver.find_element(By.CSS_SELECTOR, "#txtCity").send_keys(client_city)

    def state(self, client_state):
        self.driver.find_element(By.ID, "txtState").send_keys(client_state)

    def zip_code(self, client_zip):
        self.driver.find_element(By.ID, "txtZipCode").send_keys(client_zip)

    def client_website(self, client_website):
        self.driver.find_element(By.ID, "txtCompanyWebsite").send_keys(client_website)

    def saveb(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

