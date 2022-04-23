#coding:utf-8

#Author:yangxiaoyan

import requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

operationExcel = OperationExcel()

# print(operationExcel.getUrl(2).split('/'))

def checkHeader(row,f1=None,f2=None):
    '''检测请求头'''
    url = operationExcel.getUrl(row= row)
    url = url.split('/')
    if url[4] == 'positionAjax.json?needAddtionalResult=false':
        return f1
    elif url[5] =='byPosition.json':
        return f2


class Method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()

    def post(self,row):
        try:
            r = requests.post(
                url = self.excel.getUrl(row=row),
                data = self.operationJson.getReadJson(row = row),
                header = getHeadersValue(),
                timeout = 6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')

    def post(self,row,data):
        try:
            r = requests.post(
                url = self.excel.getUrl(row=row),
                data = data,
                header = checkHeader(row=row,f1=getHeadersValue(),f2=getHeadersInfo()),
                timeout = 6)
            return r
        except Exception as e:
            raise RuntimeError('接口请求发生未知的错误')


class isContent:
    def __init__(self):
        self.excel = OperationExcel()

    def isContent(self,row,str2):
        flag = None
        if self.excel.getExpect(row = row) in str2:
            flag =  True
        else:
            flag = False
        return flag