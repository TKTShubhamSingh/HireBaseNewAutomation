import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.ClientsP import clientsP


class AddingClientTest(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.info("Setting up test environment")

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\HireBase_data.json"
                                                                 , scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_clients(self):
        self.logger.info("Starting test_clients")
        self.driver.get("https://hirebaseproto.tktechnico.com")

        df = pd.DataFrame(self.sheet.get_records())
        self.clients = clientsP(self.driver)

        for index, row in df.iterrows():
            self.logger.info(f"Processing row {index}: {row.to_dict()}")
            if index == 0:
                self.clients.username(row['Username'])
                self.clients.password(row['Password'])
                self.clients.login_btn()
                time.sleep(5)

                act_title = self.driver.title
                self.logger.debug(f"Page title after login: {act_title}")
                assert act_title == "Hirebase", f"Expected title 'Hirebase', but got '{act_title}'"

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
                self.logger.info(f"Client {row['client_name']} added successfully")
            else:
                self.logger.warning("Title does not match. Taking screenshot.")
                self.driver.save_screenshot("invalid_title.png")
                self.fail("Title does not match. Test failed.")

            break

    def tearDown(self):
        self.logger.info("Tearing down test environment")
        self.driver.quit()
