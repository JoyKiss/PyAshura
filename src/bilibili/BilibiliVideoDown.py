#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-18 18:40:54


# import os

import sys
# reload(sys)

# sys.setdefaultencoding('utf-8')
'''
import urllib2
import json

# 注意 1056,修改这个数字得到其他视频集
jsonurl = "https://bangumi.bilibili.com/jsonp/seasoninfo/1056.ver?callback=seasonListCallback&jsonp=jsonp"

data = urllib2.urlopen(jsonurl).read()

first = data.index("{")
last = data.rindex("}")
json_data = data[first:last+1]

j = json.loads(json_data)
list = j['result']['episodes']

for item in list:
    print item['index']," ",item['index_title']," ",item['webplay_url']
'''
from you_get import common as you_get
dic = 'E:\\ship'
url = "http://api.tianxianle.com/jx/dapi.php?id=q6SqraGao3fHz6Gs0KOqZGNiZ2VomZJiZmSZnJidm6tpmqWraWuepMoo00oQnJvLygO0O0OO0O0O"
sys.argv = ['you_get','-o',dic,url]
you_get.main()