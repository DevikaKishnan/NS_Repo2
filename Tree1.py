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
    def __init__(self, value = None, nodes = None, left = None, right = None):
        self.value = value
        self.nodes = nodes
        self.left = left
        self.right = right
        

    def evaluate(self):
        self.left = self.leftsib() 
        self.right = self.rightsib() 
        a = [self.left, self.right]
        return a   
            
    def leftsib(self):
        if self.nodes == 0:
            self.left = self.value
            return self.left
        else:
            self.left = self.value + self.left
        return self.left
        
    def rightsib(self):
        if self.nodes == 0:
            self.right = self.value 
            return self.right
        else:
            self.right = self.value + self.right 
            return self.right
    
tree = [0]            
for i in range(nodes):
        c = makelevel.evaluate(makelevel(value,i,tree[i],tree[i]))
        print c
        tree.append(c[0])
        tree.append(c[1])
        for j in range(2):
            value = c[j]
            e = makelevel(value,j,tree[j],tree[j+1])
            f = makelevel.evaluate(e)
            print tree[j],' ',f[0],' ',f[1],' ', tree[(j)]
            
#3rint tree[1],' ', tree[3],' ', tree[4],' ', tree[2]

    
    
  
            




#my_expr = exprnode('*', exprnode('+',exprnode(2),exprnode(3)),exprnode(4))



#    child[1] = [1]
#    child[2] = [1,1]
#    child[3] = [child[2][0],child[2][0] + child[2][1], child[2][1] + child[2][0], child[2][1]]
#    child[4] = [ child[3][0],child[3][0] + child[3][1],child[3][1] + child[3][0],child[3][1] + child[3][2],child[3][2]+child[3][1],child[3][2]+child[3][3],child[3][3]+child[3][2],child[3][3]]

