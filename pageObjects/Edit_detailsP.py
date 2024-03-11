from selenium.webdriver.common.by import By


class Edit_detailsP:

    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(username)

    def password(self, password):
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='col-md-12 btn btn-login pt-2 mt-4']").click()

    def drop_down(self):
        self.driver.find_element(By.XPATH, "//a[@role='button']").click()
        (self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/nav[1]/div[1]/div[1]/ul[2]/li[3]/ul[1]/li[2]/a[1]")
         .click())

    def leads(self):
        self.driver.find_element(By.LINK_TEXT, "leads").click()
