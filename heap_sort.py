#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:38:01 2022

@author: ataltiwari
"""

# Heap Sort in python

def heapify(ar, n, i):
    large = i
    left = i*2+1
    right = i*2+2
    
    if left < n and ar[i] < ar[left]:
        large = left
    if right < n and ar[large] < ar[right]:
        large = right
        
    if i != large:
        ar[i], ar[large] = ar[large], ar[i]
        heapify(ar, n, large)
        
    
    
    
def heapSort(ar):
    n = len(ar)
    
    for i in range(n//2-1,-1,-1):
        heapify(ar,n, i)
        
    for i in range(n-1, 0, -1):
        ar[i], ar[0] = ar[0], ar[i]
        heapify(ar, i, 0)
        
ar = [7,4,2,1,6]
heapSort(ar)
print (ar)