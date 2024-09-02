import datetime
import logging
import os
import time
import gspread
import pandas as pd
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from oauth2client.service_account import ServiceAccountCredentials
from pageObjects.loginPage import LoginP


class Login_test(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='test2.log', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')

        self.logger.info('Setting up test environment')

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.sheet = spreadsheet.worksheet('Sheet2')
        self.lp = LoginP(self.driver)
        self.driver.get("https://hirebaseproto.tktechnico.com/login")

    def test_Login(self):
        self.logger.info('Starting login test')
        df = pd.DataFrame(self.sheet.get_records())
        count = 0
        for index, row in df.iterrows():
            if count <= 2:
                self.lp.setUserName(row['username'])
                self.lp.setPassword(row['password'])
                self.lp.login()
                count += 1
                time.sleep(5)

                try:
                    invalid_login_element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Invalid login attempt.')]"))
                    )
                    assert invalid_login_element, "Invalid login attempt message not found"
                    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    folder_name = "Screenshots"
                    if not os.path.exists("C:\\pythonProject\\Framework\\Screenshots"):
                        os.makedirs(folder_name)
                    filename = f"{folder_name}/invalid_login_{current_datetime}.png"
                    self.driver.save_screenshot(filename)
                    self.logger.info(f'Saved screenshot: {filename}')
                except Exception as e:
                    self.logger.error(f'Error occurred: {str(e)}')
                    assert False, f"Exception occurred: {str(e)}"
            else:
                self.logger.info('Test completed successfully')
                break

    def tearDown(self):
        self.logger.info('Tearing down test environment')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
