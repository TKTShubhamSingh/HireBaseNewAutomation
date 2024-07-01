import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SkillPage:
    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        try:
            self.driver.find_element(By.ID, "txtEmail").send_keys(username)
        except Exception as e:
            raise Exception(f"Error entering username: {e}")

    def password(self, password):
        try:
            self.driver.find_element(By.ID, "txtPassword").send_keys(password)
        except Exception as e:
            raise Exception(f"Error entering password: {e}")

    def login(self):
        try:
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        except Exception as e:
            raise Exception(f"Error clicking login button: {e}")

    def settings(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".bg-transparent > img").click()
        except Exception as e:
            raise Exception(f"Error clicking settings button: {e}")

    def skills(self):
        try:
            self.driver.find_element(By.LINK_TEXT, "Skills").click()
        except Exception as e:
            raise Exception(f"Error clicking skills link: {e}")

    def AddnewSkill(self, Skillname):
        try:
            self.driver.find_element(By.XPATH, "//button[@class='c-btn dark-btn']").click()
        except Exception as e:
            raise Exception(f"Error clicking Add new skill button: {e}")

        time.sleep(2)

        try:
            self.driver.find_element(By.XPATH, "//input[@id='txtExperienceName']").send_keys(Skillname)
        except Exception as e:
            raise Exception(f"Error sending keys to the skill name input: {e}")

    def fieldType(self):
        element = self.driver.find_element(By.XPATH, "//select[@id='drpType']")
        select = Select(element)
        select.select_by_index(2)

        time.sleep(2)

    def options(self, Option1, Option2, Option3, Option4):
        self.driver.find_element(By.ID, "txtExperienceOption-0").send_keys(Option1)
        time.sleep(2)
        button_locator = (By.XPATH, "//button[contains(text(),'Add Option')]")

        try:
            for _ in range(3):
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(button_locator)
                )

                button.click()

        except Exception as e:
            print("An error occurred:", e)

        self.driver.find_element(By.ID, "txtExperienceOption-1").send_keys(Option2)
        self.driver.find_element(By.ID, "txtExperienceOption-2").send_keys(Option3)
        self.driver.find_element(By.ID, "txtExperienceOption-3").send_keys(Option4)

    def Status(self):
        element = self.driver.find_element(By.ID, "drpStatuses")
        select = Select(element)
        select.select_by_index(1)

    def Skill_Group(self):
        element = self.driver.find_element(By.ID, "drpSkillGroupId")
        select = Select(element)
        select.select_by_index(3)

    def Save(self):
        self.driver.find_element(By.XPATH, "//button[@class='c-btn dark-btn' and text()='Save']").click()