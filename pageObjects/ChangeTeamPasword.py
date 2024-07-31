import logging
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.Methods import Methods


class ChangeTeamPasword:

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
            rows = self.driver.find_elements(By.CSS_SELECTOR, '.e-rowcell.e-focus.e-selectionbackground.e-active')
            for row in rows:
                row_name = row.find_element(By.XPATH,
                                            '//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div['
                                            '2]/div[1]/div[4]/div[1]/table[1]/tbody[1]/tr[3]/td[1]').text
                row_email = row.find_element(By.CSS_SELECTOR, 'div.my-container.active-cont div.app-container '
                                                              'div.px-3.pt-3 div.row div.col-md-10 '
                                                              'div.default-root-container.detail-container '
                                                              'div.col-md-12 div.row.p-3:nth-child(2) '
                                                              'div.e-control.e-grid.e-lib.e-gridhover.e-grid-min'
                                                              '-height.e-responsive.e-default.e-droppable.e-resize'
                                                              '-lines.e-tooltip.e-keyboard div.e-gridcontent '
                                                              'div.e-content table.e-table tbody:nth-child(2) '
                                                              'tr.e-row:nth-child(3) > '
                                                              'td.e-rowcell.e-focus.e-selectionbackground.e-active'
                                                              ':nth-child(4)').text
                if row_name == dname and row_email == dmail:
                    change_password = row.find_element(By.XPATH, '//tbody/tr[3]/td[7]/div[1]/i[2]')
                    change_password.click()
                    self.logger.info(f"Deleted profile: {dname}, {dmail}")
                    break
        except Exception as e:
            raise ElementNotVisibleException(f"Exception caught: {e}")

    def Change_pwd(self):
        data = self.get_data_from_sheet()
        for record in data:
            dname = record['Name']
            dmail = record['Email']
            self.search(dname)
            self.Change_password(dname, dmail)
