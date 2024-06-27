from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddTeamMemberP:
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

    def addnewuser(self):
        self.driver.find_element(By.XPATH, "//button[@class='c-btn dark-btn']").click()

    def teamfname(self, tname):
        self.driver.find_element(By.XPATH, "//input[@id='txtFirstName']").send_keys(tname)

    def teamlname(self, lname):
        self.driver.find_element(By.XPATH, "//input[@id='txtLastName']").send_keys(lname)

    def teamPhonenumber(self, tphnumber):
        self.driver.find_element(By.XPATH, "//input[@id='txtPhone']").send_keys(tphnumber)

    def role(self):
        element = self.driver.find_element(By.XPATH, "//select[@id='drpRoles']")
        select = Select(element)
        select.select_by_index(1)

    def status(self):
        element2 = self.driver.find_element(By.XPATH, "//select[@id='drpStatuses']")
        select = Select(element2)
        select.select_by_index(1)

    def location(self):
        element3 = self.driver.find_element(By.XPATH, "//select[@id='drpLocations']")
        select = Select(element3)
        select.select_by_index(4)

    def email(self, Tmail):
        self.driver.find_element(By.XPATH, "//input[@id='txtEmail']").send_keys(Tmail)

    def Tpassword(self, Tpass):
        element = self.driver.find_element(By.XPATH,
                                           "//div[@id='root']/div[2]/div/div[2]/div[8]/div/div/input").send_keys(Tpass)
        element.click()

    def Tconfpass(self, Tconfpass):
        element = self.driver.find_element(By.XPATH,
                                           "//div[@id='root']/div[2]/div/div[2]/div[9]/div/div/input").send_keys(
            Tconfpass)
        element.click()

    def save(self):
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
