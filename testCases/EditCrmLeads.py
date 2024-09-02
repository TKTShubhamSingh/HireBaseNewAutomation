import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.EditCrmLeads import EditCrm_Leads
from pageObjects.Methods import Methods


class EditCrmLeads(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\Framework\\TestData\\HireBase_data"
                                                                 ".json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet('Sheet1')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.CrmLeads = EditCrm_Leads(self.driver)
        self.Methods = Methods(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_EditCrmLeads(self):
        try:
            df = pd.DataFrame(self.sheet.get_all_records())
            for index, row in df.iterrows():
                if index == 0:
                    self.CrmLeads.Username(row['Username'])
                    self.CrmLeads.Password(row['Password'])

                    self.Methods.take_Screenshot("LoginPage")

                    self.CrmLeads.LoginBtn()

                    WebDriverWait(self.driver, 10).until(

                        EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-xl fa-dashboard text-white']"))
                    )
                    self.CrmLeads.CrmDropDown()
                    self.CrmLeads.Crm()


                    time.sleep(5)


        except Exception as e:
            raise NoSuchElementException(f"Exception caught: {str(e)}")
