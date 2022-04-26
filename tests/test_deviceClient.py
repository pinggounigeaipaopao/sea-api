import unittest
import json
from base.method import Method,isContent
from page.deviceClient import *
from utils.public import *
from utils.operationExcel import *

class deviceClient(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = isContent()
        self.excel = OperationExcel()

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
        self.excel.writeResult(1,"pass")

        # 将拿到的token写到文件当中
        token=r.json()['data']['token']
        writeDcToken(json.dumps(token))
        print(token)


    # def test_getToken_002(self,row):
    #     # 获取不同设备sn的token
    #     r = self.obj.get(row=1, data=setSearch("F1N717P002774"))
    #     self.isContent(r=r,row=row)



if __name__ == '__main__':
    unittest.main(verbosity = 2)