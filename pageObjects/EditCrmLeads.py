import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Methods import Methods


class EditCrm_Leads:

    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)

        self.wait = WebDriverWait(driver, 10)

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData"
                                                                 "\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        sheet = spreadsheet.worksheet('Sheet1')
        data = sheet.get_all_records()
        self.df = pd.DataFrame(data)

    def Username(self, Username):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", Username)

        except Exception as e:
            raise ElementNotInteractableException(f"Exception caught:{str(e)}")

    def Password(self, Password):
        try:
            self.Methods.enter_text(By.ID, "txtPassword", Password)

        except Exception as e:
            raise ElementNotInteractableException(f"Exception caught:{str(e)}")

    def LoginBtn(self):
        try:
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")

        except Exception as e:
            raise ElementClickInterceptedException(f"Exception caught:{str(e)}")

    def CrmDropDown(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, ".dropdown-toggle")

        except Exception as e:
            raise ElementClickInterceptedException(f"Exception caught:{str(e)}")

    def Crm(self):
        try:
            self.Methods.hover_and_click(By.CSS_SELECTOR, "li:nth-child(2) a:nth-child(1)")

        except Exception as e:
            raise ElementClickInterceptedException(f"Exception caught:{str(e)}")

    def




