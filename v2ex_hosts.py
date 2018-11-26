# -*-coding:utf-8-*-

# Date: 2018.11.26
# ToDo: 爬虫 - 获取所有热门主题

import requests
from bs4 import BeautifulSoup

# 定义被抓取页面的url
url = 'http://www.v2ex.com/'
# 获取被抓取页面的html代码，并使用html.parser来实例化BeautifulSoup，属于固定套路
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# 遍历页面上所有的class=item_hot_topic_title的span。
# 注意是class_，不是class，因为class是python的关键字，所以后面要加个尾巴，防止冲突
for span in soup.find_all('span', class_ = 'item_hot_topic_title'):
    # span.find('a').text：层级遍历，先找到span，再从span下找到a，这是常用套路
    # span.find('a')['href']：获取href属性，在bs4里，我们可以通过[attribute_name]的方式来获取元素的属性
    print(span.find('a').text,  span.find('a')['href'])