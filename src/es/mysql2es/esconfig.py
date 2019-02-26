# -*- coding: utf-8 -*-

'''

Created on 2018年8月17日

@author: D

'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')
mysql = {
    # mysql连接信息
    "mysql_connection_string": "root:111111@127.0.0.1:3306/lol",
    # sql文件信息
    "statement_filespath":[
        # sql对应的es索引和es类型
        {
          "index":"lol",
          "sqlfile":"Champion.sql",
          "type":"ChampionInfo"
        }
    ],
}
 
# es的ip和端口
elasticsearch = {
    "hosts":"127.0.0.1:9200",
}
 
# 字段顺序与sql文件字段顺序一致，这是存进es中的字段名，这里用es的type名作为标识
db_field = {
        "ChampionInfo":
            ("no",
"id",
"key",
"name",
"title",
"tags",
"image_full",
"image_group",
"image_sprite",
"image_h",
"image_w",
"image_y",
"image_x",
"attack",
"defense",
"magic",
"difficulty",
"version",
"updated",
"lore",
"blurb",
"allytips",
"enemytips"

          )
 
   
}
 
 
es_config = {
    # 间隔多少秒同步一次
    "sleep_time":10000,
    # 为了解决服务器之间时间差问题
    "time_difference":3,
    # show_json 用来展示导入的json格式数据，
    "show_json":True,
}