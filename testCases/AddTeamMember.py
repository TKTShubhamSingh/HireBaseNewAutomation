import logging
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.AddTeamMemberP import AddTeamMemberP
from selenium.webdriver.support import expected_conditions as EC


class AddTeamMember(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.INFO, format=':%(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.info("Setting up test environment")

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:/pythonProject/Framework/TestData/hiredata.json", scope)

        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        self.sheet = spreadsheet.worksheet('Sheet1')

    def test_AddTeamMember(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()

        df = pd.DataFrame(self.sheet.get_records())
        self.AddTeam = AddTeamMemberP(self.driver)

        for index, row in df.iterrows():
            self.logger.info(f"Processing row{index}: {row.to_dict}")
            if index == 0:
                self.AddTeam.username(row['Username'])
                self.AddTeam.password(row['Password'])
                self.AddTeam.login()
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img")))

                act_title = self.driver.title
                self.logger.debug(f"Page title after login: {act_title}")
                assert act_title == "Hirebase", f"Expected title 'Hirebase', but got '{act_title}'"

                self.AddTeam.settings()
                self.AddTeam.team()

    def tearDown(self):
        self.driver.quit()