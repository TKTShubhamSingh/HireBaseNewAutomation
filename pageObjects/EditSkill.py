import logging
import time
from pynput.keyboard import Controller, Key
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Methods import Methods


class EditSkill:
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(driver)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def username(self, Username):
        try:
            self.methods.enter_text(By.XPATH, "//input[@id='txtEmail']", Username)
            self.logger.info("element found")
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def password(self, Password):
        try:
            self.methods.enter_text(By.NAME, "txtPassword", Password)
            self.logger.info("element found")
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def loginbtn(self):
        try:
            self.methods.click_element(By.XPATH, "//button[@class='col-md-12 btn btn-login pt-2 mt-4']")
            self.logger.info("element Clicked")
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def click_setting(self):
        try:
            time.sleep(2)
            self.methods.click_element(By.CSS_SELECTOR, ".bg-transparent > img")
            self.logger.info("Element Clicked")
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def skills(self):
        try:
            self.methods.hover_and_click(By.CSS_SELECTOR, "a:nth-child(6)")
            self.logger.info("element found")
        except Exception as e:
            raise Exception(f"Element not found:{e}")

    def Searching_skill(self, Test_skill):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, "#grid_1760696226_1_searchbar")
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
            time.sleep(3)
            self.logger.info("Element clicked")
            if element:
                time.sleep(2)
                element.send_keys(Test_skill)
                time.sleep(1)
                keyboard = Controller()
                keyboard.press(Key.enter)
                time.sleep(1)
                keyboard.release(Key.enter)
            else:
                print("Error element not interactable")
        except Exception as e:
            raise Exception(f"Element not found{e}")

    def Edit(self):
        try:
            self.methods.click_element(By.CSS_SELECTOR, "i[title='Edit']")
            self.logger.info("element clicked")
        except Exception as e:
            raise Exception(f"Element not found{e}")

    def Edit_skill(self, SkillnameNew, Option1, Option2, Option3, Option4):
        try:

            self.driver.find_element(By.XPATH, "//button[@class='c-btn dark-btn']").click()
        except Exception as e:
            raise Exception(f"Error clicking Add new skill button: {e}")

        time.sleep(2)

        try:
            # Enter the skill name
            element = self.driver.find_element(By.XPATH, "//input[@id='txtExperienceName']")
            element.clear()
            time.sleep(1)
            element.send_keys(SkillnameNew)
        except Exception as e:
            raise Exception(f"Error sending keys to the skill name input: {e}")

        # Select the field type
        element = self.driver.find_element(By.XPATH, "//select[@id='drpType']")
        select = Select(element)
        select.select_by_index(2)
        time.sleep(2)

        # Enter options
        self.driver.find_element(By.ID, "txtExperienceOption-0").send_keys(Option1)
        time.sleep(2)
        button_locator = (By.XPATH, "//button[contains(text(),'Add Option')]")

        try:
            for _ in range(3):
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(button_locator)
                )
                button.click()
        except Exception as e:
            print("An error occurred:", e)

        self.driver.find_element(By.ID, "txtExperienceOption-1").send_keys(Option2)
        self.driver.find_element(By.ID, "txtExperienceOption-2").send_keys(Option3)
        self.driver.find_element(By.ID, "txtExperienceOption-3").send_keys(Option4)

        # Select the status
        element = self.driver.find_element(By.ID, "drpStatuses")
        select = Select(element)
        select.select_by_index(1)

        # Select the skill group
        element = self.driver.find_element(By.ID, "drpSkillGroupId")
        select = Select(element)
        select.select_by_index(3)

        # Click the Save button
        self.driver.find_element(By.XPATH, "//button[@class='c-btn dark-btn' and text()='Save']").click()

        time.sleep(5)