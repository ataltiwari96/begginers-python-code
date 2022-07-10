#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 15:44:29 2022

@author: ataltiwari
"""

#Insrtion Sort

ar = [3,7,2,4,1,8]

l= len(ar)

for i in range(1,l):
    temp = ar[i]
    j = i-1
    while (temp < ar[j] and j>=0):
        ar[j+1] = ar[j]
        j-=1
    ar[j+1] = temp
    
print (ar)