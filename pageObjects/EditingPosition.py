import logging
import time
from pynput.keyboard import Controller, Key
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException


class EditingPosition:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def wait_for_element(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            self.logger.info(f"Element located: {value}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found within the timeout period: {value}")
            return None

    def hover_and_click(self, by, value):
        element = self.wait_for_element(by, value)
        if element:
            try:
                hover = ActionChains(self.driver).move_to_element(element)
                hover.perform()
                time.sleep(2)
                element.click()
                self.logger.info(f"Element hovered and clicked: {value}")
            except ElementNotInteractableException:
                self.logger.error(f"Element not interactable: {value}")
        else:
            self.logger.error(f"Failed to hover and click element: {value}")

    def enter_text(self, by, value, text):
        element = self.wait_for_element(by, value)
        if element:
            element.send_keys(text)
            self.logger.info(f"Text '{text}' entered in element: {value}")
        else:
            self.logger.error(f"Failed to enter text in element: {value}")

    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        if element:
            element.click()
            self.logger.info(f"Element clicked: {value}")
        else:
            self.logger.error(f"Failed to click element: {value}")

    def username(self, username):
        self.enter_text(By.XPATH, "//input[@id='txtEmail']", username)

    def password(self, password):
        self.enter_text(By.ID, "txtPassword", password)

    def login(self):
        self.click_element(By.XPATH, "//button[@type='submit']")
        self.logger.info("Attempted to log in")

    def clickSettings(self):
        self.click_element(By.CSS_SELECTOR, ".bg-transparent > img")

    def clickPosition(self):
        self.hover_and_click(By.XPATH, "//i[@class='fa-solid fa-street-view pe-2']")

    def searchPosition(self, searchPosition):
        element = self.wait_for_element(By.XPATH, "//input[@placeholder='Search']")
        if element:
            try:
                hover = ActionChains(self.driver).move_to_element(element)
                hover.perform()
                time.sleep(1)
                element.clear()
                element.send_keys(searchPosition)
                time.sleep(1)
                keyboard = Controller()
                keyboard.press(Key.enter)
                time.sleep(1)
                keyboard.release(Key.enter)
                self.logger.info(f"Searched for position: {searchPosition}")
            except ElementNotInteractableException:
                self.logger.error(f"Search input not interactable")
        else:
            self.logger.error("Search input element not found")

    def clickEdit(self):
        self.click_element(By.XPATH, '//i[contains(@class, "fa fa-pencil")]')

    def enterNewPosition(self, enterNewPosition):
        self.driver.find_element(By.ID, "txtPositionName").clear()
        time.sleep(1)
        self.enter_text(By.ID, "txtPositionName", enterNewPosition)

    def save(self):
        self.click_element(By.XPATH, "//button[contains(text(), 'Save')]")
