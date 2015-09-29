# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:00:42 2015

@author: Devi
"""

#Tree
# Creating a tree

class exprnode(object):
    def __init__(self, value = None, left = None, right  = None):
        self.value = value
        self.left = left
        self.right = right
        
    def evaluate(self):
        if self.value == '+':
            ret1 = self.left.evaluate() + self.right.evaluate()
            print 
            return ret1 
        elif self.value == '-':
            ret2 = self.left.evaluate() - self.right.evaluate()
            print ret2
            return ret2
        elif self.value == '*':
            ret3 = self.left.evaluate()*self.right.evaluate()
            print ret3
            return ret3
        elif self.value == '/':
            ret4 = self.left.evaluate()/self.right.evaluate()
            print ret4
            return ret4
        else:
            print self.value
            return self.value

s = exprnode(1)
t = s.evaluate()

  


            
#my_expr = exprnode('*', exprnode('+',exprnode(2),exprnode(3)),exprnode(4))



#    child[1] = [1]
#    child[2] = [1,1]
#    child[3] = [child[2][0],child[2][0] + child[2][1], child[2][1] + child[2][0], child[2][1]]
#    child[4] = [ child[3][0],child[3][0] + child[3][1],child[3][1] + child[3][0],child[3][1] + child[3][2],child[3][2]+child[3][1],child[3][2]+child[3][3],child[3][3]+child[3][2],child[3][3]]

