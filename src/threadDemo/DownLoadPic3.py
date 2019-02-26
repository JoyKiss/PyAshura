# -*- coding: utf-8 -*-

'''

Created on 2018年7月16日

@author: D

'''
import multiprocessing
from utils.csv2Mysql import * 
import requests
from lxml import etree
import MySQLdb
import urllib2
import os
from concurrent.futures import ThreadPoolExecutor
import urllib
from utils.Utils import *
from utils.StockUtils import *
import time
# from matplotlib.font_manager import path
def downPic(url,filepath,name):
    global thredaStack

    if not os.path.exists(os.path.join("./data", filepath)):
        os.makedirs(os.path.join("./data", filepath))
    
    downpath = u'./%s/%s/%s'%('data',filepath,name+os.path.splitext(url)[1])
    print downpath 
#     print url
#     urllib.urlretrieve(url, downpath, Schedule)  
    urllib.urlretrieve(url, downpath)  
        
    updataSql = "update AllPic set `load` = '1' where  id = '%s'"%(name)
    conn = get_conn("duowan")
    cursor = conn.cursor() 
    cursor.execute(updataSql)
    conn.commit()
    conn.close()
    cursor.close()
    thredaStack.pop()
#     print thredaStack.size()
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per
def report(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r%d%%" % percent + ' complete')
    sys.stdout.flush()
executor = ThreadPoolExecutor(16)
thredaStack = Stack()
def trim(s):
    '''首先判断该字符串是否为空，如果为空，就返回该字符串，
    如果不为空的话，就判断字符串首尾字符是否为空，
    如果为空，就使用递归再次调用该函数trim(),否则就返回该函数'''
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return (trim(s[1:]))
    elif s[-1] == ' ':
        return (trim(s[:-1]))
    return s
if __name__ == '__main__':

    index = 0

    conn = get_conn("duowan")
    cursor = conn.cursor() 
    selectSql = "select col3,id,col2 from AllPic where `load` is null"
    cursor.execute(selectSql)
    urls = cursor.fetchall()
    while True:
#         print "."*10+ str(thredaStack.size())
        if thredaStack.size() > 32:
            time.sleep(2)
            continue
        result = urls[index]
#         print str(result[0])
        thredaStack.push("1")
        executor.submit(downPic, result[0].strip('\n'),trim(result[2]),str(result[1]))
        index = index + 1
    print '*'*10 + '处理完成'+'*'*10