import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.ChangeTeamPasword import ChangeTeamPasword
from pageObjects.Methods import Methods


class Change_TeamPasword(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData"
                                                                 "\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet('Sheet1')
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_DeleteTeam(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.DeleteTeam = ChangeTeamPasword(self.driver)
            self.Methods = Methods(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    logo = self.wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='hirebase "
                                                                                     "logo']")))
                    assert logo.is_displayed(), "The hirebase logo is not displayed."

                    self.DeleteTeam.Username(row['Username'])
                    self.DeleteTeam.Password(row['Password'])
                    self.DeleteTeam.login_btn()
                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img"))
                    )
                    self.Methods.take_Screenshot("Dashboard")
                    act_title = self.driver.title
                    assert act_title == "Hirebase", f"but got {act_title}"
                    self.DeleteTeam.click_Settings()
                    self.DeleteTeam.Team()
                    time.sleep(1)
                    element = self.driver.find_element(By.CSS_SELECTOR, ".detail-container-title")
                    text = element.text
                    time.sleep(4)
                    self.assertIn('Team', text, "Text not found in the specified element")
                    self.Methods.take_Screenshot("Team")
                    time.sleep(1)
                    self.DeleteTeam.search(row['sname'])
                    time.sleep(1)
                    self.DeleteTeam.clickPwd()
                    time.sleep(1)
                    self.DeleteTeam.new_pass(row['pass_1'], row['pass_2'])
                    time.sleep(3)
        except Exception as e:
            self.logger.info(f"{e}: Exception occurred")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
