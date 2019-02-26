# -*- coding: utf-8 -*-

'''

Created on 2018年8月3日

@author: D

'''
import sys
reload(sys)
sys.path.append("..")
from utils.csv2Mysql import readCsvToMysqlHead

# readCsvToMysqlHead(unicode('./echart.csv'), "echartDetail", 'echart', 1)
readCsvToMysqlHead(unicode('./echartinfo.csv'), "echartinfo", 'echart', 1)
