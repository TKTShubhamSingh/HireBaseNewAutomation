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
from pageObjects.DeletingSkillsGroup import DeletingSkillGroups


log_directory = "log"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

log_file_path = os.path.join(log_directory, "automation.log")

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler(log_file_path),
                              logging.StreamHandler()])

logging.getLogger().info("Logging setup complete. Starting the script.")


class DeletingSkillsGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData"
                                                                     "\\HireBase_data.json"
                                                                     , scope)
            client = gspread.authorize(creds)
            spreadsheet = client.open('Leads')
            cls.sheet = spreadsheet.worksheet('Sheet1')
            cls.logger = logging.getLogger(__name__)
            cls.logger.info("Google Sheets authentication successful")
        except Exception as e:
            cls.logger.error(f"Error in setUpClass: {e}")
            raise

    def setUp(self):
        try:
            self.driver = webdriver.Chrome()  
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 10)
            self.logger.info("Chrome browser launched successfully")
        except Exception as e:
            self.logger.error(f"Error in setUp: {e}")
            raise

    def take_screenShot(self, name):
        try:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenShotName = os.path.join('Screenshots', f"{name}_{timestamp}.png")
            self.driver.save_screenshot(screenShotName)
            self.logger.info(f"Screenshot saved: {screenShotName}")
        except Exception as e:
            self.logger.error(f"Error taking screenshot: {e}")

    def test_DeletingSkillsGroup(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")
            self.logger.info("Navigated to the website")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.DeletingSkillsGroup = DeletingSkillGroups(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.DeletingSkillsGroup.username(row['Username'])
                    self.DeletingSkillsGroup.password(row['Password'])
                    self.DeletingSkillsGroup.login()
                    self.take_screenShot("login done")
                    time.sleep(2)
                    self.wait.until(EC.url_to_be("https://hirebaseproto.tktechnico.com/dashboard"))
                    time.sleep(2)
                    act_title = self.driver.title
                    self.logger.debug(f"Page title after login: {act_title}")
                    expected_title = "Hirebase"
                    if act_title == expected_title:
                        self.logger.info("Login successful, title matched")
                        self.DeletingSkillsGroup.click_Settings()
                        time.sleep(2)
                        self.DeletingSkillsGroup.click_skillsGroup()
                        time.sleep(2)
                        self.DeletingSkillsGroup.search_textfield(row['DeleteSkillGroup'])
                        time.sleep(1)
                        self.DeletingSkillsGroup.click_search()
                        self.take_screenShot("Searched")
                        time.sleep(1)
                        self.DeletingSkillsGroup.click_delete()
                        time.sleep(1)
                        self.DeletingSkillsGroup.click_delete_confirm()
                        time.sleep(3)

                    else:
                        self.logger.error(f"Expected title '{expected_title}', but got '{act_title}'")
                        self.fail(f"Expected title '{expected_title}', but got '{act_title}'")

        except Exception as e:
            self.logger.error(f"Error in test_DeletingSkillsGroup: {e}")
            self.fail(f"Test failed due to error: {e}")

    def tearDown(self):
        try:
            self.driver.quit()
            self.logger.info("Chrome browser closed")
        except Exception as e:
            self.logger.error(f"Error in tearDown: {e}")


if __name__ == "__main__":
    unittest.main()

# Verify that the log file is created
if os.path.exists(log_file_path):
    print(f"Log file created successfully: {log_file_path}")
else:
    print(f"Failed to create log file: {log_file_path}")
