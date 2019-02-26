# -*- coding: utf-8 -*-

'''

Created on 2018年7月10日

@author: D

'''
import multiprocessing
import time
import os
from lxml import etree
import requests
import sys
import json
reload(sys)
import threading
import time
sys.path.append("..")
from utils.Utils import *
# 首先导包
from concurrent.futures import ThreadPoolExecutor
sys.setdefaultencoding('utf-8')

def duowanThread(url,offset):
    print "*"*100
    print url
    print "*"*100
    try:
        requests.adapters.DEFAULT_RETRIES = 5
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
        r = requests.get(url,headers=headers)
        r.encoding='utf-8'
        content=r.text
#         print content
        response=etree.HTML(content)
        item = {}
        boxs = response.xpath("//*[@class='pic-box']")
        # for box in boxs:
            # print box.xpath("a/span/@data-img")[0]
            # print box.xpath("p/text()")[0].encode("utf-8")
        nexts = response.xpath("//*[@id='yw0']")[0].xpath("a/@href")
        for next in nexts:
            print baseUrl+next
            getPicUrl(baseUrl+next)
        f = open('info2.csv',"a+")
        f.write(url+"\n")
        f.close()
    except Exception as e:
        print e

def getPicUrl(url):
    requests.adapters.DEFAULT_RETRIES = 5
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    r = requests.get(url,headers=headers)
    r.encoding='utf-8'
    content=r.text
    
    response=etree.HTML(content)
    item = {}
    boxs = response.xpath("//*[@class='pic-box']")
    for box in boxs:
        print box.xpath("a/span/@data-img")[0]
        print box.xpath("p/text()")[0].encode("utf-8")
baseUrl='http://tu.duowan.com'       
if __name__ == "__main__":
       
    f = open('offset.txt','a+')
    f.seek(0)
    offset = f.read()
    if offset == '':
        offset = 0
    offset = (int(offset) + 1) 
    #爬取URL设定
    f.close()
    start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
    
    # 创建线程池
    while True:  
    #     executor.submit(duowanThread, start_urls,offset)
        pool = multiprocessing.Pool(processes = 10)
        for i in xrange(11):
            pool.apply_async(duowanThread, (start_urls,offset))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
            offset = offset + 1
            start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
    
        pool.close()
        pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
        offset = offset + 1
        f = open('offset.txt','w')
        f.write(str(offset))
        f.close()