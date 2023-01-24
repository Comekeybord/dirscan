# -*- coding: UTF-8 -*-
# Time : 2023/1/20 15:57
# FILE : setting
# PROJECT : dirscan
# Author : kkk

# 配置文件


# 配置数据库
# 数据库配置,用于存放代理的表
dbSetting = {
    # 数据库管理系统链接地址
    'host': 'localhost',
    # 数据库管理系统端口
    'port': 3306,
    # 数据库管理系统用户名
    'usr': 'root',
    # 数据库管理系统密码
    'pwd': 'admin666',
    # 库名
    'dbName': 'proxy_pool',
    # 表名
    'tableName': 'proxy_list',
    # ip列名
    'ip_column_name': 'proxy_ip',
    # 端口列名
    'port_column_name': 'proxy_port',
    # 是否存活列名
    'live_column_name': 'is_live'
}

scannerConfig = {
    # 字典绝对路径
    'dic': 'E:\信息安全\PyToolByMyself\目录扫描\字典\默认整理的御剑字典\php.txt',
    # 线程数
    'threads': 20,
    # 目标
    'url': 'http://php.kaiostech.com'
}

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

# 是否开启代理扫描
proxyConfig = True
# 是否使用付费代理,如使用动态付费代理请填写付费代理ip或域名, False 表示不使用
charge_proxy = False
