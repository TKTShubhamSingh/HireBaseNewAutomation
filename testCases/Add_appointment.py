import time
import unittest
import os
import gspread
import pandas as pd
from gspread import Worksheet
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from pageObjects.Adding_appointment import Adding_appointmentP
from utilities.readdata import Readconfig


class Adding_appointment(unittest.TestCase):

    def setUp(self):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\Framework\\TestData\\hiredata.json", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet("Sheet1")

    def test_Adding_appointment(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get("https://hirebaseproto.tktechnico.com")
            self.driver.maximize_window()

            df = pd.DataFrame(self.sheet.get_records())
            self.add_appointment = Adding_appointmentP(self.driver)

            for index, row in df.iterrows():
                if index == 0:
                    self.add_appointment.username(row['Username'])
                    self.add_appointment.password(row['Password'])
                    time.sleep(2)
                    self.add_appointment.login_button()
                    time.sleep(5)
                    self.add_appointment.drop_down()
                    time.sleep(1)
                    self.add_appointment.leads()
                    time.sleep(1)
                    self.add_appointment.location_drop()
                    time.sleep(1)
                    self.add_appointment.filter()
                    time.sleep(2)
                    self.add_appointment.people_card()
                    time.sleep(2)
                    self.add_appointment.appointment()
                    time.sleep(2)
                    self.add_appointment.date()
                    time.sleep(5)
                    self.add_appointment.Add_title(row['Title'])
                    time.sleep(2)
                    self.add_appointment.more_details()
                    time.sleep(2)
                    self.add_appointment.title(row['Title1'])
                    time.sleep(2)
                    self.add_appointment.status()
                    time.sleep(2)
                    self.add_appointment.status2()
                    time.sleep(2)
                    self.add_appointment.description(row['description'])
                    time.sleep(2)
                    self.add_appointment.meeting_with(row['meeting_with'])
                    time.sleep(2)
                    self.add_appointment.feedback()
                    time.sleep(2)
                    self.add_appointment.feed_back()
                    time.sleep(2)
                    self.add_appointment.save()
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            current_datetime = time.strftime("%Y-%m-%d_%H-%M-%S")
            folder_name = "Screenshots"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            filename = f"{folder_name}/error_{current_datetime}.png"
            self.driver.save_screenshot(filename)
            self.logger.info(f"Screenshot saved: {filename}")
            raise e

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
