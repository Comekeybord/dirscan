# -*- coding: UTF-8 -*-
# Time : 2023/1/12 22:44
# FILE : 目录扫描绕waf
# PROJECT : dirscan.py
# Author : kkk
import queue
import os
# 导入随机库
import random
# 导入多线程库
import threading
# 导入配置文件
from setting import setting
from scanner import scanner
import time

# 配置请求头
headers = setting.headers

url = setting.scannerConfig['url']

# 配置代理
proxyList = None
proxy_modle2 = False
if setting.proxyConfig:
    if setting.charge_proxy is False:
        # 导入获取代理模块
        from getProxy import getProxy

        proxyList = []
        if len(proxyList) == 0:
            # 如果没获取过就重新获取
            proxyList = getProxy.getProxyList()
    else:
        proxy_modle2 = True

    # 生产者线程 生产请求结果


def do_getrep(path_queue: queue.Queue, rep_queue: queue.Queue):
    while True:
        # 配置字典
        proxies = {}
        if proxyList is not None:
            # 代理模式一：随机取免费代理
            # 配置代理
            # 随机取一个代理
            proxy = random.choices(proxyList)[0]
            # 配置代理
            proxies['http'] = proxy
        elif proxy_modle2 == True:
            # 代理模式二：使用付费动态代理
            proxies['http'] = setting.charge_proxy
        else:
            # 代理模式三：不使用代理
            proxies = None
        # 取路径
        path = path_queue.get()
        rep = scanner.getRep(path, proxies=proxies)
        rep_queue.put(rep)
        # 输出线程信息
        # print(f"{threading.current_thread().name}, {path}, path_queue_size: {path_queue.qsize()}")
        # 睡眠一到两秒
        # time.sleep(random.randint(1, 2))
        if path_queue.qsize() == 0:
            return


# 消费者线程
def do_getres(path_queue: queue.Queue, rep_queue: queue.Queue, res_queue: queue.Queue):
    while True:
        rep = rep_queue.get()
        res = scanner.getRes(rep[0], rep[1])
        if res is not None:
            print(res)
            # 将结果保存到结果队列
            res_queue.put(res)
        # 输出线程信息
        # print(f"{threading.current_thread().name}, {res}, rep_queue_size: {rep_queue.qsize()}")
        # time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    # 使用生产者消费者模式实现多线程
    # 生产者就是待扫描路径path 消费者就是请求结果res
    path_queue = queue.Queue()
    rep_queue = queue.Queue()
    # 存放扫描结果的队列
    res_queue = queue.Queue()
    # 将path加入队列
    for path in scanner.paths:
        path_queue.put(path)

    # print(path_queue.qsize())
    # 文件操作
    save_path = './results/'
    # 判断是否存在文件夹
    if not os.path.exists(save_path):
        # 文件夹不存在 创建
        os.mkdir(save_path)
    # print(filename)

    # 记录线程
    threads = []
    # 开启生产者多线程
    for idx in range(setting.scannerConfig['threads']):
        t = threading.Thread(target=do_getrep, args=(path_queue, rep_queue),
                             name=f"getrep {idx}"
                             )
        threads.append(t)
        t.start()

    # 开启消费者多线程
    for i in range(setting.scannerConfig['threads'] - 1):
        t = threading.Thread(target=do_getres, args=(path_queue, rep_queue, res_queue),
                             name=f"getres  {i}"
                             )
        threads.append(t)
        t.start()
    # 阻塞线程
    for thread in threads:
        thread.join()

    # 写入文件
    filename = setting.scannerConfig['url'].split('//')[1]
    with open(f"./results/{filename}.txt", 'w', encoding='utf8') as fp:
        resTmp = ''
        for idx in range(res_queue.qsize()):
            res = res_queue.get()
            resTmp += str(res) + '\n'
        fp.write(resTmp)
