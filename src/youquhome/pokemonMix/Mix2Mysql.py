# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-12-05 17:46:45
import sys
reload(sys)
sys.path.append("..")
sys.path.append("../..")
from utils.csv2Mysql import *
readCsvToMysqlNoHead('test.csv','pokemonMix','pokemon',1,',')