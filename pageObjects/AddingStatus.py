import logging
import time
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import (NoSuchElementException, ElementNotVisibleException, ElementNotInteractableException,
                             ElementClickInterceptedException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Methods import Methods


class Adding_status:
    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)

        logging.basicConfig(level=logging.INFO)
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData"
                                                                 "\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        sheet = spreadsheet.sheet1
        data = sheet.get_all_records()
        self.df = pd.DataFrame(data)

    def Username(self, Username):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", Username)
        except Exception as e:
            raise NoSuchElementException(f"Exception caught: {str(e)}")

    def Password(self, Password):
        try:
            self.Methods.enter_text(By.ID, "txtPassword", Password)
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{str(e)}")

    def login_btn(self):
        try:
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")
        except Exception as e:
            raise ElementClickInterceptedException(f"Element not found:{str(e)}")

    def Settings(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, ".bg-transparent > img")
        except Exception as e:
            raise ElementClickInterceptedException(f"Element not found: {str(e)}")

    def Status(self):
        try:
            self.Methods.hover_and_click(By.CSS_SELECTOR, "a:nth-child(6)")
        except Exception as e:
            raise ElementClickInterceptedException(f"Element not clicked:{str(e)}")

    def Add_status(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, ".c-btn.dark-btn")
        except Exception as e:
            raise ElementClickInterceptedException(f"Not able to click on the element:{e}")

    def Status_name(self, NewStatusName):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtStatusName']", NewStatusName)
        except Exception as e:
            raise ElementNotInteractableException(f"Element not intractable: {str(e)}")

    def get_cell_value(self, row_index, column_name):
        print(f"Fetching value from row: {row_index}, column: {column_name}")
        return self.df.at[row_index, column_name]

    def dropdown(self, option_text_Status):
        element = self.driver.find_element(By.XPATH, "//select[@id='drpPrimaryStatus']")
        option = Select(element)
        try:
            option.select_by_visible_text(option_text_Status)
        except NoSuchElementException:
            raise NoSuchElementException(f"Option '{option_text_Status}' not found in the drop-down list")

    def Visibility(self, Visibility):
        element = self.driver.find_element(By.XPATH, "//select[@id='drpStatus']")
        option = Select(element)

        try:
            option.select_by_visible_text(Visibility)
        except NoSuchElementException:
            raise NoSuchElementException(f"Option '{Visibility}' not found in the drop down")

    def save(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
        except Exception:
            raise NoSuchElementException(f"Element not found")
