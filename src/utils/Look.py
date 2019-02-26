#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-10 17:23:28


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')
import csv  
  
  
with open(str(csv.__file__),"r") as f:  
    print (f.read())  