import json

import requests
# 引入多进程,队列
from multiprocessing import Queue

# api = "http://api.douguo.net/recipe/v2/search/0/20"

# 创建队列
queue_list = Queue()


def handel_request(url, data):
    headers = {
        "client": "4",
        "version": "6947.2",
        "device": "Le X620", "sdk": "23,6.0",
        "imei": "861891034910877",
        "channel": "qqkp",
        # "mac": "02:00:00:00:00:00",
        "resolution": "1920*1080",
        "dpi": "2.625",
        # "android-id": "c6b20e2f93733b14",
        # "pseudo-id": "LE67A06210328218",
        "brand": "LeEco",
        "scale": "2.625",
        "timezone": "28800",
        "cns": "13",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Le X620 Build/HEXCNFN6003009092S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.91 Mobile Safari/537.36",
        "uuid": "defb6da9-dda1-4c5b-9d14-1b4e6de67436",
        "battery-level": "0.00",
        "battery-state": "2",
        "newbie": "1",
        "reach": "10000",
        "act-code": "d5c4335466f31a9a06a742f72aa58d90",
        "act-timestamp": "1571407453",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        # "Cookie": "duid=61535681",
        "Host": "api.douguo.net",
        # "Content-Length": "98"
    }
    # 返回响应
    response = requests.post(url=url, headers=headers, data=data)
    return response


def handler_index():
    url = "http://api.douguo.net/recipe/flatcatalogs"
    # client = 4 & _session = 1571407453111861891034910877 & v = 1503650468 & _vs = 2305
    data = {
        "client": 4,
        # "_session": "1571407453111861891034910877",
        # "v": "1503650468",
        "_vs": 2305
    }

    response = handel_request(url=url, data=data)
    response_dict = json.loads(response.text)
    for index_item in response_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for index_item_2 in index_item_1['cs']:
                # client=4&_session=1571410552843861891034910877&keyword=土豆&order=0&_vs=11111&type=0
                data_2 = {
                    "client": "4",
                    "keyword": index_item_2['name'],
                    "order": 0,
                    "_vs": "11111",
                    "type": "0"
                }
                queue_list.put(data_2)


handler_index()
print(queue_list.qsize())
