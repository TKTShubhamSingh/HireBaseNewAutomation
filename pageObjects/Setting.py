from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class settingP:

    def __init__(self, driver):
        self.driver = driver

    def username(self, Username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(Username)

    def password(self, Password):
        self.driver.find_element(By.ID, "txtPassword").send_keys(Password)

    def login_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='col-md-12 btn btn-login pt-2 mt-4']").click()

    def settings(self):
        self.driver.find_element(By.CSS_SELECTOR, ".bg-transparent > img").click()

    def team(self):
        self.driver.find_element(By.LINK_TEXT, "Team").click()

    def add_new_user(self):
        self.driver.find_element(By.CSS_SELECTOR, ".c-btn.dark-btn").click()

    def First_name(self, first_name):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(first_name)

    def Last_name(self, last_name):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/input[1]").send_keys(last_name)

    def Phone_number(self, Phone_number):
        self.driver.find_element(By.XPATH, "//input[@id='txtPhone']").send_keys(Phone_number)

    def Team_role(self):
        element = self.driver.find_element(By.XPATH, "//select[@id='drpRoles']")
        select = Select(element)
        select.select_by_visible_text("Admin")

    def Team_status(self):
        element2 = self.driver.find_element(By.XPATH, "//select[@name='drpStatuses']")
        select = Select(element2)
        select.select_by_visible_text("Active")

    def Team_location(self):
        element3 = self.driver.find_element(By.XPATH, "//select[@id='drpLocations']")
        select = Select(element3)
        select.select_by_visible_text("BUENA PARK")

    def Team_email(self, Team_email):
        self.driver.find_element(By.XPATH, "//input[@id='txtEmail']").send_keys(Team_email)

    def Team_password(self, Team_password):
        self.driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys(Team_password)

    def eye1(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[8]/div[1]/div[1]/span["
                                           "1]/i[1]").click()

    def eye2(self):
        self.driver.find_element(By.XPATH, "//div[9]//div[1]//div[1]//span[1]//i[1]").click()

    def Team_confirm_password(self, Team_change_password):
        self.driver.find_element(By.XPATH, "//input[@id='txtConfirmPassword']").send_keys(Team_change_password)

    def save1(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()