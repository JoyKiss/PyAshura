# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-10-31 14:58:20
import sys
reload(sys)
sys.path.append("..")
import wechatsogou

def prints(info):
	print str(info).encode('utf-8').decode('unicode_escape')
ws_api =wechatsogou.WechatSogouAPI()
prints(ws_api.get_gzh_info('Rita暴雨桑'))