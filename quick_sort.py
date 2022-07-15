
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 02:18:29 2022

@author: ataltiwari
"""

# Python program for implementation of Quick Sort

def partition(ar, l, r):
    i = l-1
    pivot = ar[r]
    for j in range(l,r):
        if ar[j] <= pivot: 
            i+=1
            ar[i], ar[j] = ar[j],ar[i]
    i+=1
    ar[i],ar[r] = ar[r], ar[i]
    return i
    
def mergeSort(ar, l, r):
    if l < r:
        pi = partition(ar, l, r)
        mergeSort(ar, l, pi-1)
        mergeSort(ar, pi+1, r)
        

ar = [2,3,7,3,4]
mergeSort(ar,0,len(ar)-1)
print (ar)
