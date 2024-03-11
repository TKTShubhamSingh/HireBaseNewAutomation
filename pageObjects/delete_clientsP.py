from selenium.webdriver.common.by import By


class delete_clientsP:
    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(username)

    def password(self, password):
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='col-md-12 btn btn-login pt-2 mt-4']").click()

    def settings(self):
        self.driver.find_element(By.CSS_SELECTOR, ".bg-transparent > img").click()

    def delete_button(self):
        self.driver.find_element(By.XPATH, "//td[@class='e-rowcell e-templatecell e-selectionbackground "
                                           "e-active']//i[@class='fa fa-trash ps-3']").click()

    def yes(self):
        self.driver.find_element(By.XPATH, "//button[contains(@title,'Accept changes')]").click()