import logging
import unittest

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.DeleteTeam import DeleteTeam


class Delete_Team(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData\\hiredata"
                                                                 ".json", scope)
        client = gspread.authorize(creds)
        Spreadsheet = client.open('Leads')
        cls.sheet = Spreadsheet.worksheet('Sheet1')
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_DeleteTeam(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")

            df = pd.DataFrame(self.sheet.get_all_records())
            self.DeleteTeam = DeleteTeam(self.driver)





        except Exception as e:
            self.logger.info(f"{e}:Exception occur")



