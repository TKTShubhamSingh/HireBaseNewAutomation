import datetime
import logging
import os
import time
import gspread
import pandas as pd
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.RegistrationP import RegisP
from oauth2client.service_account import ServiceAccountCredentials


class TestRegistration(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\HireBase_data.json",
            scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.baseurl = Readconfig.getAppurl()
        self.sheet = spreadsheet.worksheet('Sheet4')
        self.rp = RegisP(self.driver)
        self.driver.get("https://hirebaseproto.tktechnico.com/login")

    def test_Regis(self):
        df = pd.DataFrame(self.sheet.get_records())
        for index, row in df.iterrows():
            self.rp.regbtn()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "txtFirstName")))
            self.rp.fName(row['First_name'])
            self.rp.sName(row['Second_name'])
            self.rp.Phnum(row['Phone Number'])
            self.rp.Email(row['Email'])
            self.rp.pss(row['Password'])
            time.sleep(2)
            self.rp.psseye()
            time.sleep(1)
            self.rp.cpss(row['Confirm Password'])
            time.sleep(1)
            self.rp.cpsseye()
            self.rp.BD(row['Birth Date'])
            time.sleep(1)
            self.rp.loc(row['Location'])
            time.sleep(2)
            self.rp.regis()
            time.sleep(10)
            self.rp.address(row['Address'])
            time.sleep(2)
            self.rp.city(row['City'])
            time.sleep(2)
            self.rp.state(row['State'])
            self.rp.ziip(row['Zip'])
            time.sleep(2)
            self.rp.continue1()
            time.sleep(2)
            self.rp.ssn(row['Social security number'])
            time.sleep(2)
            self.rp.alterPh(row['Alternate ph'])
            time.sleep(2)
            print("clickable")
            self.rp.pos()
            time.sleep(2)
            self.rp.shifts()
            time.sleep(2)
            self.rp.Emp_type()
            time.sleep(2)
            self.rp.Marital()
            time.sleep(2)
            self.rp.Gender()
            time.sleep(2)
            self.rp.conti()
            time.sleep(5)
            self.rp.reference_name(row['Ref_name'])
            time.sleep(2)
            self.rp.reference_num(row['Ref_number'])
            time.sleep(2)
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//*[text()='{"Continue"}']")))
            time.sleep(3)
            element.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='rdbtnEMYD'] ")))
            time.sleep(2)
            self.rp.wh()
            time.sleep(2)
            self.rp.empt(row['Empr'])
            time.sleep(2)
            self.rp.adr(row['Address1'])
            time.sleep(2)
            self.rp.phnemp(row['Phone_number1'])
            time.sleep(2)
            self.rp.Tele(row['Telephone1'])
            time.sleep(2)
            self.rp.pos2()
            time.sleep(2)
            self.rp.superv(row['Supervisor'])
            time.sleep(2)
            self.rp.currentlyemp()
            time.sleep(2)
            self.rp.doe(row['Doe'])
            time.sleep(2)
            self.rp.doet(row['Doet'])
            self.rp.any_other()
            time.sleep(2)
            self.rp.Other(row['Other'])
            time.sleep(2)
            self.rp.discharged()
            time.sleep(2)
            self.rp.explain(row['Explain'])
            time.sleep(2)
            self.rp.contiw()
            time.sleep(2)
            self.rp.edu_details()
            time.sleep(2)
            self.rp.hgs()
            time.sleep(2)
            self.rp.dip()
            time.sleep(2)
            self.rp.Ged()
            time.sleep(1)
            self.rp.School(row['School'])
            time.sleep(1)
            self.rp.City(row['City1'])
            time.sleep(1)
            self.rp.Others(row['Other1'])
            time.sleep(1)
            self.rp.cntinue()
            time.sleep(3)

            try:
                user_already_present = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".Toastify__toast-body > div:nth-child(2)"))
                )
                if user_already_present:
                    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    folder_name = "Screenshots"
                    if not os.path.exists("C:\\pythonProject\\Framework\\Screenshots"):
                        os.makedirs(folder_name)
                    filename = f"{folder_name}/user_present{current_datetime}.png"
                    self.driver.save_screenshot(filename)
            except:
                pass

        else:
            print("done")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
