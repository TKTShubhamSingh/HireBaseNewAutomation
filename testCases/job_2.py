import logging
import time
import unittest
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.JobOrderP import JobOrderP
from selenium.webdriver.support import expected_conditions as EC


class Job(unittest.TestCase):

    def setUp(self):

        logging.basicConfig(filename='test.log', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet5')

    def test_job_op(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com/login")
        self.driver.maximize_window()

        df = pd.DataFrame(self.sheet.get_records())
        self.jb = JobOrderP(self.driver)

        for index, row in df.iterrows():
            if index == 0:
                self.jb.setUserName(row['Username'])
                self.jb.setPassword(row['Password'])
                self.jb.login()
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "(//li[@class='nav-link'])[6]")))
            self.jb.job()
            time.sleep(2)
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='c-btn dark-btn ms-3']")))

            expected_title = "Hirebase"
            actual_title = self.driver.title

            if expected_title == actual_title:
                self.jb.addbtn()
                time.sleep(2)
                self.jb.locdrop()
                time.sleep(2)
                self.jb.s_option(row['Location'])
                time.sleep(2)
                self.jb.calendar()
                time.sleep(2)
                self.jb.ddae(row['Request Date'])
                time.sleep(2)
                self.jb.clientdrop()
                time.sleep(2)
                self.jb.clientselect(row['Client Name'])
                time.sleep(2)
                self.jb.startd(row['Start Date'])
                time.sleep(2)
                self.jb.starttime(row['Start Time'])
                time.sleep(2)
                self.jb.rep_to()
                time.sleep(2)
                self.jb.op(row['Report To'])
                time.sleep(2)
                self.jb.dress(row['Dress Code'])
                time.sleep(2)
                self.jb.endd(row['End Date'])
                time.sleep(2)
                self.jb.endtime(row['End Time'])
                time.sleep(2)
                self.jb.arr_pm_2()
                time.sleep(2)
                self.jb.add()
                time.sleep(2)
                self.jb.jobp()
                time.sleep(2)
                self.jb.jobpos(row['Job position'])
                time.sleep(2)
                self.jb.desc()
                time.sleep(2)
                self.jb.desc2(row['Description'])
                time.sleep(2)
                self.jb.Rbl()
                time.sleep(2)
                self.jb.Quan(row['Quantity'])
                time.sleep(2)
                self.jb.Pay(row['Pay Rate'])
                time.sleep(2)
                self.jb.notes(row['Notes'])
                time.sleep(2)

                self.jb.save()
                time.sleep(2)
                print("job created")
            break

    def tearDown(self):
        self.driver.quit()
