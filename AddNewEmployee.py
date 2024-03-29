# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import Chrome, ChromeOptions
import unittest, time, re

from LoginStandardUser import LoginStandardUser
from Employee import *

class AddNewEmployee(unittest.TestCase):
    def setUp(self):
        opts = ChromeOptions()
        opts.add_argument("--window-size=2560,1440")
        self.driver = webdriver.Chrome(options=opts)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_new_employee(self):
        EmployeeName = "User"
        driver = self.driver
        LoginStandardUser(self)
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        # driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[2]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        #driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        #CreateEmployee(self,"User","One")
        #CreateEmployeeFull(self,EmployeeName,"One")

        #SearchEmployee(self,EmployeeName)

        time.sleep(10)

        NomTrouve =  driver.find_elements(By.XPATH,"//div[@class='oxd-table-cell'][1]")

        for n in NomTrouve:
            print(f"----->{n.text}<-----")

        print(f"Nom trouve =======> {NomTrouve} <=======================")

      
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
