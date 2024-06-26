import time

from selenium.webdriver.common.by import By


class edit_team_detailsP:

    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(username)

    def password(self, password):
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def settings(self):
        self.driver.find_element(By.CSS_SELECTOR, ".bg-transparent > img").click()

    def team(self):
        self.driver.find_element(By.LINK_TEXT, "Team").click()

    def search(self, sname):
        element = self.driver.find_element(By.CSS_SELECTOR, "#grid_1760696226_0_searchbar")
        element.click()
        element.send_keys(sname)

    def edit(self):
        self.driver.find_element(By.CSS_SELECTOR, ".e-row:nth-child(1) .fa-pencil").click()

    def edited_username(self, edited_firstname):
        self.driver.find_element(By.XPATH, "//input[@id='txtFirstName']").send_keys(edited_firstname)

    def edited_password(self, edited_password):
        self.driver.find_element(By.ID, "//input[@id='txtLastName']").send_keys(edited_password)
