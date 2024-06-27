from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SkillGroupPage:

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

    def skillg(self):
        self.driver.find_element(By.LINK_TEXT, "Skills Group").click()

    def addSKillGroup(self):
        self.driver.find_element(By.XPATH, "//button[@class='c-btn dark-btn']").click()

    def skillGroupName(self, skillGroupName):
        self.driver.find_element(By.XPATH, "//input[@id='txtSkillGroupName']").send_keys(skillGroupName)

    def skillStatus(self):
        element = self.driver.find_element(By.XPATH, "//select[@id='drpStatuses']")
        select = Select(element)
        select.select_by_index(1)

    def Save(self):
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
