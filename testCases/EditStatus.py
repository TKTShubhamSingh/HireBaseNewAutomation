import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.EditStatus import Edit_Status
from pageObjects.Methods import Methods


class EditStatus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Google Sheets API setup
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\HireBase_data.json", scope
        )

        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet('Sheet1')

    def setUp(self):
        # WebDriver setup
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.driver.maximize_window()
        self.EditStatus = Edit_Status(self.driver)
        self.Methods = Methods(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_EditStatus(self):
        try:
            df = pd.DataFrame(self.sheet.get_all_records())
            for index, row in df.iterrows():
                if index == 0:
                    self.EditStatus.Username(row['Username'])
                    self.EditStatus.Password(row['Password'])
                    self.EditStatus.LoginBtn()

                    time.sleep(10)

                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img"))
                    )

                    act_title = self.driver.title
                    assert act_title == "Hirebase", f"Expected title 'Hirebase', but got '{act_title}'"

                    if act_title == "Hirebase":
                        self.Methods.take_Screenshot("Dashboard")
                        time.sleep(2)

                        # Wait until the settings are visible
                        WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img"))
                        )

                        self.EditStatus.Settings()
                        self.EditStatus.Status()
                        self.EditStatus.search_status(row['NewStatusName'])
                        print(f"Status name entered in the text field")
                        self.EditStatus.click_search()
                        time.sleep(2)
                        self.EditStatus.verify_text(row['NewStatusName'], 2)

                        self.EditStatus.click_edit()
                        time.sleep(5)

                        try:
                            element = WebDriverWait(self.driver, 10).until(
                                EC.visibility_of_element_located((By.XPATH, "//div[@class='flyout-card-title']"))
                            )
                            text = element.text
                            print(f"Retrieved text: '{text}'")

                            # Validate the retrieved text
                            assert text == "Edit Status Details", f"Expected 'Edit Status Details', but got '{text}'"

                            if text == "Edit Status Details":
                                self.EditStatus.status_name(row['StatusNewName'])
                                time.sleep(1)
                                self.EditStatus.Primary_status(row['primary_status'])
                                self.EditStatus.Visibility(row['Visibility'])

                                self.EditStatus.save()

                                time.sleep(5)

                        except TimeoutException:
                            print("Element with XPATH //div[@class='flyout-card-title'] was not found in time.")

                    else:
                        print("Title not matched")

        except Exception as e:
            raise NoSuchElementException(f"Exception caught: {str(e)}")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
