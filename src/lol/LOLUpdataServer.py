#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-29 13:10:18


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')
import pymysql
from lxml import etree
import requests
import execjs
import json
import ast

response = requests.get("http://gameact.qq.com/comm-htdocs/js/game_area/lol_server_select.js")
# html = etree.HTML(response.content)
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='111111', db='lol', charset='utf8')
    return conn
# print response.text
js = response.text
fun = """
            function run(){
                %s;
                return LOLServerSelect.STD_DATA;
            }
        """ % js  # 构造函数调用产生pages变量结果
pages = execjs.compile(fun).call('run')
std_data = "{'data':%s}"%pages
datas = ast.literal_eval(std_data)
print '-'*30
for data in datas['data']:
    
    name = data['t'].replace('  ',' ').split(' ')[0]
    if len(data['t'].replace('  ',' ').split(' ')) == 1:
        type = data['t'].replace('  ',' ').split(' ')[0]
    else :
        type = data['t'].replace('  ',' ').split(' ')[1]
    
    area = data['v']
    status = data['status']
    conn = get_conn()
    cursor = conn.cursor()
    updataSql = "REPLACE INTO ServerInfo (area,name,type,status) VALUES ('%s','%s','%s','%s');"%(area,name,type,status)
    print updataSql
    cursor.execute(updataSql)
    conn.commit()
# print url_list
# for data in url_list:
#     print data