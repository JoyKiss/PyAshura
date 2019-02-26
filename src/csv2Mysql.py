# -*- coding: utf-8 -*-
import pymysql
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#从创建数据库连接
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='111111', db='test', charset='utf8')
    return conn

#执行sql文
def insert(cur, sql, args):
    cur.execute(sql, args)

#读取指定csv文件,并导入数据
def read_csv_to_mysql(filename,tableName):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        heads = next(reader)
        conn = get_conn()
        cur = conn.cursor()
       	count =0;
        tableCheckSql = "DROP TABLE IF EXISTS `"+tableName+"`;"
        cur.execute(tableCheckSql)
       	creatsql = "CREATE TABLE `"+tableName+"` ("
       	col = ""
       	#for index,head in enumerate(heads):
       	for index,head in enumerate(heads):
       		#ol = col+"`"+head+"` varchar(255) DEFAULT NULL,"
          if index == len(heads) -1 :
            col = col+"`"+head.encode('utf-8').decode('utf-8-sig')+"` varchar(255) DEFAULT NULL"
          else:
            col = col+"`"+head.encode('utf-8').decode('utf-8-sig')+"` varchar(255) DEFAULT NULL,"
        creatsql = creatsql + col + ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        creatsql =  creatsql.encode('utf-8').decode('utf-8-sig')
        print creatsql
        cur.execute(creatsql)
        count =0;
        #数据插入
        for item in reader:
          if item[1] is None or item[1] == '':  # item[1]作为唯一键，不能为null
                continue
          sql="insert into "+ tableName + " values(%s)" % (','.join('"' + str(c).replace("\\", "\\\\").replace("\"", "\\\"").replace("\'", "\\\'") + '"' for c in item))
          print sql
          cur.execute(sql)
          
          count = count + 1
          #每创建10调数据,做commit操作
          if count > 10:
            conn.commit()
            count = 0
        conn.commit()
        cur.close()
        conn.close()

def readCsvToMysqlNoHead(filename,tableName):
    with codecs.open(filename=filename, mode='r', encoding='utf-8') as f:
      reader = csv.reader(f,delimiter='\t')
      conn = get_conn()
      cur = conn.cursor()
      count =0;
      tableCheckSql = "DROP TABLE IF EXISTS `"+tableName+"`;"
      cur.execute(tableCheckSql)
      creatsql = "CREATE TABLE `"+tableName+"` ("
      
      count =0;
      #数据插入
      for index,item in enumerate(reader):
        if index == 0:
          tableCreate(item,tableName,cur)
        if item[1] is None or item[1] == '':  # item[1]作为唯一键，不能为null
              continue
        sql="insert into "+ tableName + " values(%s)" % (','.join('"' + str(c).replace("\\", "\\\\").replace("\"", "\\\"").replace("\'", "\\\'") + '"' for c in item))
        print sql
        cur.execute(sql)
        
        count = count + 1
        #每创建10调数据,做commit操作
        if count > 10:
          conn.commit()
          count = 0
      conn.commit()
      cur.close()
      conn.close()

def tableCreate(heads,tableName,cur):
  tableCheckSql = "DROP TABLE IF EXISTS `"+tableName+"`;"
  cur.execute(tableCheckSql)
  creatsql = "CREATE TABLE `"+tableName+"` ("
  print len(heads)
  col = ""
  for index in range(len(heads)):
    head = "col" + bytes(index+1)
    if index == len(heads) -1 :
      col = col+"`"+head.encode('utf-8').decode('utf-8-sig')+"` varchar(255) DEFAULT NULL"
    else:
      col = col+"`"+head.encode('utf-8').decode('utf-8-sig')+"` varchar(255) DEFAULT NULL,"
  creatsql = creatsql + col + ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
  creatsql =  creatsql.encode('utf-8').decode('utf-8-sig')
  print creatsql
  cur.execute(creatsql)


if __name__ == '__main__':
    #读取中文路径bug,使用unicode转换
    # readCsvToMysqlNoHead(unicode('E:/dmp部署/五矿数据/khxx.csv'),"khxx")
    # read_csv_to_mysql(unicode('./redis/wanplus.csv'),"wanplus")
    readCsvToMysqlNoHead(unicode('./b.txt'),"b")