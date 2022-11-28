# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 08:28:22 2021

@author: Admin
"""

from numpy import zeros


f = open('InputDay5.txt','r')
lines = f.readlines()

cLines = []
for i in lines:
    
    I = i.split('\n')
    F,L = I[0].split(' -> ')
    
    temp = [[],[]]
    
    sF = F.split(',')
    sL = L.split(',')
    
    temp[0].append(int(sF[0]))
    temp[0].append(int(sF[1]))
    
    temp[1].append(int(sL[0]))
    temp[1].append(int(sL[1]))
    
    cLines.append(temp)
    
grid1 = zeros((1000,1000))

grid2 = zeros((1000,1000))

cross = 0

for i in cLines:
    # print(i)
    if i[0][0] == i[1][0]:
        # print(f' ici, {i[0][0]} = {i[1][0]}')
        if i[0][1] > i[1][1]:
            # print(f' et {i[0][1]} > {i[1][1]}')
            num = i[0][1]
            while num != i[1][1] -1:
                grid1[i[0][0]][num] += 1
                if grid1[i[0][0]][num] == 2:
                    cross += 1
                num -= 1
        elif i[1][1] > i[0][1]:
            # print(f' et {i[1][1]} > {i[0][1]}')
            num = i[1][1]
            while num != i[0][1] - 1:
                grid1[i[0][0]][num] += 1
                if grid1[i[0][0]][num] == 2:
                    cross += 1
                num -= 1
    elif i[0][1] == i[1][1]:
        # print(f' ici, {i[0][1]} = {i[1][1]}')
        if i[0][0] > i[1][0]:
            # print(f' et {i[0][0]} > {i[1][0]}')
            num = i[0][0]
            while num != i[1][0] - 1:
                grid1[num][i[1][1]] += 1
                if grid1[num][i[1][1]] == 2:
                    cross += 1
                num -= 1
        elif i[1][0] > i[0][0]:
            # print(f' et {i[1][0]} > {i[0][0]}')
            num = i[1][0]
            while num != i[0][0] - 1:
                
                grid1[num][i[1][1]] += 1
                if grid1[num][i[1][1]] == 2:
                    cross += 1
                num -= 1 
    else:
        d1 = int(abs(i[1][0] - i[0][0])/(i[1][0] - i[0][0]))
        d2 = int(abs(i[1][1] - i[0][1])/(i[1][1] - i[0][1]))
        p1 = i[0][0]
        p2 = i[0][1]
       
        grid1[p1][p2] += 1
        if grid1[p1][p2] == 2:
            cross += 1
        while p1 != i[1][0]:
            p1 += d1
            p2 += d2
            grid1[p1][p2] += 1
            if grid1[p1][p2] == 2:
                cross += 1
            
            
# Not working                         
# for i in cLines:
#     if i[0][0] == i[1][0]:
        
#         treat = 1
#         l=0
#         c=1
#         if i[0][c] > i[1][c]:
#             j=0
#             k=1
            
#         elif i[1][c] > i[0][c]:
#             j=1
#             k=0

#     elif i[0][1] == i[1][1]:
        
#         treat = 1
#         l=0
#         c=1
#         if i[0][c] > i[1][l]:
#             j=0
#             k=1

#         elif i[1][c] > i[0][l]:
#             j=1
#             k=0
     
#     if treat == 1:
        
#         num = i[j][c]
#         while num != i[k][c]:
#             grid2[i[l][l]][num] += 1
#             if grid2[i[l][l]][num] == 2:
#                 cross += 1
#             num -= 1
#         treat = 0

