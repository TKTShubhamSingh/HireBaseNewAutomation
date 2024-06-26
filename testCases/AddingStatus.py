import logging
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
import time
from pageObjects.Adding_status import Adding_status


class AddingStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO, filename='test.log', filemode='a',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        cls.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet('Sheet1')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()
        self.AddingStatus = Adding_status(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_status(self):
        try:
            df = pd.DataFrame(self.sheet.get_all_records())
            for index, row in df.iterrows():
                if index == 0:
                    self.AddingStatus.username(row['Username'])
                    self.AddingStatus.password(row['Password'])
                    self.AddingStatus.login_button()
                    time.sleep(5)


        except Exception as e:
            self.logger.error(f"Error during test execution: {e}")
            raise

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
