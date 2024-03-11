import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.locationP import locationP


class adding_Location (unittest.TestCase):

    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')

    def test_location(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()

        df = pd.DataFrame(self.sheet.get_records())
        self.location = locationP(self.driver)

        for index, row in df.iterrows():
            if index == 0:
                self.location.username(row['Username'])
                self.location.password(row['Password'])
                self.location.login_btn()
                time.sleep(5)
                self.location.setting()

            act_title = self.driver.title

            if act_title == "Hirebase":
                self.location.location()
                time.sleep(1)
                self.location.add_location()
                time.sleep(1)
                self.driver.refresh()
                self.location.location()
                time.sleep(1)
                self.location.add_location()
                time.sleep(1)
                self.location.location_name(row['location_name'])
                time.sleep(1)
                self.location.location_address(row['location_address'])
                time.sleep(1)
                self.location.location_city(row['location_city'])
                time.sleep(1)
                self.location.location_state()
                time.sleep(1)
                self.location.location_zip(row['location_zip'])
                time.sleep(1)
                self.location.location_phone(row['location_phone'])
                time.sleep(1)
                self.location.location_email(row['location_email'])
                time.sleep(1)
                self.location.save1()

            else:
                print("title not matched")
            self.driver.quit()





