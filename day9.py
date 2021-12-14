# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:41:03 2021

@author: Admin
"""

f = open('InputDay9.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()]

temp = ['9'*len(lines[0])] + lines + ['9'*len(lines[0])]

heightmap = [ '9' + x + '9' for x in temp]

risk = 0

coord = []
for x in range(len(heightmap) - 2):
        
    for y in range(len(heightmap[0]) - 2):
        
        up = int(heightmap[x][y+1])

        left = int(heightmap[x+1][y])

        down = int(heightmap[x+2][y+1])

        right = int(heightmap[x+1][y+2])
        
        i = int(heightmap[x+1][y+1])
        
        if i < up and i < left and i < down and i < right:
            risk += i + 1
            coord.append((x+1,y+1))
            
        # if i == 0:
        #     up = 9
        # else:
        #     up = int(lines[i][x+1])
        # if x == 0:
        #     left = 9
        # else:
        #     left = int(lines[i+1][x])
        # if i == len(lines) - 1:
        #     down = 9
        # else:
        #     down = int(lines[i+2][x+1])
        # if x == len(lines[0]) - 1:
        #     right = 9
        # else:
        #     right = int(lines[i+1][x+2])
        


checks = [[ 0 for y in range(len(heightmap[0]))] for x in range(len(heightmap))]

def checkBassin(x,y,checks):
    checks[x][y] = 1

    n = 0
    if heightmap[x+1][y] != '9' and checks[x+1][y] == 0:
        checks[x+1][y] = 1
        n += checkBassin(x+1,y,checks)

    if heightmap[x-1][y] != '9' and checks[x-1][y] == 0:
        checks[x-1][y] = 1
        n += checkBassin(x-1,y,checks)

    if heightmap[x][y+1] != '9' and checks[x][y+1] == 0:
        checks[x][y+1] = 1
        n += checkBassin(x,y+1,checks)

    if heightmap[x][y-1] != '9' and checks[x][y-1] == 0:
        checks[x][y-1] = 1
        n += checkBassin(x,y-1,checks)
        
    return n+1

max3 = [0,0,0]

for i in coord:
    checks =  [[ 0 for y in range(len(heightmap[0]))] for x in range(len(heightmap))]
    r = checkBassin(i[0],i[1],checks)
    if r > max3[0]:
        max3[2] = max3[1]
        max3[1] = max3[0]
        max3[0] = r
    elif r > max3[1]:
        max3[2] = max3[1]
        max3[1] = r
    elif r > max3[2]:
        max3[2] = r

print(max3[0] * max3[1] * max3[2])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    