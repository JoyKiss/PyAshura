# -*- coding: utf-8 -*-

'''

Created on 2018年8月17日

@author: D

'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from sql_manage import MysqlManager
from esconfig import mysql, elasticsearch, db_field, es_config
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import traceback
import time
 
 
class TongBu(object):
 
    def __init__(self):
        try:
            # 是否展示json数据在控制台
            self.show_json = es_config.get("show_json")
            # 间隔多少秒同步一次
            self.sleep_time = es_config.get("sleep_time")
            # 为了解决同步时数据更新产生的误差
            self.time_difference = es_config.get("time_difference")
            # 当前时间,留有后用
            self.datetime_now = ""
            # es的ip和端口
            es_host = elasticsearch.get("hosts")
            # 连接es
            self.es = Elasticsearch(es_host)
            # 连接mysql
            self.mm = MysqlManager()
        except :
            print(traceback.format_exc())
    def tongbu_es_mm(self):
        try:
            # 同步开始时间
            start_time = time.time()
            print("start..............", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
            # 这个list用于批量插入es
            actions = []
            # 获得所有sql文件list
            statement_filespath = mysql.get("statement_filespath", [])
            if self.datetime_now:
                # 当前时间加上时间差(间隔时间加上执行同步用掉的时间，等于上一次同步开始时间)再字符串格式化
                # sql中格式化时间时年月日和时分秒之间不能空格，不然导入es时报解析错误，所以这里的时间格式化也统一中间加一个T
                self.datetime_now = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time() - (self.sleep_time + self.time_difference)))
            else:
                self.datetime_now = "1999-01-01T00:00:00"
            if statement_filespath:
                for filepath in statement_filespath:
                    # sql文件
                    sqlfile = filepath.get("sqlfile")
                    # es的索引
                    es_index = filepath.get("index")
                    # es的type
                    es_type = filepath.get("type")
                    # 读取sql文件内容
                    with open(sqlfile, "r") as opf:
                        sqldatas = opf.read()
                        # ::datetime_now是一个自定义的特殊字符串用于增量更新
                        if "::datetime_now" in sqldatas:
                            sqldatas = sqldatas.replace("::datetime_now", self.datetime_now)
                        else:
                            sqldatas = sqldatas
                        # es和sql字段的映射
                        dict_set = db_field.get(es_type)
                        # 访问mysql，得到一个list，元素都是字典，键是字段名，值是数据
                        db_data_list = self.mm.select_all_dict(sqldatas, dict_set)
                        if db_data_list:
                            # 将数据拼装成es的格式
                            for db_data in db_data_list:
                                action = {
                                    "_index": es_index,
                                    "_type": es_type,
                                    "@timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time())),
                                    "_source": db_data
                                }
                                # 如果没有id字段就自动生成
                                es_id = db_data.get("id", "")
                                if es_id:
                                    action["_id"] = es_id
                                # 是否显示json再终端
                                if self.show_json:
                                    print(action)
                                # 将拼装好的数据放进list中
                                actions.append(action)
            # list不为空就批量插入数据到es中
            if len(actions) > 0 :
                helpers.bulk(self.es, actions)
 
        except Exception as e:
            print(traceback.format_exc())
        else:
            end_time = time.time()
            print("end...................", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
            self.time_difference = end_time - start_time
 
        finally:
            # 报错就关闭数据库
            self.mm.close()
 
def main():
    tb = TongBu()
    # 间隔多少秒同步一次
    sleep_time = tb.sleep_time
    # 死循环执行导入数据，加上时间间隔
    while True:
        tb.tongbu_es_mm()
        time.sleep(sleep_time)
 
if __name__ == '__main__':
    main()
