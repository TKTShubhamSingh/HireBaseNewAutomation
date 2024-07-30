import time
from pynput.keyboard import Controller, Key
from selenium.common import TimeoutException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class EditingSkillGroup:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            return element
        except TimeoutException:
            raise TimeoutException(f"Element not found within the timeout period: {value}")

    def hover_and_click(self, by, value):
        element = self.wait_for_element(by, value)
        if element:
            try:
                hover = ActionChains(self.driver).move_to_element(element)
                hover.perform()
                time.sleep(1)
                element.click()
            except ElementNotInteractableException:
                raise ElementNotInteractableException(f"Element not interactable: {value}")

    def enter_text(self, by, value, text):
        element = self.wait_for_element(by, value)
        assert element is not None, f"Failed to find element: {value}"
        element.send_keys(text)

    def click_element(self, by, value):
        element = self.wait_for_element(by, value)
        assert element is not None, f"Failed to find element: {value}"
        element.click()

    def username(self, username):
        try:
            self.enter_text(By.XPATH, "//input[@id='txtEmail']", username)
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def password(self, password):
        try:
            self.enter_text(By.ID, "txtPassword", password)
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def login(self):
        try:
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def clickSettings(self):
        try:
            self.click_element(By.CSS_SELECTOR, ".bg-transparent > img")
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def clickSkillGroup(self):
        try:
            self.click_element(By.LINK_TEXT, "Skills Group")
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def search(self, skillsgroup):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, "#grid_1760696226_1_searchbar")
            action = ActionChains(self.driver).move_to_element(element)
            action.perform()
            time.sleep(1)
            element.send_keys(skillsgroup)
            time.sleep(2)
            keyboard = Controller()
            keyboard.press(Key.enter)
            time.sleep(1)
            keyboard.release(Key.enter)
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def click_edit(self):
        try:
            self.wait_for_element(By.XPATH, "//i[contains(@title,'Edit')]").click()
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def edited_name(self, txtSkillGroupName):
        try:
            element = self.wait_for_element(By.ID, "txtSkillGroupName")
            element.clear()
            time.sleep(1)
            element.send_keys(txtSkillGroupName)
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def set_Status(self):
        try:
            element = self.wait_for_element(By.NAME, "drpStatuses")
            dropdown = Select(element)
            dropdown.select_by_index(1)
            time.sleep(1)
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def click_save(self):
        try:
            self.wait_for_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")
