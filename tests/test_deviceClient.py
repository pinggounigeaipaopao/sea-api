import unittest
import json
from base.method import Method,isContent
from page.laGou import *
from utils.public import *

class deviceClient(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = isContent()

    def statusCode(self,r):
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['errorcode'],0)
    #
    def isContent(self,r,row):
        self.statusCode(r)
        self.assertTrue(self.p.isContent(row,r.text))

    def test_getToken(self):
        # 获取客户端token,row-行
        r = self.obj.get(1)
        self.isContent(r=r,row=1)
        print(r.text.data)


if __name__ == '__main__':
    unittest.main(verbosity = 2)