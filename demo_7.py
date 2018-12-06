# -*-coding:utf-8-*-

# Date: 2018.11.16
# ToDo: 练习Requests - get

import requests
import unittest


class GetRequest(unittest.TestCase):
    def setUp(self):
        self.get_url = 'http://vodcms-testnew.cloutropy.com/vodcms/test/uploade'

    def test_get_01(self):
        url = self.get_url
        r = requests.get(url)
        print(r.json())

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
