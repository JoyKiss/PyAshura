#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-23 13:21:08


import os

from kafka import KafkaConsumer  
import time  
  
def log(str):  
        t = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())  
        print("[%s]%s"%(t,str))  

'''
kafka消费者
'''
def getMsg():
  	consumer = KafkaConsumer(bootstrap_servers=['192.168.10.173:9092'])
	consumer.subscribe(topics=('testPython','test0'))
	while True:
	    msg = consumer.poll(timeout_ms=5)   #从kafka获取消息
	    print msg
	    time.sleep()

def getMsgByOffset():
	consumer = KafkaConsumer('testPython',
                         auto_offset_reset='earliest',
                         bootstrap_servers=['192.168.10.173:9092'])
                         
	for message in consumer:
		print ("%s:%d:%d: key=%s value=%s" %(message.topic, message.partition,message.offset, message.key,message.value))

if __name__ == '__main__':
	getMsgByOffset()

