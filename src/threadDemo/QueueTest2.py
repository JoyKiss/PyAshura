# -*- coding: utf-8 -*-

'''

Created on 2018年7月10日

@author: D

'''
import multiprocessing
import Queue
from multiprocessing import Process, Queue
import os
from lxml import etree
import requests
import sys
import json
reload(sys)
import threading
import time
sys.path.append("..")

# 首先导包
from concurrent.futures import ThreadPoolExecutor
sys.setdefaultencoding('utf-8')

def duowanThread(url,offset,q):
    print "*"*100
    print url
    print "*"*100
    baseUrl='http://tu.duowan.com'
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
#             getPicUrl(baseUrl+next)
            q.put(baseUrl+next)
        f = open('infoQueue2.csv',"a+")
        f.write(url+"\n")
        f.close()
    except Exception as e:
        e

def getPicUrl(q):
    while True:
        url = q.get()
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
#         q.task_done()
        
baseUrl='http://tu.duowan.com'       
if __name__ == "__main__":
       
    f = open('offsetQueue2.txt','a+')
    f.seek(0)
    offset = f.read()
    if offset == '':
        offset = 0
    offset = (int(offset) + 1) 
    #爬取URL设定
    f.close()
    start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
    manager = multiprocessing.Manager()
    q = manager.Queue()
    pr = Process(target=getPicUrl, args=(q,))
    pr.start()
    print 'pr开始'
    # 创建线程池
    while True:  
    #     executor.submit(duowanThread, start_urls,offset)
        print "开始"
#         pw = Process(target=duowanThread, args=(start_urls,offset,q))
#         pw.start()
#         pw.join()
        print q.full()
        duowanThread(start_urls,offset,q)
        offset = offset + 1
        start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
#         offset = offset + 1
#         start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
        f = open('offsetQueue2.txt','w')
        f.write(str(offset))
        f.close()