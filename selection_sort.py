#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:30:37 2022

@author: ataltiwari
"""

#Selection Sort
#Algo: Find the smallest element in the list and swap it with the /
#      beginning of the element. 

ar = [5,3,2,4,62,5,1,6,9]

l = len(ar)

for i in range(0,l):
    small  = i
    for j in range(i+1,l):
        if ar[small] > ar[j]:
            small = j
    ar[i], ar[small] = ar[small], ar[i]
    
print (ar)