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

def bilibiliThread(url,offset):

    requests.adapters.DEFAULT_RETRIES = 5
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    content=requests.get(url,headers=headers).text.decode('utf-8')
    response=etree.HTML(content)
    item = {}
    item['no'] = offset
    item['author'] = ""
    item['days'] = ""
    #写入CSV文件 
    if len(response.xpath("//*[@class='error-body']")) < 1:
        try:
            item['no'] = offset
            print offset
            # item['author'] = response.xpath("//*[@name='author']/@content").extract()[0].encode("utf-8")
            item['author'] =  response.xpath("/html/body/div/div[@id='banner']/div/h2")[0].xpath('text()')[0]
            item['days'] =  response.xpath("/html/body/div[@class='body-inner']/div[@id='info']/div[@class='look_right']/ul[@class='look_right_list']/li[2]/em")[0].xpath('text()')[0]
            # item['author'] = response.xpath("/html/body/div/div[@id='banner']/div/h2").extract()[0].encode("utf-8")
            # item['days'] = response.xpath("//*html/body/div[@class='body-inner']/div[@id='info']/div[@class='look_right']/ul[@class='look_right_list']/li[2]/em")[0].encode("utf-8")
            
        except Exception as e:
            print e
            f = open('error.csv',"a+")
            f.write(url+"\n")
            f.close()
    if item['author'] != "":
        addInfo = [ str(item['no']),str(item['author']),str(item['days'])]
        data = json.dumps(item,encoding='utf-8',ensure_ascii=False).decode('utf-8')
        print(data)
        for index in range(len(addInfo)):
            addInfo[index] = "\"" + addInfo[index].replace("\"", "\"\"").replace("\n", "\\r\\n").replace("\r", "\\r\\n") + "\""

        # print addInfo
        pushRedis("localhost","wanplusPeople",data)
    global thredaStack
    thredaStack.pop()
    # f = open('bilibiliVideoTest.csv',"a+")
    # f.write(",".join(addInfo)+"\n")
    # f.flush()
    # f.close()


#设定爬取baseURL
baseUrl='http://www.wanplus.com/people/'
#读取OFFSET文件
f = open('offset.txt','a+')
f.seek(0)
offset = f.read()
if offset == '':
    offset = 0
offset = (int(offset) + 1) 
#爬取URL设定
start_urls = baseUrl+ str(offset)
f.close()


# 创建线程池
executor = ThreadPoolExecutor(1000)
thredaStack = Stack()
while True:
    if thredaStack.size() > 50:
        continue

    thredaStack.push("1")
    executor.submit(bilibiliThread, start_urls,offset)
    # bilibiliThread(start_urls, offset)

    offset = offset + 1
    f = open('offset.txt','w')
    f.write(str(offset))
    f.close()
    start_urls =baseUrl + str(offset)


        