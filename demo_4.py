# -*-coding:utf-8-*-

# Date: 2018.11.14
# ToDo: Python3 - Get请求

from urllib import parse
from urllib import request

url = "http://zxreg.speiyou.com/login/ajax_login"

# 定义请求数据，并对数据进行赋值
data = {}
data['loginname'] = 'student08@qq.com'
data['password'] = '111111'

# 对请求数据进行编码
data = parse.urlencode(data).encode('utf-8')
print(data)
# 将数据和url进行连接
req = request.Request(url='%s%s%s' % (url, '?', data))
# 打开请求，获取对象
requestResponse = request.urlopen(req)
# 读取服务端返回的数据
ResponseStr = requestResponse.read()
# 打印数据
print(ResponseStr)
print(ResponseStr.decode(encoding='utf-8'))