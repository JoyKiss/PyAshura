#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-02 13:58:36


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
pub_key="116413621980381519652653352305998782383115356219159711473034578060959775431289847243587787983313650282129518539092542505917696635739835055497628359024925256367296895821044308069933001083812918579280335373930779321114796803717487523220789853087043432522259241883118343456964070633828502709753689226014250017266"# ===>新浪微博的公钥模数，抓包而来

# 从little-endian格式的数据缓冲data中解析公钥模数并构建公钥
def populate_public_key(data):
    # convert bytes to integer with int.from_bytes
    # 指定从little格式将bytes转换为int，一句话就得到了公钥模数，省了多少事
    n = int(data,16)
    e = 65537

    # 使用(e, n)初始化RSAPublicNumbers，并通过public_key方法得到公钥
    # construct key with parameter (e, n)
    key = rsa.RSAPublicNumbers(e, n).public_key(default_backend())

    return key


# 将公钥以PEM格式保存到文件中
def save_pub_key(pub_key, pem_name):
    # 将公钥编码为PEM格式的数据
    pem = pub_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # print(pem)

    # 将PEM个数的数据写入文本文件中
    with open(pem_name, 'w+') as f:
        f.writelines(pem.decode())

    return

if __name__ == '__main__':
        pub_key = populate_public_key(data=pub_key)
        pem_file = r'pub_key.pem'
        save_pub_key(pub_key, pem_file)