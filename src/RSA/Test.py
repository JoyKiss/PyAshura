#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-02 14:34:28


import os

import sys
reload(sys)

sys.setdefaultencoding('utf-8')
import random
 
def gcd(a, b):
   if a < b:
     a, b = b, a
   while b != 0:
     temp = a % b
     a = b
     b = temp
   return a
 
def getpq(n,e,d):
    p = 1
    q = 1
    while p==1 and q==1:
        k = d * e - 1
        g = random.randint ( 0 , n )
        while p==1 and q==1 and k % 2 == 0:
            k /= 2
            y = pow(g,k,n)
            if y!=1 and gcd(y-1,n)>1:
                p = gcd(y-1,n)
                q = n/p
    return p,q
 
def main():
    n = 0xa66791dc6988168de7ab77419bb7fb0c001c62710270075142942e19a8d8c51d053b3e3782a1de5dc5af4ebe99468170114a1dfe67cdc9a9af55d655620bbab
    e = 0x10001
    d = 0x123c5b61ba36edb1d3679904199a89ea80c09b9122e1400c09adcf7784676d01d23356a7d44d6bd8bd50e94bfc723fa87d8862b75177691c11d757692df8881

    p,q = getpq(n,e,d)
    print hex(p),hex(q)
 
if __name__ == '__main__':
    main()
 
'''
ex1:
n=25777,e=3,d=16971
p=149,q=173
ex2:
n = 0xa66791dc6988168de7ab77419bb7fb0c001c62710270075142942e19a8d8c51d053b3e3782a1de5dc5af4ebe99468170114a1dfe67cdc9a9af55d655620bbab
e = 0x10001
d = 0x123c5b61ba36edb1d3679904199a89ea80c09b9122e1400c09adcf7784676d01d23356a7d44d6bd8bd50e94bfc723fa87d8862b75177691c11d757692df8881
p = 0x335e8408866b0fd38dc7002d3f972c67389a65d5d8306566d5c4f2a5aa52628b
q = 0x33d48445c859e52340de704bcdda065fbb4058d740bd1d67d29e9c146c11cf61
'''