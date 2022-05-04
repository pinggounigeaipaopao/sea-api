import requests
from utils.excel_data import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

operationExcel = OperationExcel()
operationJson = OperationJson()

class Method:
    def __init__(self):
        self.operationJson = OperationJson()
        self.excel = OperationExcel()

# post请求：
    def post(self, row, token=None, params=None, file=1):
        try:
            r = requests.post(
                url=self.excel.getUrl(row=row, file=file),
                data=params,
                headers=getHeadersValue(token),
                timeout=6)

            return r
        except Exception as e:
            raise RuntimeError(e)

# get请求
    def get(self, row, params=None, token=None, file=1):
        url = self.excel.getUrl(row=row, file=file)
        headers = getHeadersValue(token)
        r = requests.get(url=url, headers=headers, params=params, timeout=6)
        return r

# put请求
    def put(self, row, token=None, params=None, ID=None, file=1):
        url = self.excel.getUrl(row=row, file=file)+'/'+ID
        headers = getHeadersValue(token)
        r = requests.put(url=url, headers=headers, params=params, timeout=6)
        return r

# del 请求
    def delete(self, row, token=None, ID=None, file=1):
        url = self.excel.getUrl(row=row, file=file)+'/'+ID
        headers = getHeadersValue(token)
        r = requests.delete(url=url, headers=headers, timeout=6)
        return r



# 返回校验 返回码的校验
class isContent:
    def __init__(self):
        self.excel = OperationExcel()

    def isContent(self, row, str2):
        flag = None
        if self.excel.getExpect(row=row) in str2:
            flag = True
        else:
            flag = False
        return flag

    def isCheck(self, row=None, statusCodeList=None):
        if 500 in statusCodeList:
            self.excel.writeResult(row, 'fail')
        else:
            self.excel.writeResult(row, 'pass')


