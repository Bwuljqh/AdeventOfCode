# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:00:01 2021

@author: Admin
"""

import numpy as np

f = open('InputDay3.txt','r')
lines = f.readlines()

linesCleaned = []
for i in lines:
    I = i.split('\n')
    linesCleaned.append(I[0])
    
def listRemover(criteria, listR, pos):
    if len(listR) == 1:
        return listR
    elif len(listR) == 0:
        return 'wtf bro'
    else :
        if pos >= len(listR[0]):
            pos = 0
        else : 
            pos += 1
            
        number = 0
        
        list1 = []
        list0 = []
        resutl = []
        
        for y in listR:
            if y[pos] == '0':
                number -= 1
                list0.append(y)
            else:
                number += 1
                list1.append(y)
        
        if number == 0:
            if criteria == 'least':
                result = list0
            elif criteria == 'most':
                result = list1
        elif abs(number)/number == 1:
            if criteria == 'least':
                result = list0
            elif criteria == 'most':
                result = list1
        elif abs(number)/number == -1:
            if criteria == 'least':
                result = list1
            elif criteria == 'most':
                result = list0
            
        return listRemover(criteria, result, pos)
    
a = listRemover('least',linesCleaned,-1)[0]
b =listRemover('most',linesCleaned,-1)[0]


print(int('0b' + a,2) * int('0b' + b,2))
# results = [0,0,0,0,0,0,0,0,0,0,0,0]

# for i in lines:
#     I = i.split('\n')
#     for j in range(len(I[0])):
#         if int(I[0][j]):
#             results[j] += 1

# a = np.array(results)//500
# b = abs(a - 1)

# bina = ''.join(map(str,a))
# binb = ''.join(map(str,b))

# print(int('0b' + bina,2) * int('0b' + binb,2))