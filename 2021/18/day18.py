# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 08:50:32 2021

@author: Admin
"""

from math import ceil, floor
from copy import deepcopy

f = open('InputDay18.txt','r')
lines = [x.split('\n')[0]for x in f.readlines()]

class pair():
    
    def __init__(self, string, parentPair = None, LeftTerm = None, RightTerm = None):
        
        self.parent = parentPair
        
        if string == None:
            self.string = '[' + str(LeftTerm) + ',' + str(RightTerm) + ']'
        else:    
            self.string = string
        
        if LeftTerm != None and RightTerm != None:
            self.LeftTerm = LeftTerm
            self.RightTerm = RightTerm
        else:
            nested = 0
            firstTerm = True
            tempString = ''
            i = 1
            while True:	

                if i >= len(string)-1:
                    break
                
                if nested == 0:
                    if string[i] == ',':
                        i += 1
                        continue
                    
                    elif string[i].isnumeric():
                        j = 1   
                        
                        num = string[i]
                        while string[i+j].isnumeric():
                            num += string[i+j]
                            j += 1
                            break
                        if firstTerm == True:
                            self.LeftTerm = int(num)
                            firstTerm = False
                            i += len(num)
                        else:
                            self.RightTerm = int(num)
                            i += len(num)
                    elif string[i] == '[':
                        nested += 1
                        tempString = string[i]
                        i += 1
                        
                else:
                    if string[i] == ']':
                        tempString += string[i]
                        nested -= 1
                        if nested == 0:
                            if firstTerm == True:
                                self.LeftTerm = pair(tempString,self)
                                tempString = ''
                                firstTerm = False
                                i += 1
                            else:
                                self.RightTerm = pair(tempString,self)
                                tempString = ''
                                i += 1
                        else:
                            i+=1
                    elif string[i] == '[':
                        nested += 1
                        tempString += string[i]
                        i += 1
                    else:
                        tempString += string[i]
                        i += 1
            # nested = 0
            # firstTerm = True
            # tempString = ''
            # for i in string[1:-1]:
            #     if nested == 0:
            #         if i == ',':
            #             continue
            #         if i.isnumeric():
            #             if firstTerm == True:
            #                 self.LeftTerm = int(i)
            #                 firstTerm = False
            #             else:
            #                 self.RightTerm = int(i)
            #         if i == '[':
            #             nested += 1
            #             tempString = i
            #     else:
            #         if i == ']':
            #             tempString += i
            #             nested -= 1
            #             if nested == 0:
            #                 if firstTerm == True:
            #                     self.LeftTerm = pair(tempString,self)
            #                     tempString = ''
            #                     firstTerm = False
            #                 else:
            #                     self.RightTerm = pair(tempString,self)
            #                     tempString = ''
            #         elif i == '[':
            #             nested += 1
            #             tempString += i
            #         else:
            #             tempString += i
        

    
    def __str__(self):
        return f'[{self.LeftTerm},{self.RightTerm}]'
    
    def magnitude(self):
        magn = 0
        if type(self.RightTerm) == int:
            magn += 2*self.RightTerm
        elif type(self.RightTerm) == pair:
            magn += 2*self.RightTerm.magnitude()
        
        if type(self.LeftTerm) == int:
            magn += 3*self.LeftTerm
        elif type(self.LeftTerm) == pair:
            magn += 3*self.LeftTerm.magnitude()
            
        return magn
        
    def __add__(self,other):
        if type(other) == pair: 
            temp = pair(None,None,self,other)
            notCorrect = True
            while notCorrect:
                if bool(temp.Explode(0, [None,None,None])):
                    
                    temp = temp.Explode(0, [None,None,None])
                    continue
                elif bool(temp.Split()):
                    temp = temp.Split()
                    continue
                else:
                    notCorrect = False
            return temp
        else:
            print("Operation Not supported")
            
    def Explode(self,nested,numbers):
        
        nested = 0
        Numbers = [None,None,None]
        s = deepcopy(self.string)
        i=0
        while True:     

            if s[i] == ',':
                i += 1
                continue
            elif s[i].isnumeric():
                j = 1
                length = 1
                while s[i+j].isnumeric():
                    length +=1 
                    j += 1
                Numbers = [(i,length),Numbers[0],Numbers[1]]
                
                i = i+j
                continue
                
            elif s[i] == '[':
                nested += 1
                i+=1
                continue
                    
            elif s[i] == ']':
                if nested == 5:
                    #Look for NextNumber
                    NextNumber = None
                    pos = i
                    for k in s[i:]:

                        if k.isnumeric():
                            j = 1
                            length = 1 

                            while s[pos+j].isnumeric():

                                length +=1 
                                j += 1
                            NextNumber = (pos, length)
                            break
                        pos += 1
                       
                    
                    tString = ''
                    if Numbers[-1] != None:
                        leftnum = int(s[Numbers[-2][0]:Numbers[-2][0]+Numbers[-2][1]]) + int(s[Numbers[-1][0]:Numbers[-1][0]+Numbers[-1][1]])
                        tString += s[:Numbers[-1][0]] + str(leftnum)+ s[Numbers[-1][0]+Numbers[-1][1]:Numbers[-2][0]-1] + '0'
                    else:
                        tString += s[:Numbers[-2][0]-1] + '0'
                    if NextNumber != None:
                        rightnum = int(s[Numbers[0][0]:Numbers[0][0]+Numbers[0][1]]) + int(s[NextNumber[0]:NextNumber[0]+NextNumber[1]])
                        tString += s[Numbers[0][0]+1+Numbers[0][1]:NextNumber[0]] + str(rightnum) + s[NextNumber[0] + NextNumber[1]:]
                    else:
                        tString += s[Numbers[0][0]+1+Numbers[0][1]:]
                    return pair(tString)
                
                else: 
                    nested -= 1
                    if nested == 0:
                        return False
                    i += 1
                    continue
                
        # if type(self.LeftTerm()) == pair:
        #     if nested == 3:
        #         l = self.RightTerm.LeftTerm
        #         r = self.RightTerm.RightTerm
        #         self.LeftTerm.explode()
        #         self.LeftTerm = 0
        #         return False
        #     else:
        #         nested += 1
        #         self.LetfTerm.checkValid(nested)
        # else:
            
        # if type(self.RightTerm()) == pair:
        #     if nested == 3:
        #         l = self.RightTerm.LeftTerm
        #         r = self.RightTerm.RightTerm
        #         self.RightTerm.explode()
        #         self.RightTerm = 0
        #         return False
        #     else:
        #         nested += 1
        #         self.RightTerm.checkValid(nested)
                
     
    def Split(self):
        result = False
        if type(self.LeftTerm) == int:
            if self.LeftTerm > 9:
                # self.LeftTerm = split(self.LeftTerm,self)
                return pair(None,self.parent,split(self.LeftTerm,self),self.RightTerm)
        else:
            if bool(self.LeftTerm.Split()):
                return pair(None,self.parent,self.LeftTerm.Split(),self.RightTerm)
            
        if type(self.RightTerm) == int :
            if self.RightTerm > 9:
                return pair(None,self.parent,self.LeftTerm,split(self.RightTerm,self))
        else: 
            if bool(self.RightTerm.Split()):
                return pair(None,self.parent,self.LeftTerm,self.RightTerm.Split())
        return False

    
def split(x,parent):
    return pair(None,parent,floor(x/2),ceil(x/2))
            
            
            
tot = pair(lines[0])
for i in lines[1:]:
  tot = tot + pair(i)
            
print(tot.magnitude())
            
# a = pair('[[[5,3],[[8,6],[7,1]]],[8,0]]')
# a = pair('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
# a = pair('[[[[0,7],4],[15,[0,13]]],[1,1]]')
# a.Split()
# print(a.Split())

maxMag = 0 

for i in lines:
    for j in lines:
        res = pair(i) + pair(j)
        if res.magnitude() > maxMag:
            maxMag = res.magnitude()
        
    
print(maxMag)





