from selenium.webdriver.common.by import By


class SkillPage:
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