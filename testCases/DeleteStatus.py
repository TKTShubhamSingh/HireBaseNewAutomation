import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Delete_Status import Delete_status
from pageObjects.Methods import Methods


class DeleteStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        cls.sheet = spreadsheet.worksheet('Sheet1')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()
        self.DeleteStatus = Delete_status(self.driver)
        self.Methods = Methods(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_DeleteStatus(self):
        try:
            df = pd.DataFrame(self.sheet.get_all_records())
            for index, row in df.iterrows():
                if index == 0:
                    # Login sequence
                    self.DeleteStatus.Username(row['Username'])
                    self.DeleteStatus.Password(row['Password'])
                    self.DeleteStatus.LoginBtn()

                    # Verify login was successful by checking the page title
                    act_title = self.driver.title
                    assert act_title == "Hirebase", f"Expected title: 'Hirebase', But got '{act_title}'"

                    if act_title == "Hirebase":
                        time.sleep(2)
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img"))
                        )
                        self.Methods.take_Screenshot("Dashboard")

                        # Navigating to settings and status
                        self.DeleteStatus.Settings()
                        self.DeleteStatus.Status()

                        time.sleep(2)
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, "#grid_1760696226_1_searchbar"))
                        )

                        self.DeleteStatus.search_status(row['NewStatusName'])
                        self.DeleteStatus.click_search()

                        search_result = self.Methods.wait_for_element(By.CSS_SELECTOR,
                                                                      "#grid_1760696226_1_searchbar")
                        assert search_result, "No results found for the provided status name."

                        self.Methods.hover_and_click(By.XPATH,
                                                     "//i[@class='fa fa-trash ms-3']")

                        self.Methods.wait_for_element(By.CSS_SELECTOR, ".c-btn:nth-child(2)")
                        self.Methods.hover_and_click(By.CSS_SELECTOR, ".c-btn:nth-child(2)")
                        time.sleep(2)

                        self.Methods.take_Screenshot("After_Delete")
                        print(f"Status '{row['NewStatusName']}' deleted successfully.")



        except Exception as e:
            print(f"Exception caught: {e}")
            self.Methods.take_Screenshot("Error")
            raise

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
