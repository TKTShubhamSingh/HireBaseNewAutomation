import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Lead:
    usn_id = "txtEmail"
    usp_id = "txtPassword"
    eyebtn = "//i[@class='fa fa-eye password-toggle-icon']"
    loginbtn = "//button[@class='col-md-12 btn btn-login pt-2 mt-4']"
    dd = "//a[@class='nav-link dropdown-toggle text-primary show']"
    lt = "//a[@role='button']"
    crm = "/html[1]/body[1]/div[1]/nav[1]/div[1]/div[1]/ul[2]/li[3]/ul[1]/li[2]/a[1]"
    ld = "//div[@class='nav-item-box-img active']"
    locdrp = "//div[@class='filter-bar p-3']//div[1]//div[1]//span[2]"

    add = "button[class='c-btn dark-btn ms-3']"
    ad = "//input[@id='txtAddress2']"
    loc = "drpLocations"
    ltype = "//select[@name='drpLeadType']"
    cname = "//input[@id='txtLeadName']"
    comp_ph = "//input[@id='txtLeadPhone']"
    comp_fax = "//input[@id='txtFaxNumber']"
    comp_email = "#txtLeadEmail"

    def __init__(self, driver):
        self.driver = driver

    def usn(self, user):
        self.driver.find_element(By.ID, self.usn_id).send_keys(user)

    def pss(self, passw):
        self.driver.find_element(By.ID, self.usp_id).send_keys(passw)

    def eye(self):
        self.driver.find_element(By.XPATH, self.eyebtn).click()

    def lgbtn(self):
        self.driver.find_element(By.XPATH, self.loginbtn).click()

    def dropd(self):
        self.driver.find_element(By.XPATH, self.lt).click()
        self.driver.find_element(By.XPATH, self.crm).click()

    def lead(self):
        self.driver.find_element(By.XPATH, self.ld).click()

    def drp(self):
        self.driver.find_element(By.XPATH, self.locdrp).click()
        time.sleep(2)

    def adld(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add).click()

    def address(self, address):
        self.driver.find_element(By.XPATH, "//input[@id='txtAddress2']").send_keys(address)



    def location(self, loca):
        self.driver.find_element(By.ID, self.loc).send_keys(loca)

    def ldtype(self, leadt):
        self.driver.find_element(By.XPATH, self.ltype).click()
        self.driver.find_element(By.XPATH, self.ltype).send_keys(leadt)

    def company_n(self, cmname):
        self.driver.find_element(By.XPATH, self.cname).send_keys(cmname)

    def company_ph(self, companyphone):
        self.driver.find_element(By.XPATH, self.comp_ph).send_keys(companyphone)

    def company_fax(self, companyfax):
        self.driver.find_element(By.XPATH, self.comp_fax).send_keys(companyfax)

    def company_email(self, cemail):
        cm = self.driver.find_element(By.CSS_SELECTOR, self.comp_email)
        cm.send_keys(cemail)

    def company_website(self, csite):
        self.driver.find_element(By.XPATH, "//input[@name='txtWebsite']").send_keys(csite)

    def assigned_1(self, assigned_1):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                                           "2]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/span[1]").send_keys(assigned_1)

    def assigned_2(self, assigned_2):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                                           "2]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/span[1]").send_keys(assigned_2)

    def sales_manager(self, sales_manager):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                                           "2]/div[1]/div[7]/div[3]/div[1]/div[1]/div[1]/span[1]").send_keys(
            sales_manager)

    def contact_name(self, contact_name):
        self.driver.find_element(By.XPATH, "//input[@id='txtSupervisor']").send_keys(contact_name)

    def contact_number(self, contact_number):
        self.driver.find_element(By.XPATH, "//input[@id='txtLeadTelePhone']").send_keys(contact_number)

    def contact_position(self, contact_position):
        self.driver.find_element(By.XPATH, "//input[@id='drpPosition']").send_keys(contact_position)

    def number_of_employee(self, number_of_employee):
        self.driver.find_element(By.XPATH, "//input[@id='txtNumberOfEmployees']").send_keys(number_of_employee)

    def industry_type(self, industry_type):
        self.driver.find_element(By.XPATH, "//select[@id='drpIndustryType']").send_keys(industry_type)

    def source_type(self, source_type):
        self.driver.find_element(By.XPATH, "//select[@id='drpSourceType']").send_keys(source_type)

    def sc_type_details(self, sc_type_details):
        self.driver.find_element(By.XPATH, "//input[@id='txtReference']").send_keys(sc_type_details)

    def using_agency(self):
        self.driver.find_element(By.XPATH, "//input[@id='flexSwitchCheckDefault']").click()

    def scroll(self):
        element = self.driver.find_element(By.XPATH, "//textarea[@id='txtAdditionalNote']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def Agency_name1(self, Agency_name1):
        self.driver.find_element(By.XPATH, "//input[@id='txtAgency']").send_keys(Agency_name1)

    def on_site1(self):
        self.driver.find_element(By.XPATH, "//input[@id='rdbtnIsHaveOnSite']").click()

    def mark_up1(self, mark_up1):
        self.driver.find_element(By.XPATH, "//input[@name = 'txtMarkUpRate'] ").send_keys(mark_up1)

    def Agency_name2(self, Agency_name2):
        self.driver.find_element(By.XPATH, "//input[@id = 'txtAgency2'] ").send_keys(Agency_name2)

    def on_site2(self):
        self.driver.find_element(By.XPATH, "//input[@name = 'rdbtnIsHaveOnSite2']").click()

    def mark_up2(self, mark_up2):
        self.driver.find_element(By.XPATH, "//input[@name = 'txtMarkUpRate2']").send_keys(mark_up2)

    def Agency_name3(self, Agency_name3):
        self.driver.find_element(By.XPATH, "//input[@id = 'txtAgency3'] ").send_keys(Agency_name3)

    def on_site3(self):
        self.driver.find_element(By.XPATH, "//input[@name = 'rdbtnIsHaveOnSite3']").click()

    def mark_up3(self, mark_up3):
        self.driver.find_element(By.XPATH, "//input[@name = 'txtMarkUpRate3']").send_keys(mark_up3)

    def Date_signed(self, Date_signed):
        self.driver.find_element(By.XPATH, "//input[@id='txtDateSigned']").send_keys(Date_signed)

    def commission(self, commission):
        self.driver.find_element(By.XPATH, "//input[@id='txtCommission']").send_keys(commission)

    def conversion_fee(self, conversion_fee):
        self.driver.find_element(By.XPATH, "//input[@id='txtConversionFee']").send_keys(conversion_fee)

    def contribution(self, contribution):
        self.driver.find_element(By.XPATH, "//input[@id='txtContributions']").send_keys(contribution)

    def annual_revenue(self, annual_revenue):
        self.driver.find_element(By.XPATH, "//input[@id='txtAnnualRevenue']").send_keys(annual_revenue)

    def additional_note(self, additional_note):
        self.driver.find_element(By.XPATH, "//textarea[@id='txtAdditionalNote']").send_keys(additional_note)

    def save1(self):
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-solid fa-floppy-disk']").click()

    def other_details(self):
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) button:nth-child(1)").click()

    def scroll2(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_UP).perform()

    def Required_number(self, Required_number):
        self.driver.find_element(By.XPATH, "//input[@id='txtNoOfPeopleRequired']").send_keys(Required_number)

    def shifts(self):
        self.driver.find_element(By.XPATH, "//div[contains(@class,'selected-options-container')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".multi-selector-option:nth-child(1) > .checkbox").click()

    def office_servicing(self, office_servicing):
        self.driver.find_element(By.XPATH, "//input[@id='txtOfficeServicing']").send_keys(office_servicing)

    def general_labor(self, general_labor):
        self.driver.find_element(By.CSS_SELECTOR, "#txtGeneralLaborPercentage").send_keys(general_labor)

    def over_time(self, over_time):
        self.driver.find_element(By.XPATH, "//input[@id='txtOverTimePercentage']").send_keys(over_time)

    def clerical(self, clerical):
        self.driver.find_element(By.XPATH, "//input[@id='txtClericalPercentage']").send_keys(clerical)

    def roll_over(self, roll_over):
        self.driver.find_element(By.NAME, "txtRolloverPercentage").send_keys(roll_over)

    def sick_days(self, sick_days):
        self.driver.find_element(By.XPATH, "//input[@id='txtSickDays']").send_keys(sick_days)

    def billed_sick_days(self):
        self.driver.find_element(By.XPATH, "//input[@id='rdbtnIsBilledSickDays']").click()

    def holiday(self, holiday):
        self.driver.find_element(By.CSS_SELECTOR, "#txtHolidays").send_keys(holiday)

    def billed_holidays(self):
        self.driver.find_element(By.XPATH, "//input[@name='rdbtnIsBilledHolidays']").click()

    def vacation(self, vacation):
        self.driver.find_element(By.XPATH, "//input[@id='txtVacation']").send_keys(vacation)

    def billed_vacation(self):
        self.driver.find_element(By.XPATH, "//input[@name='rdbtnIsBilledVacation']").click()

    def save3(self):
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/i[1]").click()
