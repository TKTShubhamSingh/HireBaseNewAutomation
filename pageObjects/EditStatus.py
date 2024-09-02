import logging
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Methods import Methods


class Edit_Status:

    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)

        logging.basicConfig(level=logging.INFO)
        self.wait = WebDriverWait(driver, 10)

        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\pythonProject\\HireBase_data.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open('Leads')
        sheet = spreadsheet.worksheet('Sheet1')
        data = sheet.get_all_records()
        self.df = pd.DataFrame(data)

    def Username(self, Username):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", Username)

        except Exception as e:
            raise ElementNotInteractableException(f"Exception caught:{str(e)}")

    def Password(self, Password):
        try:
            self.Methods.enter_text(By.ID, "txtPassword", Password)

        except Exception as e:
            raise ElementNotInteractableException(f"Exception caught:{str(e)}")

    def LoginBtn(self):
        try:
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")
        except Exception as e:
            raise ElementClickInterceptedException(f"Exception caught:{str(e)}")

    def Settings(self):
        try:
            self.Methods.hover_and_click(By.XPATH, "//div[@class='nav-item-box-img bg-transparent']")
        except Exception as e:
            raise ElementClickInterceptedException(f"Element not found:{str(e)}")

    def Status(self):
        try:
            self.Methods.hover_and_click(By.CSS_SELECTOR, "a:nth-child(6)")

        except Exception as e:
            raise ElementClickInterceptedException(f"Element not found:{str(e)}")

    def search_status(self, NewStatusName):
        try:
            self.Methods.hover_and_enter_text(By.CSS_SELECTOR, "#grid_1760696226_1_searchbar", NewStatusName)
        except Exception as e:
            raise ElementNotInteractableException(f"exception caughtElement not intractable:{str(e)}")

    def click_search(self):
        try:
            self.Methods.click_element(By.ID, "grid_1760696226_1_searchbutton")
        except Exception as e:
            raise ElementNotInteractableException(f"Exception caught Element click interrupted:{str(e)}")

    def verify_text(self, by_locator, column_name, row_index):
        try:

            element = self.Methods.wait_for_element(*by_locator)

            web_element_text = element.text.strip()

            google_sheet_text = self.df.at[row_index - 1, column_name].strip()

            assert web_element_text == google_sheet_text, (f"Text mismatch: Web element has '{web_element_text}', but "
                                                           f"Google Sheet has '{google_sheet_text}'")

            return True

        except NoSuchElementException as e:
            raise NoSuchElementException(f"Web element not found: {str(e)}")

        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f"Web element not interactable: {str(e)}")

        except AssertionError as e:
            print(f"Verification failed: {str(e)}")
            raise

        except Exception as e:
            print(f"Verification failed: {str(e)}")
            raise

    def click_edit(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, ".e-row:nth-child(1) .fa-pencil")

        except Exception as e:
            raise ElementNotInteractableException(f"Element click interrupted exception caught:{str(e)}")

    def status_name(self, StatusNewName):
        self.Methods.wait_for_element(By.ID, "txtStatusName").clear()
        try:
            self.Methods.enter_text(By.ID, "txtStatusName", StatusNewName)

        except Exception as e:
            raise NoSuchElementException(f"Web element not found{str(e)}")

    def Primary_status(self, primary_status):
        element = self.Methods.wait_for_element(By.XPATH, "//select[@name='drpPrimaryStatus']")
        option = Select(element)
        try:
            option.select_by_visible_text(primary_status)

        except Exception as e:
            raise NoSuchElementException(f"Option not found{str(e)}")

    def Visibility(self, Visibility):
        element = self.Methods.wait_for_element(By.XPATH, "//select[@id='drpStatus']")
        element.click()
        options = Select(element)
        try:
            options.select_by_visible_text(Visibility)

        except Exception as e:
            raise NoSuchElementException(f"Option not found: {str(e)}")

    def save(self):
        try:
            self.Methods.hover_and_click(By.XPATH, "(//button[@type='button'])[2]")

        except Exception as e:
            raise ElementClickInterceptedException(f"Not able to click on element{str(e)}")




