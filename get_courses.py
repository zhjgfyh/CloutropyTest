# -*-coding:utf-8-*-

# Date: 2018.11.26
# ToDo: 爬虫 - 获取所有课程信息

import requests
from bs4 import BeautifulSoup

# 定义被抓取页面的url
url = 'http://www.itest.info/courses'
# 获取被抓取页面的html代码，并使用html.parser来实例化BeautifulSoup，属于固定套路
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# 遍历页面上所有的h4
for course in soup.find_all('h4'):
    # 打印出h4的text属性
    print(course.text)