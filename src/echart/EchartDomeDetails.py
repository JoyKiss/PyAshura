# -*- coding: utf-8 -*-

'''

Created on 2018年8月2日

@author: D

'''
import sys
reload(sys)
sys.path.append("..")
import urllib
import json
from IPython.core.page import page
from utils.csv2Mysql import * 
from utils.csv2Mysql import get_conn
from utils.CsvWrite import addCsv
import code

def down(cid, codeurl, cursor):  
    request = codeurl
    response = urllib.urlopen(request)
    obj = json.load(response)
#     
    
    cid = obj['data']['cid']
    authorUid = obj['data']['authorUid']
    authorUserName = obj['data']['authorUserName']
    title = obj['data']['title']
    description = obj['data']['description']
    latestVersion = obj['data']['latestVersion']
    alwaysLatest = obj['data']['alwaysLatest']
    createTime = obj['data']['createTime']
    lastUpdateTime = obj['data']['lastUpdateTime']
    auth = obj['data']['auth']
    uid = obj['data']['uid']
    publishedVersion = obj['data']['publishedVersion']
    forkFrom = obj['data']['forkFrom']
    isSpam = obj['data']['isSpam']
    version = obj['data']['version']
    parentVersion = obj['data']['parentVersion']
    echartsVersion = obj['data']['echartsVersion']
    versionCreateTime = obj['data']['versionCreateTime']
    code = obj['data']['code']
    html = obj['data']['html']
    externalScripts = obj['data']['externalScripts']
    updaterUID = obj['data']['updaterUID']
    theme = obj['data']['theme']
    layout = obj['data']['layout']
    userName = obj['data']['userName']
    commentCount = obj['data']['commentCount']
    starCount = obj['data']['starCount']
    viewCount = obj['data']['viewCount']
    isStared = obj['data']['isStared']
    thumbnailURL = obj['data']['thumbnailURL']
    isCustomThumbnail = obj['data']['isCustomThumbnail']
    builtinTags = ",".join(obj['data']['builtinTags'])
    customTags = ",".join(obj['data']['customTags'])
    updaterUserName = obj['data'].get('updaterUserName', '')
    
    list = []
    list.append(transf(cid))
    list.append(transf(authorUid))
    list.append(transf(authorUserName))
    list.append(transf(title))
    list.append(transf(description))
    list.append(transf(latestVersion))
    list.append(transf(alwaysLatest))
    list.append(transf(createTime))
    list.append(transf(lastUpdateTime))
    list.append(transf(auth))
    list.append(transf(uid))
    list.append(transf(publishedVersion))
    list.append(transf(forkFrom))
    list.append(transf(isSpam))
    list.append(transf(version))
    list.append(transf(parentVersion))
    list.append(transf(echartsVersion))
    list.append(transf(versionCreateTime))
    list.append(transf(code))
    list.append(transf(html))
    list.append(transf(externalScripts))
    list.append(transf(updaterUID))
    list.append(transf(theme))
    list.append(transf(layout))
    list.append(transf(userName))
    list.append(transf(commentCount))
    list.append(transf(starCount))
    list.append(transf(viewCount))
    list.append(transf(isStared))
    list.append(transf(thumbnailURL))
    list.append(transf(isCustomThumbnail))
    list.append(transf(builtinTags))
    list.append(transf(customTags))
    list.append(transf(updaterUserName))

    
    
    updateSql = "insert into echartDetail select %s FROM DUAL WHERE NOT EXISTS(SELECT cid FROM echartDetail WHERE cid = '%s')" % ("\'" + "','".join(list) + "\'", cid)
    print(updateSql)
    cursor.execute(updateSql)
    conn.commit()
#     print builtinTags    
def transf(strInfo):
    if strInfo == None:
        return "";
    return str(strInfo).replace("\\", "\\\\").replace("\'", "\\'");
conn = get_conn("echart")
cursor = conn.cursor() 
selectSql = "select cid,codeUrl from (select ei.cid,ei.codeUrl, ed.cid as cidT from echartInfo ei left join echartDetail ed on ei.cid = ed.cid) data where cidT is null"
cursor.execute(selectSql)
results = cursor.fetchall()

for result in results:
    print(result[0])
    print(result[1])
    down(result[0], result[1], cursor)
#     down(index, cursor)
