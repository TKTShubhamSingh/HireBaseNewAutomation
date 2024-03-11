import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.Prospects_to_Leads import prospects_to_leadsP
import datetime


class prospects_To_leads(unittest.TestCase):

    def setUp(self):

        logging.basicConfig(filename='test.log', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.baseurl = Readconfig.getAppurl()
        self.sheet = spreadsheet.worksheet('Sheet1')
        self.driver.get("https://hirebaseproto.tktechnico.com/login")

    def test_Login(self):
        df = pd.DataFrame(self.sheet.get_records())
        self.prospects_To_leads = prospects_to_leadsP(self.driver)
        for index, row in df.iterrows():
            if index == 0:
                self.prospects_To_leads.Username(row['Username'])
                time.sleep(2)
                self.prospects_To_leads.Password(row['Password'])
                time.sleep(2)
                self.prospects_To_leads.login_button()
            time.sleep(2)

            self.prospects_To_leads.dropdown()
            time.sleep(2)
            self.prospects_To_leads.prospects()
            time.sleep(1)
            self.prospects_To_leads.location_drop()
            time.sleep(1)
            self.prospects_To_leads.filter()
            time.sleep(1)
            self.prospects_To_leads.add_as_lead()
            time.sleep(1)
            self.prospects_To_leads.save()
            break

    def tearDown(self):
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"final_screenshot_{current_datetime}.png"
        self.driver.save_screenshot(filename)
        self.logger.info("Test completed. Closing browser.")
        self.driver.quit()
