# -*-coding:utf-8-*-

# Date: 2018.12.14
# ToDo: Appium - Calculator - Smartisan T2

# import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'a5d31fc4'
        desired_caps['appPackage'] = 'com.smartisanos.calculator'
        desired_caps['appActivity'] = '.Calculator'
        desired_caps['unicodeKeyboard'] = "True"
        desired_caps['resetKeyboard'] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testAdd(self):
        number8 = self.driver.find_element_by_id("digit8")
        number8.click()
        addoperation = self.driver.find_element_by_id("add")
        # Operate操作加号这个元素
        addoperation.click()
        # Locate定位数字5这个元素
        number5 = self.driver.find_element_by_id("digit5")
        # Operate操作数字5这个元素
        number5.click()
        # Locate定位等号这个元素
        equal = self.driver.find_element_by_id("equal")
        # Operate操作等号这个元素
        equal.click()
        # Verify验证操作的结果
        try:
            result = self.driver.find_element_by_id("show")
            value = result.text
            self.assertEqual("13", value)
        # Exception出理异常的情况
        except Exception:
            print("程序出现异常了")
            self.fail("程序出现异常了")


if __name__ == '__main__':
    unittest.main()
