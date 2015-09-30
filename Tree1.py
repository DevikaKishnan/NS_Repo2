# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:00:42 2015

@author: Devi
"""

#Tree
# Creating a tree

nodes = int(raw_input('Give nodes of tree'))
value = int(raw_input('Give value'))

class makelevel(object):
    def __init__(self, value = None, nodes = None):
        self.value = value
        self.nodes = nodes
        self.left = 0
        self.right = 0
        
    def leftsib(self):
        self.left = self.value + self.left
        return self.left
        
    def rightsib(self):
        self.right = self.value + self.right 
        return self.right
        
    def evaluate(self):
        self.left == self.leftsib() 
        self.right == self.rightsib() 
        a  = [self.leftsib(), self.rightsib()]
        return a
    
                
for i in range(nodes):
    c = makelevel.evaluate(makelevel(value,i))
    print c
    for j in range(2):
        value = c[j]
        e = makelevel(value,j)
        f = makelevel.evaluate(e)
        print f[0],' ',f[1]
            




#my_expr = exprnode('*', exprnode('+',exprnode(2),exprnode(3)),exprnode(4))



#    child[1] = [1]
#    child[2] = [1,1]
#    child[3] = [child[2][0],child[2][0] + child[2][1], child[2][1] + child[2][0], child[2][1]]
#    child[4] = [ child[3][0],child[3][0] + child[3][1],child[3][1] + child[3][0],child[3][1] + child[3][2],child[3][2]+child[3][1],child[3][2]+child[3][3],child[3][3]+child[3][2],child[3][3]]

