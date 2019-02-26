#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-01 20:54:36


import os
from lxml import etree
import requests
import sys
import json
reload(sys)
import threading
import time
sys.path.append("..")
from utils.Utils import *
from utils.StockUtils import *

url = 'https://i.dmzj.com/ajax/my/subscribe'
cookies = dict(BAIDU_SSP_lc='https://www.baidu.com/link?url=NoFXt7eZ8oEWYe3gTjxGcCmIeuJQbbVZpBHIDRWSzZMj_LhLAtdIMxI4U5mAq_Rr&wd=&eqid=fdb219ff00016a74000000055ae1ad04',
    UM_distinctid='16285edadfba5-0482297e85895-3e3d5f01-144000-16285edadfd329',
    love='ccf4611081f86eeb050c5bf5fecf6974',
    my='101666652%7CMewtwo%7C%7Cdb8ef23646d3d7e90561932b168f9e59',
    show_tip='0',
    show_tip_1='0',
    sns_comic_101666652='16685\%23\%232136',
    type='qq')
r = requests.post(url, cookies=cookies)
print r.text