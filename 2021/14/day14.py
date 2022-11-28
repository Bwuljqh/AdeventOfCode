# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:59:58 2021

@author: Admin
"""

from copy import deepcopy
from collections import Counter

f = open('InputDay14.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()]

p = lines[0]
I = lines[2:]

Instructions = dict([(i.split(' -> ')[0],(i.split(' -> ')[0][0] + i.split(' -> ')[1],i.split(' -> ')[1] + i.split(' -> ')[0][1])) for i in I])
Polymer = [p[i] + p[i+1] for i in range(len(p)-1)]

Polymer = Counter(Polymer)

def clean(poly):
    temp = []
    for i in poly:
        if len(i) == 3:
            
            temp.append(i[0] + i[1])
            temp.append(i[1] + i[2])
        else:
            temp.append(i)
    return temp


for i in range(40):
    d = deepcopy(Polymer)

    for j in Polymer.keys():
        if j in Instructions.keys() and Polymer[j] != 0:

            n = Polymer[j]

            p1 = Instructions[j][0]
            p2 = Instructions[j][1]

            if p1 in d.keys():
                d[p1] += n
            else:
                d[p1] = n
                
            if p2 in d.keys():
                d[p2] += n
            else:
                d[p2] = n

            d[j] -= n

    Polymer = deepcopy(d)
    
# for i in range(40):
#     for j in range(len(Polymer)):
#         if Polymer[j] in Instructions.keys():
#             Polymer[j] = Instructions[Polymer[j]]
#     Polymer = clean(Polymer)

# tot = ''        
# for i in Polymer:
#     tot += i[0]
# tot += Polymer[-1][-1]
# dtot = Counter(tot)

# print(max(dtot.values()) - min(dtot.values()))

tot = {}

for i in Polymer.keys():
    if i[0] in tot:
        tot[i[0]] += Polymer[i]
    else:
        tot[i[0]] = Polymer[i]

tot[p[-1]] += 1

print(max(tot.values()) - min(tot.values()))





