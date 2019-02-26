# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-12-03 19:14:52
# 
# http://pokemon.alexonsager.net
import sys
reload(sys)
sys.path.append("..")
sys.path.append("../..")
from lxml import etree
import requests
from utils.Utils import *
from utils.csv2Mysql import *
#玩家赛事比赛记录
def transf(object):
	if len(object) > 0:
		return object[0]
	else :
		return ""

def getInfo(id):
	print '*' * 10 + str(id)
	data = {'id':id}
	res=requests.post("http://nsf.mimoe.cc/player.php",data=data)
	res.encoding="utf-8"
	html=res.text
	# print res.content

	print res.content
	response = etree.HTML(html)
	# print len(response.cssselect('.SONG_AUTHOR'))

	sqlname = response.xpath("//div[@class='sqlname']/text()")
	SONG_TITLE = response.xpath("//div[@class='SONG_TITLE']/text()")
	SONG_AUTHOR = response.xpath("//div[@class='SONG_AUTHOR']/text()")
	SONG_COPYRIGHT = response.xpath("//div[@class='SONG_COPYRIGHT']/text()")
	file = response.xpath("//param[@name='flashvars']/@value")
	if len(file) >0:
		if file[0].find('nsf') > 0:
		# file.substring()
		# print file[0].split('temp/')[1].split('.nsf')[0]

			map = {}
			map['sqlname'] = transf(sqlname)
			map['SONG_TITLE'] = transf(SONG_TITLE)
			map['SONG_AUTHOR'] = transf(SONG_AUTHOR)
			map['SONG_COPYRIGHT'] = transf(SONG_COPYRIGHT)
			map['file'] = 'http://nsf.mimoe.cc/temp/'+file[0].split('temp/')[1].split('.nsf')[0]+'.nsf'
			map2Csv(map, "test.csv","test_head")
			print map
def getMix(x,y):
	url = "http://pokemon.alexonsager.net/" + str(x) + "/" + str(y)
	print url
	res=requests.get(url)
	res.encoding="utf-8"
	html=res.text
	# print res.content

	# print res.content
	response = etree.HTML(html)
	children = response.cssselect('#pk_name')[0].text
	childrenImg = response.cssselect('#pk_img')[0].get("src")
	father = response.cssselect('#select1 > option[selected="selected"]')[0].text
	fatherImg = response.cssselect('#pic1')[0].get("src")
	mather = response.cssselect('#select2 > option[selected="selected"]')[0].text
	matherImg = response.cssselect('#pic2')[0].get("src")
	map = {}
	map['children'] = children
	map['childrenImg'] = childrenImg
	map['father'] = father
	map['fatherImg'] = fatherImg
	map['mather'] = mather
	map['matherImg'] = matherImg
	map2Csv(map, "test.csv","test_head")
	print map

# for x in xrange(1801,3049):
# 	getInfo(x)
# readCsvToMysqlNoHead('test.csv','nsfInfo','nsf',1,',')
max1 = 152
max2 = 152
for x in xrange(73,max1):
	for y in xrange(1,max2):
		getMix(x,y)
