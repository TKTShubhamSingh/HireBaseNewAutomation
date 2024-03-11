import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class changing_the_statusP:

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

    def search_record(self, search):
        self.driver.find_element(By.NAME, "txtSearch").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "txtSearch").send_keys(search)
        time.sleep(1)
        search_bt = self.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass")
        action = ActionChains(self.driver)
        time.sleep(1)
        action.move_to_element(search_bt).perform()
        time.sleep(1)
        search_bt.click()

    def location_drop_down(self):
        self.driver.find_element(By.XPATH, "//span[text()='Location']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".filter-list-item:nth-child(4) > .ms-3").click()

    def profile(self):
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Ale Johnson']").click()

    def details(self):
        self.driver.find_element(By.ID, "dropdownMenuClickableOutside").click()

    def status(self):
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(5)").click()

    def reason(self, reason):
        self.driver.find_element(By.XPATH, "//textarea[@id='txtStatusNote']").send_keys(reason)

    def save(self):
        self.driver.find_element(By.XPATH, "//button[@title='Accept changes']").click()

    def cancel(self):
        self.driver.find_element(By.XPATH, "//button[@title='Cancel operation']").click()
