#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09 16:45:21


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
        e

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


#http://tu.duowan.com/scroll/137235.html
#设定爬取baseURL
baseUrl='http://tu.duowan.com'
#读取OFFSET文件
# f = open('offset.txt','a+')
# f.seek(0)
# offset = f.read()
# if offset == '':
#     offset = 0
# offset = (int(offset) + 1) 
# #爬取URL设定
# start_urls = baseUrl+ str(offset)
# f.close()
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
executor = ThreadPoolExecutor(1000)
while True:  
#     executor.submit(duowanThread, start_urls,offset)
    duowanThread(start_urls,offset)
    offset = offset + 1
    f = open('offset.txt','w')
    f.write(str(offset))
    f.close()
    start_urls = baseUrl + '/scroll/'+str(offset)+'.html'
# for x in range(100000):
#     print "*"*100
#     print 'http://tu.duowan.com/scroll/'+str(x)+'.html'
#     print "*"*100
#     duowanThread('http://tu.duowan.com/scroll/'+str(x)+'.html', '')
# # 创建线程池
# executor = ThreadPoolExecutor(1000)
# while True:  
#     executor.submit(duowanThread, start_urls,offset)
#     offset = offset + 1
#     f = open('offset.txt','w')
#     f.write(str(offset))
#     f.close()
#     start_urls =baseUrl + str(offset)


        