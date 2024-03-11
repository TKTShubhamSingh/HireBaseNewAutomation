import logging
import time
import unittest

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Route_list import Route_listP
from selenium.webdriver.support import expected_conditions as EC


class Route_List(unittest.TestCase):

    def setup(self):
        logging.basicConfig(filename='test.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet3')
        self.driver = webdriver.Chrome()
       # self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.get("https://hirebaseproto.tktechnico.com/login")

    def Route_list1(self):

        df = pd.DataFrame(self.sheet.get_records())
        self.route_list = Route_listP(self.driver)

        for index, row in df.iterrows():
            self.route_list.username(row['Username'])
            time.sleep(1)
            self.route_list.password(row['Password'])
            time.sleep(1)
            self.route_list.login_button()
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html[1]/body[1]/div[1]/nav[1]/div[1]/div[1]/ul[2]/li[3]/a[1]")))
            title = self.driver.title
            if "Hirebase" in title:
                self.route_list.drop_down()
                time.sleep(1)
                self.route_list.Route_list()
                time.sleep(1)
                self.route_list.Add_route()
                time.sleep(1)
                self.route_list.username1(row['User'])
                time.sleep(1)
                self.route_list.date(row['Date'])
                time.sleep(1)
                self.route_list.add_route()
                time.sleep(1)
                self.route_list.add_pipline()
                time.sleep(1)
                self.route_list.save()
                time.sleep(2)
                self.route_list.save1()
                time.sleep(5)

                print("title=>" + title)
                break
            else:
                print("title not matched")

    def tearDown(self):
        self.driver.quit()