#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-23 13:23:18


import os
from kafka import KafkaProducer
'''
kafka生产者
'''
producer = KafkaProducer(bootstrap_servers=['192.168.10.173:9092'])  #此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]

for i in range(3):
    msg = "msg%d" % i
    producer.send('testPython', msg)
producer.close()