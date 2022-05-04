import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excel_data import *

class OperationExcel:
    # 定义域名，测试环境：os-daily.duochang.cc；预发布环境：os-prod.duochang.cc
    fUrl = 'http://os-daily.duochang.cc'
    # 定义表类型，1 data.xls
    fexcal = 1

# 获取表格
    def getExcel(self, file=1):
        filename = None
        if file == 1:
            filename = "data.xls"
        elif file == 2:
            filename = "tokenIds.xls"
        db = xlrd.open_workbook(data_dir("data", filename))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        '''获取excel的行数'''
        return self.getExcel().nrows

    def get_row_cel(self, row, col, file=1):
        '''获取单元格的内容'''
        return self.getExcel(file).cell_value(row,col)

# 获取单元格参数值
    def getCaseID(self,row):
        '''测试ID'''
        return self.get_row_cel(row,getCaseID())

    def getUrl(self,row,file=1):
        '''获取请求地址'''
        return self.fUrl + self.get_row_cel(row, getUrl(), file=file)

    def getRequestData(self, row, file=1):
        '''获取请求参数'''
        return self.get_row_cel(row, getRequestData(), file=file)

    def getExpect(self, row):
        '''获取期望的结果'''
        return self.get_row_cel(row, getExpect())

    def getResult(self, row, file=1):
        '''获取实际的结果'''
        return self.get_row_cel(row, getResult(), file=file)

    def getFunction(self, row, file=1):
        # 获取实际的请求方法
        return self.get_row_cel(row, getFunction(), file=file)

    # 写入pass，获取成功用例和失败用例，并计算成功率
    def writeResult(self, row, content, file=1):
        # 将测试结果写入到文件中
        filename = None
        if file == 1:
            filename = "data.xls"
        elif file == 2:
            filename = "tokenIds.xls"

        col = getResult()
        work = xlrd.open_workbook(data_dir("data", filename))
        old_content = copy(work)
        ws = old_content.get_sheet(0)
        ws.write(row, col, content)
        old_content.save(data_dir("data", filename))

    def getSuccessResult(self):
        #获取成功的测试用例
        passCount = []
        for i in range(1,self.get_rows()):
            if self.getResult(i) == "pass":
                passCount.append(i)
        return int(len(passCount))

    def getFailResult(self):
        # 执行失败的测试用例
        return int((self.get_rows()-1)-self.getSuccessResult())

    def runPassRate(self):
        # 测试通过率
        rate = ''
        if self.getFailResult() == 0:
            rate = "100%"
        elif self.getFailResult()!=0:
            rate = str(int(self.getSuccessResult()/(self.get_rows()-1)*100))+'%'
            return rate


