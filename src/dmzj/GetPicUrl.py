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
from utils.Utils import *
from utils.StockUtils import *
# 首先导包
from concurrent.futures import ThreadPoolExecutor
sys.setdefaultencoding('utf-8')

def Dmzj(url,offset):

    requests.adapters.DEFAULT_RETRIES = 5
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    content=requests.get(url,headers=headers).text.decode('utf-8')
    # print content
    print content
    response=etree.HTML(content)
    print "*" * 10
    # href =  response.xpath("//div[@class='cartoon_online_border']/ul/li/a")
    href =  response.xpath("//select")
    print len(href)
    for a in href:
        print a.xpath("@value")[0]
    # f = open('bilibiliVideoTest.csv',"a+")
    # f.write(",".join(addInfo)+"\n")
    # f.flush()
    # f.close()


#设定爬取baseURL
baseUrl='https://manhua.dmzj.com/lingnengbaifenbai/75675.shtml#@page=1'
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


# 创建线程池
executor = ThreadPoolExecutor(1000)
thredaStack = Stack()
# # while True:
# if thredaStack.size() > 1:
#     continue

thredaStack.push("1")
executor.submit(Dmzj, baseUrl,"")
    # bilibiliThread(start_urls, offset)

    # offset = offset + 1
    # f = open('offset.txt','w')
    # f.write(str(offset))
    # f.close()
    # start_urls =baseUrl + str(offset)


