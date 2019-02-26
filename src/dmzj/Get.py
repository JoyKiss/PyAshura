# -*- coding: UTF-8 -*-
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
    try:
        html = etree.HTML(response.content)
        script_content = html.xpath('//script[1]/text()')[0]

        vars = script_content.strip().split('\n')
        
        parse_str = vars[2].strip()  # 取到eval()
        print parse_str
        parse_str = parse_str.replace('function(p,a,c,k,e,d)', 'function fun(p, a, c, k, e, d)')

        parse_str = parse_str.replace('eval(', '')[:-1]  # 去除eval
        
        fun = """
                function run(){
                    var arr_img = new Array();
                    var page = '';
                    var result = %s;
                    return result;
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
            datas = pages.split('=')[1][1:-2]  # var pages={}
            print 3
            # url_list = json.JSONDecoder().decode(datas)['page_url'].split('\r\n')
        for url in url_list:
            print "https://images.dmzj.com/" + url.decode("utf-8")
            host = "https://images.dmzj.com/"
        headers['Referer'] = info['href']
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
    except Exception as e:
        raise e

if __name__ == '__main__':


    info = { "title": "妹妹消失的第一百天-46话", "href": "https://manhua.dmzj.com/lingnengbaifenbai/64296.shtml"} 
    # 以第一页请求为例子
    get_request("https://manhua.dmzj.com/luomandike/67504.shtml")
    # get_request("https://www.dmzj.com/view/aiqinggushibuhaoshuo/76013.html")
