#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-21

import csv

# 添加多行数据到文件当中
def addCsvs(fileName, list):
	f = open(fileName, "ab")
	# 加引号csv.QUOTE_NONNUMERIC
	writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
	for data in list:
		writer.writerow(data)
	f.close()

# 添加多行数据到文件当中
def addCsv(fileName, list):
	f = open(fileName, "ab")
	# 加引号csv.QUOTE_NONNUMERIC
	writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
	writer.writerow(list)		
	f.close()

if __name__ == "__main__":
	list1 = ['11避', '21', '31']
	list2 = ['a1', 'b1', 'c1']
	list = []
	list.append(list1)
	list.append(list2)
	addCsvs("text.csv", list)

