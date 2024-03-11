import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.Prospects_to_Leads import prospects_to_leadsP
import datetime
import os


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
        try:
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
                success_message = self.prospects_To_leads.get_success_message()
                assert "Lead added successfully" in success_message, "Lead addition failed"
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            folder_name = "Screenshots"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            filename = f"{folder_name}/error_{current_datetime}.png"
            self.driver.save_screenshot(filename)
            self.logger.info(f"Screenshot saved: {filename}")
            raise e

    def tearDown(self):
        try:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"screenshot_{current_datetime}.png"
            folder_name = "Screenshots"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            full_path = os.path.join(folder_name, filename)
            self.driver.save_screenshot(full_path)
            self.logger.info(f"Screenshot saved: {full_path}")
            self.logger.info("Test completed. Closing browser.")
            self.driver.quit()
        except Exception as e:
            self.logger.error(f"An error occurred during teardown: {str(e)}")
            raise e


if __name__ == "__main__":
    unittest.main()
