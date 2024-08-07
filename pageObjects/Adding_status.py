import logging
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import NoSuchElementException
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

    def get_cell_value(self, row_index, column_name):
        return self.df.at[row_index, column_name]

    def username(self, Username):
        try:
            self.Methods.enter_text(By.ID, "txtEmail", Username)
        except Exception as e:
            raise NoSuchElementException(f"Exception caught: {e}")

    def password(self, Password):
        try:
            self.Methods.enter_text(By.ID, "txtPassword", Password)
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def login_button(self):
        try:
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")
        except Exception as e:
            raise NoSuchElementException(f"Exception caught: {e}")

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

    def Add_status(self):
        try:
            self.Methods.click_element(By.XPATH, "//body/div[@id='root']/div[3]/div[1]/div[1]/div[1]/div["
                                                 "2]/div[1]/div[1]/div[1]/div[2]/button[1]")
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def NewStatus(self, NewStatusName):
        try:
            self.Methods.enter_text(By.NAME, "txtStatusName", NewStatusName)
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def dropdown(self, option_text_Status):
        element = self.driver.find_element(By.XPATH, "//select[@id='drpPrimaryStatus']")
        option = Select(element)
        try:
            option.select_by_visible_text(option_text_Status)
        except NoSuchElementException:
            raise NoSuchElementException(f"Option '{option_text_Status}' not found in the drop-down list")

    def Visibility_drop(self, Visibility_drop):
        element = self.driver.find_element(By.ID, "drpStatus")
        option = Select(element)

        try:
            option.select_by_visible_text(Visibility_drop)
        except Exception:
            raise NoSuchElementException(f"Option'{Visibility_drop}' not found in the drop-down list")

    def save(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, "button:nth-child(2)")
        except Exception:
            raise NoSuchElementException(f"Element not found")



