import logging
import os.path
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.DeletingPosition import DeletingPositions


class DeletingPosition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData\\hiredata"
                                                                 ".json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        cls.sheet = spreadsheet.worksheet("Sheet1")

        logging.basicConfig(level=logging.INFO)
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def take_Screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join('Screenshots', f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"Screenshot saved{screenshot_name}")

    def test_DeletingPostiton(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/login")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.DeletingPosition = DeletingPositions(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.DeletingPosition.username(row['Username'])
                    self.DeletingPosition.password(row['Password'])
                    self.DeletingPosition.login()
                    self.take_Screenshot("LoginScreen")

                    self.wait.until(EC.url_to_be("https://hirebaseproto.tktechnico.com/dashboard"))
                    self.logger.info(f"Current URL: {self.driver.current_url}")
                    self.assertEqual(self.driver.current_url, "https://hirebaseproto.tktechnico.com/dashboard", "URL "
                                                                                          "after login does not match "
                                                                                                                "expected URL.")
                    time.sleep(3)
                    self.DeletingPosition.click_Settings()
                    time.sleep(2)
                    self.DeletingPosition.click_Position()
                    time.sleep(1)
                    self.take_Screenshot("postitions")
                    time.sleep(3)
                    self.DeletingPosition.searchPosition(row['Dposition'])

        except Exception as e:
            self.logger.error(f"{e}: element not found")
            self.take_Screenshot("Error")

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
