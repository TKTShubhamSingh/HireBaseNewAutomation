import logging
import os
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.SkillPage import SkillPage
from HtmlTestRunner import HTMLTestRunner


class Skill(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s: %(levelname)s: %(message)s',
            handlers=[
                logging.FileHandler("Test.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("Setting up the environment")

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/pythonProject/Framework/TestData/hiredata.json",
                                                                 scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        self.sheet = spreadsheet.worksheet('Sheet1')

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def takeScreenShot(self, step_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join('Screenshots', f"{step_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"ScreenShot taken: {screenshot_name}")

    def test_Skill(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/login")
            df = pd.DataFrame(self.sheet.get_all_records())

            self.Skills = SkillPage(self.driver)

            for Outer_index, row in df.iterrows():
                if Outer_index == 0:
                    self.Skills.username(row['Username'])
                    self.Skills.password(row['Password'])
                    self.Skills.login()

                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img"))
                    )
                    self.takeScreenShot("Dashboard")
                    act_title = self.driver.title
                    self.logger.debug(f"Page title after login: {act_title}")
                    assert act_title == "Hirebase", f"Expected title 'Hirebase', but got {act_title}'"
                    self.logger.info("Login successful, title matched")

                    self.Skills.settings()
                    self.takeScreenShot("Settings")

                    time.sleep(2)

                    self.Skills.skills()
                    time.sleep(2)
                    self.Skills.AddnewSkill(row['Skillname'])

                    time.sleep(2)
                    self.Skills.fieldType()
                    time.sleep(2)
                    self.Skills.options(row['Option 1'], row['Option 2'], row['Option 3'], row['Option 4'])
                    time.sleep(3)
                    self.Skills.Status()
                    time.sleep(1)
                    self.Skills.Skill_Group()
                    time.sleep(1)
                    self.Skills.Save()
                    time.sleep(1)

        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            self.takeScreenShot("Error")
            raise

    def tearDown(self):
        self.driver.quit()
        self.logger.info("Test completed and browser closed")


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output='Reports'))
