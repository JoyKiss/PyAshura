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
def Dmzj(url):
    print url
    requests.adapters.DEFAULT_RETRIES = 5
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    content=requests.get(url,headers=headers).text.decode('utf-8')
    # print content
    response = etree.HTML(content)
    # print content
    print "*" * 10
    # global thredaStack
    if ".html" in url:
        # hrefs = response.xpath("//ul[@class='list_con_li autoHeight']/li/a")

        # thredaStack.pop()
        return
    else:
        hrefs = response.xpath("//div[@class='cartoon_online_border_other']/ul/li/a | //div[@class='cartoon_online_border']/ul/li/a")

    try:
        if ".html" in url:
            name = response.xpath("//h1/a/text()")[0]
        else:
            if len(response.xpath("//h1/text()")) == 0:
                return
            name = response.xpath("//h1/text()")[0]
        len(name)
        list = []
        if ".html" in url:
            list.append(url.replace("http://www.dmzj.com/info/", ""))
        else:
            list.append(url.replace("https://manhua.dmzj.com/", ""))
        list.append(name.replace("'","''"))
        if ".html" in url:
            htmlInfo = response.xpath("//ul[@class='comic_deCon_liO']/li/text()")
            list.append("")
            list.append("")
            list.append(htmlInfo[0])
            list.append("")
            list.append(htmlInfo[1])
            list.append("")
            list.append(htmlInfo[2])
            list.append(htmlInfo[3])
            list.append("")
        else:
            print len(response.xpath("//div[@class='anim-main_list']"))
            for index,td in enumerate(response.xpath("//div[@class='anim-main_list']")[0].xpath(".//td")):
                info = td.xpath("string(.)")
                info = info.replace("'","''")
                print '#'*10
                print info
                list.append(info) 
            if len(list) != 11:
                list.append("")
        for st in list:
            print st
        list.append(url)
        conn = get_conn()
        cursor = conn.cursor()  
        # execute SQL statement  
        insertSql = "INSERT INTO Info(suolueName,cnName,bieMing,yuanMing,author,diqu,STATUS,renqi,ticai,fenlei,newStatus,url) SELECT %s FROM DUAL WHERE NOT EXISTS(SELECT suolueName FROM Info WHERE suolueName = '%s')"%("\'"+"','".join(list)+"\'",list[0])
        print insertSql
        cursor.execute(insertSql)  
        id = cursor.lastrowid
        if id == 0:
            selectSql = "select id from Info where suolueName = '%s'"%list[0]
            cursor.execute(selectSql)
            results = cursor.fetchall()
            for row in results:
                id = row[0]
        print id
        conn.commit()
        for href in hrefs:
            juanMing = href.xpath("string(.)")
            juanUrls = href.xpath("@href")
            if ".html" in url:
                juanUrl = juanUrls[0]
            else:
                juanUrl = "https://manhua.dmzj.com"+juanUrls[0]

            insertSqlJuan = "INSERT INTO JuanInfo (id,juanMing,url) SELECT '%s','%s','%s' FROM DUAL WHERE NOT EXISTS(SELECT url FROM JuanInfo WHERE url = '%s')"%(id,juanMing.replace("'","''"),juanUrl,juanUrl)
            
            print insertSqlJuan
            cursor.execute(insertSqlJuan) 
            jid = cursor.lastrowid
            if jid == 0:
                selectSqlJuan = "select jid from JuanInfo where url = '%s'"%juanUrl
                cursor.execute(selectSqlJuan)
                results = cursor.fetchall()   
                for row in results:
                    jid = row[0]
            print jid
            conn.commit()

            # get_request(juanUrl,jid)
        updataSql = "update dmzj set `load` = 1 where url = '%s'"%url
        cursor.execute(updataSql)
        conn.commit()
        conn.close()
        # thredaStack.pop()
    except Exception as e:
        print e
        raise

   


    # for a in href:
        # print a.xpath("text()")[0]
        # print a.xpath("@href")[0]
        #host = "https://manhua.dmzj.com/"
    # f = open('bilibiliVideoTest.csv',"a+")
    # f.write(",".join(addInfo)+"\n")
    # f.flush()
    # f.close()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Referer': 'http://www.dmzj.com/category'
}
def get_request(href,jid):
    response = requests.get(href, headers=headers)

    try:
        html = etree.HTML(response.content)
        script_content = html.xpath('//script[1]/text()')[0]
        vars = script_content.strip().split('\n')
        parse_str = vars[2].strip()  # 取到eval()
        parse_str = parse_str.replace('function(p,a,c,k,e,d)', 'function fun(p, a, c, k, e, d)')
        parse_str = parse_str.replace('eval(', '')[:-1]  # 去除eval
        fun = """
                function run(){
                    var result = %s;
                    return result;
                }
            """ % parse_str  # 构造函数调用产生pages变量结果
        pages = execjs.compile(fun).call('run')
        url_list = []       
        conn = get_conn()
        cursor = conn.cursor() 
        if 'shtml' in response.request.url:
            datas = pages.split('=')[2][1:-2]  # json数据块 var pages=pages=[]
            url_list = json.JSONDecoder().decode(datas)  # 解码json数据
        elif 'html' in response.request.url:
            datas = pages.split('=')[1][1:-2]  # var pages={}
            url_list = json.JSONDecoder().decode(datas)['page_url'].split('\r\n')
        for index,url in enumerate(url_list):
            print index
            yeUrl = "https://images.dmzj.com/" + url.decode("utf-8") 
            insertSqlYe = "INSERT INTO YeInfo (jid,`index`,url) SELECT '%s','%s','%s' FROM DUAL WHERE NOT EXISTS(SELECT url FROM YeInfo WHERE url = '%s' and jid = '%s')"%(jid,str(index),yeUrl,yeUrl,jid)
            print insertSqlYe
            # global insertf
            # insertf.write(insertSqlYe+";\n")
            # insertf.flush()
            cursor.execute(insertSqlYe)
            conn.commit()
            #host = "https://images.dmzj.com/"
        # headers['Referer'] = info['href']
        # if not os.path.exists('./downloads'):
        #     os.mkdir('./downloads')
        # for index, url in enumerate(url_list):
        #     img = requests.get(PREIX + url, headers=headers)
        #     import time
        #     time.sleep(1)  # 等待一些时间，防止请求过快
        #     click.echo(PREIX + url)
        #     with open('./downloads/%s.jpg' % index, mode='wb') as fp:
        #         fp.write(img.content)
        #     click.echo('save %s.jpg' % index)
        # click.echo('complete!')
        conn.close()
    except Exception as e:
        raise e

#设定爬取baseURL
conn = get_conn()
cursor = conn.cursor() 

selectSql = "select url from dmzj where `load` = 0"
cursor.execute(selectSql)
results = cursor.fetchall()

# insertf = open('insert2.sql',"a+")
for result in results:
    if ".html" in result[0]:
        continue;
    Dmzj(result[0])
# Dmzj("ttp://manhua.dmzj.com/hbgwjx")

'''
executor = ThreadPoolExecutor(1000)
thredaStack = Stack()
index = 0

while True:
    if thredaStack.size() > 20:
        continue

    thredaStack.push("1")
    executor.submit(Dmzj, results[index][0])
    index = index + 1
'''


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


        