# -*-coding:utf-8-*-

# Date: 2018.11.20
# ToDo: 验证selenium环境是否成功

from selenium import webdriver
from time import sleep
# 打开视频云管理后台
driver = webdriver.Chrome()
driver.get('http://vodcms-testnew.cloutropy.com')
driver.maximize_window()
# 登录
driver.find_element_by_name('username').send_keys('zhaojie')
sleep(3)
driver.find_element_by_name('password').send_keys('1234')
sleep(3)
driver.find_element_by_class_name('btn').click()
sleep(3)
# 点击视频管理
driver.find_element_by_xpath('//*[@id="top"]/nav/div/div[2]/ul/li[1]/a').click()
sleep(2)

driver.quit()
