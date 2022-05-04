import unittest
import json
import sys
from base.method import Method, isContent
from utils.operationExcel import *
import utils.public as mylog

import page.agent as ag
from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel

operationJson = OperationJson()


class agent(unittest.TestCase):
    def setUp(self):
        self.obj = Method()
        self.p = isContent()
        self.excel = OperationExcel()
        self.json = OperationJson()

    def statusCode(self, r):
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['errorcode'], 0)

    def isContent(self, r, row):
        self.statusCode(r)
        self.assertTrue(self.p.isContent(row, r.text))

    # 登录接口
    def test_getToken_01(self):
        data = self.json.getRequestData(row=1, file=1)
        print(data)
        r = self.obj.post(row=1, params=data, file=1)
        if 'token' in r.json():
            self.excel.writeResult(row=1, content=r.json()['token'], file=1)
        else:
            sys.exit()

    def operation(self, row=None, file=1, sheetId=None):
        dictKD = {}
        statusCodeList = []
        token = self.excel.getResult(row=1, file=file)
        func = self.excel.getFunction(row=row, file=1)
        if func == 'DEL':
            r = self.operationFun(row=row, token=token, func=func, file=1, sheetId=sheetId)
            mylog.getLogger().error("结果:%s", r.text)
            statusCodeList.append(r.status_code)
        else:
            dictKD = ag.setSearch(row=row, dictKD=dictKD, file=1)
            list1 = {}
            for i in range(7):
                for k, v in dictKD.items():
                    list1[k] = dictKD[k][i]
                r = self.operationFun(row=row, token=token, params=list1, func=func, file=1, sheetId=sheetId)
                mylog.getLogger().error("参数:%s,结果:%s", list1, r.text)
                statusCodeList.append(r.status_code)

        self.p.isCheck(row=row, statusCodeList=statusCodeList)

    def operationFun(self, row=None, token=None, params=None, func='GET', file=1, sheetId=None):
        r = ''
        if func == 'GET':
            r = self.obj.get(row=row, token=token, params=params, file=file)
        elif func == 'POST':
            r = self.obj.post(row=row, token=token, params=json.dumps(params), file=file)
        elif func == 'PUT':
            r = self.obj.put(row=row, token=token, params=params, ID=sheetId, file=1)
        elif func == 'DEL':
            r = self.obj.delete(row=row, token=token, ID=sheetId, file=file)
        return r

    # 代理商平台 - 禁用歌曲列表
    def test_banSongs_01(self):
        row = 2
        self.operation(row, 1)

    # 代理商平台 - 创建歌单接口
    def test_songSheets_01(self):
        row = 3
        self.operation(row, 1)

    # 代理商平台 - 更新歌单接口
    def test_songSheets_02(self):
        row = 4
        sheetId = '1'
        self.operation(row, 1, sheetId)

    # 代理商平台 - 删除歌单接口
    def test_songSheets_03(self):
        row = 5
        sheetId = '1'
        self.operation(row, 1, sheetId)

    # 代理商平台 - 歌单列表接口
    def test_songSheets_04(self):
        row = 6

    # 代理商平台 - 歌单歌曲列表接口
    def test_sheetsBindSongs_01(self):
        row = 7

    # 添加歌单歌曲















if __name__ == '__main__':
    unittest.main(verbosity=2)
