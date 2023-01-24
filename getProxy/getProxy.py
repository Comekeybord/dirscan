# -*- coding: UTF-8 -*-
# Time : 2023/1/20 16:33
# FILE : getProxy
# PROJECT : dirscan
# Author : kkk


# 得到代理


def getProxyList():
    # 导入数据库操作查询代理
    from database import db

    proxyList = []
    # 转存到列表
    proTem = db.selectProxy()
    for item in proTem:
        proxyList.append(f"{item}:{proTem[item]}")
    # 关闭数据库
    db.closeDb()
    return proxyList
