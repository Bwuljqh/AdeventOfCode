# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:24:08 2021

@author: Admin
"""

f = open('InputDay4.txt','r')
lines = f.readlines()

numbers = lines[0].split('\n')[0].split(',')

boards = []

temp = []
for i in lines[2:]:
    if i == '\n':
        # temp.append([temp[x][x] for x in range(5)])
        # temp.append([temp[x][-x-1] for x in range(5)])
        boards.append(temp)
        
        temp = []
    else:
        line = i.split('\n')[0].split(' ')
        j = 0
        while j < len(line):
            if line[j] == '':
                line.pop(j)
            else:
                j += 1
        temp.append(line)
        
# temp.append([temp[x][x] for x in range(5)])
# temp.append([temp[x][-x-1] for x in range(5)])
boards.append(temp)

def roadToVictory(boards, numbers):
    num = []
    for i in range(len(numbers)):
        print(len(boards))
        if len(boards) == 1:
            n = 0
            for y in boards[0]:
                for k in y:
                    if k not in num:
                        n += int(k)
            return int(num[-1]) * n
            return num, boards
        num = numbers[:i+6]
        for j in boards:
            V, L = isWinner(j, num)
            if V:

                boards.remove(j)
            
def isWinner(board, numbers):
    for i in board:
        if all( elem in numbers for elem in i):
            return (True, i)
    return (False, [])

# def roadToVictory(boards, numbers):
#     for i in range(len(numbers)):
#         num = numbers[:i+6]
#         for j in boards:
#             V, L = isWinner(j, num)
#             if V:
#                 n = 0
#                 for y in j:
#                     for k in y:
#                         if k not in num:
#                             n += int(k)
            
#                 return int(num[-1]) * n
            
# def isWinner(board, numbers):
#     for i in board:
#         if all( elem in numbers for elem in i):
#             return (True, i)
#     return (False, [])

print(roadToVictory(boards,numbers))

