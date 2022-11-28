# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:24:21 2021

@author: Admin
"""

f = open('InputDay2.txt','r')
lines = f.readlines()

horizontal = 0
depth = 0
aim = 0

for i in lines:
    I = i[:-1].split(' ')
    instruction = I[0]
    if instruction == 'forward':
        horizontal += int(I[1]) 
        depth += aim*int(I[1])
    elif instruction == 'down':
        aim += int(I[1])
    elif instruction == 'up':
        aim -= int(I[1])
   
print(horizontal*depth)

# horizontal = 0
# depth = 0

# for i in lines:
#     I = i[:-1].split(' ')
#     instruction = I[0]
#     if instruction == 'forward':
#         horizontal += int(I[1])  
#     elif instruction == 'down':
#         depth += int(I[1])
#     elif instruction == 'up':
#         depth -= int(I[1])
   
# print(horizontal*depth)
        
            
        