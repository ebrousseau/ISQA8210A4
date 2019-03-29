import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#Prepared by Erik Brousseau

class test_custedit__scripts(unittest.TestCase):
    # this sets up the location of the chrome driver
    def setUp(self):
        self.driver = webdriver.Chrome("C://python/8210/MSA/myvenv/Scripts/chromedriver.exe")

    def test_mfscustedit_scripts(self):

        driver = self.driver
        driver.maximize_window()

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
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[3]/td[12]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_city")
        elem.clear()
        time.sleep(2)
        elem.send_keys("Papillion")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()




