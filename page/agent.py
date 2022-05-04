import json
import itertools
import data.testData as td
import utils.public as mylog
from utils.operationJson import OperationJson

operationJson = OperationJson()


def setSearch(row=2, dictKD=None, file=None):
    # 通过第一次获取请求获取到参数，然后进行参数值的自动化修改，组合新的参数值传入测试
    t = json.loads(operationJson.getRequestData(row, file=file))
    klist = []
    for k, v in t.items():
        if not td.dataList.__contains__(k):
            mylog.getLogger().error("参数:%s 不存在", k)
        else:
            dictKD[k] = td.dataList[k]
            klist.append(k)
    return dictKD

def setParamsList(*args):
    '''
    1.传入接口参数的可能值{'singer_name': ['1', '好'], 'song_name': ['English','NULL'], 'limit': [ '1', '1.1'], 'page': ['-1', '0']}
    2.coutList 获取组合 1/English/1/-1
    3.通过拆分定义[{"song_name": "English", "limit": 1, "page": -1, "singer_name": "1"},{}....]
    '''
    singer_name = args[0]['singer_name']
    song_name = args[0]['song_name']
    limit = args[0]['limit']
    page = args[0]['page']
    coutList = list('/'.join(i) for i in itertools.product(singer_name, song_name, limit, page))

    paramslist = []
    listItems = {}
    for i in range(len(coutList)):
        listItems['singer_name'] = coutList[i].split('/', 1)[0]
        listItems['song_name'] = coutList[i].split('/', 2)[1]
        listItems['limit'] = coutList[i].split('/', 3)[2]
        listItems['page'] = coutList[i].split('/', 4)[3]
        paramslist.append(listItems)


    return paramslist

