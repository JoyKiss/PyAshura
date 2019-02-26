# -*- coding: utf-8 -*-

'''

Created on 2018年8月17日

@author: D

'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from sqlalchemy.pool import QueuePool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import traceback
import esconfig
 
 
# 用于不需要回滚和提交的操作
def find(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print(traceback.format_exc())
            print(str(e))
            return traceback.format_exc()
        finally:
            self.session.close()
 
    return wrapper
 
 
class MysqlManager(object):
    def __init__(self):
        mysql_connection_string = esconfig.mysql.get("mysql_connection_string")
 
        self.engine = create_engine('mysql+pymysql://' + mysql_connection_string + '?charset=utf8', poolclass=QueuePool,
                                    pool_recycle=3600)
        # self.DB_Session = sessionmaker(bind=self.engine)
        # self.session = self.DB_Session()
        self.DB_Session = sessionmaker(bind=self.engine, autocommit=False, autoflush=True, expire_on_commit=False)
        self.db = scoped_session(self.DB_Session)
        self.session = self.db()
 
#     @find
    def select_all_dict(self, sql, keys):
        a = self.session.execute(sql)
        a = a.fetchall()
        lists = []
        for i in a:
            if len(keys) == len(i):
                data_dict = {}
                for k, v in zip(keys, i):
                    data_dict[k] = v
                lists.append(data_dict)
            else:
                return False
        return lists
 
    # 关闭
    def close(self):
        self.session.close()
