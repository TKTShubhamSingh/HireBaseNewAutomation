import time

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium.common import ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException, \
    TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
            element = self.Methods.wait_for_element(By.XPATH, "//body/div[@id='root']/div[@class='my-container "
                                                              "active-cont']/div[@class='app-container']/div["
                                                              "@class='filter-bar"
                                                              " p-3']/div[1]")
            element.click()

            company_names = self.df['CompanyName'].tolist()

            title_elements = self.driver.find_elements(By.XPATH, "//div[@class='title w-100']")

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

    def click_edit(self):
        try:
            scroll = ActionChains(self.driver)
            for i in range(2):
                scroll.send_keys(Keys.ARROW_UP).perform()
            time.sleep(2)

            self.Methods.hover_and_click(By.XPATH, "//i[@class='fa-solid fa-pencil']")

            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                   "//button[contains(@class,"
                                                                                   "'nav-link nav-link-people "
                                                                                   "active') and contains(text(),"
                                                                                   "'Lead Details')]")))

        except NoSuchElementException as e:
            raise NoSuchElementException(f"Title elements not found: {str(e)}")
        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Exception caught while clicking on title: {str(e)}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def LeadDetails(self, Crm_lead_Address):
        try:
            title = self.Methods.wait_for_element(By.XPATH,
                                                  "//button[contains(@class,'nav-link nav-link-people active') and "
                                                  "contains(text(),'Lead Details')]")
            Leads_section = title.text.strip()
            exp_title = "Lead Details"

            if Leads_section == exp_title:
                element = self.driver.find_element(By.XPATH, "//input[@id='txtAddress2']")
                if element.is_enabled():
                    self.Methods.enter_text(By.XPATH, "//input[@id='txtAddress2']", Crm_lead_Address)

                else:
                    raise ElementNotInteractableException(f"Exception caught:{str} ")

            else:
                print("Texts do not match. Handling the mismatch.")

        except NoSuchElementException as e:
            raise NoSuchElementException(f"Title elements not found: {str(e)}")
        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Exception caught while clicking on title: {str(e)}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def Address_dropdown(self, option_text_Status):
        try:

            input_element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "// input[ @ id = 'txtAddress2']")))
            input_element.clear()
            input_element.send_keys(option_text_Status)

            time.sleep(2)

            # using actions key to move through the suggestions
            for _ in range(1000000):
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ARROW_DOWN).perform()

                focused_option = input_element.get_attribute('value')

                if option_text_Status.lower() in focused_option.lower():
                    print(f"Found matching option: '{option_text_Status}'. Selecting it.")
                    actions.send_keys(Keys.ENTER).perform()  # Select the matching option
                    return True

            print(f"No matching option found for '{option_text_Status}' in the drop-down.")
            return False

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

    def Location(self, CrmLocation):
        try:
            drop_down = self.Methods.wait_for_element(By.XPATH, "//select[@name='drpLocations']")

            drop_down.click()

            Option = Select(drop_down)
            Option.select_by_visible_text(f'{CrmLocation}')

        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Exception caught while clicking on title: {str(e)}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def Lead_type(self, Crm_Lead_type):
        try:
            Type_dropdown = self.Methods.wait_for_element(By.ID, "drpLeadType")
            Type_dropdown.click()

            Options = Select(Type_dropdown)
            Options.select_by_visible_text(f'{Crm_Lead_type}')

        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Exception caught while clicking on title: {str(e)}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def company_name(self, crm_company_name):
        try:
            element = self.Methods.wait_for_element(By.ID, "txtLeadName")

            if element.is_enabled():
                element.clear()
                element.send_keys("crm_company_name")
            else:
                raise ElementNotInteractableException

        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f"Failed to enter value in the text field, Exception caught{str(e)}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

    def Company_Phone_number(self, crm_company_Phone_number):
        try:
            element = self.driver.find_element(By.ID, "txtLeadPhone")

            if element.is_enabled():
                element.clear()
                element.send_keys(crm_company_Phone_number)
            else:
                raise ElementNotInteractableException

        except NoSuchElementException as e:
            raise NoSuchElementException(f"Exception caught:{str(e)}")

    def company_fax(self, crm_company_fax):
        try:
            element = self.driver.find_element(By.XPATH, "//input[@id='txtFaxNumber']")

            if element.is_enabled():
                element.clear()
                element.send_keys(crm_company_fax)
            else:
                raise ElementNotInteractableException

        except NoSuchElementException as e:
            raise NoSuchElementException(f"Exception caught:{str(e)}")

    def Company_email(self, crm_company_email):
        try:
            element = self.driver.find_element(By.ID, "txtLeadEmail")

            if element.is_enabled():
                element.clear()
                element.send_keys(crm_company_email)
            else:
                raise ElementNotInteractableException
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Exception caught:{str(e)}")


    def Website(self, crm_website):
        try:
            element = self.driver.find_element(By.ID, "txtWebsite")

            if element.is_enabled():
                element.clear()
                element.send_keys(crm_website)
            else:
                raise ElementNotInteractableException
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Exception caught element not found:{str(e)}")

    def Assigned(self, crm_Assigned):
        try:
            element = self.driver.find_element(By., "")
            element.click()
            options = Select(element)

            options.select_by_visible_text(crm_Assigned)

        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Element not found")

    def Assigned2(self, crm_Assigned_2):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR,"div.my-container.active-cont div.app-container div.px-3:nth-child(2) div.row div.col-md-12 div.tab-content div.tab-pane.fade.show.active:nth-child(2) div.card.a-card-wrap div.row.m-0.px-3:nth-child(7) div.col-md-4:nth-child(2) div.form-group div.e-input-group div.e-input-in-wrap > span.e-input-group.e-control-wrapper.e-ddl.e-lib.e-keyboard.e-valid-input")

            element.click()
            options = Select(element)
            options.select_by_visible_text(crm_Assigned_2)
        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException(f"Element not found")





