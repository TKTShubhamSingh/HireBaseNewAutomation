import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pynput.keyboard import Key, Controller


class Position_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def wait_for_element(self, by, value):
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            self.logger.error(f"Element not found: {value}, Exception: {e}")
            raise

    def username(self, username):
        try:
            self.wait_for_element(By.XPATH, "//input[@id='txtEmail']").send_keys(username)
            self.logger.info("Entered username successfully")
        except Exception as e:
            self.logger.error(f"Error entering username: {e}")
            raise

    def password(self, password):
        try:
            element = self.wait_for_element(By.ID, "txtPassword")
            element.send_keys(password)
            self.logger.info("Entered the password")
        except Exception as e:
            self.logger.error(f"Unable to find password element: {e}")
            raise

    def login(self):
        try:
            element = self.wait_for_element(By.XPATH, "//button[@type='submit']")
            element.click()
            self.logger.info("Clicked login button successfully")
        except Exception as e:
            self.logger.error(f"Error clicking login button: {e}")
            raise

    def click_settings(self):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, ".bg-transparent > img")
            element.click()

        except Exception as e:
            self.logger.info(f"Error in clicking settings {e}")

    def click_Position(self):
        try:
            element = self.wait_for_element(By.XPATH, "//i[@class='fa-solid fa-street-view pe-2']")
            element.click()

        except Exception as e:
            self.logger.info("element not found")
            raise

    def add_position(self, Position):
        try:
            self.wait_for_element(By.XPATH, "(//button[@class='c-btn dark-btn'])[1]").click()
            self.logger.info("Button element found and clicked")
            time.sleep(3)
            element = self.wait_for_element(By.ID, "txtPositionName")
            if element:
                element.send_keys(Position)
                self.logger.info("txtPositionName element found and keys sent")
            else:
                self.logger.info("txtPositionName element not found")
        except Exception as ec:
            self.logger.info(f"Exception occurred: {ec}")

    def save_button(self):
        try:
            self.wait_for_element(By.XPATH, "//button[@class='c-btn dark-btn' and text()='Save']").click()
            self.logger.info("Element found and clicked")

        except Exception as ec:
            self.logger.info(f"Element not found:{ec}")



