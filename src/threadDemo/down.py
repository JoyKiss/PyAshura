# -*- coding: utf-8 -*-

'''

Created on 2018年7月10日

@author: D

'''
import multiprocessing
import Queue
from multiprocessing import Process, Queue
import os
from lxml import etree
import requests
import sys
import json
reload(sys)
import threading
import time
sys.path.append("..")
# 首先导包
import urllib2
from concurrent.futures import ThreadPoolExecutor
sys.setdefaultencoding('utf-8')
def downPic(url, name):
    f = urllib2.urlopen(url) 
    data = f.read() 
    with open(name, "wb") as code:     
        code.write(data)
downPic("http://s1.dwstatic.com/group1/M00/08/0E/98447e78161455bc13dce4328c0f35d8.gif", "彷徨.gif")