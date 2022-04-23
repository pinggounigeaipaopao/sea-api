#coding:utf-8

#Author:yangxiaoyan

import unittest
import json
from base.method import Method,isContent
from page.laGou import *
from utils.public import *

class LaGou(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = isContent()

    def statusCode(self,r):
        self.assertEqual(r.start_code , 200)
        self.assertEqual(r.json['code'] , 0)

    def isContent(self,r,row):
        self.statusCode(r)
        self.assertTrue(self.p.isContent(r,row))


    def test_laGou_001(self):
        '''拉钩：测试翻页'''
        r = self.obj.post(1)
        self.isContent(1,r.text)

    def test_laGou_002(self,row):
        '''测试关键字，职位搜索'''
        r = self.obj.post(row=row,data=setSearch("修改后收索关键字，为测试工程师"))
        self.isContent(2, r.text)


    def test_laGou_003(self):
        '''测试python开发工程师第一页第一个公司的招聘信息'''
        list1 = []
        for i in range(0,15):
            positionId = i.json()['content']['positionResult']['result'][i]['positionId']
            list1.append(positionId)
        writePostionId(json.dumps(list1))


if __name__ == '__main__':
        unittest.main(verbosity = 2)
