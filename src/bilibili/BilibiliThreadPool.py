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
# 首先导包
from concurrent.futures import ThreadPoolExecutor
sys.setdefaultencoding('utf-8')

def bilibiliThread(url,offset):

    requests.adapters.DEFAULT_RETRIES = 5
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    content=requests.get(url,headers=headers).text.decode('utf-8')
    response=etree.HTML(content)
    item = {}

           #写入CSV文件 
    if len(response.xpath("//*[@class='error-body']")) < 1:
        try:
            item['no'] = offset
            # item['author'] = response.xpath("//*[@name='author']/@content").extract()[0].encode("utf-8")
            item['author'] = response.xpath("//*[@name='author']/@content")[0].encode("utf-8")
            item['videoName'] = response.xpath('//*[@id="viewbox_report"]/h1/@title')[0].encode("utf-8")
            item['description'] = response.xpath('//*[@name="description"]/@content')[0].encode("utf-8")
            item['url'] = response.xpath('//*[@itemprop="url"]/@content')[0].encode("utf-8")

            tagList = []
            tags = response.xpath('//*[@class="tag"]/a/text()')
            for tag in tags:
                tagList.append(tag.encode("utf-8"))
            item['tags'] = ",".join(tagList)
        except Exception as e:
            f = open('error.csv',"a+")
            f.write(url+"\n")
            f.close()
            item['no'] = offset
            item['author'] = ""
            item['videoName'] = ""
            item['description'] = ""
            item['url'] = ""
            item['tags'] = ""
    else :
        item['no'] = offset
        item['author'] = ""
        item['videoName'] = ""
        item['description'] = ""
        item['url'] = ""
        item['tags'] = ""
    addInfo = [ str(item['no']),str(item['videoName']),str(item['author']),str(item['description']),str(item['url']),str(item['tags'])]
    data = json.dumps(item,encoding='utf-8',ensure_ascii=False).decode('utf-8')
    print(data)
    for index in range(len(addInfo)):
        addInfo[index] = "\"" + addInfo[index].replace("\"", "\"\"").replace("\n", "\\r\\n").replace("\r", "\\r\\n") + "\""

    # print addInfo
    pushRedis("localhost","bilibiVideoTest",data)
    # f = open('bilibiliVideoTest.csv',"a+")
    # f.write(",".join(addInfo)+"\n")
    # f.flush()
    # f.close()


#设定爬取baseURL
baseUrl='https://www.bilibili.com/video/av'
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
while True:  
    executor.submit(bilibiliThread, start_urls,offset)
    offset = offset + 1
    f = open('offset.txt','w')
    f.write(str(offset))
    f.close()
    start_urls =baseUrl + str(offset)


        