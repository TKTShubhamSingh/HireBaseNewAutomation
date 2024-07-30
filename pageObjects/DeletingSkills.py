import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DeletingSkill:

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

    def username(self, username):
        try:
            element = self.wait_for_element(By.XPATH, "//input[@id='txtEmail']")
            element.send_keys(username)
            self.logger.info("Element found and key send")
        except Exception as e:
            self.logger.info(f"Element not found:{e}")

    def password(self, password):
        try:
            element = self.wait_for_element(By.ID, "txtPassword")
            element.send_keys(password)
            self.logger.info("element found and keys send")
        except Exception as e:
            self.logger.info(f"Error element not found:{e}")

    def login(self):
        try:
            self.wait_for_element(By.XPATH, "//button[@type='submit']").click()
            self.logger.info("Element clicked")
        except Exception as e:
            self.logger.info(f"Element not found:{e}")

    def click_Settings(self):
        try:
            self.wait_for_element(By.CSS_SELECTOR, ".bg-transparent > img").click()
            self.logger.info("Element clicked")

        except Exception as e:
            self.logger.info(f"Element not found: {e}")

    def click_Skills(self):
        try:
            element = self.wait_for_element(By.CSS_SELECTOR, "a:nth-child(6)")
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            element.click()
            self.logger.info("Element clicked")

        except Exception as e:
            self.logger.info(f"Element not found:{e}")

    def Searching_skill(self, Test_skill):
        try:
            element = self.wait_for_element(By.CSS_SELECTOR, "#grid_1760696226_1_searchbar")
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(3)
            self.logger.info("Element clicked")
            if element:
                time.sleep(2)
                element.send_keys(Test_skill)
            else:
                print("Error element not interactable")
        except Exception as e:
            self.logger.info(f"Element not found:{e}")

    def search(self):
        try:
            element = self.wait_for_element(By.XPATH, "//span[@id='grid_1760696226_1_searchbutton']")
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(3)
            element.click()
            self.logger.info("Element clicked")

        except Exception as e:
            self.logger.info(f"Element not found:{e}")


    def clicking_delete(self):
        try:
            element = self.wait_for_element(By.XPATH, "//i[@title='Delete']")
            action = ActionChains(self.driver).move_to_element(element)
            action.perform()
            time.sleep(2)
            element.click()

        except Exception as e:
            self.logger.info(f"Error:{e}")

    def delete(self):
        self.wait_for_element(By.CSS_SELECTOR, ".fa.fa-check.me-2").click()
