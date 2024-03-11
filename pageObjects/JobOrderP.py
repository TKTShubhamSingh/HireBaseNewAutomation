from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class JobOrderP:
    usn_username_id = "txtEmail"
    pss_password_id = "txtPassword"
    btt_login_xpath = "//button[@class='col-md-12 btn btn-login pt-2 mt-4']"
    Job_xpath = "(//li[@class='nav-link'])[6]"
    Addbtn_xpath = "//button[@class='c-btn dark-btn ms-3']"
    Locdrop_id = "drpLocations"
    cal_id = "txtReqDate"
    cdrop_id = "drpClients"
    cselect_xpath = "//option[text()='Aaron Thomas']"
    sdate = "//input[@id='txtStartDate']"
    sstdate = "18-08-2023"
    endate = "19-08-2023"
    stime = "//input[@id='txtStartTime']"
    amarr = "//div[6]//div[1]//div[1]//div[1]//div[2]//span[1]//i[1]"
    pmarr = ("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/div["
             "1]/div[1]/div[2]/span[3]/i[1]")
    pmarr_2 = ".col-md-3:nth-child(10) .fa-chevron-right"
    report_to = "//input[@id='txtReportTo']"
    drr = "//input[@id='txtDressCode']"
    edate = "//input[@id='txtEndDate']"
    etime = "//input[@id='txtEndTime']"
    addj = "//i[@class='fa fa-plus-circle fa-3x']"
    jobpo = "//div[@id='job-details']/div/div[5]/div/div[2]/div/table/tbody/tr/td[2]/div/select"
    descr = "/html[1]//tbody[1]/tr[1]/td[3]/div[1]/input[1]"
    scr = "//button[@title='Accept changes']"
    rbl = "//div[@id='job-details']/div/div[5]/div/div[2]/div/table/tbody/tr/td[4]/div/div/div/input"
    rbh = "//div[@id='job-details']/div/div[5]/div/div[2]/div/table/tbody/tr/td[4]/div/div/div[2]/input."
    quan = "//div[@id='job-details']/div/div[5]/div/div[2]/div/table/tbody/tr/td[5]/div/div/input"
    pay = "//div[@id='job-details']/div/div[5]/div/div[2]/div/table/tbody/tr/td[6]/div/div/input"
    note = "txtNotes"
    sve = "//button[@title='Accept changes']"
    Addbtn = "//button[normalize-space()='New']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.usn_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.pss_password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.btt_login_xpath).click()

    def job(self):
        self.driver.find_element(By.XPATH, self.Job_xpath).click()

    def addbtn(self):
        self.driver.find_element(By.XPATH, self.Addbtn_xpath).click()

    def locdrop(self):
        self.driver.find_element(By.ID, self.Locdrop_id).click()

    def s_option(self, loc):
        self.driver.find_element(By.ID, self.Locdrop_id).send_keys(loc)

    def calendar(self):
        self.driver.find_element(By.ID, self.cal_id).click()

    def ddae(self, cal):
        self.driver.find_element(By.ID, self.cal_id).send_keys(cal)

    def clientdrop(self):
        self.driver.find_element(By.ID, self.cdrop_id).click()

    def clientselect(self, cli):
        self.driver.find_element(By.ID, self.cdrop_id).send_keys(cli)

    def startd(self, sstdate):
        self.driver.find_element(By.XPATH, self.sdate).click()
        self.driver.find_element(By.XPATH, self.sdate).send_keys(sstdate)

    def starttime(self, sstime):
        self.driver.find_element(By.XPATH, self.stime).click()
        self.driver.find_element(By.XPATH, self.stime).send_keys(sstime)

    def arr_pm(self):
        self.driver.find_element(By.XPATH, self.pmarr).click()

    def arr_am(self):
        self.driver.find_element(By.XPATH, self.amarr).click()

    def rep_to(self):
        self.driver.find_element(By.XPATH, self.report_to).click()

    def op(self, rpdrp):
        self.driver.find_element(By.XPATH, self.report_to).send_keys(rpdrp)

    def dress(self, costume):
        self.driver.find_element(By.XPATH, self.drr).click()
        self.driver.find_element(By.XPATH, self.drr).send_keys(costume)

    def endd(self, eetdate):
        self.driver.find_element(By.XPATH, self.edate).click()
        self.driver.find_element(By.XPATH, self.edate).send_keys(eetdate)

    def endtime(self, eetime):
        self.driver.find_element(By.XPATH, self.etime).click()
        self.driver.find_element(By.XPATH, self.etime).send_keys(eetime)

    def arr_pm_2(self):
        self.driver.find_element(By.CSS_SELECTOR, self.pmarr_2).click()

    def add(self):
        self.driver.find_element(By.XPATH, self.addj).click()

    def scroll(self):
        element_to_scroll_to = self.driver.find_element(By.XPATH, self.scr)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll_to)

    def jobp(self):
        self.driver.find_element(By.XPATH, self.jobpo).click()

    def jobpos(self, jobposi):
        self.driver.find_element(By.XPATH, self.jobpo).send_keys(jobposi)

    def desc(self):
        self.driver.find_element(By.XPATH, self.descr).click()

    def desc2(self, dcrip):
        self.driver.find_element(By.XPATH, self.descr).send_keys(dcrip)

    def Rbl(self):
        self.driver.find_element(By.XPATH, self.rbl).click()

    def Rbh(self):
        self.driver.find_element(By.XPATH, self.rbh).click()

    def Quan(self, num):
        self.driver.find_element(By.XPATH, self.quan).send_keys(num)

    def Pay(self, pr):
        self.driver.find_element(By.XPATH, self.pay).send_keys(pr)

    def notes(self, nt):
        self.driver.find_element(By.ID, self.note).send_keys(nt)

    def save(self):
        self.driver.find_element(By.XPATH, self.sve).click()
