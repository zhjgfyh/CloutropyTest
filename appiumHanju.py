# -*-coding:utf-8-*-

# Date: 2018.12.14
# ToDo: Appium - Gaoqinghanju app - Smartisan T2

import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'a5d31fc4'
        desired_caps['appPackage'] = 'com.cloutropy.phone'
        desired_caps['appActivity'] = '.MainActivity'
        desired_caps['unicodeKeyboard'] = "True"
        desired_caps['resetKeyboard'] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testAdd(self):
        myBtn = self.driver.find_element_by_id("ys_search_bar")
        myBtn.click()
        self.driver.send_keys("aaa")
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()
