import logging
import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.Methods import Methods


class ProspectToLead:
    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def username(self, Username):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", Username)
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def password(self, Password):
        try:
            self.Methods.enter_text(By.ID, "txtPassword", Password)
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def login_btn(self):
        try:
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def Prospects(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) "
                                                        "> li:nth-child(5) > div:nth-child(1) > div:nth-child(1)")
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def scroll(self):
        button_locator = (By.XPATH, "//button[@class='c-btn c-btn-gray']")
        self.actions = ActionChains(self.driver)

        while True:
            try:
                button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                              (button_locator))
                self.actions.move_to_element(button).perform()
                button.click()
                time.sleep(1)
            except:
                break

    def hire(self):
        try:
            self.Methods.click_element(By.XPATH, "//span[@class='bg-green text-white py-1 px-2 "
                                                 "add-people-btn']")
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")
