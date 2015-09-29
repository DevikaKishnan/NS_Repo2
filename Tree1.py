# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:00:42 2015

@author: Devi
"""

#Tree
import string
import numpy as np
import operator as op
#a = raw_input("Please Provide nodes of tree")
node = 5
#root = ()
#parent = ()
#child = ()
b = []
c = []
b.append([0])
for i in range(1,node+1):
    b.append([i])
    s1 = op.add(b[i-1],b[i])
    c.append(s1)
print b
print c
    
#    child[1] = [1]
#    child[2] = [1,1]
#    child[3] = [child[2][0],child[2][0] + child[2][1], child[2][1] + child[2][0], child[2][1]]
#    child[4] = [ child[3][0],child[3][0] + child[3][1],child[3][1] + child[3][0],child[3][1] + child[3][2],child[3][2]+child[3][1],child[3][2]+child[3][3],child[3][3]+child[3][2],child[3][3]]

