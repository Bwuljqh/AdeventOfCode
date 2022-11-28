# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 08:38:38 2021

@author: Admin
"""

from copy import deepcopy
import numpy as np

f = open('InputDay12.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()]

# class link():
#     def __init__(this, nodeA,nodeB):
#         this.nodeA = nodeA
#         this.nodeB = nodeB
#         return
    
    
# class cave():
#     def __init__(this, name):
#         this.name = name
#         return




nodes = {}
for i in lines:
    I = i.split('-')
    if I[0] in nodes:    
        nodes[I[0]].append(I[1])
    else:
        nodes[I[0]] = []
        nodes[I[0]].append(I[1])
        
    if I[1] in nodes:    
        nodes[I[1]].append(I[0])
    else:
        nodes[I[1]] = []
        nodes[I[1]].append(I[0])

p = []

def parkour(node, parcours,dup):
    parcours.append(node)
    if node == 'end':
    
        p.append(parcours)
    else:
        n=0
        for i in nodes[node]:
            if i != 'start':
                if i.islower() and i in parcours and dup == False:
                    parkour(i,deepcopy(parcours), True)
                elif (i.isupper() or i not in parcours):
                    n += 1
                    parkour(i,deepcopy(parcours),dup)
        if n==0:
            return 'Fail'


p.append(parkour('start',[],False))
p = p[:-1]
print(len(p))

new_array = [tuple(row) for row in p]
uniques = np.unique(new_array)

print(len(uniques))