import time

from selenium.webdriver.common.by import By


class prospects_to_leadsP:

    def __init__(self, driver):
        self.driver = driver

    def Username(self, username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(username)

    def Password(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='col-md-12 btn btn-login pt-2 mt-4']").click()

    def people(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/ul[1]/li[4]/div[1]/div[1]/img[1]").click()

    def dropdown(self):
        self.driver.find_element(By.XPATH, "//a[@role='button']").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) a:nth-child(1)").click()

    def prospects(self):
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) div:nth-child(1) div:nth-child(1)").click()

    def location_drop(self):
        self.driver.find_element(By.XPATH, "//span[text()='Location']").click()
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Location']").click()
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, ".filter-list-item:nth-child(4) > .ms-3").click()

    def filter(self):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-filter me-2']").click()

    def add_as_lead(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div["
                                           "5]/button[1]").click()

    def save(self):
        self.driver.find_element(By.XPATH, "//button[@title='Accept changes']").click()