import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.delete_clientsP import delete_clientsP


class Deleting_clients(unittest.TestCase):
    def setUp(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = (ServiceAccountCredentials.from_json_keyfile_name
                 ("C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope))
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')

    def delete_client(self, setup):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()

        df = pd.DataFrame(self.sheet.get_records())
        self.delete_clients = delete_clientsP(self.driver)

        for index, row in df.iterrows():
            if index == 0:
                self.delete_clients.username(row['Username'])
                self.delete_clients.password(row['Password'])
                self.delete_clients.login_button()
                time.sleep(3)
                self.delete_clients.settings()
                time.sleep(1)
                self.delete_clients.delete_button()
                time.sleep(1)
                self.delete_clients.yes()

    def tearDown(self):
        self.driver.quit()
