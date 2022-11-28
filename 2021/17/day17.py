# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:55:19 2021

@author: Admin
"""

from numpy import sqrt

f = open('InputDay17.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()][0]
x,y = lines.split(': ')[1].split(', ')

ax1,ax2 = x.split('x=')[1].split('..')
ax1 = int(ax1)
ax2 = int(ax2)
ay2, ay1  = y.split('y=')[1].split('..')
ay1 = int(ay1)
ay2 = int(ay2)

def inArea(px0,py0,vx0,vy0,ay1,ay2,ax1,ax2):
    
    if inAreax(px0,vx0,ax1,ax2) and inAreay(py0,vy0,ay1,ay2):
        return True
    return False
    
    return
def step(coordsTuple,SpeedTuple):
   return
    
def Pyn(py0,vy0,n):
    return n*vy0 - n*(n-1)/2 + py0
    
def Pxn(px0,vx0,n): 
   if n >= vx0:
       return (vx0*(vx0+1))/2 + px0
   else:
       return ((vx0*(vx0+1))/2) - ((vx0-n)*((vx0-n)+1))/2 + px0

def Vxn(vx0,n):
    if n >= abs(vx0):
        return 0
    else:
        if vx0 <= 0:
            return vx0 + n
        else :
            return vx0 - n

def Vyn(vy0,n):
    return vy0 - n

global ymax 
def inAreay(py0,vy0,ay1,ay2):

    nup = False
    n=0
    while Vyn(vy0,n) >= 0 :
        ty = Pyn(py0,vy0,n)
        if ty <= ay1 and  ty >= ay2:
            nup = n
        n += 1
    while Pyn(py0,vy0,n) >= ay2:
        if Pyn(py0,vy0,n) <= ay1:
            ymax = 0
            if n == 13:
                ymax = vy0
                print(vy0)
            return (True,n)
        n += 1
    return False
    
def inAreax(px0,vx0,ax1,ax2):
    n=0
    while Vxn(vx0,n) != 0:
        tx = Pxn(px0,vx0,n)
        if tx >= ax1 and tx <= ax2:
            return (True,n)
        n += 1
    return

# maxn = 0
# speedsx = []
# for i in range(200):
#     p = inAreax(0,i,155,182)
#     if inAreax(0,i,155,182):
#         speedsx.append(i)
#         if maxn < p[1]:
#             print(i)
#             maxn = p[1]
        
tspeedsx = {}
for i in range(-200,200):
    tspeedsx[i] = []
    for n in range(200):
        tx = Pxn(0,i,n)
        if tx <= ax2 and tx >= ax1:
            tspeedsx[i].append(n)
        elif tx > ax2:
            break
        
speedsx = {}     
for i in tspeedsx.keys():
    if tspeedsx[i] != []:
        speedsx[i] = tspeedsx[i]

tspeedsy = {}
for i in speedsx.keys():
    tspeedsy[i] = []
    for j in speedsx[i]:
        for v in range(-200,5000):
            ty = Pyn(0,v,j)
            if ty >= ay2 and ty <= ay1:
                tspeedsy[i].append(v)

speeds = {}     
for i in tspeedsy.keys():
    if tspeedsy[i] != []:
        speeds[i] = tspeedsy[i]
    

ymax = 0
for i in speeds.keys():
    for j in speeds[i]:
        if j <= 0:
            continue
        elif Pyn(0,j,j) >= ymax:
            ymax = Pyn(0,j,j)

print(ymax)
    
    
    
    
    
    
    
    
    
    
    