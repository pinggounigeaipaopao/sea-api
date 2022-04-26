import json
from utils.public import *
from utils.operationJson import OperationJson
from utils.operationExcel import OperationExcel

operationJson = OperationJson()
operationExcel = OperationExcel()

def setSearch(kd = None):
    '''对搜索的数据重新赋值，比如多个sn请求token'''
    dicil = json.loads(operationJson.getRequestData(1))
    dicil['sn'] = kd
    return dicil

def writeDcToken(content):
    '''token写到文件中'''
    with open(data_dir(fileName='dcToken'),'w') as f:
        f.write(content)

def getDcToken():
    '''获取token'''
    with open(data_dir(fileName='dcToken'), 'r') as f:
        return json.loads(f.read())

