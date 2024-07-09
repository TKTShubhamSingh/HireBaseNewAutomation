import os
import time
import logging
import unittest
import gspread
import pandas as pd
from selenium import webdriver
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.PositionPage import Position_Page


class Position(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/pythonProject/Framework/TestData/hiredata.json",
                                                                 scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        cls.sheet = spreadsheet.worksheet("Sheet1")

        logging.basicConfig(level=logging.INFO)
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def take_screenShot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join('Screenshots', f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"Screenshot saved: {screenshot_name}")

    def test_Position(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/login")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.Position = Position_Page(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.Position.username(row['Username'])
                    self.Position.password(row['Password'])
                    self.Position.login()
                    time.sleep(2)
                    self.take_screenShot("home page")
                    self.wait.until(EC.url_to_be("https://hirebaseproto.tktechnico.com/dashboard"))
                    self.logger.info(f"current_url:{self.driver.current_url}")
                    time.sleep(1)
                    self.Position.click_settings()
                    time.sleep(1)
                    self.Position.click_Position()
                    time.sleep(1)
                    self.Position.add_position(row['New Position'])
                    time.sleep(1)
                    self.Position.save_button()
                    time.sleep(5)

        except Exception as e:
            self.logger.error(f"{e}: element not found")
            self.take_screenShot("Error")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
