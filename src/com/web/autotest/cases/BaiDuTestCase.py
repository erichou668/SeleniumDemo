'''
Created on 2019年5月2日

@author: Jennifer Shi
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from com.web.utils.Config import Config, DRIVER_PATH


class BaiDuTest(unittest.TestCase):
    
    URL = Config().get('URL')
    
    searchBox = (By.ID, 'kw')
    searchButton = (By.ID, 'su')
    result = (By.XPATH, '//div[contains(@class, "result")]/descendant::a[1]')
        
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)
        
    def tearDown(self):
        self.driver.quit()
        
    def testSearch(self):
        self.driver.find_element(*self.searchBox).send_keys('selenium')
        self.driver.find_element(*self.searchButton).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.result)
        for link in links:
            print(link.text)
        
if __name__ == '__main__':
    unittest.main()
    
 
    
    