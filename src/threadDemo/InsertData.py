# -*- coding: utf-8 -*-

'''

Created on 2018年7月13日

@author: D

'''
import multiprocessing
from utils.csv2Mysql import * 
import requests
from lxml import etree
import MySQLdb
def getPicUrl2(url):
#         url = q.get()
    print "loading>>>>>>>>>>>>>>>>>>>>>>" + url
    requests.adapters.DEFAULT_RETRIES = 5
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    r = requests.get(url,headers=headers)
    r.encoding='utf-8'
    content=r.text
    
    response=etree.HTML(content)
    item = {}
    title = response.xpath("/html/head/title/text()")[0]
    print title
    boxs = response.xpath("//*[@class='pic-box']")
#     f = open('AllPic3.csv',"a+")
    count =0;
    global cur
    global conn
    for box in boxs:
        img = box.xpath("a/span/@data-img")[0]
        msg = box.xpath("p")[0].xpath("string(.)")
        print img
        print msg
#         f.write(url+"\t"+mysqlTransf(title)+"\t"+mysqlTransf(img)+"\t"+mysqlTransf(msg)+"\n")
        print url+"\t"+title+"\t"+img+"\t"+msg
        list = []
        list.append(str(url))
        list.append(mysqlTransf(title))
        list.append(mysqlTransf(img))
        list.append(mysqlTransf(msg))
        sql="insert into  AllPic values(%s)" % (','.join('"' + str(c).replace("\\", "\\\\").replace("\"", "\\\"").replace("\'", "\\\'") + '"' for c in list))
        print sql
        cur.execute(sql)
        
        count = count + 1
        #每创建10调数据,做commit操作
        if count > 10:
          conn.commit()
          count = 0
        conn.commit()

#     f.close() 
def mysqlTransf(info):
    return str(MySQLdb.escape_string(info)).replace("\\", "\\\\").replace("\"", "\\\"").replace("\'", "\\\'")
conn = get_conn("duowan")
cur = conn.cursor()
if __name__ == '__main__':
    # 读取中文路径bug,使用unicode转换
    # readCsvToMysqlNoHead(unicode('E:/dmp部署/五矿数据/khxx.csv'),"khxx")
    # read_csv_to_mysql(unicode('./redis/wanplus.csv'),"wanplus")
#     readCsvToMysqlNoHead(unicode('./AllPic2.csv'), "AllPic", 'duowan', 1, '\t')
#     readCsvToMysqlNoHead(unicode('./infoQueueAll.csv'), "UrlInfo", 'duowan', 1, '\t')

#     f = open("infoQueue.csv","r+")
#     f.seek(0)
#     urls = f.readlines();
    conn = get_conn("duowan")
    cursor = conn.cursor() 
    selectSql = "select col1 from UrlInfo_copy where count <=0"
    cursor.execute(selectSql)
    urls = cursor.fetchall()
    poolsize = 0;
    count = 0
    pool = multiprocessing.Pool(processes = 8)
    for url in urls:
        url = url[0].strip('\n')
#         getPicUrl2(url)
        pool.apply_async(getPicUrl2, (url,))
        poolsize = poolsize +1 
        count = count + 1
        print url
        if poolsize >= 16 or count >= len(urls):
            pool.close()
            pool.join() 
            poolsize = 0
            pool = multiprocessing.Pool(processes = 16)
    cur.close()
    conn.close()
#         url = f.readline()
#     url = f.readline()
#     pool = multiprocessing.Pool(processes = 2)
#     while url:
#         url = url.strip('\n')
#         pool.apply_async(getPicUrl2, (url,))
#         url = f.readline()
#         pool.close()
#         pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print '*'*10 + '处理完成'+'*'*10
