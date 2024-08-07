import logging
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.Methods import Methods


class ChangeTeamPassword:

    def __init__(self, driver):
        self.driver = driver
        self.Methods = Methods(self.driver)
        logging.basicConfig(level=logging.INFO)
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def Username(self, Username):
        try:
            self.Methods.enter_text(By.XPATH, "//input[@id='txtEmail']", Username)
        except Exception as e:
            raise NoSuchElementException(f"Exception caught: {e}")

    def Password(self, Password):
        try:
            self.Methods.enter_text(By.ID, "txtPassword", Password)
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def login_btn(self):
        try:
            self.Methods.click_element(By.XPATH, "//button[@type='submit']")
        except Exception as e:
            raise NoSuchElementException(f"Element not found: {e}")

    def click_Settings(self):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, ".bg-transparent > img")
        except Exception as e:
            raise ElementNotVisibleException(f"Element not found: {e}")

    def Team(self):
        try:
            self.Methods.hover_and_click(By.XPATH, "//a[@class='active']")
        except Exception as e:
            raise ElementNotVisibleException(f"Element not found: {e}")

    def search(self, sname):
        try:
            self.Methods.click_element(By.CSS_SELECTOR, "#grid_1760696226_0_searchbar")
            time.sleep(1)
            self.Methods.enter_text(By.CSS_SELECTOR, "#grid_1760696226_0_searchbar", sname)
            self.logger.info("Values sent")
            time.sleep(1)
            self.Methods.hover_and_click(By.CSS_SELECTOR, "#grid_1760696226_0_searchbutton")
        except Exception as e:
            raise ElementNotVisibleException(f"Exception caught: {e}")

    def get_data_from_sheet(self):
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
            client = gspread.authorize(creds)
            sheet = client.open("Leads").sheet1
            data = sheet.get_all_records()
            return data
        except Exception as e:
            self.logger.error(f"Error fetching data from Google Sheets: {e}")
            return []

    def Change_password(self, dname, dmail):
        try:
            print("Trying to find element")
            rows = self.driver.find_elements(By.CSS_SELECTOR, '.e-rowcell.e-focus.e-selectionbackground.e-active')
            for row in rows:
                print("finding nemo")
                row_name = row.find_element(By.CSS_SELECTOR,
                                            '.e-row:nth-child(3) > .e-rowcell:nth-child(1)').text
                print("Trying to find element 2")
                row_email = row.find_element(By.CSS_SELECTOR, '').text
                print("row name and email ")
                if row_name == dname and row_email == dmail:
                    change_password = row.find_element(By.XPATH, '//tbody/tr[3]/td[7]/div[1]/i[2]')
                    print("change password button not clicked")
                    change_password.click()
                    print("change password button clicked")
                    self.logger.info(f"Deleted profile: {dname}, {dmail}")
                    break
        except Exception as e:
            raise ElementNotVisibleException(f"Exception caught: {e}")

    def Change_pwd(self):
        try:
            data = self.get_data_from_sheet()
            for record in data:
                dname = record['dname']
                dmail = record['dmail']
                self.search(dname)
                self.Change_password(dname, dmail)
        except Exception as e:
            raise ElementNotVisibleException(f"Exception caught: {e}")

    def clickPwd(self):
        try:
            self.Methods.click_element(By.XPATH, "//tbody/tr[3]/td[7]/div[1]/i[2]")
            self.logger.info("Element found and clicked")
        except Exception as e:
            raise ElementNotVisibleException(f"Exception caught:{e}")

    def new_pass(self, pass_1, pass_2):
        try:
            # Locate the password field
            elements_1 = self.driver.find_elements(By.XPATH, "//input[@id='txtPassword']")
            if elements_1:
                element_1 = elements_1[0]
                element_1.send_keys(pass_1)

                element = self.driver.find_element(By.XPATH, "//div[@class='modal-content']//div[1]//div[1]//div["
                                                             "1]//div[1]//span[1]//i[1]")
                if element:
                    element.click()
                print("Password field found and updated")
            else:
                raise NoSuchElementException("Password input field not found")

            elements_2 = self.driver.find_elements(By.XPATH, "//input[@id='txtConfirmPassword']")
            if elements_2:
                element_2 = elements_2[0]
                element_2.send_keys(pass_2)

                element = self.driver.find_element(By.XPATH, "//div[@class='modal-body']//div[2]"
                                                             "//div[1]//div[1]//div[1]//span[1]//i[1]")
                if element:
                    element.click()
                print("Confirm password field found and updated")
            else:
                raise NoSuchElementException("Confirm password input field not found")

        except NoSuchElementException as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def click_save(self):
        try:
            self.Methods.click_element(By.XPATH, "//button[@class='c-btn dark-btn  ']")
            self.logger.info("Element found and updated")

        except Exception as e:
            raise NoSuchElementException(f"Exception caught:{e}")
