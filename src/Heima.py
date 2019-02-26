# -*- coding: utf-8 -*-
# @Date    : 2018-03-21
'''
获得黑马训练营视频
'''
import requests
import os
from bs4 import BeautifulSoup

import BaiduTiebaPicLoad as load
import csv
import numpy as np
# import uniout 
from CsvWrite import *
# import pandas as pa
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging as log
log.basicConfig(level=log.NOTSET)  # 设置日志级别

def selector(url,fileName):
	#加载url
	html = load.getHtmlContent(url)

	soup =BeautifulSoup(html,'html.parser')
	# 筛选html内容
	list =  soup.select("a[down]")
	for dom in list:
		href = dom["href"]
		tite = dom["tite"]
		log.debug(u'[' + href + u'],[' + tite + u']')
		if href != "":
			add_info = [tite,href,url]
			addCsv(fileName,add_info)

for x in xrange(1,500):
	url = "http://yun.itheima.com/course/"+str(x)+".html"
	log.debug(url)
	selector(url,"heima.csv")



	

