import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.EditStatus import Edit_Status
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Methods import Methods


class EditStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        filepath = "C:\\pythonProject\\Framework\\TestData\\HireBase_data.json"
        creds = ServiceAccountCredentials.from_json_keyfile_name(filepath, scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet('Sheet1')
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_EditStatus(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")
            self.EditStatus = Edit_Status(self.driver)
            self.Methods = Methods(self.driver)

            records = self.sheet.get_all_records()
            # Check and ensure headers are unique
            headers = self.sheet.row_values(1)
            if len(headers) != len(set(headers)):
                headers = [f"{header}_{index}" if headers.count(header) > 1 else header
                           for index, header in enumerate(headers)]

                df = pd.DataFrame(records, columns=headers)
            else:
                df = pd.DataFrame(records)

            for index, row in df.iterrows():
                if index == 0:

                    logo = self.wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='hirebase logo']")))

                    assert logo.is_displayed(), "The Hirebase Logo is not displayed"

                    self.EditStatus.Username(row['Username'])
                    self.EditStatus.Password(row['Password'])
                    self.EditStatus.LoginBtn()

                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bg"
                                                                                                          "-transparent > "
                                                                                                          "img")))

                    self.Methods.take_Screenshot("Dashboard")
                    act_title = self.driver.title
                    assert act_title == "Hirebase", f"but got{act_title}"

                    if act_title == "Hirebase":
                        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bg"
                                                                                                              "-transparent > img")))
                        time.sleep(2)
                        self.EditStatus.settings()
                        self.EditStatus.status()
                        time.sleep(2)
                        self.EditStatus.search(row['NewStatusName'])
                        time.sleep(2)





        except Exception as e:
            self.logger.error(f"Error during test execution: {e}")
            raise
