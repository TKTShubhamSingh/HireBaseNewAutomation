import logging
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DeletingSkillGroups:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def wait_for_element(self, by, value):
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except Exception as e:
            self.logger.info(f"Element not found:{value}, Exception:{e}")

    def username(self, username):
        try:
            element = self.wait_for_element(By.XPATH, "//input[@id='txtEmail']")
            element.send_keys(username)
            self.logger.info("Element found and keys send")
        except Exception as e:
            self.logger.info(f"Element not found exception caught:{e}")

    def password(self, password):
        try:
            element = self.wait_for_element(By.ID, "txtPassword")
            element.send_keys(password)
            self.logger.info("element found and keys send")
        except Exception as e:
            self.logger.info(f"Element not found exception caught:{e}")

    def login(self):
        try:
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            self.logger.info("Logged in success fully")

        except Exception as e:
            self.logger.info(f"Error exception caught{e}")

    def click_Settings(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".bg-transparent > img").click()
            self.logger.info("Element clicked")
        except Exception as e:
            self.logger.info(f"Exception caught: {e}")

    def click_skillsGroup(self):
        try:
            element = self.driver.find_element(By.LINK_TEXT, "Skills Group")
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            element.click()
            self.logger.info("Element clicked")

        except Exception as e:
            self.logger.info(f"Error exception caught{e}")

    def search_textfield(self, DeleteSkillGroup):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, "#grid_1760696226_1_searchbar")
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            element.send_keys(DeleteSkillGroup)
            time.sleep(5)

        except Exception as e:
            self.logger.debug(f"Exception caught{e}")

    def click_search(self):
        try:
            element = self.wait_for_element(By.CSS_SELECTOR, "#grid_1760696226_1_searchbutton")
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(2)
            element.click()

        except Exception as e:
            self.logger.info(f"Exception element not clicked: {e}")

    def clickSearch(self):
        try:
            element = self.wait_for_element(By.XPATH, "//button[@class='c-btn dark-btn me-2']")
            element.click()
        except Exception as e:
            self.logger.info(f"Exception caught:{e}")

    def click_delete(self):
        element = self.driver.find_element(By.XPATH, "(//i[contains(@class,'fa fa-trash ps-3')])[1]")
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        time.sleep(1)
        element.click()

    def click_delete_confirm(self):
        try:
            self.wait_for_element(By.XPATH, "//button[@title='Accept changes']").click()
            self.logger.info("Element clicked")

        except Exception as e:
            self.logger.info(f"Exception caught: {e}")
