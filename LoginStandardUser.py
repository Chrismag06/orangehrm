from selenium.webdriver.common.by import By

def LoginStandardUser(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/div/div/div[2]").click()
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "username").click()
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.NAME, "password").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/div/div/div[2]").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
