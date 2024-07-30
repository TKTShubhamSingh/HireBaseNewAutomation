import logging
import os.path
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.DeletingSkills import DeletingSkill


class DeletingSkills(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData"
                                                                 "\\HireBase_data.json"
                                                                 , scope)

        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        cls.sheet = spreadsheet.worksheet("Sheet1")
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def take_ScreenShot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenShot_name = os.path.join('Screenshots', f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenShot_name)
        self.logger.info(f"Screenshot saved{screenShot_name}")

    def test_DeletingSkill(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.DeletingSkills = DeletingSkill(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.DeletingSkills.username(row['Username'])
                    self.DeletingSkills.password(row['Password'])
                    self.DeletingSkills.login()
                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img"))
                    )
                    self.take_ScreenShot("Dashboard")
                    act_title = self.driver.title
                    self.logger.debug(f"Page title after login: {act_title}")
                    assert act_title == "Hirebase", f"Expected title 'Hirebase', but got {act_title}'"
                    self.logger.info("Login successful, title matched")
                    self.DeletingSkills.click_Settings()
                    time.sleep(2)
                    self.take_ScreenShot("Settings")
                    
                    time.sleep(1)
                    self.DeletingSkills.click_Skills()
                    time.sleep(5)
                    self.DeletingSkills.Searching_skill(row['Test_skill'])
                    time.sleep(2)
                    self.take_ScreenShot("searching skill")
                    time.sleep(2)
                    self.DeletingSkills.search()
                    time.sleep(2)
                    self.DeletingSkills.clicking_delete()
                    time.sleep(2)
                    self.DeletingSkills.delete()
                    time.sleep(2)
                    self.take_ScreenShot("After deleting")

        except Exception as e:
            self.logger.info(f"{e}:Exception occur")
def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()
