# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:26:36 2021

@author: Admin
"""
from os import path
ROOTDIR = path.dirname(__file__)
f = open(path.join(ROOTDIR, 'InputDay1.txt'),'r')
lines = f.readlines()


linesB = []

for i in range(len(lines)-2): 
    linesB.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))


n = 0;
for i in range(len(linesB)-1):
    if int(linesB[i+1]) > int(linesB[i]):
        n += 1
print(n)

# n = 0;
# for i in range(len(lines)-4): 
#     if int(lines[i+4]) > int(lines[i]):
#         n += 1
# print(n)


# n = 0;
# for i in range(len(lines)-1):
#     if int(lines[i+1]) >= int(lines[i]):
#         n += 1
#     else:
#         print(f'first: {lines[i]} second: {lines[i+1]} difference: {int(lines[1+i]) - int(lines[i])}')
# print(n)