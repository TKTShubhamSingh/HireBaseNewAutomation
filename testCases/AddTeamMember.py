import logging
import time
import os
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.AddTeamMemberP import AddTeamMemberP


class AddTeamMember(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s',
            handlers=[
                logging.FileHandler("test.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("Setting up test environment")

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:/pythonProject/Framework/TestData/hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        self.sheet = spreadsheet.worksheet('Sheet1')

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def takeScreenshot(self, step_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join('Screenshots', f"{step_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"Screenshot taken: {screenshot_name}")

    def test_AddTeamMember(self):
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.takeScreenshot('LoginPage')

        # Reading data from Google Sheets
        df = pd.DataFrame(self.sheet.get_all_records())
        self.AddTeam = AddTeamMemberP(self.driver)

        for outer_index, row in df.iterrows():
            self.logger.info(f"Processing row {outer_index}: {row.to_dict()}")
            try:
                if outer_index == 0:
                    # login actions
                    self.AddTeam.username(row['Username'])
                    self.AddTeam.password(row['Password'])
                    self.AddTeam.login()

                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img")))
                    self.takeScreenshot("HomePage")
                    act_title = self.driver.title
                    self.logger.debug(f"Page title after login: {act_title}")
                    assert act_title == "Hirebase", f"Expected title 'Hirebase', but got '{act_title}'"
                    self.logger.info("Login successful, title matched")

                    self.AddTeam.settings()
                    self.takeScreenshot("Settings")
                    time.sleep(2)
                    self.AddTeam.team()
                    self.takeScreenshot("Team")
                    time.sleep(2)
                    self.AddTeam.addnewuser()
                    time.sleep(2)
                    self.takeScreenshot("Add New Member")

                    for inner_index, member_row in df.iterrows():
                        self.logger.info(f"Adding team member: {member_row.to_dict()}")
                        self.AddTeam.teamfname(row['TeamFName'])
                        self.AddTeam.teamlname(row['TeamLName'])
                        self.AddTeam.teamPhonenumber(row['TeamPhone'])
                        self.AddTeam.role()
                        self.AddTeam.status()
                        self.AddTeam.location()
                        self.AddTeam.email(row['Tmail'])
                        time.sleep(1)
                        self.AddTeam.Tpassword(row['Tpass'])
                        time.sleep(1)
                        self.AddTeam.Tconfpass(row['Tconfpass'])
                        time.sleep(1)
                        break
                    self.AddTeam.save()
                    self.takeScreenshot(f"Added Member")

            except Exception as e:
                self.logger.error(f"Error processing row {outer_index}: {e}")
                self.takeScreenshot(f"Error_Row_{outer_index}")
                continue

    def tearDown(self):
        self.driver.quit()
        print("Test environment torn down")


if __name__ == "__main__":
    unittest.main()
