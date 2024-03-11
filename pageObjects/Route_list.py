import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Route_listP:

    def __init__(self, driver):
        self.driver = driver

    def username(self, Username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(Username)

    def password(self, password):
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='col-md-12 btn btn-login pt-2 mt-4']").click()

    def drop_down(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/nav[1]/div[1]/div[1]/ul[2]/li[3]/a[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='CRM']").click()

    def Route_list(self):
        self.driver.find_element(By.XPATH, "//i[contains(@class,'fa fa-xl fa-route')]").click()

    def Add_route(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[class='c-btn dark-btn ms-3']").click()

    def username1(self, username1):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div["
                                           "1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]").send_keys(username1)

    def date(self, date):
        self.driver.find_element(By.XPATH, "//input[@id='txtRouteDate']").send_keys(date)

    def add_route(self):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-plus-circle fa-3x']").click()

    def add_pipline(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@role='dialog']/div[@role='document']/div["
                                           "@class='modal-content']/div[@class='modal-body']/div[@class='d-flex "
                                           "flex-wrap']/div[1]/div[1]/div[1]").click()

    def save(self):
        self.driver.find_element(By.XPATH, "//button[contains(@title,'Accept changes')]").click()



    def save1(self):
        self.driver.find_element(By.CSS_SELECTOR, ".fa.fa-solid.fa-floppy-disk")
        self.driver.execute_script("document.querySelector('.fa.fa-solid.fa-floppy-disk').click();")

