class ExcelVariable:
    '''定义请求参数的变量'''
    caseID = 0
    url = 2
    request_data = 3
    expect = 4
    result = 5

'''定义列变量，用来给operationExcel获取列'''
def getCaseID():
    return ExcelVariable.caseID

def getUrl():
    return ExcelVariable.url

def get_request_data():
    return ExcelVariable.request_data

def getExpect():
    return ExcelVariable.expect

def getResult():
    return ExcelVariable.result

def getHeadersValue():
    '''获取请求头'''
    headers = {

    }
    return headers

def getHeadersInfo():
    '''获取请求头'''
    headers = {

    }
    return headers