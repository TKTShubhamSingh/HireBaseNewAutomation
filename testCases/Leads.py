import logging
import time
import unittest
from selenium import webdriver
from pageObjects.Leads import Lead
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


class Leads(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(filename='test.log', level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)

        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "C:\\pythonProject\\HireBase_data.jsonn", scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open("Leads")
        self.sheet = spreadsheet.worksheet('Sheet1')
        self.driver = webdriver.Chrome()
        self.driver.get("https://hirebaseproto.tktechnico.com/login")
        self.driver.maximize_window()
        self.leads = Lead(self.driver)

    def test_leads(self):
        df = pd.DataFrame(self.sheet.get_records())
        for index, row in df.iterrows():
            if index == 0:
                self.leads.usn(row['Username'])
                time.sleep(1)
                self.leads.pss(row['Password'])
                time.sleep(1)
                # self.leads.eye()
                time.sleep(1)
                self.leads.lgbtn()
                time.sleep(5)
            self.leads.dropd()
            time.sleep(1)

            actual_title = self.driver.title
            if "Hirebase" in actual_title:
                print("Title match=>" + actual_title)
                # try:

                time.sleep(1)
                self.leads.lead()
                time.sleep(1)
                # self.leads.drp()
                print("dd clicked")
                time.sleep(3)
                self.leads.adld()
                time.sleep(1)
                self.leads.address(row['Address'])
                time.sleep(3)
                self.leads.location(row['Location'])
                time.sleep(1)
                self.leads.ldtype(row['Lead_type'])
                time.sleep(1)
                self.leads.company_n(row['Leads_company'])
                time.sleep(1)
                self.leads.company_ph(row['Company_ph'])
                time.sleep(1)
                self.leads.company_fax(row['Company Fax'])
                time.sleep(1)
                self.leads.company_email(row['Company mail'])
                time.sleep(1)
                self.leads.company_website(row['Website'])
                time.sleep(1)
                self.leads.assigned_1(row['Assigned to 1'])
                time.sleep(1)
                self.leads.assigned_2(row['Assigned 2'])
                time.sleep(1)
                self.leads.sales_manager(row['Sales manager'])
                time.sleep(1)
                self.leads.contact_name(row['Contact name'])
                time.sleep(1)
                self.leads.contact_number(row['Contact no'])
                time.sleep(1)
                self.leads.contact_position(row['Contact pos'])
                time.sleep(1)
                self.leads.number_of_employee(row['Number of Employees'])
                time.sleep(1)
                self.leads.scroll()
                self.leads.industry_type(row['Industry type'])
                time.sleep(1)
                self.leads.source_type(row['Source type'])
                time.sleep(1)
                self.leads.sc_type_details(row['Source type details'])
                time.sleep(1)
                self.leads.using_agency()
                time.sleep(1)
                self.leads.Agency_name1(row['Agency name1'])
                time.sleep(1)
                self.leads.on_site1()
                time.sleep(1)
                self.leads.mark_up1(row['Markup rate 1'])
                time.sleep(1)
                self.leads.Agency_name2(row['Agency name 2'])
                time.sleep(1)
                self.leads.on_site2()
                time.sleep(1)
                self.leads.mark_up2(row['Markup rate 2'])
                time.sleep(1)
                self.leads.Agency_name3(row['Agency name 3'])
                time.sleep(1)
                self.leads.on_site3()
                time.sleep(1)
                self.leads.mark_up3(row['Markup rate 3'])
                time.sleep(1)
                self.leads.Date_signed(row['Date signed'])
                time.sleep(1)
                self.leads.commission(row['Commission'])
                time.sleep(1)
                self.leads.conversion_fee(row['Conversion fee'])
                time.sleep(1)
                self.leads.contribution(row['Contribution'])
                time.sleep(1)
                self.leads.annual_revenue(row['Annual revenue'])
                time.sleep(1)
                self.leads.additional_note(row['Additional notes'])
                time.sleep(1)
                self.leads.other_details()
                time.sleep(1)
                self.leads.Required_number(row['Req number'])
                time.sleep(1)
                self.leads.shifts()
                time.sleep(1)
                self.leads.office_servicing(row['Office servicing'])
                time.sleep(1)
                self.leads.general_labor(row['General labour'])
                time.sleep(1)
                self.leads.over_time(row['Overtime'])
                time.sleep(1)
                self.leads.clerical(row['Clerical'])
                time.sleep(1)
                self.leads.roll_over(row['Rollover'])
                time.sleep(1)
                self.leads.sick_days(row['Sick days'])
                time.sleep(1)
                self.leads.billed_sick_days()
                time.sleep(1)
                self.leads.holiday(row['Holiday'])
                time.sleep(1)
                self.leads.billed_holidays()
                time.sleep(1)
                self.leads.vacation(row['Vacation'])
                time.sleep(1)
                self.leads.billed_vacation()
                time.sleep(2)
                self.leads.scroll2()
                time.sleep(1)
                self.leads.save3()
                time.sleep(3)
                break

        # except Exception:
        # es = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # self.driver.save_screenshot('Screenshot_' + es + '.png')

        else:
            print("Title does not match")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
