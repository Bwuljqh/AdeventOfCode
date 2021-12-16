# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:14:49 2021

@author: Admin
"""

import binascii

f = open('InputDay16.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()][0]


vSum = []


def hextobin(h):
  return bin(int(h, 16))[2:].zfill(len(h) * 4)

work = hextobin(lines)

def checkPacket(j):
    if j >= len(work):
        return (j, [])
    # print('j = ' + str(j))

    vSum.append(int(work[j:j+3],2))
    j += 3
    t = int(work[j:j+3],2)
    j += 3
    print('t = ' + str(t))
    if t != 4:
        I = work[j]
        # print('I:'+I)
        j += 1
        
        d = 0
        
        indice = 0
        v = []
        
        if I == '0':
            d = 15
            L = int(work[j:j+d],2)
            # print('L = ' + str(L))
            j += d
            c = j
            while c < j + L:

                (c,values) = checkPacket(c)
                v += values
            indice = j + L
        elif I == '1':
            d = 11
            L = int(work[j:j+d],2)
            # print('L= ' + str(L))
            j += d
            m = 0
            c = j
            while m != L:
                
                (c,values) = checkPacket(c)
                v += values
                m += 1
                # print('c= ' + str(c))
            indice = c
            
        print(f'v: {v}')
        print(f't: {t}')
        
        if t == 0:
            value = [sum(v)]
        elif t == 1:
            o = 1
            for i in v:
                o *= i
            value = [o]
        elif t == 2:
            value = [min(v)]
        elif t == 3:
            value = [max(v)]
        elif t == 5:
            if v[0] > v[1]:
                value =  [1]
            else:
                value = [0]
        elif t == 6:
            if v[0] < v[1]:
                value = [1]
            else:
                value = [0]
        elif t == 7:
            value = [int(v[0] == v[1])]
        return (indice, value)
        
    else:
        value = []
        st = ''
        print(st)
        print(j)
        while work[j] != '0':
            st += work[j+1:j+5]
            j += 5
        st += work[j+1:j+5]

        value.append(int(st,2))
        print('v' + str(value))

        return (j + 5,value)
    
print(checkPacket(0))
 
# while i < len(lines) - 1 :
    
#     j = 0
    
#     if code[i] == '0':
#         continue
    
#     work = bin(int(code[i], 16)).split('0b')[1]
#     i += 1
    
#     v = int(work[j:j+3],2)
#     j += 3

        
#     t = int(work[j:j+3],2)
#     j += 3
#     if t != 4:
#         I = work[j]
#         j += 1
        
#         d = 0
        
#         if I == '1':
#             d = 15
#         elif I == '0':
#             d = 11
            
#         while len(work) <= j + d:
#             work += bin(int(code[i], 16)).split('0b')[1]
#             i += 1 
        
#         L = int(work[j:j+d],2)
#         j += d
        
#         if I == '1':
#             while len(work) <= j + L:
#                 work += bin(int(code[i], 16)).split('0b')[1]
#                 i += 1 
#                 #Break down number here
#                 continue
        
    # else:
        
            