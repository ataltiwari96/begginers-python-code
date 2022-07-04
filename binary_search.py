#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 23:04:15 2022

@author: ataltiwari
"""

#Binary Search

arr = []
n = int(input("Enter the size of the list: "))
found = 0

for i in range(0,n):
    
    val = int(input(f"Enter the {i} element of a list: "))
    arr.append(val)
    
#Sort the list for Binary Search
arr.sort()
print (f"List: {arr}",end = "\n\n")
beg = 0
end = n-1
mid = beg+end//2

num = int(input("Enter the element to be searched: "))

while(beg<=end):
    if num == arr[mid]:
        print (f"Match found at {mid+1} position")
        found+=1
        break
    elif num>mid:
        beg = mid+1
        mid = beg+end//2
    else:
        end = mid-1
        mid = beg+end//2
        
if beg>end and found == 0:
    print ("Element Not Found")