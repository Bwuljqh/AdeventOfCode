# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:42:38 2021

@author: Admin
"""

f = open('InputDay13.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()]

n = lines.index('')

points = [[int(i.split(',')[0]),int(i.split(',')[1])] for i in lines[:n]]
instructions = [[i.split('=')[0][-1],int(i.split('=')[1])] for i in lines[n+1:]]

for I in instructions:
    if I[0] == 'x':
        for p in points:
            if p[0] > I[1]:
                p[0] = p[0] - ((p[0]-I[1])*2)
    elif I[0] == 'y':
        for p in points:
            if p[1] > I[1]:
                p[1] = p[1] - ((p[1]-I[1])*2)

r = []
for i in points:
    if i not in r:
        r.append(i)
        
print(len(r))

m = [' '*40 for y in range(10)]

for j in r:

    l = list(m[j[1]])
    l[j[0]] = '#'
    m[j[1]] = "".join(l)
