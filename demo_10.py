# -*-coding:utf-8-*-

# Date: 2018.12.6
# ToDo: Requests - post - relatedVideos API

import json
import requests
import unittest

class PostRequest(unittest.TestCase):
    def setUp(self):
        # 相关推荐接口
        self.url = 'http://vodvideo.cloutropy.com/client/video/relatedVideos'

    def test_post_01(self):
        url = self.url
        headers = {'Content-Type': 'application/json', 'Uid': 'UID_DEFAULT:GUEST',
                   'Authorization': 'CMS gM4TlH2HM6Q5TmP1:fyOUjU8W1WmzVxyMdOHc4HJclgU=',
                   'Date': 'Thu, 06 Dec 2018 07:09:42 GMT'}
        body = {'category_id': 35, 'num': 10, 'video_id': 237}
        r = requests.post(url, data=json.dumps(body), headers=headers)
        print(r.json())

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
