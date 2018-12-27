# -*- coding:utf-8 -*-

# _ksTS=1526545121518_1881时间戳滞后了 ∴要动态的传参数——(导入time模块)
# callback=jsonp1882
import requests
import time
import random
import re
import json

url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=539137284584&spuId=701871908&sellerId=929347050&order=3&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvsvvLvZIvUpCkvvvvvjiPPFdZ6jtPPLqOzjivPmPh1jDRRFchAjYbPsMh6jYWR46Cvvyv2vZjwchvJCurvpvEvvkUCgR2vV2LdphvmpvhOQb3gpCU4UhCvCLwMCHJGaMwznAY8xS50YAizRl4k46CvvyvCWgmYNZvECojvpvhvvpvvvGCvvpvvPMMuphvmvvv9bhrvjKCkphvC99vvOClpbyCvm9vvvvvphvvvvvv9F1vpvkjvvmmZhCv2CUvvUEpphvWwpvv9DCvpv11mphvLvp%2F6QvjWz7%2BkU97%2B3%2BraNBraB4AVAElYWmQrEt1pwLU%2BnezrmphQRAn3feAOHcIAXcBKFyK2ixrQj7Jymx%2F1j7QiXTAVArlMR29VEQCvpvVvvpvvhCvRphvCvvvvvm5vpvhvvmv9u6CvvyvCV4mRLyvVbervpvEvvBxvkgKv2kqRphvCvvvvvmCvpvZz2sm4VdNznswvCDfY0IwXaAv7Ihtvpvhvvvvvv%3D%3D&isg=BBgYp5ys9ga0jdox7XxaDMe26UbZGXLdB_e3zlII19NS7bvX-hKvGsuvISVdfTRj&needFold=0'

# 发送 http://请求
# t = time.time() 时间戳time()函数
# csv文件 excel 可以打开
# csv文件，编码只能‘gbk’
f = open('votes.csv', 'w', encoding='gbk')
f.write('评价内容，店家回复，昵称\n')
for i in range(99):
    t = str(time.time()).split('.')

    # 构造url的过程，get请求的参数
    pagram = {
        'currentPage': i+1,
        '_ksTS': '%s_%s' % (t[0], t[1]),
        'callback': 'jsonp%s' % (int(t[1])+1)
    }

    # 随机休眠，行为分析，防止访问过快，避免被网站检测到有问题
    time.sleep(random.random())

    response = requests.get(url, params=pagram)
    # 数据持久化——入库、文件
    # csv文件:通过','区分
    data = response.text

    # 解析数据
    data = re.findall(r'{.*}', data)[0]
    # json模块可以将  Json数据<——>为字典 互相转换

    # Json数据——>转为字典
    data = json.loads(data)
    data = data['rateDetail']['rateList']
    print(data)
    for item in data:
        f.write('%s,%s,%s'% (
            item['rateContent'].replace(',', '，'),
            item['reply'].replace(',', '，'),
            item['displayUserNick']))