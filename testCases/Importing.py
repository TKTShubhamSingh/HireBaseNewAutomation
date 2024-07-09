import os
import unittest
import logging
import time
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ImportingPage import ImportingPage


class Importing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/pythonProject/Framework/TestData/hiredata.json",
                                                                 scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet("Sheet1")

        # Set up logger
        logging.basicConfig(level=logging.INFO)
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        # Set up Selenium WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join('Screenshots', f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"Screenshot saved: {screenshot_name}")

    def test_importing(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/login")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.Import = ImportingPage(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.Import.username(row['Username'])
                    self.Import.password(row['Password'])
                    self.Import.login()
                    self.take_screenshot("login_screen.png")
                    time.sleep(10)

                    expected_url = "https://hirebaseproto.tktechnico.com/dashboard"
                    self.logger.info(f"Current URL: {self.driver.current_url}")
                    self.assertEqual(self.driver.current_url, expected_url, "URL after login does not match expected "
                                                                            "URL.")

                    dashboard_element = self.driver.find_element(By.XPATH, "//button[@class='c-btn dark-btn "
                                                                           "rounded-pill pdf-export-btn']")
                    self.assertIsNotNone(dashboard_element, "Dashboard element not found, login may have failed.")
                    self.Import.click_people()
                    print(self.driver.current_url)
                    time.sleep(2)
                    self.Import.Import()
                    time.sleep(2)
                    self.Import.upload()
                    time.sleep(2)
                    self.Import.save()
                    time.sleep(5)

        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            self.take_screenshot("error")
            raise e

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
