# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:19:37 2021

@author: Admin
"""

# This i not working, I used someone else's alogrithm to solce the second part because I couldn't get it to work faster
# I'm not used to implementing this sort of algorithms and I spent multiple hours on it. Let's hope that I will be able
# To di it next time

from numpy import array,concatenate,where

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

ways = {(1,0,'N'):BigCave[1][0],(0,1,'O'):BigCave[0][1]}
visited = []
while True:
    p = min(ways, key=ways.get)
    
    row = p[0]
    col = p[1]
    
    if row == len(l) - 1 and col == len(l[0]) - 1:
        print(ways[p])
        break
    
    d = ['S','E','N','O']
    
    if row == 0:
        d.remove('N')
        
    if row == len(l) - 1:
        d.remove('S')
        
    if col == 0:
        d.remove('O')
        
    if col == len(l[0]) - 1:
        d.remove('E')
        
    if p[2] in d:
        d.remove(p[2])
        
    for i in d:
        nav = directions[i]
        if (row + nav[0],col+nav[1]) not in visited:
            ways[(row + nav[0], col + nav[1], nav[2])] = ways[p] + BigCave[row + nav[0]][col + nav[1]]
            visited.append((row + nav[0],col+nav[1]))
    del ways[p]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        