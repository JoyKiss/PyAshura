# -*- coding: utf-8 -*-

'''

Created on 2018年7月13日

@author: D

'''
import sys
reload(sys)
sys.path.append("..")
sys.path.append("D:\\eclipse\\workspace\\PyAshura\\src")
import multiprocessing
from utils.csv2Mysql import * 
import requests
from lxml import etree
import MySQLdb


conn = get_conn("duowan")
cursor = conn.cursor() 

selectSql = "select col1 from UrlInfo_copy where count <=0"
cursor.execute(selectSql)
results = cursor.fetchall()
for result in results:
    updateSql = "update UrlInfo_copy url set url.count = (select count(1) from AllPic pic where pic.col1 = url.col1) where url.col1 = '%s'" % result[0]
    print updateSql
    cursor.execute(updateSql)
    conn.commit()