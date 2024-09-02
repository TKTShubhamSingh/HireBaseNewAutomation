import logging
import os
import time
import unittest

from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.EditingSkillGroup import EditingSkillGroup


class EditSkillGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\HireBase_data.json", scope)

        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        cls.sheet = spreadsheet.worksheet("Sheet1")

        logging.basicConfig(level=logging.INFO,
                            handlers=[logging.FileHandler("log/automation.log"), logging.StreamHandler()])

        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def take_Screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = os.path.join('Screenshots', f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        self.logger.info(f"Screenshot saved: {screenshot_name}")

    def test_EditSkillGroup(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.EditSkillGroup = EditingSkillGroup(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.EditSkillGroup.username(row['Username'])
                    self.EditSkillGroup.password(row['Password'])
                    self.EditSkillGroup.login()

                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img")))
                    self.take_Screenshot("Dashboard")
                    act_title = self.driver.title
                    self.logger.debug(f"Page title after login: {act_title}")
                    assert act_title == "Hirebase", f"Expected title 'Hirebase', but got {act_title}'"
                    self.logger.info("Login Successful, title matched")
                    self.take_Screenshot("HomeScreen")
                    self.EditSkillGroup.clickSettings()
                    self.EditSkillGroup.clickSkillGroup()
                    self.take_Screenshot("SkillGroup")
                    self.EditSkillGroup.search(row['skillsgroup'])
                    self.EditSkillGroup.click_edit()
                    self.wait = WebDriverWait(self.driver, 20)
                    self.wait.until(EC.visibility_of_element_located(
                        (By.XPATH, "//div[@class='flyout-card-title']")))
                    self.EditSkillGroup.edited_name(row['txtSkillGroupName'])
                    self.EditSkillGroup.set_Status()
                    self.EditSkillGroup.click_save()
                    self.take_Screenshot("after_save")
                    time.sleep(3)

        except Exception as e:
            self.logger.error(f"Test failed:{e}")
            self.take_Screenshot("Error")
            self.fail(f"Test failed due to:{e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
