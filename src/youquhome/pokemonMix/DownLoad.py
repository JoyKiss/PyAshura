# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-12-05 17:36:35
import sys
reload(sys)
sys.path.append("..")
import urllib 
import urllib2

#http://zjcmpp.hexin.com.cn/soft/THS_freeldy_8.70.60.exe
def writeFile(url,file):
	f = urllib2.urlopen(url) 
	with open(file, "wb") as code:
		code.write(f.read())
writeFile("http://zjcmpp.hexin.com.cn/soft/THS_freeldy_8.70.60.exe","THS_freeldy_8.70.60.exe")