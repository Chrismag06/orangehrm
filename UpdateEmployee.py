# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UpdateEmployee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_update_employee(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/150")
        driver.find_element(By.NAME, "middleName").click()
        driver.find_element(By.NAME, "middleName").clear()
        driver.find_element(By.NAME, "middleName").send_keys("the")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div/div[2]/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div/div[2]/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div/div[2]/div/div/div[2]/input").send_keys("userOne")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div[2]/div/div[2]/div/div/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]/input").send_keys("999999")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").send_keys("2025-12-31")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/div/div[2]/div/div/div[2]/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input").send_keys("1990-12-25")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/span").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div[2]/div/div[2]/div/label/span/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div/div/div/div/div[2]/div/div/div[2]/i").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button").click()
    
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
