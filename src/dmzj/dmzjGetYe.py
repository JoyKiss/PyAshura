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
import execjs
import click

import pymysql
# 首先导包
from concurrent.futures import ThreadPoolExecutor
sys.setdefaultencoding('utf-8')
#从创建数据库连接
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='111111', db='dmzj', charset='utf8')
    return conn

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Referer': 'http://www.dmzj.com/category'
}
def get_request(href,jid):
    response = requests.get(href, headers=headers)
    # global thredaStack
    html = etree.HTML(response.content)
    if hasattr(html, 'xpath') == False:
        # thredaStack.pop()
        conn = get_conn()
        cursor = conn.cursor()
        updataSql = "update JuanInfo set `load` = 'E' where jid = '%s'"%jid
        print updataSql
        cursor.execute(updataSql)
        conn.commit()
        return
    # print hasattr(html, 'xpath')
    if len(html.xpath('//script[1]/text()')) == 0:
        # thredaStack.pop()
        conn = get_conn()
        cursor = conn.cursor()
        updataSql = "update JuanInfo set `load` = 3 where jid = '%s'"%jid
        print updataSql
        cursor.execute(updataSql)
        conn.commit()
        return
    script_content = html.xpath('//script[1]/text()')[0]
    vars = script_content.strip().split('\n')
    parse_str = vars[2].strip()  # 取到eval()
    # parse_str = parse_str.replace('function(p,a,c,k,e,d)', 'function fun(p, a, c, k, e, d)')
    # parse_str = parse_str.replace('eval(', '')[:-1]  # 去除eval

    fun = """
            function run(){
                %s;
                return pages;
            }
        """ % parse_str  # 构造函数调用产生pages变量结果
    pages = execjs.compile(fun).call('run')
    url_list = []       
    conn = get_conn()
    cursor = conn.cursor() 
    if 'shtml' in response.request.url:
        # datas = pages.split('=')[2][1:-2]  # json数据块 var pages=pages=[]
        # print pages
        # print '*'*10
        datas = pages
        url_list = json.JSONDecoder().decode(datas)  # 解码json数据
    elif 'html' in response.request.url:
        # print '#'*10
        # print pages
        datas = pages  # var pages={}
        # print '!'*30
        # print datas.replace('\r\n',',')
        # print '@'*20
        # print json.JSONDecoder().decode(datas)['page_url']
        url_list = json.loads(datas.replace('\r\n',','), strict=False)['page_url'].split(',')
        # url_list = json.JSONDecoder().decode(datas.replace('\r\n',','))['page_url'].split(',')
    for index,url in enumerate(url_list):
        # print index
        yeUrl = "https://images.dmzj.com/" + url.decode("utf-8") 
        insertSqlYe = "INSERT INTO YeInfo_2 (jid,`index`,url) SELECT '%s','%s','%s' FROM DUAL WHERE NOT EXISTS(SELECT url FROM YeInfo_2 WHERE url = '%s' and jid = '%s')"%(jid,str(index),yeUrl,yeUrl,jid)
        # print insertSqlYe
        # print '-'*20
        # global insertf
        # insertf.write(insertSqlYe+";\n")
        # insertf.flush()
        cursor.execute(insertSqlYe)
    conn.commit()
    if len(url_list) > 0 :

        updataSql = "update JuanInfo set `load` = 1 where jid = '%s'"%jid
        # print '-'*20
        # print updataSql
        cursor.execute(updataSql)
        conn.commit()
    conn.close()
    # thredaStack.pop()


#设定爬取baseURL
conn = get_conn()
cursor = conn.cursor() 

selectSql = "select jid,url from JuanInfo where `load` = '0'"
cursor.execute(selectSql)
results = cursor.fetchall()
# get_request("https://manhua.dmzj.com/fuchouzhevyi/56785.shtml", "16261")
# insertf = open('insert2.sql',"a+")


# for result in results:
#     if ".html" in result[0]:
#         continue;
#     Dmzj(result[0])
# Dmzj("ttp://manhua.dmzj.com/hbgwjx")

# '''
executor = ThreadPoolExecutor(16)
thredaStack = Stack()
index = 0

for result in results:
    print str(result[0]) +"\t"+result[1]
    get_request(result[1], str(result[0]))
# while True:
#     if thredaStack.size() > 16:
#         continue
#     result = results[index]
#     print str(result[0]) +"\t"+result[1]
#     thredaStack.push("1")
#     executor.submit(get_request, result[1], str(result[0]))
#     index = index + 1
# '''


#select info.suolueName,ji.juanMing,yi.`index` from info info,JuanInfo ji,YeInfo yi where info.id = ji.id and ji.jid = yi.jid
baseUrl='http://manhua.dmzj.com/gujiantongxueyoujiaoliuzhangaizheng'
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

    # bilibiliThread(start_urls, offset)

    # offset = offset + 1
    # f = open('offset.txt','w')
    # f.write(str(offset))
    # f.close()
    # start_urls =baseUrl + str(offset)


        