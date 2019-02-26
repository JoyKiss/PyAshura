#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
reload(sys)
sys.path.append("..")
import time
import requests
from utils.Utils import *
# i = 1
# while i <= 3:
#     print i # 输出i
#     i += 1
#     time.sleep(1) # 休眠1秒
def getVote():
	co="pgv_info=ssid=s1227160000; pgv_pvid=5548731100; eas_sid=W1q5w4h0p2W7u9X7v5s3Q4G0u5; _qpsvr_localtk=0.6320395064544919; pgv_pvi=1542038528; pgv_si=s8571954176; pt2gguin=o0958685878; uin=o0958685878; skey=@N4U5J2BTw; ptisp=ctc; RK=uMgw/ABQPs; ptcz=d35e48863c637f341e7185d30f4e1926c3a447f20db2a69f1ee3ce4e29ffc0ef; p_uin=o0958685878; pt4_token=Nr0dpT6n9-tSGcT7xO1kAYb-bRAfiUW65LxToY4N14o_; p_skey=jwM0MPS6i1R9G4cXwJNo1cdZ4xcWiPWydnGxyl8eHgI_; IED_LOG_INFO2=userUin%3D958685878%26nickName%3D%2525E4%2525B8%252593%2525E5%252590%252583AB%2525E8%2525A1%252580%2525E5%25259E%25258B%2525E8%252580%252581%2525E9%2525BC%2525A0%26userLoginTime%3D1540279759; LOL_CGA_Lottery_958685878=1%7CLWL%u4E36Hadoop%7C65%7C4130599327%7C1522"
	cookies={}#初始化cookies字典变量
	for line in co.split(';'):   #按照字符：进行划分读取
	    #其设置为1就会把字符串拆分成2份
	    # print line
	    name=line.strip().split('=')[0]
	    value=line.strip().split('=')[1]
	    cookies[name]=value  #为字典cookies添加内容
	res=requests.get("https://lol.ams.game.qq.com/CGA_v1/ExecTask?p0=Browser&p1=303&p2=11830&p3=1&p4=&p5=0&ProdId=",cookies=cookies)
	# print res.content
	datas = json.JSONDecoder().decode(res.content) 
	# print str(len(datas['msg']['data']))
	info = datas['msg']['data']
	map = {}
	key = ""
	for x in info:
		if key == "":
			key = x
		else:
			map[key] = x
			key = ""
	print map
	map['zztime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
	print map['zztime']
	# items = map.items()
	# items.sort()
	# for key,value in items:
	#    print key, value # print key,dict[key]
	map2Csv(map, "test.csv","test_head")

import time
while True :
    time.sleep(1) # 休眠1秒
    getVote()
