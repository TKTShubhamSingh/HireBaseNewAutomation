import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ImportingClients:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def wait_for_element(self, by, value):
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            self.logger.error(f"Error waiting for element: {value}, Exception: {e}")
            raise

    def username(self, username):
        try:
            element = self.wait_for_element(By.ID, "txtEmail")
            element.send_keys(username)
            self.logger.info("Entered the username")
        except Exception as e:
            self.logger.error(f"Unable to find username element: {e}")
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

    def click_Settings(self):
        try:
            self.wait_for_element(By.CSS_SELECTOR, ".bg-transparent > img").click()
            self.logger.info("Settings element clicked")
        except Exception as e:
            self.logger.error(f"Error clicking settings element: {e}")
            raise

    def click_Client(self):
        try:
            self.wait_for_element(By.CSS_SELECTOR, ".bg-transparent > img").click()
            self.logger.info("Client element clicked")
        except Exception as e:
            self.logger.error(f"Error clicking client element: {e}")
            raise

    def Import_btn(self):
        try:
            element = self.wait_for_element(By.XPATH, "//button[@class='c-btn dark-btn position-relative mx-3']")
            element.click()
            self.logger.info("Import button clicked")
        except Exception as e:
            self.logger.error(f"Error clicking import button: {e}")
            raise
