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

visited = [] # List for visited nodes.
queue = [] 
q= []    #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)
  q.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        q.append(neighbour)
    
            
bfs(visited,graph,'1')
print (q)