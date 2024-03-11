import time
from pyasn1.compat.octets import null
from selenium.webdriver.common.by import By



class RegisP:
    a = null
    reg = "//a[@class='text-pink']"
    FN = "txtFirstName"
    LN = "txtLastName"
    phn = "//input[@id='txtPhoneNumber']"
    em = "//input[@type='email']"
    pswd = "txtPassword"
    eye1 = "//div[@class='row']//div[1]//div[1]//div[1]//div[1]//span[1]//i[1]"
    cpswd = "txtConfirmPassword"
    eye2 = "//div[@class='col-md-8 py-3']//div[2]//div[1]//div[1]//div[1]//span[1]//i[1]"
    bd = "//input[@class='form-control ']"
    loca = "drpLocations"
    registration = "//button[@class='btn btn-danger  ']"
    addr = "//input[@id='txtAddress']"
    cities = "//input[@id='txtCity']"
    sd = "//select[@id='txtState']"
    zzip = "//input[@id='txtZipcode']"
    conti1 = "//button[@title='Click to continue']"
    ba1 = "//button[@title='Click to go back']"
    sos = "//input[@id='txtSSN']"
    alterP = "//input[@id='txtAlternatePhone']"
    Posi = "//div[@class='selected-options-container ']"
    shift = "//div[@id='drpShifts']"
    emp = "//div[@id='drpEmploymentTypes']"
    married = "//input[@value = 'Married']"
    gen = "//input[@id='rdbtnMale']"
    contiue = "button[title='Click to continue']"
    # reference
    ref_name = "//input[@id='txtRefName1']"
    ref_number = "//input[@name='txtRefPhone1']"
    conti = "button[title='Click to continue']"
    # Work history
    work = "//input[@class='form-check-input']"
    emp1 = "//input[@id = 'txtEmployer1']"
    adrrs = "//input[@name ='txtEmployerAddress1']"
    phno = "//input[@id = 'txtEmployerPhone1']"
    tele = "//input[@id='txtEmployerTelePhone1']"
    posi2 = "//div[@class='selected-options-container ']"
    supervi = "//input[@id='txtSupervisor1']"
    any = "//input[@id='rdbtnAONEAge']"
    dis = "//input[@name='rdbtnEBAR']"
    CE = "#rdbtnCEM"
    da = "#txtDOEFrom1"
    doets = "//input[@id='txtDOETo1']"
    other = "//input[@id='txtOtherEmploymentName']"
    exp = "//input[@id='txtExplain']"
    con = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]"
    # Education
    ED = "//input[@class='form-check-input']"
    high = "//input[@id='rdbtnHSOne']"
    diploma = "//input[@name='rdbtnD']"
    ged = "#rdbtnGED"
    school_xpath = "//input[@id='txtSchools']"
    city_xpath = "//input[@id='txtEDCityState']"
    others_xpath = "//input[@id='txtEDOthers']"

    def __init__(self, driver):
        self.driver = driver

    def regbtn(self):
        self.driver.find_element(By.XPATH, self.reg).click()

    def fName(self, First_name):
        self.driver.find_element(By.ID, self.FN).send_keys(First_name)

    def sName(self, Second_name):
        self.driver.find_element(By.ID, self.LN).send_keys(Second_name)

    def Phnum(self, Phone):
        self.driver.find_element(By.XPATH, self.phn).send_keys(Phone)

    def Email(self, EM):
        self.driver.find_element(By.XPATH, self.em).send_keys(EM)

    def pss(self, Pass):
        self.driver.find_element(By.ID, self.pswd).send_keys(Pass)

    def psseye(self):
        self.driver.find_element(By.XPATH, self.eye1).click()

    def cpss(self, cPass):
        self.driver.find_element(By.ID, self.cpswd).send_keys(cPass)

    def cpsseye(self):
        self.driver.find_element(By.XPATH, self.eye2).click()

    def BD(self, birth):
        self.driver.find_element(By.XPATH, self.bd).send_keys(birth)

    def loc(self, location):
        self.driver.find_element(By.NAME, self.loca).click()
        self.driver.find_element(By.NAME, self.loca).send_keys(location)

    def regis(self):
        self.driver.find_element(By.XPATH, self.registration).click()

    # personal info section

    def address(self, add):
        self.driver.find_element(By.XPATH, self.addr).send_keys(add)

    def city(self, ci):
        self.driver.find_element(By.XPATH, self.cities).send_keys(ci)

    def state(self, stated):
        self.driver.find_element(By.XPATH, self.sd).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.sd).send_keys(stated)

    def ziip(self, zip):
        self.driver.find_element(By.XPATH, self.zzip).send_keys(zip)

    def continue1(self):
        self.driver.find_element(By.XPATH, self.conti1).click()

    def back1(self):
        self.driver.find_element(By.XPATH, self.ba1).click()

    # personal info section 2

    def ssn(self, sossn):
        self.driver.find_element(By.XPATH, self.sos).send_keys(sossn)

    def alterPh(self, Alter):
        self.driver.find_element(By.XPATH, self.alterP).send_keys(Alter)

    def pos(self):
        self.driver.find_element(By.XPATH, self.Posi).click()
        self.driver.find_element(By.CSS_SELECTOR, ".multi-selector-option:nth-child(1) > .ms-3").click()

    def shifts(self):
        self.driver.find_element(By.XPATH, self.shift).click()
        self.driver.find_element(By.CSS_SELECTOR, ".multi-selector-option:nth-child(1) > .ms-3").click()

    def Emp_type(self):
        self.driver.find_element(By.XPATH, self.emp).click()
        self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > "
                                                  "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                                  "div:nth-child(4)"
                                                  "> div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > "
                                                  "div:nth-child("
                                                  "2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > "
                                                  "span:nth-child(3)").click()

    def Marital(self):
        self.driver.find_element(By.XPATH, self.married).click()

    def Gender(self):
        self.driver.find_element(By.XPATH, self.gen).click()

    def conti(self):
        self.driver.find_element(By.CSS_SELECTOR, self.contiue).click()

    # References

    def reference_name(self, ref_n):
        self.driver.find_element(By.XPATH, self.ref_name).send_keys(ref_n)

    def reference_num(self, ref_m):
        self.driver.find_element(By.XPATH, self.ref_number).send_keys(ref_m)

    def contin(self):
        self.driver.find_element(By.XPATH, self.conti).click()

    # Work history

    def wh(self):
        self.driver.find_element(By.XPATH, self.work).click()

    def empt(self, empr):
        self.driver.find_element(By.XPATH, self.emp1).click()
        self.driver.find_element(By.XPATH, self.emp1).send_keys(empr)

    def adr(self, adrr):
        self.driver.find_element(By.XPATH, self.adrrs).click()
        self.driver.find_element(By.XPATH, self.adrrs).send_keys(adrr)

    def phnemp(self, phn):
        self.driver.find_element(By.XPATH, self.phno).send_keys(phn)

    def Tele(self, tel):
        self.driver.find_element(By.XPATH, self.tele).send_keys(tel)

    def pos2(self):
        self.driver.find_element(By.XPATH, self.posi2).click()
        self.driver.find_element(By.CSS_SELECTOR, ".multi-selector-option:nth-child(1) > .ms-3 ").click()

    def superv(self, su):
        self.driver.find_element(By.XPATH, self.supervi).send_keys(su)

    def currentlyemp(self):
        self.driver.find_element(By.CSS_SELECTOR, self.CE).click()

    def doe(self, DOE):
        self.driver.find_element(By.CSS_SELECTOR, self.da).click()
        self.driver.find_element(By.CSS_SELECTOR, self.da).send_keys(DOE)

    def doet(self, DOET):
        self.driver.find_element(By.XPATH, self.doets).click()
        self.driver.find_element(By.XPATH, self.doets).send_keys(DOET)

    def any_other(self):
        self.driver.find_element(By.XPATH, self.any).click()

    def Other(self, oth):
        self.driver.find_element(By.XPATH, self.other).send_keys(oth)

    def discharged(self):
        self.driver.find_element(By.XPATH, self.dis).click()

    def explain(self, Explain):
        self.driver.find_element(By.XPATH, self.exp).send_keys(Explain)

    def contiw(self):
        self.driver.find_element(By.XPATH, self.con).click()

    # Education details

    def edu_details(self):
        self.driver.find_element(By.XPATH, self.ED).click()

    def hgs(self):
        self.driver.find_element(By.XPATH, self.high).click()

    def dip(self):
        self.driver.find_element(By.XPATH, self.diploma).click()

    def Ged(self):
        self.driver.find_element(By.CSS_SELECTOR, self.ged).click()

    def School(self, sch):
        self.driver.find_element(By.XPATH, self.school_xpath).send_keys(sch)

    def City(self, cit):
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(cit)

    def Others(self, oths):
        self.driver.find_element(By.XPATH, self.others_xpath).send_keys(oths)

    def cntinue(self):
        self.driver.find_element(By.CSS_SELECTOR, ".continue-button").click()