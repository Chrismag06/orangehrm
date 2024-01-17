# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

def CreateEmployee(self,firstName,lastName):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").clear()
    self.driver.find_element(By.NAME, "firstName").send_keys(firstName)
    self.driver.find_element(By.NAME, "lastName").clear()
    self.driver.find_element(By.NAME, "lastName").send_keys(lastName)
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

def CreateEmployeeFull(self,firstName,lastName):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").clear()
    self.driver.find_element(By.NAME, "firstName").send_keys(firstName)
    self.driver.find_element(By.NAME, "middleName").clear()
    self.driver.find_element(By.NAME, "middleName").send_keys("Test")
    self.driver.find_element(By.NAME, "lastName").clear()
    self.driver.find_element(By.NAME, "lastName").send_keys(lastName)
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/184")
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div/div[2]/div/div/div[2]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div/div[2]/div/div/div[2]/input").clear()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div/div[2]/div/div/div[2]/input").send_keys("TestOne")
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]/input").click()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]/input").clear()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]/input").send_keys("999999")
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").clear()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input").send_keys("2044-12-31")
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/div/div[2]/div/div/div[2]/i").click()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div[2]/div/div[2]/div/div/div[2]/i").click()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/i").click()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input").click()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input").clear()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input").send_keys("1990-12-31")
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/span").click()
    self.driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[4]/div/div[2]").click()
    self.driver.find_element(By.XPATH, "//button[@type='submit']").click()