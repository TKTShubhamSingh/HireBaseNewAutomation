import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver

from pageObjects.Changing_the_statusP import changing_the_statusP


class changing_the_status(unittest.TestCase):
    def setUp(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json",
            scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.baseurl = Readconfig.getAppurl()
        self.sheet = spreadsheet.worksheet('Sheet6')
        self.driver.get("https://hirebaseproto.tktechnico.com/login")

        self.cts = changing_the_statusP(self.driver)

    def test_changing_the_status(self):
        df = pd.DataFrame(self.sheet.get_records())
        for index, row in df.iterrows():
            if index == 0:
                self.cts.Username(row['username'])
                self.cts.Password(row['password'])
                self.cts.login_button()
                time.sleep(10)
                self.cts.people()
                time.sleep(1)
                self.cts.location_drop_down()
                time.sleep(2)
                self.cts.search_record(row['search'])
                time.sleep(1)
                self.cts.profile()
                time.sleep(1)
                self.cts.details()
                time.sleep(1)
                self.cts.status()
                time.sleep(1)
                self.cts.reason(row['reason'])
                time.sleep(3)
                self.cts.save()
                time.sleep(5)
                break

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
