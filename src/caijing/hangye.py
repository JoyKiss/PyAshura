#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-06 09:55:35


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')
import tushare as ts
datas = ts.get_industry_classified()
datas.to_csv('test.csv')
datas = ts.get_concept_classified()
datas.to_csv('test2.csv')