import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.ClientsP import clientsP


class adding_Client(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(filename='test.log',)
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')

    def test_clients(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()

        df = pd.DataFrame(self.sheet.get_records())
        self.clients = clientsP(self.driver)

        for index, row in df.iterrows():
            if index == 0:
                self.clients.username(row['Username'])
                self.clients.password(row['Password'])
                self.clients.login_btn()
                time.sleep(5)

            act_title = self.driver.title
            if act_title == "Hirebase":
                self.clients.settings()
                time.sleep(2)
                self.clients.add_client()
                time.sleep(1)
                self.clients.client_name(row['client_name'])

                self.clients.clientNumber(row['clientNumber'])

                self.clients.status_drop()
                self.clients.Address(row['client_address'])

                self.clients.location(row['client_location'])

                self.clients.city(row['client_city'])

                self.clients.state(row['client_state'])

                self.clients.zip_code(row['client_zip'])

                self.clients.client_website(row['client_website'])
            else:
                print("Title does not match")
                time.sleep(5)
                self.driver.save_screenshot("invalid_title_.png")
                time.sleep(5)
            break

    def tearDown(self):
        self.driver.quit()