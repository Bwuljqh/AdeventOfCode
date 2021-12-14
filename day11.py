# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 09:38:55 2021

@author: Admin
"""

from numpy import array, where

arround = [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]

f = open('InputDay11.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()]

octopi = array([[int(lines[x][y]) for y in range(10)] for x in range(10)])

def flash(x,y,table):
    table[x][y] = 0
    
    n = 0
    for xi,yi in arround: 
        if not (x + xi > 9 or y + yi > 9 or x+ xi == -1 or y + yi ==-1):
            if table[x + xi][y + yi] != 0:
                table[x + xi][y + yi] += 1
                if table[x + xi][y + yi] > 9:
                    n += flash(x + xi,y + yi,table)
    return n + 1

totf = 0
oldtot = 0
for i in range(1000):
    
    octopi += 1
    
    T = where(octopi == 10)
    
    flashes = [(T[0][a],T[1][a]) for a in range(len(T[0]))]
    
    for o in flashes:
        if octopi[o[0]][o[1]] == 10:
            totf += flash(o[0],o[1],octopi)
     
    if totf - oldtot == 100:
        print(i+1)
        break;
    # n = 0
    # for l in octopi:
    #     if not(all(l == array([0]*10))):
    #         break;
    #     n += 1
    
    # if n == 10:
    #    print(i+1)
    #    print(octopi)
    #    break;
    oldtot = totf