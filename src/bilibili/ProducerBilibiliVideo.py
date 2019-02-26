#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-09 13:22:43


import os

import sys
import csv
reload(sys)
sys.path.append("..")
import json
import codecs
from utils.Utils import *
sys.setdefaultencoding('utf-8')
import pandas as pd 

def do(datas):
    for data in datas:
        print data.decode("utf-8")
        map = json.loads(data,encoding='utf-8')
        print map['author']

if __name__ == '__main__':
    getRedisByOffsetDo("192.168.0.189", "bilibiVideoTest", "bilibiVideo_offset",do,10)
