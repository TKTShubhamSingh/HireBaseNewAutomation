from selenium.webdriver.common.by import By


class LoginP:
    usn_username_id = "txtEmail"
    pss_password_id = "txtPassword"
    btt_login_xpath = "//button[@class='col-md-12 btn btn-login pt-2 mt-4']"
    drop_down_xpath = "//a[@class='nav-link dropdown-toggle text-primary show']"
    link_logout_linktext = "Log Out"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.usn_username_id).clear()
        self.driver.find_element(By.ID, self.usn_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.pss_password_id).clear()
        self.driver.find_element(By.ID, self.pss_password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.btt_login_xpath).click()

    def drop(self):
        self.driver.find_element(By.XPATH, self.drop_down_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()




