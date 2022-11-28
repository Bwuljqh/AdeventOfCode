# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:01:28 2021

@author: Admin
"""

sizes = [6,2,5,5,4,5,6,3,7,6]
alphabet = 'abcdefg'

f = open('InputDay8.txt','r')
temp = [x.split('\n')[0]for x in f.readlines()]
lines = [x.split('|')for x in temp]
I =  [lines[x][0].split(' ') for x in range(len(lines))]
Oold = [lines[x][1].split(' ')[1:] for x in range(len(lines))]

O = []
for i in Oold:
    temp =[]
    for x in i:
        x = "".join(sorted(x))
        temp.append(x)
    O.append(temp)
decrypt = []

for i in I:
    digits = [""]*7
    numbers = [""]*10
    len6 = []
    len5 = []
    for x in i:
        if len(x) == 2:
            numbers[1] = "".join(sorted(x))
        elif len(x) == 3:
            numbers[7] = "".join(sorted(x))
        elif len(x) == 4:
            numbers[4] = "".join(sorted(x))
        elif len(x) == 6:
            len6.append(x)
        elif len(x) == 7:
            numbers[8] = "".join(sorted(x))
        elif len(x) == 5:
            len5.append(x)
    candidat25 = [numbers[1][0],numbers[1][1]]
    for x in numbers[7]:
        if x not in numbers[1]:
            digits[0] = x
            break
    candidat13 = []
    for x in numbers[4]:
        if x not in numbers[1]:
            candidat13.append(x)
    candidat46 = []
    for x in alphabet:
        if x not in candidat13 and x not in candidat25 and x != digits[0]:
            candidat46.append(x)
    for x in len6:
        if (candidat13[0] in x and candidat13[1] not in x):
            numbers[0] = "".join(sorted(x))
            digits[1] = candidat13[0]
            digits[3] = candidat13[1]
            len6.pop(len6.index(x))
            break
        elif (candidat13[1] in x and candidat13[0] not in x):
            numbers[0] = "".join(sorted(x))
            digits[1] = candidat13[1]
            digits[3] = candidat13[0]
            len6.pop(len6.index(x))
            break
    for x in len6:
        if (candidat25[0] in x and candidat25[1] not in x):
            numbers[6] = "".join(sorted(x))
            digits[5] = candidat25[0]
            digits[2] = candidat25[1]
            len6.pop(len6.index(x))
            break
        elif (candidat25[1] in x and candidat25[0] not in x):
            numbers[6] = "".join(sorted(x))
            digits[5] = candidat25[1]
            digits[2] = candidat25[0]
            len6.pop(len6.index(x))
            break
    if (candidat46[0] in len6[0] and candidat46[1] not in len6[0]):
        numbers[9] = "".join(sorted(len6[0]))
        digits[6] = candidat46[0]
        digits[4] = candidat46[1]
    elif (candidat46[1] in len6[0] and candidat46[0] not in len6[0]):
        numbers[9] = "".join(sorted(len6[0]))
        digits[6] = candidat46[1]
        digits[4] = candidat46[0]
    for x in len5:
        if digits[0] in x and digits[2] in x and digits[3] in x and digits[4] in x and digits[6] in x:
            numbers[2] = "".join(sorted(x))
        elif digits[0] in x and digits[2] in x and digits[3] in x and digits[5] in x and digits[6] in x:
            numbers[3] = "".join(sorted(x))
        elif digits[0] in x and digits[1] in x and digits[3] in x and digits[5] in x and digits[6] in x:
            numbers[5] = "".join(sorted(x))
    decrypt.append(numbers)

sum = 0
for i in range(len(O)):
    sum += int("".join([ str(decrypt[i].index(x)) for x in O[i]]))
# n = 0
# for i in O:
#     for x in i:
#         if len(x) != 5 and len(x) != 6:
#             n += 1
    # temp = [len(x) for x in i]
    # l.append(temp)