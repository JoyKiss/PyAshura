# -*- coding: utf-8 -*-

'''

Created on 2018年7月11日

@author: D

'''
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
import urllib2
import MySQLdb
from concurrent.futures import ThreadPoolExecutor
sys.setdefaultencoding('utf-8')
import pymysql

def duowanThread(url,offset):
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
            getPicUrl2(baseUrl+next)
#             q.put(baseUrl+next)
            f = open('infoQueueAll.csv',"a+")
            f.write(baseUrl+next+"\n")
            f.close()
    except Exception as e:
        e

def getPicUrl(q):
    while True:
        url = q.get()
        print "loading>>>>>>>>>>>>>>>>>>>>>>" + url
        requests.adapters.DEFAULT_RETRIES = 5
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
        r = requests.get(url,headers=headers)
        r.encoding='utf-8'
        content=r.text
        
        response=etree.HTML(content)
        item = {}
        title = response.xpath("/html/head/title/text()")[0]
        print title
        boxs = response.xpath("//*[@class='pic-box']")
        f = open('AllPic.csv',"a+")
        for box in boxs:
            img = box.xpath("a/span/@data-img")[0]
            msg = box.xpath("p/string(.)")[0].encode("utf-8")
            print img
            print msg
            f.write(url+"\t"+mysqlTransf(title)+"\t"+mysqlTransf(img)+"\t"+mysqlTransf(msg)+"\n")
            print url+"\t"+title+"\t"+img+"\t"+msg
        f.close()
def mysqlTransf(info):
    return str(MySQLdb.escape_string(info)).replace("\\", "\\\\").replace("\"", "\\\"").replace("\'", "\\\'")
def getPicUrl2(url):
#         url = q.get()
    print "loading>>>>>>>>>>>>>>>>>>>>>>" + url
    requests.adapters.DEFAULT_RETRIES = 5
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    r = requests.get(url,headers=headers)
    r.encoding='utf-8'
    content=r.text
    
    response=etree.HTML(content)
    item = {}
    title = response.xpath("/html/head/title/text()")[0]
    print title
    boxs = response.xpath("//*[@class='pic-box']")
    f = open('AllPic3.csv',"a+")
    for box in boxs:
        img = box.xpath("a/span/@data-img")[0]
        msg = box.xpath("p")[0].xpath("string(.)")
        print img
        print msg
        f.write(url+"\t"+mysqlTransf(title)+"\t"+mysqlTransf(img)+"\t"+mysqlTransf(msg)+"\n")
        print url+"\t"+title+"\t"+img+"\t"+msg
    f.close()
#         q.task_done()
def downPic(url,name):
    f = urllib2.urlopen(url) 
    data = f.read() 
    with open(name, "wb") as code:     
        code.write(data)
        
baseUrl='http://tu.duowan.com'       
if __name__ == "__main__":
    f = open("infoQueueAll.csv","r+")
    f.seek(0)
    urls = f.readlines();
    poolsize = 0;
    count = 0
    pool = multiprocessing.Pool(processes = 50)
    for url in urls:
        url = url.strip('\n')
        getPicUrl2(url)
#         pool.apply_async(getPicUrl2, (url))
#         poolsize = poolsize +1 
#         count = count + 1
#         if poolsize >= 150 or count >= len(urls):
#             pool.close()
#             pool.join() 
#             poolsize = 0
#             pool = multiprocessing.Pool(processes = 50)
#         url = f.readline()
#     url = f.readline()
#     pool = multiprocessing.Pool(processes = 2)
#     while url:
#         url = url.strip('\n')
#         pool.apply_async(getPicUrl2, (url,))
#         url = f.readline()
#         pool.close()
#         pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print '*'*10 + '处理完成'+'*'*10
#     f = open('offsetQueue.txt','r+')
#     f.seek(0)
#     offset = f.read()
#     if offset == '':
#         offset = 0
#     offset = (int(offset) + 1) 
#     #爬取URL设定
#     f.close()
#     start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
# #     manager = multiprocessing.Manager()
# #     q = manager.Queue()
# #     pr = Process(target=getPicUrl, args=(q,))
# #     pr.start()
#     print 'pr开始'
#     # 创建线程池
#     while True:  
#     #     executor.submit(duowanThread, start_urls,offset)
#         print "开始"
# #         pw = Process(target=duowanThread, args=(start_urls,offset,q))
# #         pw.start()
# #         pw.join()
# 
#         pool = multiprocessing.Pool(processes = 50)
#         for i in xrange(150):
#             pool.apply_async(duowanThread, (start_urls,offset))
#             offset = offset + 1
#             start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
#         pool.close()
#         pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
# #         offset = offset + 1
# #         start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
#         f = open('offsetQueue.txt','w')
#         f.write(str(offset))
#         f.close()