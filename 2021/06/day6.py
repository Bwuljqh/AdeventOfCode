# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:11:08 2021

@author: Admin
"""

import numpy as np
import time

f = open('InputDay6.txt','r')
lines = f.readlines()


T = lines[0].split(",")

fish = np.array([int(x) for x in T])

simpleFish = [0,0,0,0,0,0,0,0,0]

for i in fish:
    simpleFish[i] += 1
    
start_time = time.time()

for i in range(256):
    newborn = simpleFish[0]
    simpleFish = simpleFish[1:] + [newborn]
    simpleFish[6] += newborn
    print(simpleFish)
# history = [len(fish)]

# for i in range(80):
#     fish -= 1
#     history.append(len(fish))
#     i = np.where( fish == -1)
#     fish[i[0]] = 6
#     fish = np.append(fish,len(i[0])*[8])

            
# def evolution(f, day, daytogo):
#     day += 1
#     f -= 1
#     if f == -1:
#          return evolution(6,day,daytogo) + evolution(8,day,daytogo)
#     return evolution(6,day,daytogo)

# fishes = len(fish)
# moreFish = 0

# for i in fish:
#     moreFish += evolution(i,0,80)

print("--- %s seconds ---" % (time.time() - start_time))            
            
            
            
# for i in range(80):
#     fish -= 1

#     for f in range(len(fish)):
        
#         if fish[f] == -1:
#             fish[f] = 6
#             fish = np.append(fish, 8)
            