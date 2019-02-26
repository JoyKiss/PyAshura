#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-23 09:33:34


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import *

#创建Hbase连接池
transport = TSocket.TSocket('192.168.10.173', 9090)

transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

# contents = ColumnDescriptor(name='cf:', maxVersions=1)
# client.deleteTable('test')
# client.createTable('test', [contents])

# print client.getTableNames()

# # insert data
# # transport.open()

# row = 'row-key1'

# mutations = [Mutation(column="cf:a", value="1")]
# client.mutateRow('test', row, mutations)

# 列查询
tableName = 'FG_RESULT'
rowKey = '15215327432859D0614B2B9ED'

result = client.getRow(tableName, rowKey)
print result
for r in result:
    print 'the row is ', r.row
    print 'the values is ', r.columns.get('info:FG_171.optime').value

client.