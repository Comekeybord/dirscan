# -*- coding: UTF-8 -*-
# Time : 2023/1/20 15:55
# FILE : db
# PROJECT : dirscan
# Author : kkk

# 链接数据库获取代理
import pymysql

# 导入数据库配置
from setting.setting import dbSetting

# 创建数据库链接
db = pymysql.connect(
    host=dbSetting['host'],
    port=dbSetting['port'],
    user=dbSetting['usr'],
    password=dbSetting['pwd'],
    charset='utf8',
    database=dbSetting['dbName'],
)
print('数据库链接成功!')

# 创建浮标
cur = db.cursor()


# 提交操作
def commit(sql):
    try:
        # print(cur)
        # 使用 execute()  方法执行 SQL 语句
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        print('数据库操作错误!', e)


# 查询代理列表
def selectProxy():
    sql = '''
    select {},{} from {}
    '''.format(
        dbSetting['ip_column_name'],
        dbSetting['port_column_name'],
        dbSetting['tableName'])
    resTem = commit(sql)
    res = {}
    for item in resTem:
        ip = item[0]
        port = item[1]
        res[ip] = port
    return res


def closeDb():
    # 关闭浮标和链接
    cur.close()
    db.close()
