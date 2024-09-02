import logging
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.AddingStatus import Adding_status
from pageObjects.Methods import Methods


class AddingStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        cls.logger = logging.getLogger(__name__)

        # Google Sheets API setup
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet('Sheet1')

    def setUp(self):
        # Set up WebDriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()
        self.AddingStatus = Adding_status(self.driver)
        self.Methods = Methods(self.driver)

    def tearDown(self):
        # Quit WebDriver
        self.driver.quit()

    def test_status(self):
        try:
            # Read data from Google Sheet
            df = pd.DataFrame(self.sheet.get_all_records())
            for index, row in df.iterrows():
                if index == 0:
                    # try:
                    #     # Check if the hirebase logo is displayed
                    #     hirebase_logo = self.driver.find_element(By.CSS_SELECTOR, ".d-block")
                    #     if not hirebase_logo.is_displayed():
                    # Perform login
                    self.AddingStatus.Username(row['Username'])
                    self.AddingStatus.Password(row['Password'])
                    self.AddingStatus.login_btn()
                    time.sleep(1)

                    # Check page title
                    act_title = self.driver.title
                    assert act_title == "Hirebase", f"Expected title 'Hirebase', but got '{act_title}'"
                    if act_title == "Hirebase":
                        self.Methods.take_Screenshot("Dashboard")

                        # Navigate to Settings and Status
                        time.sleep(2)
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img")))
                        self.AddingStatus.Settings()
                        self.AddingStatus.Status()
                        time.sleep(5)

                        # Add new status
                        self.AddingStatus.Add_status()
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, "//div[@class='flyout-card-title']")

                        # Fill in status details
                        self.AddingStatus.Status_name(row['NewStatusName'])
                        time.sleep(2)
                        self.AddingStatus.dropdown(row['option_text_Status'])
                        time.sleep(2)
                        self.AddingStatus.Visibility(row['Visibility'])
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "button:nth-child(2)")))
                        time.sleep(1)
                        self.AddingStatus.save()
                        time.sleep(2)
                        self.Methods.take_Screenshot("final")
                else:
                    print("Title not matched")

                # except NoSuchElementException as e:
                #     raise NoSuchElementException("The hirebase logo is not displayed. Stopping execution.") from e

        except Exception as e:
            self.logger.error(f"Error during test execution: {e}")
            raise

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
