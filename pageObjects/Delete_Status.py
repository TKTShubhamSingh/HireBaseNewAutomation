import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

from pageObjects.Methods import Methods


class Delete_status:

    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData"
                                                                 "\\HireBase_data.json", scope)

        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        sheet = spreadsheet.worksheet('Sheet1')
        data = sheet.get_all_records()
        sheet.df = pd.DataFrame(data)

    def Username(self, Username):
        try:
            self.Methods.wait_for_element(By.XPATH, "//input[@id='txtEmail']")
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", Username)

        except Exception as e:
            raise NoSuchElementException(f"Exception caught:{str(e)}")

    def Password(self, Password):
        try:
            self.Methods.wait_for_element(By.ID, "txtPassword")
            self.Methods.enter_text(By.ID, "txtPassword", Password)

        except Exception as e:
            raise ElementNotInteractableException(f"Exception caught:{str(e)}")

    def LoginBtn(self):
        try:
            self.Methods.wait_for_element(By.XPATH, "//button[@type='submit']")
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")
        except Exception as e:
            raise ElementClickInterceptedException(f"Exception caught:{str(e)}")

    def Settings(self):
        try:
            self.Methods.hover_and_click(By.XPATH, "//div[@class='nav-item-box-img bg-transparent']")
        except Exception as e:
            raise ElementClickInterceptedException(f"Element not found:{str(e)}")

    def Status(self):
        try:
            self.Methods.hover_and_click(By.CSS_SELECTOR, "a:nth-child(6)")

        except Exception as e:
            raise ElementClickInterceptedException(f"Element not found:{str(e)}")

    def search_status(self, NewStatusName):
        try:
            self.Methods.hover_and_enter_text(By.CSS_SELECTOR, "#grid_1760696226_1_searchbar", NewStatusName)
        except Exception as e:
            raise ElementNotInteractableException(f"exception caughtElement not intractable:{str(e)}")

    def click_search(self):
        try:
            self.Methods.click_element(By.ID, "grid_1760696226_1_searchbutton")
        except Exception as e:
            raise ElementNotInteractableException(f"Exception caught Element click interrupted:{str(e)}")
