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
sys.setdefaultencoding('utf-8')

class BilibiliThread(threading.Thread):
    def __init__(self,start_urls,offset):
        threading.Thread.__init__(self)
        self.start_urls = start_urls
        self.offset = offset
    def run(self):
        url = self.start_urls
        offset = self.offset 
        requests.adapters.DEFAULT_RETRIES = 5
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
        content=requests.get(url,headers=headers).text.decode('utf-8')
        response=etree.HTML(content)
        item = {}
        item['no'] = offset
        item['author'] = ""
        item['videoName'] = ""
        item['description'] = ""
        item['url'] = ""
        item['tags'] = ""
               #写入CSV文件 
        if len(response.xpath("//*[@class='error-body']")) < 1:
            try:
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
        addInfo = [ str(item['no']),str(item['videoName']),str(item['author']),str(item['description']),str(item['url']),str(item['tags'])]
        print(json.dumps(addInfo,encoding='utf-8',ensure_ascii=False).decode('utf-8'))
        for index in range(len(addInfo)):
            addInfo[index] = "\"" + addInfo[index].replace("\"", "\"\"").replace("\n", "\\r\\n").replace("\r", "\\r\\n") + "\""

        # print addInfo
        pushRedis("192.168.0.189","bilibiVideoTest",",".join(addInfo))
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
while True:  
    thread1 = BilibiliThread(start_urls,offset)
    thread1.start()
    offset = offset + 1
    f = open('offset.txt','w')
    f.write(str(offset))
    f.close()
    start_urls =baseUrl + str(offset)


        