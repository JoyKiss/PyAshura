#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-18 14:44:31


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')
import zipfile
import pymysql
import shutil
import re
sys.path.append("..")
#从创建数据库连接
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='111111', db='dmzj', charset='utf8')
    return conn
# def do(file,zip_name):
#     files = []
#     files.append(file)
#     zip_files(files, zip_name)
# def zip_files( files, zip_name ):
#     zip = zipfile.ZipFile( zip_name, 'w', zipfile.ZIP_DEFLATED )
#     for file in files:
#         print ('compressing', file)
#         zip.write( file )
#     zip.close()
#     print ('compressing finished')



# files = '.\\123'#文件的位置，多个文件用“，”隔开
# zip_file = '.\\m66y.zip'#压缩包名字
# do(files, zip_file)
def zip_ya(startdir,file_news):
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) #参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'') #这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            
    z.close()
    print ('压缩成功')
def filesZip(startdir,zipName):
    file_news = zipName +'.zip' # 压缩后文件夹的名字 
    zip_ya(startdir,file_news)
def replace(st):
    return re.sub('[\/:*?"<>|]','-',st).strip()
# filesZip(".\\123", "456")
conn = get_conn()
cursor = conn.cursor() 

selectSql = "SELECT CONCAT(info.id,'_',info.cnName) from Info where `status` = '已完结'"
cursor.execute(selectSql)
results = cursor.fetchall()

# insertf = open('insert2.sql',"a+")
for result in results:
    down = "down"
    finish = "finish"
    file = str(replace(result[0])).strip().decode('utf-8')
    oldPath = "%s/%s"%(down,file)
    newPath = "%s/%s"%(finish,file)
    if os.path.exists(os.path.join("./", oldPath)):
        filesZip(os.path.join("./", oldPath), file)
    
        shutil.move(u'./%s/%s'%(down,file),u'./%s/%s'%(finish,file)) 
