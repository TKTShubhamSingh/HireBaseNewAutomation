import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Adding_appointmentP:

    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(By.ID, "txtEmail").send_keys(username)

    def password(self, password):
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)

    def login_button(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def drop_down(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[role='button']").click()
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/nav[1]/div[1]/div[1]/ul[2]/li[3]/ul[1]/li[2]/a[1]").click()

    def leads(self):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-xl fa-building-flag text-white']").click()

    def location_drop(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/span[1]").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".ms-3.filter-selected").click()

    def filter(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Filter']").click()

    def people_card(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[3]/div[1]/div["
                                           "1]/div[2]").click()

    def appointment(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link")))
        self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5) > .nav-link").click()

    def date(self):
        self.driver.find_element(By.CSS_SELECTOR, ".e-work-cells.e-work-days.e-current-date").click()

    def Add_title(self, Title):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Add title']").send_keys(Title)

    def more_details(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[title='More Details']").click()

    def title(self, Title1):
        self.driver.find_element(By.XPATH, "//input[@id='Summary']").send_keys(Title1)

    def status(self):
        self.driver.find_element(By.XPATH, "//form[@id='scheduleEditForm']/div/table/tbody/tr[2]/td[2]/span").click()

    def status2(self):
        self.driver.find_element(By.XPATH, "//ul[@id='Status_options']/li").click()

    def description(self, description):
        self.driver.find_element(By.XPATH, "//textarea[@id='Description']").send_keys(description)

    def meeting_with(self, meeting_with):
        self.driver.find_element(By.XPATH, "//input[@id='MeetingWith']").send_keys(meeting_with)

    def feedback(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//form[@id='scheduleEditForm"
                                                                                       "']/div/table/tbody/tr[7]/td["
                                                                                       "2]/span")))
        self.driver.find_element(By.XPATH, "//form[@id='scheduleEditForm']/div/table/tbody/tr[7]/td[2]/span").click()

    def feed_back(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[1]/ul[1]/li[2]").click()

    def save(self):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[3]/button[2]").click()