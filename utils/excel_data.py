class ExcelVariable:
    '''定义请求参数的变量'''
    caseID = 0
    url = 2
    request_data = 3
    expect = 4
    result = 5
    function = 6

'''定义列变量，用来给operationExcel获取列'''
def getCaseID():
    return ExcelVariable.caseID

def getUrl():
    return ExcelVariable.url

def getRequestData():
    return ExcelVariable.request_data

def getExpect():
    return ExcelVariable.expect

def getResult():
    return ExcelVariable.result

def getFunction():
    return ExcelVariable.function

def getHeadersValue(token=None):
    '''获取请求头'''
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        # 'Content-Length': '22',
        # 'Connection': 'keep-alive',
        # 'vary': 'Origin',
        # 'x-frame-options': 'SAMEORIGIN',
        # 'x-xss-protection':
        #     '1; mode=block',
        # 'x-content-type-options': 'nosniff',
        # 'x-download-options': 'noopen',
        # 'x-readtime': '21',
        # 'x-envoy-upstream-service-time': '24',
        'Authorization': token
    }
    return headers

def getHeadersInfo():
    '''获取请求头'''
    headers = {

    }
    return headers