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