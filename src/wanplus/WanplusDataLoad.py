# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-10-30 16:18:56
import sys
reload(sys)
sys.path.append("..")
import requests
from utils.Utils import *
sys.setdefaultencoding('utf8')
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch([{'host':'localhost', 'port':9200}])
# i = 1
# while i <= 3:
#     print i # 输出i
#     i += 1
#     time.sleep(1) # 休眠1秒
def getGamen(id):
	co="wanplus_token=a8d000fe62bad2459a3e7371a0bf705d; wanplus_storage=lf4m67eka3o; wanplus_sid=cae572dd843ff535c3e77f43aee11418; wanplus_csrf=_csrf_tk_945700120; gameType=2; UM_distinctid=166c3fdef753aa-032792d1db098b-6d55742d-1fa400-166c3fdef76818; wp_pvid=2937363251; wp_info=ssid=s961095312; Hm_lvt_f69cb5ec253c6012b2aa449fb925c1c2=1540886491; CNZZDATA1275078652=1770452343-1540881657-https%253A%252F%252Fwww.wanplus.com%252F%7C1540881657; Hm_lpvt_f69cb5ec253c6012b2aa449fb925c1c2=1540886783"
	headers={'x-csrf-token':'945700120','x-requested-with':'XMLHttpRequest'}
	# print headers
	cookies={}#初始化cookies字典变量
	for line in co.split(';'):   #按照字符：进行划分读取
	    #其设置为1就会把字符串拆分成2份
	    # print line
	    name=line.strip().split('=')[0]
	    value=line.strip().split('=')[1]
	    cookies[name]=value  #为字典cookies添加内容
	#玩家赛事比赛记录
	res=requests.get("https://m.wanplus.com/ajax/matchdetail/"+str(id)+"?_gtk=945700120",cookies=cookies,headers=headers)
	# print res.content
	data = json.JSONDecoder().decode(res.content) 
	if data['msg'] == 'success':
		# print data['data']
		actions = []
		datas = {"_index": "wanplus_data",
          "_type": "lol_data",
          "_id": x,
          # "data": data['data']
          "data":res.content
          }
		actions.append(datas)
		rs = bulk(es, actions=actions)
	# print str(len(datas['msg']['data']))
	# info = datas['msg']['data']
	# map = {}
	# key = ""
	# for x in info:
	# 	if key == "":
	# 		key = x
	# 	else:
	# 		map[key] = x
	# 		key = ""
	# print map
	# map['zztime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
	# print map['zztime']
	# # items = map.items()
	# # items.sort()
	# # for key,value in items:
	# #    print key, value # print key,dict[key]
	# map2Csv(map, "test.csv","test_head")
# 37
for x in xrange(38,1000000):
	print x
	getGamen(x)