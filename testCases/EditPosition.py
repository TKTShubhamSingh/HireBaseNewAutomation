import logging
import os
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.EditingPosition import EditingPosition


class EditPosition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        cls.sheet = spreadsheet.worksheet('Sheet1')
        logging.basicConfig(level=logging.INFO,
                            handlers=[logging.FileHandler("log/automation.log"), logging.StreamHandler()])
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def take_screenShot(self, name):
        try:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenShotName = os.path.join('Screenshots', f"{name}_{timestamp}.png")
            self.driver.save_screenshot(screenShotName)
            self.logger.info(f"Screenshot saved: {screenShotName}")
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")

    def test_EditPosition(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")
            self.logger.info("Navigate to the application")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.EditPosition = EditingPosition(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.EditPosition.username(row['Username'])
                    self.EditPosition.password(row['Password'])
                    self.EditPosition.login()

                    self.wait.until(EC.url_to_be("https://hirebaseproto.tktechnico.com/dashboard"))
                    self.logger.info(f"Current URL: {self.driver.current_url}")
                    self.assertEqual(self.driver.current_url, "https://hirebaseproto.tktechnico.com/dashboard",
                                     "URL after login does not match expected URL.")
                    time.sleep(2)
                    self.EditPosition.clickSettings()
                    time.sleep(1)
                    self.EditPosition.clickPosition()
                    self.EditPosition.searchPosition(row['searchPosition'])
                    self.EditPosition.clickEdit()
                    time.sleep(1)
                    self.EditPosition.enterNewPosition(row['enterNewPosition'])
                    self.EditPosition.save()
                    time.sleep(5)


        except Exception as e:
            self.logger.info(f"Error occurred: {e}")
            self.fail(f"Test failed due to:{e}")

    def tearDown(self):
        self.driver.quit()
        self.logger.info("TearDown completed successfully.")


if __name__ == "__main__":
    unittest.main()
