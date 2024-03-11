import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver

from pageObjects.Edit_team_details import edit_team_detailsP


class edit_team_details(unittest.TestCase):

    def setUp(self):

        logging.basicConfig(filename='test1.log', level=logging.INFO,format=':%(message)s')
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')

    def edit_Team_detail(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()

        df = pd.DataFrame(self.sheet.get_records())
        self.edit_team = edit_team_detailsP(self.driver)

        for index, row in df.iterrows():
            if index == 0:
                self.edit_team.username(row['Username'])
                self.edit_team.password(row['Password'])
                self.edit_team.login()
