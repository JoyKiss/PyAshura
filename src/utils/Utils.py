#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09 10:56:44


import os
import ast
import sys
reload(sys)
import json
sys.setdefaultencoding('utf-8')
import redis
import csv
'''
发送数据到redis中(List)
'''
def pushRedis(host,key,value):
    r = redis.Redis(host=host, port=6379,db=0)
    r.rpush(key, value)
'''
从redis中取出一条数据
'''
def popRedis(host,key):
    r = redis.Redis(host=host, port=6379,db=0)
    return ast.literal_eval(r.rpop(key))
'''
从redis中取出一条数据
'''
def popRedisDo(host,key,func,cyl = True):
    r = redis.Redis(host=host, port=6379,db=0)
    do = True
    while do:
        data = r.rpop(key)
        if data != null:
            func(ast.literal_eval(data))
        elif cyl == False:
            do = False
'''
从redis数据根据offset
host:redishost配置
key:读取信息的键值
offsetName:存放指定键值的offset的key名称
'''
def getRedisByOffset(host,key,offsetName):
    r = redis.Redis(host=host, port=6379,db=0)
    max = r.llen(key)
    offset = r.get(offsetName)

    if offset == None:
        offset = "0"
    print ("----------------------------")
    print ("数据长度:[" + max + "]")
    print ("offset :[" + offset + "]")
    print ("----------------------------")
    datas = r.lrange(key, offset, max)
    r.set(offsetName, max)
def getRedisByOffsetDo(host,key,offsetName,do,size=10000):
    r = redis.Redis(host=host, port=6379,db=0)
    max = r.llen(key)
    offset = r.get(offsetName)

    if offset == None:
        offset = "0"
    if size == -1:
        uOffset = max
        end = -1
    else : 
        end = int(offset) + size -1
        uOffset = int(offset) + size
        if end >= max -1:
            uOffset = max
            end = -1
    print ("----------------------------")
    print ("数据长度:[" + str(max) + "]")
    print ("offset :[" + str(offset) + "]")
    print ("读取位置 :[" + str(offset) + "~" + str(end)+ "]")
    print ("----------------------------")
    datas = r.lrange(key, offset, end)
    print len(datas)
    do(datas)
    r.set(offsetName, uOffset)

def getRedis(host,key,start=0,end=-1):
    r = redis.Redis(host=host, port=6379,db=0)
    datas = r.lrange(key, start, end)
    result = []
    for data in datas:
        print data
        result.append(ast.literal_eval(datas))
    return result

# getRedisByOffsetDo("localhost", "test2", "test2_Offset",do)

'''
mao内容写入到csv当中
输出文件为csv+csvhead
map:写入文件内容
fileName:输出csv文件名称
head:csv文件的头
'''
def map2Csv(map,fileName,headName):
    headRead = open(headName,"a+")
    head = headRead.read()
    if head == "":
        headRead = open(headName,"w+")
        headsTmp = map.keys()
        headRead.write(",".join(headsTmp))
        headRead.close()
    else :
        headsTmp = head.split(",")
    data = []
    for col in headsTmp:
        data.append(str(map[col]))
    with open(fileName, 'ab') as file:
        #csv.QUOTE_MINIMAL
        spamwriter = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        spamwriter.writerow(data)

    # file.write(",".join(data))
    # file.write("\n")
    file.close()
    headRead.close()

def maps2Csv(maps,fileName,head):
    headRead = open(head,"r+")
    headsTmp = headRead.read().split(",")

    if(len(headsTmp)) == 0:
        headsTmp = maps[0].keys()
        headRead.write(",".join(heads))
        headRead.close()
    with open(fileName, 'ab') as file:
        spamwriter = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for map in maps:
            data = []
            for col in headsTmp:
                data.append(str(map[col]))
            spamwriter.writerow(data)
    file.close()
    headRead.close()

if __name__ == '__main__':
    list = []
    map = {'a':1,'b':2}
    map2 = {'a':1,'b':2}
    list.append(map)
    list.append(map2)
    maps2Csv(list, "test.csv","test_head")
    