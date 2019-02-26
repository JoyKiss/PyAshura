# -*- coding: utf-8 -*-

'''

Created on 2018年8月16日

@author: D

'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch([{'host':'localhost', 'port':9200}])
query_all = {
    'query': {
        'match_all': {}
    }
}
# search
print('search:')
res = es.search(index="lagou", body=query_all)
print(res)

# 批量索引文档
actions = []
action = {"_index": "kad_info",
          "_type": "articles",
          "_id": "1",
          "_source": {
              "article_crawtime": "2017-03-10 15:05:00",
              "keywords01": "辅助用药 芜湖市 转化糖电解质注射液",
              "keywords02": [{"keyword": "辅助用药", "weight": 0.9}, {"keyword": "芜湖市", "weight": 0.8},
                             {"keyword": "转化糖电解质注射液", "weight": 0.7}],
              "title": ";01又有21个品种进辅助用药目录01;"
          }}
actions.append(action)
action = {"_index": "kad_info",
          "_type": "articles",
          "_id": "2",
          "_source": {
              "article_crawtime": "2017-03-10 15:05:00",
              "keywords01": "辅助用药 芜湖市 转化糖电解质注射液",
              "keywords02": [{"keyword": "辅助用药", "weight": 0.9}, {"keyword": "芜湖市", "weight": 0.8},
                             {"keyword": "转化糖电解质注射液", "weight": 0.7}],
              "title": ";02又有21个品种进辅助用药目录01;"
          }}
actions.append(action)
rs = bulk(es, actions=actions)
print('成功插入%d个文档...' % (rs[0]))