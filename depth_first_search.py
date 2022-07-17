#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:32:24 2022

@author: ataltiwari
"""

graph = {
'1' : ['2','4','5'],
'5' : [],
'4' : [],
'2' : ['3','6','7'],
'7' :[],
'6' : [],
'3' :[] }

visited = set()
q = []

def dfs (visited, graph, node):
    if node not in visited:
        q.append(node)
        visited.add(node)
        for i in graph[node]:
            dfs(visited, graph, i)
    
            
dfs(visited,graph,'1')
print (q)