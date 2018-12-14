# -*-coding:utf-8-*-

# Date: 2018.12.13
# ToDo: Apk auto-install

import os
from appium import webdriver

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

desired_caps ={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'a5d31fc4'

desired_caps['app'] = apk_path + '\\gaoqinghanju.apk'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)