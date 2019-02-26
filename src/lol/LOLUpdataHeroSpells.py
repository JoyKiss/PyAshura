#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-29 13:10:18


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')
import pymysql
from lxml import etree
import requests
import execjs
import json
import ast

# html = etree.HTML(response.content)
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='111111', db='lol', charset='utf8')
    return conn
def getInfo(mapInfo,key):
    if mapInfo == None or len(mapInfo) == 0:
        return ""
    return mapInfo.get(key,"")
# print response.text
def do(championId,championKey):
    conn = get_conn()
    cursor = conn.cursor()
    url = "http://lol.qq.com/biz/hero/%s.js"%championKey
    response = requests.get(url)
    js = response.text
    fun = """
                function run(){
                    %s;
                    return LOLherojs.champion.%s;
                }
            """ % (js,championKey)  # 构造函数调用产生pages变量结果
    pages = execjs.compile(fun).call('run')
    std_data = "{'data':%s}"%pages
    datas = ast.literal_eval(std_data)
    print '-'*30
    # print datas['data']
    version = datas['data']['version']
    updated = datas['data']['updated']
    for data in datas['data']['data']:
        dataM = datas['data']['data']
        print data
        id = dataM.get("key")
        info = dataM.get('info')
        #物理攻击
        attack = getInfo(info,'attack')
        #防御
        defense = getInfo(info,'attack')
        #魔法
        magic = getInfo(info,'attack')
        #难易
        difficulty = getInfo(info,'attack')
        #简介
        blurb = dataM.get('blurb')
        #详细
        lore = dataM.get('lore')
        #使用者
        allytips = "<br/>".join(dataM.get('allytips'))
        #对战者
        enemytips = "<br/>".join(dataM.get('enemytips'))

        spells = dataM.get('spells')
        for spell in spells:
            #技能物理名
            spellId = spell.get('id')
            #技能伦理名
            name = spell.get('name')
            #技能描述
            description = spell.get('description')
            #技能图片信息
            image = spell.get('image')
            image_full = ""
            image_group = ""
            image_sprite = ""
            image_h = ""
            image_w = ""
            image_y = ""
            image_x = ""
            image_url = "http://ossweb-img.qq.com/images/lol/img/spell/%s.png"%spellId
            if image != None:
                image_full = image.get('full',"")
                image_group = getInfo(image,'group')
                image_sprite = getInfo(image,'sprite')
                image_h = getInfo(image,'h')
                image_w = getInfo(image,'w')
                image_y = getInfo(image,'y')
                image_x = getInfo(image,'x')
            #技能详细
            tooltip = spell.get('tooltip')
            leveltip = spell.get('leveltip')
            #技能等级说明
            # print "+"*100
            # print getInfo(leveltip, 'label')
            leveltip_labels = "<br/>".join(getInfo(leveltip, 'label'))
            leveltip_effects = "<br/>".join(getInfo(leveltip, 'effect'))
            #技能消耗
            resource = spell.get('resource')
            updataSqlSpells1 = "REPLACE INTO `ChampionSpells` (`champion_id`, `spellId`, `name`, `description`, `image_full`, `image_group`, `image_sprite`, `image_h`, `image_w`, `image_y`, `image_x`, `image_url`, `tooltip`, `leveltip_labels`, `leveltip_effects`, `resource`, `version`, `updated`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(championId, spellId, name, description.replace("\'","\""), image_full, image_group, image_sprite, image_h, image_w, image_y, image_x, image_url, tooltip.replace("\'","\""), leveltip_labels, leveltip_effects, resource, version, updated)
            print updataSqlSpells1
            cursor.execute(updataSqlSpells1)
            conn.commit()
        passive = dataM.get('passive')
        global s
        for i in passive:
            s.add(i)
        #技能物理名
        spellId = championKey + '_Passive'
        #技能伦理名
        name = passive.get('name')
        #技能描述
        description = passive.get('description')
        #技能图片信息
        image = passive.get('image')
        image_full = ""
        image_group = ""
        image_sprite = ""
        image_h = ""
        image_w = ""
        image_y = ""
        image_x = ""
        image_url = "http://ossweb-img.qq.com/images/lol/img/spell/%s.png"%spellId
        if image != None:
            image_full = image.get('full',"")
            image_group = getInfo(image,'group')
            image_sprite = getInfo(image,'sprite')
            image_h = getInfo(image,'h')
            image_w = getInfo(image,'w')
            image_y = getInfo(image,'y')
            image_x = getInfo(image,'x')
            image_url = "http://ossweb-img.qq.com/images/lol/img/passive/%s"%image_full
            
        updataSqlSpells2 = "REPLACE INTO `ChampionSpells` (`champion_id`, `spellId`, `name`, `description`, `image_full`, `image_group`, `image_sprite`, `image_h`, `image_w`, `image_y`, `image_x`, `image_url`, `version`, `updated`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(championId, spellId, name, description.replace("\'","\""), image_full, image_group, image_sprite, image_h, image_w, image_y, image_x, image_url, version, updated)
        print updataSqlSpells2
        cursor.execute(updataSqlSpells2)
        conn.commit()
    
        updataSql = "REPLACE INTO `ChampionInfo` (`id`, `attack`, `defense`, `magic`, `difficulty`, `version`, `updated`, `lore`, `blurb`, `allytips`, `enemytips`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(id, attack, defense, magic, difficulty, version, updated, lore, blurb, allytips, enemytips)
        print updataSql
        cursor.execute(updataSql)
        conn.commit()


        # for i in data:
        #     print i
    #     print '-'*30
    #     champion = datas['data']['data'][data]
    #     key = data
    #     print key
    #     name =  champion['name']
    #     title = champion['title']
    #     tags = ','.join(champion['tags'])
    #     no = champion['key']
    #     id = champion['id']
    #     image_full = champion['image']['full']
    #     image_group = champion['image']['group']
    #     image_sprite = champion['image']['sprite']
    #     image_h = champion['image']['h']
    #     image_w = champion['image']['w']
    #     image_y = champion['image']['y']
    #     image_x = champion['image']['x']

    #     # print "REPLACE INTO Champion (no,id,key,name,title,tags,image_full,image_group,image_sprite,image_h,image_w,image_y,image_x) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(no,id,key,name,title,tags,image_full,image_group,image_sprite,image_h,image_w,image_y,image_x)

    #     conn = get_conn()
    #     cursor = conn.cursor()
    #     updataSql = "REPLACE INTO Champion (no,id,`key`,name,title,tags,image_full,image_group,image_sprite,image_h,image_w,image_y,image_x) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(no,id,key,name,title,tags,image_full,image_group,image_sprite,image_h,image_w,image_y,image_x)
    #     print updataSql
    #     cursor.execute(updataSql)
    #     conn.commit()
# print url_list
# for data in url_list:
#     print data
# do('126', "Jayce")
conn = get_conn()
cursor = conn.cursor() 

selectSql = "select no,`key` from Champion"
cursor.execute(selectSql)
results = cursor.fetchall()
s = set()
for result in results:
    print str(result[0]) + '\t' + result[1]
    do(str(result[0]), result[1])
# do('126', "Jayce")
print "*"*100
for x in s :
    print x
#     print "*"*100