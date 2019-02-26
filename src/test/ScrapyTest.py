#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-20 16:10:11
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

def de(url,offset):

    requests.adapters.DEFAULT_RETRIES = 5
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    content=requests.get(url,headers=headers).text.decode('utf-8')
    response=etree.HTML(content)
    item = {}

           #写入CSV文件 
    try:
        item['no'] = offset
        # item['author'] = response.xpath("//*[@name='author']/@content").extract()[0].encode("utf-8")
        item['author'] = response.xpath("//*[@name='author']/@content")[0].encode("utf-8")
    except Exception as e:
        print e
 
    addInfo = [ str(item['no']),str(item['videoName']),str(item['author']),str(item['description']),str(item['url']),str(item['tags'])]
    data = json.dumps(item,encoding='utf-8',ensure_ascii=False).decode('utf-8')
    print(data)
    # for index in range(len(addInfo)):
    #     addInfo[index] = "\"" + addInfo[index].replace("\"", "\"\"").replace("\n", "\\r\\n").replace("\r", "\\r\\n") + "\""

    # print addInfo
    # pushRedis("localhost","bilibiVideoTest",data)
    # f = open('bilibiliVideoTest.csv',"a+")
    # f.write(",".join(addInfo)+"\n")
    # f.flush()
    # f.close()


#设定爬取baseURL
baseUrl='https://www.bilibili.com/video/av'
offset = ""
 
#爬取URL设定
start_urls = baseUrl+ str(offset)


# 创建线程池
executor = ThreadPoolExecutor(1000)
executor.submit(do, start_urls,offset)
