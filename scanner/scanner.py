# -*- coding: UTF-8 -*-
# Time : 2023/1/21 23:29
# FILE : scanner
# PROJECT : dirscan
# Author : kkk
import queue

import requests
from setting import setting

# 加载待扫描路径
paths = [
    '''{}'''.format(path.replace('\n', ''))
    for path in open(setting.scannerConfig['dic'], 'r', encoding='utf8')
]


# print(paths)


# 生产者 生产请求结果
def getRep(path, proxies=None):
    url = setting.scannerConfig['url'] + path
    # print(url)
    # print(proxies)
    if proxies is None:
        code = requests.get(url=url, headers=setting.headers).status_code
        return [url, code]
    try:
        code = requests.get(url, headers=setting.headers, proxies=proxies).status_code
        return [url, code]
    except Exception as e:
        print(f'{path}路径请求出错!', e)
        return [None, None]


# 消费者 翻译请求结果
def getRes(url, code):
    if url is not None:
        if code == 200:
            return f"{url}    code=200 响应正常"
        elif code == 403:
            return f"{url}    code=403 重定向"
        # elif code == 404:
        #     return f"{url}    code=404 页面不存在"

# rep = getRep(paths[0], setting.scannerConfig['url'], setting.headers)
# print(rep)
# print(getRes(rep[0], rep[1]))
