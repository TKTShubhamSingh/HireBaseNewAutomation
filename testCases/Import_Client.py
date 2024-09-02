import os
import time
import logging
import unittest
import gspread
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from oauth2client.service_account import ServiceAccountCredentials

from pageObjects.ImportingClientPage import ImportingClients
from pageObjects.PositionPage import Position_Page


class Position(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\HireBase_data.json", scope)
            client = gspread.authorize(creds)
            spreadsheet = client.open('Leads')
            cls.sheet = spreadsheet.worksheet("Sheet1")
            logging.basicConfig(level=logging.INFO)
            cls.logger = logging.getLogger(__name__)
            cls.logger.info("SetupClass completed successfully.")
        except Exception as e:
            logging.error(f"Error in setUpClass: {e}")
            raise

    def setUp(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 10)
            self.logger.info("Setup completed successfully.")
        except Exception as e:
            self.logger.error(f"Error in setUp: {e}")
            raise

    def take_screenShot(self, name):
        try:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = os.path.join('Screenshots', f"{name}_{timestamp}.png")
            self.driver.save_screenshot(screenshot_name)
            self.logger.info(f"Screenshot saved: {screenshot_name}")
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")

    def test_Import_client(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/login")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.Import = ImportingClients(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.Import.username(row['Username'])
                    self.Import.password(row['Password'])
                    self.Import.login()
                    self.logger.info("Successfully logged in")
                    self.take_screenShot("LoginPage")

                    self.wait.until(EC.url_to_be("https://hirebaseproto.tktechnico.com/dashboard"))
                    self.logger.info(f"Current URL: {self.driver.current_url}")
                    self.assertEqual(self.driver.current_url, "https://hirebaseproto.tktechnico.com/dashboard", "URL "
                                                                                                                "after login does not match expected URL.")
                    print("clicking in setting")
                    self.Import.click_Settings()
                    time.sleep(2)
                    self.Import.click_Client()
                    time.sleep(2)
                    self.Import.Import_btn()

        except TimeoutException as TE:
            self.logger.error(f"Timeout occurred: {TE}")
            self.take_screenShot("TimeoutError")
        except NoSuchElementException as NE:
            self.logger.error(f"Element not found: {NE}")
            self.take_screenShot("ElementNotFoundError")
        except Exception as e:
            self.logger.error(f"Error: {e}")
            self.take_screenShot("TestError")

    def tearDown(self):
        try:
            self.driver.quit()
            self.logger.info("TearDown completed successfully.")
        except Exception as e:
            self.logger.error(f"Error in tearDown: {e}")
            raise


if __name__ == "__main__":
    unittest.main()
