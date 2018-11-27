# -*-coding:utf-8-*-

# Date: 2018.11.26
# ToDo: 图片爬虫 - jandan

import requests
from bs4 import BeautifulSoup

headers = {'user-agent':  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/70.0.3538.77 Safari/537.36'}

def download_file(url):
    print('Downloading %s' % url)
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True, headers=headers)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_filename


url = 'http://jandan.net/drawings/page-21'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')


def valid_img(src):
    return src.endswith('jpg')  and 'img.jandan.net' in src


for img in soup.find_all('img', src=valid_img):
    src = img['src']
    if not src.startswith('http'):
        src = 'http:' + src
    download_file(src)
