#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-30 15:19:58


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')

import pytesseract
from PIL import Image
from PIL import ImageEnhance
#解决异常
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

img=Image.open("jietu.jpg")
enhancer = ImageEnhance.Color(img)
enhancer = enhancer.enhance(0)
enhancer = ImageEnhance.Brightness(enhancer)
enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
img = enhancer.enhance(20)
text=pytesseract.image_to_string(img,config=tessdata_dir_config,lang='chi_sim')
print text