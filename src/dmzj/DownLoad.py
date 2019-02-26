#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-07 23:32:48


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')
import requests
import json
from lxml import etree
import execjs
import os
import click
import pymysql
sys.path.append("..")
from concurrent.futures import ThreadPoolExecutor
from utils.StockUtils import *
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Referer': 'http://www.dmzj.com/category'
}

PREIX = 'http://images.dmzj.com/'
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='111111', db='dmzj', charset='utf8')
    return conn
def down(pathCn,pathJuan,file,url,yid):
    path = str('%s/%s/'%(pathCn,pathJuan)).strip().decode('utf-8')
    print path+file
    
    if not os.path.exists(os.path.join("./", path)):
        os.makedirs(os.path.join("./", path))
    
    img = requests.get(url, headers=headers)
    # import time
    # time.sleep(1)  # 等待一些时间，防止请求过快
    
    with open(u'./%s/%s/%s'%(pathCn,pathJuan,file), mode='wb') as fp:
        fp.write(img.content)
    updataSql = "REPLACE INTO YeInfoTmp(`yid`, `jid`, `index`, `url`, `downFlag`)(select * from YeInfo where yid = '%s');"%(yid)
    deleteSql = "delete from YeInfo where yid = '%s';"%(yid)
    conn = get_conn()
    cursor = conn.cursor() 
    cursor.execute(updataSql)
    cursor.execute(deleteSql)
    conn.commit()

    # global thredaStack
    # thredaStack.pop()
    
def replace(st):
    return re.sub('[\/:*?"<>|]','-',st).strip()
conn = get_conn()
cursor = conn.cursor() 

selectSql = "SELECT CONCAT(info.id,'_',info.cnName),ji.juanMing,yi.`index`,yi.url,yi.yid FROM info info, JuanInfo ji, YeInfo yi WHERE info.id = ji.id AND ji.jid = yi.jid and yi.downFlag = '0'"
cursor.execute(selectSql)
results = cursor.fetchall()
for result in results:
    down(replace(result[0]),replace(result[1]),replace(result[2].zfill(5))+'.jpg',result[3],result[4])
# down('罗曼蒂克','第01话 罗曼蒂克','0.jpg','https://images.dmzj.com/l/%E7%BD%97%E6%9B%BC%E8%92%82%E5%85%8B/%E7%AC%AC1%E7%AF%87%20%E7%BD%97%E6%9B%BC%E8%92%82%E5%85%8B_1517404465/1.jpg','1')

# executor = ThreadPoolExecutor(10000)
# thredaStack = Stack()
# index = 0

# while index <= len(results):
#     if thredaStack.size() > 500:
#         continue

#     thredaStack.push("1")
#     result = results[index]

#     executor.submit(down, replace(result[0]),replace(result[1]),replace(result[2].zfill(5))+'.jpg',result[3],result[4])
#     index = index + 1