# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 16:55:12 2014

@author: akshay
"""
from math import sqrt

def akshay(j, c):
    if j % 2 == 0:
        return None
    for k in xrange(1, int(sqrt(c))+ 1, 2):
         if j == k:
             continue
         if j % k == 0 and j/k != j:
              return None
         
    return j
a = int(raw_input())
for i in xrange(a):
    b,c = map(int, raw_input().split(' '))
    for j in xrange(b,c+1):
        z = akshay(j, c)
        if z == None or z == 1:
            pass
        else:
            print z