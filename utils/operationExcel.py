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






