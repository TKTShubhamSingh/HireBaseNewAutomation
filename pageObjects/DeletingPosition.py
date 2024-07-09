import logging
import  time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class DeletingPositions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def wait_for_element(self, by, value):
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            self.logger.info(f"Not element found:{value}, Exception:{e}")
            raise

    def username(self, username):
        try:
            element = self.wait_for_element(By.XPATH, "//input[@id='txtEmail']")
            element.send_keys(username)
            self.logger.info("Element found")
        except Exception as e:
            self.logger.info(f"Exception found:{e}")
        raise

    def password(self, password):
        try:
            element = self.wait_for_element(By.ID, "txtPassword")
            element.send_keys(password)
            self.logger.info("Element found")
        except Exception as e:
            self.logger.info(f"Exception:{e}")
        raise

    def login(self):
        try:
            element = self.wait_for_element(By.XPATH, "//button[@type='submit']")
            element.click()
            self.logger.info("element clicked")
        except Exception as e:
            self.logger.info(f"Exception:{e}")
        raise

    def click_Settings(self):
        try:
            element = self.wait_for_element(By.CSS_SELECTOR, ".bg-transparent > img")
            element.click()
        except Exception as e:
            self.logger.info(f"element not found:{e}")
        raise

    def click_Position(self):
        try:
            element = self.wait_for_element(By.XPATH, "//i[@class='fa-solid fa-street-view pe-2']")
            element.click()

        except Exception as e:
            self.logger.info("element not found")
            raise

    def searchPosition(self, Dposition):
        try:
            element = self.wait_for_element(By.XPATH, "//input[@placeholder='Search']")
            element.click()
            self.logger.info("Element clicked")
            time.sleep(2)
            if element:
                element.send_keys(Dposition)
            else:
                self.logger.info("Error found")
                print("Not enabled")
        except Exception as e:
            self.logger.info(f"Exception occur")
        raise
