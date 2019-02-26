#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-08 09:29:58


import os
from lxml import etree
import requests
import json
import sys
reload(sys)
sys.path.append("..")
from utils.Utils import *
sys.setdefaultencoding('utf-8')


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
# 获取html文档  
def get_html(url,offset):  
    content=requests.get(url).text.decode('utf-8')
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
    print(json.dumps(addInfo,encoding='utf-8',ensure_ascii=False).decode('utf-8'))
    for index in range(len(addInfo)):
        addInfo[index] = "\"" + addInfo[index].replace("\"", "\"\"").replace("\n", "\\r\\n").replace("\r", "\\r\\n") + "\""

    # print addInfo
    pushRedis("localhost","bilibiVideo",",".join(addInfo))
    # f = open('bilibiliVideoTest.csv',"a+")
    # f.write(",".join(addInfo)+"\n")
    # f.flush()
    # f.close()

while True:
    get_html(start_urls,offset)
    offset = offset + 1
    f = open('offset.txt','w')
    f.write(str(offset))
    f.close()
    start_urls =baseUrl + str(offset)


