# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:19:37 2021

@author: Admin
"""

# This i not working, I used someone else's alogrithm to solce the second part because I couldn't get it to work faster
# I'm not used to implementing this sort of algorithms and I spent multiple hours on it. Let's hope that I will be able
# To di it next time

from numpy import array,concatenate,where,Inf

directions = {'N':(-1,0,'S'),'S':(1,0,'N'),'E':(0,1,'O'),'O':(0,-1,'E')}

f = open('InputDay15.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()]



row,col = 0,0

cave = array([[int(i) for i in y] for y in lines])

BigLineCave = concatenate((cave,(cave+1)%10,(cave+2)%10,(cave+3)%10,(cave+4)%10),1)
BigCave = concatenate((BigLineCave,(BigLineCave+1)%10,(BigLineCave+2)%10,(BigLineCave+3)%10,(BigLineCave+4)%10),0)

# sGrid = [[0 for i in range(100)]for j in range(100)]
# test = [[0 for i in range(100)]for j in range(100)]

# def wayRecur(row,col,S):
#     S += cave[row][col]
#     if row == 99 and col == 99:
#         risks.append(S)
#     else:
#         if row != 99:
#             return
#         if col != 99:
#             wayRecur(row,col+1,S)



l = cave


visits = [[False for i in range(len(l[0]))] for j in range(len(l))]

ways = {(1,0):BigCave[1][0],(0,1):BigCave[0][1]}
visits[0][0] = True
while True:
    
    p = min(ways, key=ways.get)
    n = Inf
    for i in ways.keys():
        if not(visits[i[0]][i[1]]) and ways[i] < n:
            n = ways[i]
            p = i
    
    
    
    
    row = p[0]
    col = p[1]
    
    if row == len(l) - 1 and col == len(l[0]) - 1:
        print(ways[p])
        break
    
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    
    if row == 0:
        d.remove((-1,0))
        
    if row == len(l) - 1:
        d.remove((1,0))
        
    if col == 0:
        d.remove((0,-1))
        
    if col == len(l[0]) - 1:
        d.remove((0,1))
        
    for i in d:
        if (row + i[0],col+i[1]) not in visits:
            
            ways[(row + i[0], col + i[1])] = ways[p] + BigCave[row + i[0]][col + i[1]]
            visits[row + i[0]][col + i[1]] = True
    del ways[p]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        