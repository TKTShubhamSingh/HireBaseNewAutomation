import logging
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException


class Methods:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def take_Screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join('Screenshots', f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"Screenshot saved: {screenshot_name}")

    def wait_for_element(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            return element
        except TimeoutException:
            raise TimeoutException(f"Element not found within the timeout period: {value}")

    def hover_and_click(self, by, locator):
        element = self.wait_for_element(by, locator)
        if element:
            try:
                hover = ActionChains(self.driver).move_to_element(element)
                hover.perform()
                time.sleep(1)
                element.click()
            except ElementNotInteractableException as e:
                raise ElementNotInteractableException(f"Element not interactable: {str(e)}")

    def hover_and_enter_text(self, by, locator, value):
        element = self.wait_for_element(by, locator)
        element.click()
        if element:
            try:
                hover = ActionChains(self.driver).move_to_element(element)
                hover.perform()
                time.sleep(1)
                element.send_keys(value)
            except Exception as e:
                raise ElementNotInteractableException(f"Exception caught:{str(e)}")

    def enter_text(self, by, value, text):
        element = self.wait_for_element(by, value)
        assert element is not None, f"Failed to find element: {value}"
        element.send_keys(text)

    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        assert element is not None, f"Failed to find element: {value}"
        element.click()

    def searching_skill(self, by, value, text):
        element = self.wait_for_element(by, value)
        if element:
            try:
                hover = ActionChains(self.driver).move_to_element(element)
                hover.perform()
                time.sleep(3)
                self.logger.info("Element hovered")
                time.sleep(2)
                element.send_keys(text)
            except ElementNotInteractableException:
                raise ElementNotInteractableException(f"Element not interactable: {value}")
            except Exception as e:
                self.logger.info(f"Error interacting with element: {e}")
        else:
            self.logger.info("Error: element not found or interactable")
