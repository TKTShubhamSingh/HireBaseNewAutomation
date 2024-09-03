import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Methods import Methods
import time


class EditCrm_Leads:

    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)
        self.wait = WebDriverWait(driver, 10)

        # Google Sheets setup
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')

        sheet = spreadsheet.worksheet('Sheet1')
        data = sheet.get_all_records()
        self.df = pd.DataFrame(data)

    def Username(self, username):
        """Enter the username in the login form."""
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", username)
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f"Exception caught while interacting with Username field: {str(e)}")
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Username input element not found: {str(e)}")

    def Password(self, password):
        """Enter the password in the login form."""
        try:
            self.Methods.enter_text(By.ID, "txtPassword", password)
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f"Exception caught while interacting with Password field: {str(e)}")
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Password input element not found: {str(e)}")

    def LoginBtn(self):
        """Click the login button."""
        try:
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")
        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Exception caught while clicking Login button: {str(e)}")
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Login button element not found: {str(e)}")

    def CrmDropDown(self):
        """Click on the CRM dropdown."""
        try:
            self.Methods.click_element(By.CSS_SELECTOR, ".dropdown-toggle")
        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Exception caught while clicking CRM dropdown: {str(e)}")
        except NoSuchElementException as e:
            raise NoSuchElementException(f"CRM dropdown element not found: {str(e)}")

    def Crm(self):
        """Hover and click on the CRM option."""
        try:
            self.Methods.hover_and_click(By.CSS_SELECTOR, "li:nth-child(2) a:nth-child(1)")
        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Exception caught while interacting with CRM link: {str(e)}")
        except NoSuchElementException as e:
            raise NoSuchElementException(f"CRM link element not found: {str(e)}")

    def click_until_element_is_displayed(self):
        """Click a button repeatedly until a specific element is displayed."""
        button_xpath = "//button[@class='c-btn c-btn-gray']"
        element_xpath = "//button[@class='c-btn c-btn-gray']"
        max_timeout = 5  # seconds
        wait = WebDriverWait(self.driver, max_timeout)

        while True:
            try:
                # Wait for the element to be visible
                element = wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
                if element.is_displayed():
                    print("Element is now displayed.")
                    break
            except TimeoutException:
                # If element not displayed, click the button again
                print("Element not displayed yet, clicking the button again.")
                self.Methods.click_element(By.XPATH, button_xpath)
                time.sleep(1)  # Small delay to prevent rapid clicking
