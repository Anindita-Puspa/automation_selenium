import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome('./chromedriver')

    def test_success_login_with_valid_email_password(self): 

        driver = self.driver 

        driver.get("http://barru.pythonanywhere.com/login")
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("cobapopo@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("cobabin")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)

        response_status = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
        
        self.assertIn("Welcome", response_status)
        self.assertEqual(response_message, "Anda Berhasil Login")

    def test_failed_login_with_valid_email_invalid_password(self): 

        driver = self.driver 

        driver.get("http://barru.pythonanywhere.com/login")
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("ngasal@gmail.com")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("yuhuuuuu")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)

        response_status = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
        
        self.assertEqual(response_status, "User's not found")
        self.assertEqual(response_message, "Email atau Password Anda Salah")

    def test_failed_login_with_invalid_email_format(self): 

        driver = self.driver 

        driver.get("http://barru.pythonanywhere.com/login")
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("ngasal")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("yuhuuuuu")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)

        status = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/form/input[1]"))).get_attribute("validationMessage")

        self.assertEqual(status, "Please include an '@' in the email address. 'ngasal' is missing an '@'.")

    def test_failed_login_with_empty_email(self): 

        driver = self.driver 

        driver.get("http://barru.pythonanywhere.com/login")
        time.sleep(2)
        driver.find_element_by_id("email").send_keys("")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("yuhuuuuu")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/form/input[3]").click()
        time.sleep(2)

        response_status = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
        
        self.assertEqual(response_status, "Email tidak valid")
        self.assertEqual(response_message, "Cek kembali email anda")

    def tearDown(self): 
        self.driver.close() 
  
# execute the script 
if __name__ == "__main__": 
    unittest.main() 
