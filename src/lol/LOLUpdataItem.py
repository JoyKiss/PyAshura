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
import re
response = requests.get("http://lol.qq.com/biz/hero/item.js")
# html = etree.HTML(response.content)
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='111111', db='lol', charset='utf8')
    return conn
def getInfo(mapInfo,key):
    if len(mapInfo) == 0:
        return ""
    return mapInfo.get(key,"")
# print response.text
js = response.text
fun = """
            function run(){
                %s;
                return LOLitemjs;
            }
        """ % js  # 构造函数调用产生pages变量结果
pages = execjs.compile(fun).call('run')
std_data = "{'data':%s}"%pages
datas = ast.literal_eval(std_data)
print '-'*30
# print datas['data']
for data in datas['data']:
    print data
print '-'*30
data = datas['data']['data']
# print data
print '-'*30
b = set()
s = set()
# print len(data)
version = datas['data']['version']
updated = datas['data']['updated']
conn = get_conn()
cursor = conn.cursor()
for item in data:
    # print data[item] 
    id = item
    #装备来源
    fromP = ",".join(data[item].get('from',""))
    #名称
    name = data[item].get('name',"")

    gold = data[item].get('gold')
    #售价
    gold_sell = ""
    #合计总价
    gold_total = ""
    #合成价格
    gold_base = ""
    #是否可买
    gold_purchasable = ""
    if gold != None:
        #售价
        gold_sell = gold.get('sell',"")
        #合计总价
        gold_total = gold.get('total',"")
        #合成价格
        gold_base = gold.get('base',"")
        #是否可买
        gold_purchasable = gold.get('purchasable',"")

    #
    tags = ",".join(data[item]['tags'])
    #装备说明
    plaintext = data[item].get('plaintext',"")

    #图片信息
    image = data[item].get('image')
    image_full = ""
    image_group = ""
    image_sprite = ""
    image_h = ""
    image_w = ""
    image_y = ""
    image_x = ""
    image_url = "http://ossweb-img.qq.com/images/lol/img/item/%s.png"%id
    if image != None:
        image_full = image.get('full',"")
        image_group = getInfo(image,'group')
        image_sprite = getInfo(image,'sprite')
        image_h = getInfo(image,'h')
        image_w = getInfo(image,'w')
        image_y = getInfo(image,'y')
        image_x = getInfo(image,'x')

    #效果
    effect = data[item].get('effect')
    effect_Effect10Amount = ""
    effect_Effect11Amount = ""
    effect_Effect12Amount = ""
    effect_Effect13Amount = ""
    effect_Effect14Amount = ""
    effect_Effect15Amount = ""
    effect_Effect16Amount = ""
    effect_Effect17Amount = ""
    effect_Effect18Amount = ""
    effect_Effect19Amount = ""
    effect_Effect1Amount = ""
    effect_Effect2Amount = ""
    effect_Effect3Amount = ""
    effect_Effect4Amount = ""
    effect_Effect5Amount = ""
    effect_Effect6Amount = ""
    effect_Effect7Amount = ""
    effect_Effect8Amount = ""
    effect_Effect9Amount = ""
    if effect != None:
        effect_Effect10Amount = getInfo(effect, "Effect10Amount")
        effect_Effect11Amount = getInfo(effect, "Effect11Amount")
        effect_Effect12Amount = getInfo(effect, "Effect12Amount")
        effect_Effect13Amount = getInfo(effect, "Effect13Amount")
        effect_Effect14Amount = getInfo(effect, "Effect14Amount")
        effect_Effect15Amount = getInfo(effect, "Effect15Amount")
        effect_Effect16Amount = getInfo(effect, "Effect16Amount")
        effect_Effect17Amount = getInfo(effect, "Effect17Amount")
        effect_Effect18Amount = getInfo(effect, "Effect18Amount")
        effect_Effect19Amount = getInfo(effect, "Effect19Amount")
        effect_Effect1Amount = getInfo(effect, "Effect1Amount")
        effect_Effect2Amount = getInfo(effect, "Effect2Amount")
        effect_Effect3Amount = getInfo(effect, "Effect3Amount")
        effect_Effect4Amount = getInfo(effect, "Effect4Amount")
        effect_Effect5Amount = getInfo(effect, "Effect5Amount")
        effect_Effect6Amount = getInfo(effect, "Effect6Amount")
        effect_Effect7Amount = getInfo(effect, "Effect7Amount")
        effect_Effect8Amount = getInfo(effect, "Effect8Amount")
        effect_Effect9Amount = getInfo(effect, "Effect9Amount")

    #
    colloq = data[item].get('colloq',"")
    #消耗？？
    consumed = data[item].get('consumed',"")
    #消耗？？
    consumeOnFull = data[item].get('consumeOnFull',"")
    #
    info = ",".join(data[item].get('into',""))

    #
    stacks = data[item].get('stacks',"")
    #店内？？
    inStore = data[item].get('inStore',"")

    #合成Map
    maps = data[item].get('maps')
    maps_8 = ""
    maps_10 = ""
    maps_11 = ""
    maps_12 = ""
    maps_14 = ""
    maps_16 = ""
    maps_18 = ""
    maps_19 = ""
    if maps != None:
        maps_8 = getInfo(maps,'8')
        maps_10 = getInfo(maps,'10')
        maps_11 = getInfo(maps,'10')
        maps_12 = getInfo(maps,'10')
        maps_14 = getInfo(maps,'10')
        maps_16 = getInfo(maps,'10')
        maps_18 = getInfo(maps,'10')
        maps_19 = getInfo(maps,'10')
    #合成深度
    depth = data[item].get('depth',"")
    #专属装备
    requiredChampion = data[item].get('requiredChampion',"")
    #？？
    hideFromAll = data[item].get('hideFromAll',"")
    #升级提供者
    requiredAlly = data[item].get('requiredAlly',"")

    #统计
    stats = data[item].get('stats')
    stats_FlatMagicDamageMod = ""
    stats_PercentMovementSpeedMod = ""
    stats_FlatSpellBlockMod = ""
    stats_FlatArmorMod = ""
    stats_PercentLifeStealMod = ""
    stats_FlatMPPoolMod = ""
    stats_FlatPhysicalDamageMod = ""
    stats_FlatHPRegenMod = ""
    stats_FlatMovementSpeedMod = ""
    stats_FlatHPPoolMod = ""
    stats_PercentAttackSpeedMod = ""
    stats_FlatCritChanceMod = ""

    if stats != None:
        stats_FlatMagicDamageMod = getInfo(stats, "FlatMagicDamageMod")
        stats_PercentMovementSpeedMod = getInfo(stats, "PercentMovementSpeedMod")
        stats_FlatSpellBlockMod = getInfo(stats, "FlatSpellBlockMod")
        stats_FlatArmorMod = getInfo(stats, "FlatArmorMod")
        stats_PercentLifeStealMod = getInfo(stats, "PercentLifeStealMod")
        stats_FlatMPPoolMod = getInfo(stats, "FlatMPPoolMod")
        stats_FlatPhysicalDamageMod = getInfo(stats, "FlatPhysicalDamageMod")
        stats_FlatHPRegenMod = getInfo(stats, "FlatHPRegenMod")
        stats_FlatMovementSpeedMod = getInfo(stats, "FlatMovementSpeedMod")
        stats_FlatHPPoolMod = getInfo(stats, "FlatHPPoolMod")
        stats_PercentAttackSpeedMod = getInfo(stats, "PercentAttackSpeedMod")
        stats_FlatCritChanceMod = getInfo(stats, "FlatCritChanceMod")

    #专属合成
    specialRecipe = data[item].get('specialRecipe',"")
    #描述
    description = data[item].get('description',"")
    updataSql = "REPLACE INTO `ItemInfo` (`id`, `from`, `name`, `gold_sell`, `gold_total`, `gold_base`, `gold_purchasable`, `tags`, `plaintext`, `image_full`, `image_group`, `image_sprite`, `image_h`, `image_w`, `image_y`, `image_x`, `image_url`, `effect_Effect1Amount`, `effect_Effect2Amount`, `effect_Effect3Amount`, `effect_Effect4Amount`, `effect_Effect5Amount`, `effect_Effect6Amount`, `effect_Effect7Amount`, `effect_Effect8Amount`, `effect_Effect9Amount`, `effect_Effect10Amount`, `effect_Effect11Amount`, `effect_Effect12Amount`, `effect_Effect13Amount`, `effect_Effect14Amount`, `effect_Effect15Amount`, `effect_Effect16Amount`, `effect_Effect17Amount`, `effect_Effect18Amount`, `effect_Effect19Amount`, `colloq`, `consumed`, `consumeOnFull`, `info`, `stacks`, `inStore`, `maps_8`, `maps_10`, `maps_11`, `maps_12`, `maps_14`, `maps_16`, `maps_18`, `maps_19`, `depth`, `requiredChampion`, `hideFromAll`, `requiredAlly`, `stats_FlatMagicDamageMod`, `stats_PercentMovementSpeedMod`, `stats_FlatSpellBlockMod`, `stats_FlatArmorMod`, `stats_PercentLifeStealMod`, `stats_FlatMPPoolMod`, `stats_FlatPhysicalDamageMod`, `stats_FlatHPRegenMod`, `stats_FlatMovementSpeedMod`, `stats_FlatHPPoolMod`, `stats_PercentAttackSpeedMod`, `stats_FlatCritChanceMod`, `specialRecipe`, `description`, `version`, `updated`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"%(id, fromP, name, gold_sell, gold_total, gold_base, gold_purchasable, tags, plaintext, image_full, image_group, image_sprite, image_h, image_w, image_y, image_x, image_url, effect_Effect1Amount, effect_Effect2Amount, effect_Effect3Amount, effect_Effect4Amount, effect_Effect5Amount, effect_Effect6Amount, effect_Effect7Amount, effect_Effect8Amount, effect_Effect9Amount, effect_Effect10Amount, effect_Effect11Amount, effect_Effect12Amount, effect_Effect13Amount, effect_Effect14Amount, effect_Effect15Amount, effect_Effect16Amount, effect_Effect17Amount, effect_Effect18Amount, effect_Effect19Amount, colloq, consumed, consumeOnFull, info, stacks, inStore, maps_8, maps_10, maps_11, maps_12, maps_14, maps_16, maps_18, maps_19, depth, requiredChampion, hideFromAll, requiredAlly, stats_FlatMagicDamageMod, stats_PercentMovementSpeedMod, stats_FlatSpellBlockMod, stats_FlatArmorMod, stats_PercentLifeStealMod, stats_FlatMPPoolMod, stats_FlatPhysicalDamageMod, stats_FlatHPRegenMod, stats_FlatMovementSpeedMod, stats_FlatHPPoolMod, stats_PercentAttackSpeedMod, stats_FlatCritChanceMod, specialRecipe, description.replace('\'','\"'), version, updated)
    print updataSql
    cursor.execute(updataSql)
    conn.commit()


# conn = get_conn()
# cursor = conn.cursor()
# for key in datas['data']['keys']:
#     print '-'*30
#     print key
#     data = datas['data']['keys'][key]
#     heros = datas['data']['data'][data]
#     print heros
#     for hero in heros:
#         chromas = hero['chromas']
#         num = hero['num']
#         id = hero['id']
#         name = hero['name']
#         url = 'http://ossweb-img.qq.com/images/lol/appskin/%s.jpg'%id
#         bigurl = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big%s.jpg'%id
#         updataSql = "REPLACE INTO SkinInfo (champ_id,chromas,num,skin_id,name,url,bigurl,version,updated) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(key,chromas,num,id,name.replace('\'',"\""),url,bigurl,version,updated)
#         print updataSql
#         cursor.execute(updataSql)
#         conn.commit()