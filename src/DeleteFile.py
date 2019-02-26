#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-04 18:06:26


import os
import os
n = 0
for root, dirs, files in os.walk('E:\\python\\pachong\\.scrapy\\httpcache\\bilibiliVideo'):
    for name in files:                                                                                
            n += 1
            print(os.path.join(root, name))
            os.remove(os.path.join(root, name))