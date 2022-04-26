#coding:utf-8

#Author:yangxiaoyan

import xlrd
from xlutils.copy import copy
from utils.public import *
from utils.excel_data import *

class OperationExcel:
    def getExcel(self):
        db = xlrd.open_workbook(data_dir("data","data.xls"))
        sheet = db.sheet_by_index(0)
        return sheet

    def get_rows(self):
        '''获取excel的行数'''
        return self.getExcel().nrows

    def get_row_cel(self,row,col):
        '''获取单元格的内容'''
        return self.getExcel().cell_value(row,col)

    def getCaseID(self,row):
        '''测试ID'''
        return self.get_row_cel(row,getCaseID())

    def getUrl(self,row):
        '''获取请求地址'''
        return self.get_row_cel(row,getUrl())

    def get_request_data(self,row):
        '''获取请求参数'''
        return self.get_row_cel(row,get_request_data())

    def getExpect(self,row):
        '''获取期望的结果'''
        return self.get_row_cel(row,getExpect())

    def getResult(self,row):
        '''获取实际的结果'''
        return self.get_row_cel(row,getResult())

    def writeResult(self,row,content):
        # 将测试结果写入到文件中
        col = getResult()
        work = xlrd.open_workbook(data_dir("data","data.xls"))
        old_content = copy(work)
        ws = old_content.get_sheet(0)
        ws.write(row,col,content)
        old_content.save(data_dir("data","data.xls"))

    def getSuccessResult(self):
        #获取成功的测试用例
        passCount = []
        failCount = None
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

op = OperationExcel()
print(op.runPassRate())






