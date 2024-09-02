import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.EditSkill import EditSkill
from pageObjects.Methods import Methods


class EditSkills(unittest.TestCase):
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

    def test_EditSkillGroup(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.methods = Methods(self.driver)
            self.EditSkills = EditSkill(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.EditSkills.username(row['Username'])
                    self.EditSkills.password(row['Password'])
                    self.EditSkills.loginbtn()
                    self.methods.take_Screenshot("Login_screen")
                    time.sleep(2)
                    act_title = self.driver.title
                    self.logger.debug(f"Page title after login: {act_title}")
                    assert act_title == "Hirebase", f"Expected title 'Hirebase', but got {act_title}'"
                    self.logger.info("Login Successful, title matched")
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img")))
                    self.methods.take_Screenshot("Dashboard")
                    self.EditSkills.click_setting()
                    self.EditSkills.skills()
                    element = self.driver.find_element(By.XPATH, '//span[contains(text(), "Skill")]')
                    assert element is not None
                    self.EditSkills.Searching_skill(row['Test_skill'])
                    time.sleep(1)
                    self.EditSkills.Edit_skill(row['SkillnameNew'], row['Option 1'], row['Option 2'], row['Option 3'],
                                               row['Option 4'])


        except Exception as e:
            self.logger.error(f"Test failed:{e}")
            self.methods.take_Screenshot("Error")
            self.fail(f"Test failed due to:{e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
