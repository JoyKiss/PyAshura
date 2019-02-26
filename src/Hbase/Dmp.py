#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-23 11:12:20

from thrift.transport import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import ColumnDescriptor
from hbase.ttypes import Mutation


class HBaseClient(object):
    def __init__(self, ip, port=9090):
        """
        建立与thrift server端的连接
        """
        # server端地址和端口设定
        self.__transport = TBufferedTransport(TSocket.TSocket(ip, port))
        # 设置传输协议
        protocol = TBinaryProtocol.TBinaryProtocol(self.__transport)
        # 客户端
        self.__client = Hbase.Client(protocol)
        # 打开连接
        self.__transport.open()

    def __del__(self):
        self.__transport.close()

    def get_tables(self):
        """
        获得所有表
        :return:表名列表
        """
        return self.__client.getTableNames()

    def create_table(self, table, *columns):
        """
        创建表格
        :param table:表名
        :param columns:列族名
        """
        func = lambda col: ColumnDescriptor(col)
        column_families = map(func, columns)
        self.__client.createTable(table, column_families)

    def put(self, table, row, columns):
        """
        添加记录
        :param table:表名
        :param row:行键
        :param columns:列名
        :return:
        """
        func = lambda (k, v): Mutation(column=k, value=v)
        mutations = map(func, columns.items())
        self.__client.mutateRow(table, row, mutations)

    def delete(self, table, row, column):
        """
        删除记录
        :param table:表名
        :param row:行键
        """
        self.__client.deleteAll(table, row, column)

    def scan(self, table, start_row="", columns=None):
        """
        获得记录
        :param table: 表名
        :param start_row: 起始行
        :param columns: 列族
        :param attributes:
        """
        scanner = self.__client.scannerOpen(table, start_row, columns)
        # func = lambda (k, v): (k, v.value)
        while True:
            r = self.__client.scannerGet(scanner)
            if not r:
                break
            yield r[0].row
    def getRow(self, table, row):
        """
        获得记录
        :param table: 表名
        :param start_row: 起始行
        :param columns: 列族
        :param attributes:
        """
        list = self.__client.getRow(table, row)
        func = lambda (k, v): (k, v.value)
       	return dict(map(func, list[0].columns.items()))

def getId(map):
	 for x in map:
	    if x.startswith("info:1046_"):
			return x.split("info:1046_", 1)[1]

def writeFile(fileName,string):
	f = open(fileName,"ab")
	f.write(string+"\n")
	f.close()

if __name__ == '__main__':
    client = HBaseClient("192.168.10.173")

    # client.create_table('student', 'name', 'course')
    # client.put("student", "1",
    #            {"name:": "Jack",
    #             "course:art": "88",
    #             "course:math": "12"})

    # client.put("student", "2",
    #            {"name:": "Tom", "course:art": "90",
    #             "course:math": "100"})

    # client.put("student", "3",
    #            {"name:": "Jerry"})
    # client.delete('student', '1', 'course:math')
    for v in client.scan('TG_RESULT'):
        # print v
        writeFile("gid2.txt",v)


    # f = open("gid.txt")
    # for line in f:
    # 	# print (line.strip())
    # 	str = getId(client.getRow("UM_MAPPER_GID",line.strip()))
    # 	print str
    # 	if str != None:
    # 		writeFile(u'资金账户.txt',str)
    # f.close()
    