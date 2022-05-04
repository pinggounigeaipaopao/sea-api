#coding:utf-8

#Author:yangxiaoyan

import json
from utils.public import *
from utils.operationExcel import OperationExcel


class OperationJson:
    def __init__(self):
        self.excel = OperationExcel()

    def getReadJson(self):
        with open(data_dir(fileName='requestData.json'), encoding='utf-8') as fp:
                data = json.load(fp)
                return data

    def getRequestData(self, row, file=1):
        '''获取请求参数'''
        return json.dumps(self.getReadJson()[self.excel.getRequestData(row=row, file=file)])



