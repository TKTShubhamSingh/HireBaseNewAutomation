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
from pageObjects.EditCrmLeads import EditCrm_Leads
from pageObjects.Methods import Methods


class TestEditCrmLeads(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up Google Sheets API client and spreadsheet access."""
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        cls.sheet = spreadsheet.worksheet('Sheet1')

    def setUp(self):
        """Set up the WebDriver instance and navigate to the test URL."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://hirebaseproto.tktechnico.com")
        self.CrmLeads = EditCrm_Leads(self.driver)
        self.Methods = Methods(self.driver)

    def tearDown(self):
        """Close the WebDriver instance."""
        self.driver.quit()

    def test_EditCrmLeads(self):
        """Test case for editing CRM leads."""
        try:
            # Fetch data from Google Sheets into a DataFrame
            df = pd.DataFrame(self.sheet.get_all_records())
            print("Data fetched from Google Sheets.")

            for index, row in df.iterrows():
                if index == 0:  # Assuming you want to perform actions for the first row only
                    # Perform login actions
                    print("Performing login actions...")
                    self.CrmLeads.Username(row['Username'])
                    self.CrmLeads.Password(row['Password'])

                    # Take a screenshot of the login page
                    self.Methods.take_Screenshot("LoginPage")

                    # Click login button
                    self.CrmLeads.LoginBtn()

                    # Wait for the dashboard to be visible
                    print("Waiting for dashboard to be visible...")
                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-xl fa-dashboard text-white']"))
                    )
                    print("Dashboard is visible.")

                    # Perform CRM navigation
                    self.CrmLeads.CrmDropDown()
                    self.CrmLeads.Crm()
                    time.sleep(2)
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//button["
                                                                                                     "@type='button"
                                                                                                     "'])[3]")))
                    self.CrmLeads.load_btn()
                    time.sleep(1)
                    self.CrmLeads.verify_title()
                    time.sleep(1)
                    self.CrmLeads.click_edit()
                    time.sleep(1)
                    self.CrmLeads.LeadDetails(row['Crm_lead_Address'])
                    time.sleep(1)
                    self.CrmLeads.Address_dropdown(row['Crm_lead_Address'])
                    time.sleep(1)
                    self.CrmLeads.Location(row['CrmLocation'])
                    time.sleep(2)

        except (NoSuchElementException, TimeoutException) as e:
            self.fail(f"Test failed due to exception: {str(e)}")


if __name__ == "__main__":
    unittest.main()