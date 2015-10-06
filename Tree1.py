
#Tree
# Creating a tree

nodes = int(raw_input('Give nodes of tree'))
value = int(raw_input('Give value'))

global i

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
        elif self.left == None:
            self.left = self.value
            return self.left
        else:
            self.left = self.value + self.left
        return self.left
        
    def rightsib(self):
        if self.nodes == 0:
            self.right = self.value 
            return self.right
        elif self.right == None:
            self.right = self.value
            return self.right
        else:
            self.right = self.value + self.right 
            return self.right

tree = [0,0]
    
def fortree(value,left,right):
    a = makelevel.evaluate(makelevel(value,i,left,right))
    return a
        
x =int(0)        
    
for i in range(nodes):
    if i == 0:
        a = fortree(value,tree[i],tree[i+1])
        b = [0,a[0],a[1],0]
        c = [a[0],a[1]]
        print value
        x = -2
    else:
        for j in range(1,len(a)+1):
            value = c[x]
            e = fortree(value,b[j-1],b[j+1])
            c.append(e[0])
            c.append(e[1])
            b.append(0),b.append(e[0]),b.append(e[1]),b.append(0)
            x= x+1
        j = j+4   
    x=x+2        
    print b
    print c

            
    
