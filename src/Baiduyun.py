#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-21 18:27:10


import os
import BaiduTiebaPicLoad as load
from bs4 import BeautifulSoup
url = 'http://pan.baidu.com/s/1pLc7AvL'
html = load.getHtmlContent(url)

soup =BeautifulSoup(html,'html.parser')

print html
