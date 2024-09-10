import logging
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pynput.keyboard import Key, Controller


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
            self.logger.error(f"Element not found: {value}, Exception: {e}")
            return None

    def send_keys(self, by, value, keys):
        element = self.wait_for_element(by, value)
        if element:
            element.send_keys(keys)
            self.logger.info(f"Keys sent to element: {value}")
        else:
            self.logger.error(f"Failed to send keys to element: {value}")

    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        if element:
            element.click()
            self.logger.info(f"Element clicked: {value}")
        else:
            self.logger.error(f"Failed to click element: {value}")

    def hover_and_click(self, by, value):
        element = self.wait_for_element(by, value)
        if element:
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            element.click()
            self.logger.info(f"Element hovered and clicked: {value}")
        else:
            self.logger.error(f"Failed to hover and click element: {value}")

    def username(self, username):
        self.send_keys(By.XPATH, "//input[@id='txtEmail']", username)

    def password(self, password):
        self.send_keys(By.ID, "txtPassword", password)

    def login(self):
        self.click_element(By.XPATH, "//button[@type='submit']")

    def click_Settings(self):
        self.click_element(By.CSS_SELECTOR, ".bg-transparent > img")

    def click_Position(self):
        self.hover_and_click(By.XPATH, "//i[@class='fa-solid fa-street-view pe-2']")

    def searchPosition(self, Dposition):
        element = self.wait_for_element(By.XPATH, "//input[@placeholder='Search']")
        if element:
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            element.send_keys(Dposition)
            self.logger.info(f"Search text entered: {Dposition}")
            time.sleep(2)
            keyboard = Controller()
            keyboard.press(Key.enter)
            time.sleep(1)
            keyboard.release(Key.enter)
        else:
            self.logger.error("Search field not found")

    def click_delete(self):
        self.driver.find_element(By.XPATH, "//i[contains(@class, 'fa fa-trash ps-3')]").click()
        time.sleep(2)

    def delete_confirmation(self):
        element = self.driver.find_element(By.XPATH, "//button[contains(@class, 'c-btn dark-btn me-2')]")
        time.sleep(2)
        element.click()

