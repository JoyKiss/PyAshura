#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-10 14:02:03


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')
# 首先导包
from concurrent.futures import ThreadPoolExecutor

# 创建线程池
executor = ThreadPoolExecutor(10)

# 测试方法
def test_function(num1, num2):
    print(num1, num2)
    return num1 + num2

# 第一个参数为具体的方法，后面为方法的参数
future = executor.submit(test_function, 1, 2)
# future的result()方法可以获取到函数的执行结果
print(future.result())
