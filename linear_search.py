#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:30:12 2022

@author: ataltiwari
"""

#Linear Search

ar = [1,2,5,6,7,8,3]

key = 6

l = len(ar)

found = 0

for i in range(0,l-1):
    if ar[i] == key:
        found+=1
        print("Match found")
    else:
        continue
if found== 0:
    print ("Element not found")
        