import logging
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Methods import Methods


class DeleteTeam:

    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)
        logging.basicConfig(level=logging.INFO)
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def Username(self, Username):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", Username)
        except Exception as e:
            raise NoSuchElementException(f"Exception caught:{e}")

    def Password(self, Password):
        try:
            self.Methods.enter_text(By.ID, "txtPassword", Password)
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def login_btn(self):
        try:
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def click_Settings(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, ".bg-transparent > img")
        except Exception as e:
            raise ElementNotVisibleException(f"Element not found:{e}")

    def Team(self):
        try:
            self.Methods.hover_and_click(By.XPATH, "//a[@class='active']")
        except Exception as e:
            raise ElementNotVisibleException(f"Element not found:{e}")