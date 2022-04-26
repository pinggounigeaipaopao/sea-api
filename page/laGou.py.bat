#coding:utf-8

#Author:yangxiaoyan

import json
from utils.public import *

from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel

operationJson = OperationJson()

def setSearch(kd = None):
    '''对搜索的数据重新赋值'''
    dicil = json.loads(operationJson.getRequestData(1))
    dicil['kd'] = kd
    return  dicil

def writePostionId(content):
    '''把职位的ID写到文件中'''
    with open(data_dir(fileName='positionId'),'w') as f:
        f.write(content)

def getPositionId():
    '''获取职位招聘的信息'''
    with open(data_dir(fileName='positionId'), 'r') as f:
        return json.loads(f.read())



def setPositionInfo(row):
    dicil = json.loads(operationJson.getRequestData(row = row))
    dicil['positionId'] = positionId()[0]
    return dicil