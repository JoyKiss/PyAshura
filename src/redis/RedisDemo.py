#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09 09:41:56


import os
import json
import sys
import ast
reload(sys)

sys.setdefaultencoding('utf-8')
sys.path.append("..") 
import redis
from utils.Utils import *
# r = redis.Redis(host="192.168.0.189", port=6379,db=0)
# print r.bitcount("bilibiVideoTest")
# r = redis.Redis(host='192.168.0.189', port=6379,db=0)
# # print r.get("name")
# datas = r.lrange('bilibiVideoTest',140, 149)
# for data in datas:
#     print data.decode("UTF-8")
#     # print "--------------------"
#     map = json.loads(data,encoding='utf-8')
#     print map['author']
#     logic(fun, ast.literal_eval(data))
# datas = getRedis("localhost","bilibiVideo")
# for data in datas:
#     print data
def do(datas):
    for data in datas:
        # print data.decode("utf-8")
        map = json.loads(data,encoding='utf-8')
        # print len(map.keys())
        # print map['author']
        map2Csv(map, "wanplus2.csv", "wanplus_head")

if __name__ == '__main__':
    getRedisByOffsetDo("localhost", "wanplusPeople", "wanplusPeople_offset",do,-1)

