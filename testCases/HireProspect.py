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
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.HireProspect import ProspectToLead
from pageObjects.Methods import Methods


class HireProspect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        cls.sheet = spreadsheet.worksheet("Sheet1")
        logging.basicConfig(level=logging.INFO,
                            handlers=[logging.FileHandler("log/automation.log"), logging.StreamHandler()])
        cls.logger = logging.getLogger()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.Methods = Methods(self.driver)
        self.actions = ActionChains(self.driver)

    def test_hireProspect(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/login")
            df = pd.DataFrame(self.sheet.get_all_records())
            self.HireProspect = ProspectToLead(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.HireProspect.username(row['Username'])
                    self.HireProspect.password(row['Password'])
                    self.HireProspect.login_btn()
                    time.sleep(2)
                    act_title = self.driver.title
                    assert act_title == "Hirebase", f"Expected title 'Hirebase', but got: {act_title}"
                    self.logger.info("Title matched")
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Dashboard')]")))
                    element = self.driver.find_element(By.XPATH, "//a[contains(text(),'Dashboard')]")
                    if element:
                        time.sleep(2)
                        self.HireProspect.Prospects()
                        self.HireProspect.scroll()

                    # taking the name of the person from sheet
                    try:
                        card_name = row['record']
                        card = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{card_name}')]"))
                        )

                        assert card_name in card.text
                        time.sleep(3)
                        actions = ActionChains(self.driver)
                        actions.move_to_element(card).perform()
                        time.sleep(1)
                        card.click()
                        time.sleep(3)

                        print(f"Test passed: Card with text '{card_name}' found, clicked, and hovered successfully.")
                        self.HireProspect.hire()
                        time.sleep(5)

                    except Exception as e:
                        raise Exception(f"Exception found:{e}")

        except Exception as e:
            self.logger.error(f"Test failed: {e}")
            self.Methods.take_Screenshot("Error")
            self.fail(f"Test failed due to: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
