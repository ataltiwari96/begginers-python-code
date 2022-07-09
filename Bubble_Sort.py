#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 01:30:03 2022

@author: ataltiwari
"""

#Bubble Sort

num = int(input("Enter the number of elements: "))

li = []

for i in range(0,num):
    n = int(input(f"Enter the {i+1} element: "))
    li.append(n)
    
t = 0
    
for j in range(num-1):
    for k in range(0,num-1):
        if li[k] > li[k+1]:
            li[k], li[k+1] = li[k+1], li[k]
            
print (li)