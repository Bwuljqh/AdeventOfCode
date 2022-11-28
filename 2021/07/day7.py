# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 07:58:23 2021

@author: Admin
"""

from numpy import array

f = open('InputDay7.txt','r')
lines = [x.split('\n')[0] for x in f.readlines()]
    
crabs = [int(x) for x in lines[0].split(',')]

mean = sum(crabs)/len(crabs)
aCrabs = array(crabs)

l = []
for i in range(1736):
    x = 0 + i
    temp = abs(aCrabs -x)
    result = (temp * (temp+1))/2
    l.append(sum(result))

print(min(l))