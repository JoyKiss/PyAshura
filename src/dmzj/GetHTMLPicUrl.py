#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-11 09:09:35


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')


import requests
import json
from lxml import etree
import execjs
import os
import click

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Referer': 'http://www.dmzj.com/category'
}

PREIX = 'http://images.dmzj.com/'


def get_request(href):
    response = requests.get(href, headers=headers)
    html = etree.HTML(response.content)
    script_content = html.xpath('//script[1]/text()')[0]

    vars = script_content.strip().split('\n')
    
    parse_str = vars[2].strip()  # 取到eval()
    # print parse_str
    # parse_str = parse_str.replace('function(p,a,c,k,e,d)', 'function fun(p, a, c, k, e, d)')

    # parse_str = parse_str.replace('eval(', '')[:-1]  # 去除eval
    print "*"*10
    print parse_str
    fun = """
            function run(){
              var arr_img = new Array();
                var page = '';
                 %s;
                return pages;
            }
        """ % parse_str  # 构造函数调用产生pages变量结果
    print fun
    pages = execjs.compile(fun).call('run')
    url_list = []       
    if 'shtml' in response.request.url:
        datas = pages.split('=')[2][1:-2]  # json数据块 var pages=pages=[]
        url_list = json.JSONDecoder().decode(datas)  # 解码json数据
    elif 'html' in response.request.url:
        print "*"*10
        print pages
        print "*"*10
        datas = pages.replace('\r\n',',')  # var pages={}
        print datas
        print 3
        url_list = json.JSONDecoder().decode(datas)['page_url'].split(',')
    for url in url_list:
        print "https://images.dmzj.com/" + url.decode("utf-8")
        host = "https://images.dmzj.com/"
    headers['Referer'] = href
    if not os.path.exists('./downloads'):
        os.mkdir('./downloads')
    for index, url in enumerate(url_list):
        img = requests.get(PREIX + url, headers=headers)
        import time
        time.sleep(1)  # 等待一些时间，防止请求过快
        click.echo(PREIX + url)
        with open('./downloads/%s.jpg' % index, mode='wb') as fp:
            fp.write(img.content)
        click.echo('save %s.jpg' % index)
    click.echo('complete!')


url = "https://www.dmzj.com/view/aiqinggushibuhaoshuo/76013.html"
get_request(url)