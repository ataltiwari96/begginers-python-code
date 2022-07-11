#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:47:37 2022

@author: ataltiwari
"""

def mergeSort(ar):
    #Check if array has more than 1 element otherwise it will be considered as sorted
    if len(ar) > 1:
        #find the mid
        mid = len(ar) // 2  
        left = ar[:mid]
        right = ar[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = 0
        j = 0
        k = 0
        
        while (i < len(left) and j < len(right)):
            if left[i] <= right[j]:
                ar[k] = left[i]
                i+=1
            else:
                ar[k] = right[j]
                j+=1
            k+=1
            
        while i < len(left):
            ar[k] = left[i]
            i+=1
            k+=1
            
        while j < len(right):
            ar[k] = right[j]
            j+=1
            k+=1
            
    else:
        return "List Already Sorted or has no item to sort"
        
ar = [1,5,7,8,4,24,5]    
mergeSort(ar)
print (ar)
        