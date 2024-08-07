import logging
import time

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Methods import Methods


class Edit_Status:

    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)
        logging.basicConfig(level=logging.INFO)
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData\\HireBase_data"
                                                                 ".json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        sheet = spreadsheet.sheet1
        data = sheet.get_all_records()
        self.df = pd.DataFrame(data)

    def Username(self, Username):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@name='txtEmail']", Username)
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def Password(self, Password):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@name='txtPassword']", Password)
        except Exception:
            raise NoSuchElementException(f"Element not found")

    def LoginBtn(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, "button[type='submit']")
        except Exception:
            raise NoSuchElementException(f"Element not found")

    def settings(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, ".bg-transparent > img")
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def status(self):
        try:
            self.Methods.hover_and_click(By.CSS_SELECTOR, "a:nth-child(6)")
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def search(self, status):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "#grid_1760696226_1_searchbar").clear()
            time.sleep(2)
            self.Methods.enter_text(By.CSS_SELECTOR, "#grid_1760696226_1_searchbar", status)
            time.sleep(2)
            self.Methods.hover_and_click(By.CSS_SELECTOR, "#grid_1760696226_1_searchbutton")
        except Exception as e:
            raise NoSuchElementException(f"Element not found:{e}")

    def get_data_from_sheet(self):
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
            client = gspread.authorize(creds)
            sheet = client.open("Leads").sheet1
            data = sheet.get_all_records()
            return data
        except Exception as e:
            self.logger.error(f"Error fetching data from Google Sheets: {e}")
            return []


