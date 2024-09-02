import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.Edit_detailsP import Edit_detailsP


class edit_details(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')

    def test_edit_detail(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()

        df = pd.DataFrame(self.sheet.get_records())
        self.edit_details = Edit_detailsP(self.driver)

        for index, row in df.iterrows():
            if index == 0:
                self.edit_details.username(row['Username'])
                self.edit_details.password(row['Password'])
                self.edit_details.login_button()
                time.sleep(5)
                self.edit_details.drop_down()

