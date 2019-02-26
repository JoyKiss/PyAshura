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

def down(num, cursor):
    request = 'http://gallery.echartsjs.com/chart/list?builtinTags%5B%5D=category-work&sortBy=createTime&pageSize=1&pageNumber=' + str(num) + '&author=all'
    response = urllib.urlopen(request)
    obj = json.load(response)
    
    pageNumber = obj['data']['pageNumber']
    cid = obj['data']['charts'][0]['cid']
    version = obj['data']['charts'][0]['version']
    createTime = obj['data']['charts'][0]['createTime']
    title = obj['data']['charts'][0]['title']
    auth = obj['data']['charts'][0]['auth']
    description = obj['data']['charts'][0]['description']
    lastUpdateTime = obj['data']['charts'][0]['lastUpdateTime']
    uid = obj['data']['charts'][0]['uid']
    starCount = obj['data']['charts'][0]['starCount']
    commentCount = obj['data']['charts'][0]['commentCount']
    viewCount = obj['data']['charts'][0]['viewCount']
    rankScore = obj['data']['charts'][0]['rankScore']
    forkFrom = obj['data']['charts'][0]['forkFrom']
    thumbnailURL = obj['data']['charts'][0]['thumbnailURL']
    isCustomThumbnail = obj['data']['charts'][0]['isCustomThumbnail']
    userName = obj['data']['charts'][0]['userName']
    avatar = obj['data']['charts'][0]['avatar']
    isStared = obj['data']['charts'][0]['isStared']
    url = "http://gallery.echartsjs.com/editor.html?c=" + cid
    codeUrl = "http://gallery.echartsjs.com/chart/get/" + cid
    
    
    list = []

    list.append(str(cid).replace("\'", "\\'"))
    list.append(str(version).replace("\'", "\\'"))
    list.append(str(createTime).replace("\'", "\\'"))
    list.append(str(title).replace("\'", "\\'"))
    list.append(str(auth).replace("\'", "\\'"))
    list.append(str(description).replace("\'", "\\'"))
    list.append(str(lastUpdateTime).replace("\'", "\\'"))
    list.append(str(uid).replace("\'", "\\'"))
    list.append(str(starCount).replace("\'", "\\'"))
    list.append(str(commentCount).replace("\'", "\\'"))
    list.append(str(viewCount).replace("\'", "\\'"))
    list.append(str(rankScore).replace("\'", "\\'"))
    list.append(str(forkFrom).replace("\'", "\\'"))
    list.append(str(thumbnailURL).replace("\'", "\\'"))
    list.append(str(isCustomThumbnail).replace("\'", "\\'"))
    list.append(str(userName).replace("\'", "\\'"))
    list.append(str(avatar).replace("\'", "\\'"))
    list.append(str(isStared).replace("\'", "\\'"))
    list.append(str(codeUrl).replace("\'", "\\'"))
    list.append(str(url).replace("\'", "\\'"))
#     addCsv('echart.csv', list)
    updateSql = "insert into echartInfo select %s FROM DUAL WHERE NOT EXISTS(SELECT cid FROM echartInfo WHERE cid = '%s')" % ("\'" + "','".join(list) + "\'", cid)
    print(updateSql)
    cursor.execute(updateSql)
    conn.commit()
    # print(obj)
    # print(url)
    # print(cid)
    # print(version)
    # print(createTime)
    # print(title)
    # print(auth)
    # print(description)
    # print(lastUpdateTime)
    # print(uid)
    # print(starCount)
    # print(commentCount)
    # print(viewCount)
    # print(rankScore)
    # print(forkFrom)
    # print(thumbnailURL)
    # print(isCustomThumbnail)
    # print(userName)
    # print(avatar)
    # print(isStared)
    # print(codeUrl)
    
#     request = codeUrl
#     response = urllib.urlopen(request)
#     obj = json.load(response)
#     
    
#     cid = obj['data']['cid']
#     authorUid = obj['data']['authorUid']
#     authorUserName = obj['data']['authorUserName']
#     title = obj['data']['title']
#     description = obj['data']['description']
#     latestVersion = obj['data']['latestVersion']
#     alwaysLatest = obj['data']['alwaysLatest']
#     createTime = obj['data']['createTime']
#     lastUpdateTime = obj['data']['lastUpdateTime']
#     auth = obj['data']['auth']
#     uid = obj['data']['uid']
#     publishedVersion = obj['data']['publishedVersion']
#     forkFrom = obj['data']['forkFrom']
#     isSpam = obj['data']['isSpam']
#     version = obj['data']['version']
#     parentVersion = obj['data']['parentVersion']
#     echartsVersion = obj['data']['echartsVersion']
#     versionCreateTime = obj['data']['versionCreateTime']
#     code = obj['data']['code']
#     html = obj['data']['html']
#     externalScripts = obj['data']['externalScripts']
#     updaterUID = obj['data']['updaterUID']
#     theme = obj['data']['theme']
#     layout = obj['data']['layout']
#     userName = obj['data']['userName']
#     commentCount = obj['data']['commentCount']
#     starCount = obj['data']['starCount']
#     viewCount = obj['data']['viewCount']
#     isStared = obj['data']['isStared']
#     thumbnailURL = obj['data']['thumbnailURL']
#     isCustomThumbnail = obj['data']['isCustomThumbnail']
#     builtinTags = ",".join(obj['data']['builtinTags'])
#     customTags = ",".join(obj['data']['customTags'])
#     updaterUserName = obj['data']['updaterUserName']
    # print builtinTags    
conn = get_conn("echart")
cursor = conn.cursor() 
for index in range(0, 4656):
    print(index)
    down(index, cursor)
