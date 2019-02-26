# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-12-04 10:27:02
import sys
reload(sys)
sys.path.append("..")
import pymysql
import urllib 
import urllib2
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='nsf', charset='utf8')
    return conn
def writeFile(url,file):
	f = urllib2.urlopen(url) 
	with open(file, "wb") as code:
		code.write(f.read())
import re
 
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
conn = get_conn()
cursor = conn.cursor() 
selectSql = "select name,file from (select REPLACE(CONCAT(sqlname,'(',TRIM(SONG_TITLE),')','_',SONG_COPYRIGHT,'.nsf'),'　','') as name, file from nsfinfo)data "
cursor.execute(selectSql)
results = cursor.fetchall()
index = 0
for result in results:
	if index > 1815:
		urllib.urlretrieve(result[1], str(index) + '.nsf')
		# writeFile(result[1],validateTitle(result[0]))
		# print result[1]+'\t'+ validateTitle(result[0])
		print '-' * 10 + str(index)
	index = index +1 