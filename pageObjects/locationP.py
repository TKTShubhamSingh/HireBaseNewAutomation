from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class locationP:

    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(username)

    def password(self, password):
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)

    def login_btn(self):
        self.driver.find_element(By.XPATH, "//button[@class='col-md-12 btn btn-login pt-2 mt-4']").click()

    def setting(self):
        self.driver.find_element(By.CSS_SELECTOR, ".bg-transparent > img").click()

    def location(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Locations']").click()

    def add_location(self):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-plus']").click()

    def location_name(self, location_name):
        (self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").
         send_keys(location_name))

    def location_address(self, location_address):
        (self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/input[1]").
         send_keys(location_address))

    def location_city(self, location_city):
        self.driver.find_element(By.ID, "txtCity").send_keys(location_city)

    def location_state(self):
        drop_down = self.driver.find_element(By.ID, "txtState")
        select = Select(drop_down)
        select.select_by_visible_text("CA")

    def location_zip(self, location_zip):
        self.driver.find_element(By.ID, "txtPincode").send_keys(location_zip)

    def location_phone(self, location_phone):
        self.driver.find_element(By.NAME, "txtPhone").send_keys(location_phone)

    def location_email(self, location_email):
        self.driver.find_element(By.ID, "txtEmail").send_keys(location_email)

    def save1(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()