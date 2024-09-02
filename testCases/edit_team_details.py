import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Edit_team_details import edit_team_detailsP


class edit_team_details(unittest.TestCase):

    def setUp(self):

        logging.basicConfig(filename='test1.log', level=logging.INFO, format=':%(message)s')
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')

    def test_edit_Team_detail(self):
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
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img")))
                self.edit_team.settings()
                time.sleep(2)
                self.edit_team.team()
                time.sleep(2)
                # WebDriverWait(self.driver, 10).until(
                # EC.element_to_be_clickable((By.XPATH, "//input[@id='grid_1252991807_2_searchbar']")))
                self.edit_team.search(row['sname'])
                time.sleep(2)
                self.edit_team.edit()
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//input[@id='txtFirstName']")))
                self.edit_team.edited_username(row['edited_firstname'])
                time.sleep(2)
                self.edit_team.edited_password(row['edited_password'])
