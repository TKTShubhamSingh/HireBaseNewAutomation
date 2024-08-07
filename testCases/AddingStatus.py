import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Adding_status import Adding_status
from pageObjects.Methods import Methods


class AddingStatus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        file_path = "C:\\pythonProject\\Framework\\TestData\\HireBase_data.json"
        creds = ServiceAccountCredentials.from_json_keyfile_name(file_path, scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet('Sheet1')
        cls.logger = logging.getLogger(__name__)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def is_element_present_with_text(self, by, value, expected_text):
        try:
            element = self.driver.find_element(by, value)
            return element.text == expected_text
        except NoSuchElementException:
            return False

    def test_status(self):
        try:
            self.driver.get("https://hirebaseproto.tktechnico.com/")

            # Fetch records from the sheet
            records = self.sheet.get_all_records()

            # Check and ensure headers are unique
            headers = self.sheet.row_values(1)
            if len(headers) != len(set(headers)):
                headers = [f"{header}_{index}" if headers.count(header) > 1 else header
                           for index, header in enumerate(headers)]

                df = pd.DataFrame(records, columns=headers)
            else:
                df = pd.DataFrame(records)

            self.AddingStatus = Adding_status(self.driver)
            self.Methods = Methods(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    logo = self.wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='hirebase logo']")))
                    assert logo.is_displayed(), "The hirebase logo is not displayed."

                    self.AddingStatus.username(row['Username'])
                    self.AddingStatus.password(row['Password'])
                    self.AddingStatus.login_button()
                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-transparent > img"))
                    )
                    self.Methods.take_Screenshot("Dashboard")
                    act_title = self.driver.title
                    assert act_title == "Hirebase", f"but got {act_title}"

                    self.AddingStatus.settings()
                    self.AddingStatus.status()
                    self.Methods.take_Screenshot("Status")
                    time.sleep(3)
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "//body/div[@id='root']/div["
                                                                                         "3]/div[1]/div[1]/div[1]/div["
                                                                                         "2]/div[1]/div[1]/div["
                                                                                         "1]/div[2]/button[1]")))
                    self.AddingStatus.Add_status()
                    time.sleep(5)

                    element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flyout-card-title")))

                    text = element.text

                    # Print the text
                    print(f"Text from the element: {text}")

                    expected_text = "Add Status Details"
                    print(f"{expected_text}")
                    element_present_with_text = self.is_element_present_with_text("css selector", ".flyout-card-title",
                                                                                  expected_text)
                    assert element_present_with_text, f"Element with text '{expected_text}' not found."
                    if element_present_with_text:
                        self.AddingStatus.NewStatus(row['NewStatusName'])
                        self.AddingStatus.dropdown(row['option_text_Status'])
                        time.sleep(1)
                        self.AddingStatus.Visibility_drop(row['Visibility_drop'])
                        self.AddingStatus.save()
                        time.sleep(2)

                    else:
                        print("Element with expected text not found.")

        except Exception as e:
            self.logger.error(f"Error during test execution: {e}")
            raise

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
