import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException, \
    TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Methods import Methods


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
        """Enter the username."""
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", username)
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f"Exception caught while interacting with Username field: {str(e)}")
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Username input element not found: {str(e)}")

    def Password(self, password):
        """Enter the password."""
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

    def load_btn(self):
        try:
            while True:
                try:
                    # Wait for the button to be located
                    button = self.Methods.wait_for_element(By.XPATH, "(//button[@type='button'])[3]")

                    # Scroll to the button to ensure it's visible in the viewport
                    actions = ActionChains(self.driver)
                    actions.move_to_element(button).perform()

                    # Check if the button is displayed and enabled
                    if button.is_displayed() and button.is_enabled():
                        # Click the button
                        self.Methods.click_element(By.XPATH, "(//button[@type='button'])[3]")
                    else:
                        break

                except (NoSuchElementException, ElementClickInterceptedException) as e:
                    print(f"Exception caught: {str(e)}")
                    # If the element is not found or is not clickable, raise the exception
                    raise Exception(f"Exception caught: {str(e)}")

        except TimeoutException:
            print("The element was not found within the timeout period.")

    def verify_title(self):
        try:
            # Retrieve the CompanyName column from the Google Sheet
            company_names = self.df['CompanyName'].tolist()

            # Find all elements that match the XPath
            title_elements = self.driver.find_elements(By.XPATH, "//div[@class='title w-100']")

            # Iterate over all title elements
            for title_element in title_elements:
                title_text = title_element.text.strip()

                if title_text in company_names:
                    print(f"Found matching title: '{title_text}'. Clicking on it.")

                    actions = ActionChains(self.driver)
                    actions.move_to_element(title_element).perform()

                    # Click on the matching element
                    title_element.click()
                    return True

            print("No matching title found in the Google Sheet.")
            return False

        except NoSuchElementException as e:
            raise NoSuchElementException(f"Title elements not found: {str(e)}")
        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Exception caught while clicking on title: {str(e)}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
