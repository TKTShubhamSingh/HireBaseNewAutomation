import logging
import time
import unittest

import gspread
import pandas as pd
from gspread import worksheet
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.Setting import settingP
from utilities.readdata import Readconfig


class Adding_team_member(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')

    def test_Adding_user(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://hirebaseproto.tktechnico.com/login")

        df = pd.DataFrame(self.sheet.get_records())
        self.add_user = settingP(self.driver)

        for index, row in df.iterrows():
            if index == 0:
                self.add_user.username(row['Username'])
                self.add_user.password(row['Password'])
                time.sleep(1)
                self.add_user.login_button()
                time.sleep(5)
                self.add_user.settings()
                time.sleep(3)

            act_title = self.driver.title

            if act_title == "Hirebase":
                self.add_user.team()
                time.sleep(3)
                self.add_user.add_new_user()
                time.sleep(2)
                self.add_user.First_name(row['Team_First_name'])
                time.sleep(1)
                self.add_user.Last_name(row['Team_Last_name'])
                time.sleep(1)
                self.add_user.Phone_number(row['Team_Phone_number'])
                time.sleep(1)
                self.add_user.Team_role()
                time.sleep(1)
                self.add_user.Team_status()
                time.sleep(1)
                self.add_user.Team_location()
                time.sleep(1)
                self.add_user.Team_email(row['Team_email'])
                time.sleep(1)
                self.add_user.Team_password(row['Team_password'])
                time.sleep(1)
                self.add_user.eye1()
                self.add_user.Team_confirm_password(row['Team_confirm_password'])
                time.sleep(1)
                self.add_user.eye2()
                time.sleep(1)
                self.add_user.save1()
                time.sleep(5)
                break
            self.driver.quit()