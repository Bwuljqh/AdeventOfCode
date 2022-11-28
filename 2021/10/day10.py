# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:07:04 2021

@author: Admin
"""

from collections import Counter
import statistics

cost = {')':3,']':57,'}':1197,'>':25137}
cost2 = {'(':1,'[':2,'{':3,'<':4}
inverse = [('(',')'),('[',']'),('{','}'),('<','>')]

f = open('InputDay10.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()]

linesDict = []

corruptedSymbols = []

total = []

for x in lines:
    corrupted = False
    temp = []
    symbols = {'(':0,'[':0,'{':0,'<':0}
    for y in x:
        if y in symbols.keys():
            symbols[y] += 1
            temp.append(y)
        else:
            closingSymbol = ()
            for i in inverse:
                if y == i[1]:
                    closingSymbol = i
                    break
            if temp[-1] != closingSymbol[0]:
                corruptedSymbols.append(y)
                corrupted = True
                break
            else:
                symbols[closingSymbol[0]] -= 1
                temp.pop()
    linesDict.append(symbols)
    
    
    
    if corrupted == False:
        n=0
        for i in temp[::-1]:
            n *= 5
            n += cost2[i]
    
    
        total.append(n)
a = Counter(corruptedSymbols)

n = 0

for k,v in a.items():
    print((k,v))
    n += cost[k]*v
    
print(n)

print(statistics.median(total))
