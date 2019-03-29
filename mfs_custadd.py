import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#Prepared by Erik Brousseau

class mfs_custadd(unittest.TestCase):
    # this sets up the location of the chrome driver
    def setUp(self):
        self.driver = webdriver.Chrome("C://python/8210/MSA/myvenv/Scripts/chromedriver.exe")

    def test_mfscustadd_scripts(self):

        driver = self.driver
        driver.maximize_window()


        #Login/Add Customer

        driver.get("http://127.0.0.1:8000/")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("admin")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("eB708199")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Erik Brousseau")
        elem = driver.find_element_by_id("id_organization")
        elem.send_keys("PKI")
        elem = driver.find_element_by_id("id_role")
        elem.send_keys("Student")
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("PKI 172")
        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys("10")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("9810 V Plaza")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("NE")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68127")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("pythonrocks225@gmail.com")
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("402-657-1789")
        time.sleep(4)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(4)

    def tearDown(self):
        self.driver.close()








