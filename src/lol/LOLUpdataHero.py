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

response = requests.get("http://lol.qq.com/biz/hero/champion.js")
# html = etree.HTML(response.content)
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='111111', db='lol', charset='utf8')
    return conn
# print response.text
js = response.text
fun = """
            function run(){
                %s;
                return LOLherojs.champion;
            }
        """ % js  # 构造函数调用产生pages变量结果
pages = execjs.compile(fun).call('run')
std_data = "{'data':%s}"%pages
datas = ast.literal_eval(std_data)
print '-'*30
print datas['data']['data']
for data in datas['data']['data']:
    print '-'*30
    champion = datas['data']['data'][data]
    key = data
    print key
    name =  champion['name']
    title = champion['title']
    tags = ','.join(champion['tags'])
    no = champion['key']
    id = champion['id']
    image_full = champion['image']['full']
    image_group = champion['image']['group']
    image_sprite = champion['image']['sprite']
    image_h = champion['image']['h']
    image_w = champion['image']['w']
    image_y = champion['image']['y']
    image_x = champion['image']['x']

    # print "REPLACE INTO Champion (no,id,key,name,title,tags,image_full,image_group,image_sprite,image_h,image_w,image_y,image_x) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(no,id,key,name,title,tags,image_full,image_group,image_sprite,image_h,image_w,image_y,image_x)

    conn = get_conn()
    cursor = conn.cursor()
    updataSql = "REPLACE INTO Champion (no,id,`key`,name,title,tags,image_full,image_group,image_sprite,image_h,image_w,image_y,image_x) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(no,id,key,name,title,tags,image_full,image_group,image_sprite,image_h,image_w,image_y,image_x)
    print updataSql
    cursor.execute(updataSql)
    conn.commit()
# print url_list
# for data in url_list:
#     print data