import logging
import os.path
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.SkillGroupPage import SkillGroupPage


class SkillGroup(unittest.TestCase):

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
        self.logger.info("Setting up the test environment")

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData"
                                                                 "\\HireBase_data.json"
                                                                 , scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        self.sheet = spreadsheet.worksheet('Sheet1')

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def takeScreenShot(self, step_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join('Screenshots', f"{step_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"Screenshot taken: {screenshot_name}")

    def test_SkillGroup(self):
        self.driver.get("https://hirebaseproto.tktechnico.com/login")
        self.takeScreenShot('LoginPage')

        df = pd.DataFrame(self.sheet.get_all_records())
        self.SkillGroup = SkillGroupPage(self.driver)

        for Outer_index, row in df.iterrows():
            if Outer_index == 0:
                self.SkillGroup.username(row['Username'])
                self.SkillGroup.password(row['Password'])
                self.SkillGroup.login()

                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img"))
                )
                self.takeScreenShot("Dashboard")
                act_title = self.driver.title
                self.logger.debug(f"Page title after login: {act_title}")
                assert act_title == "Hirebase", f"Expected title 'Hirebase', but got '{act_title}'"
                self.logger.info("Login successful, title matched")

                self.SkillGroup.settings()
                self.takeScreenShot('Settings')
                time.sleep(2)
                self.SkillGroup.skillg()
                time.sleep(2)
                self.SkillGroup.addSKillGroup()
                time.sleep(2)
                self.SkillGroup.skillGroupName(row['skillGroupName'])
                time.sleep(2)
                self.SkillGroup.skillStatus()
                time.sleep(2)
                self.takeScreenShot("Skill group")
                self.SkillGroup.Save()

                time.sleep(1)
                self.takeScreenShot("Before dismissing toast")

                try:
                    toast_close_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//button[@class='Toastify__close-button Toastify__close-button--light']"))
                    )
                    time.sleep(2)
                    self.takeScreenShot("Before dismissing toast2")
                    toast_close_button.click()
                    self.logger.info("Toast notification dismissed.")
                except Exception as e:
                    self.logger.error(f"No toast notification found: {e}")

    def tearDown(self):
        self.driver.quit()
        self.logger.info("Test environment torn down")


if __name__ == "__main__":
    unittest.main()
